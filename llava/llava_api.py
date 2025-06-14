# llava_api.py

import os
import torch
from PIL import Image
from io import BytesIO

from llava.utils import disable_torch_init
from llava.conversation import conv_templates
from llava.model.builder import load_pretrained_model
from llava.mm_utils import tokenizer_image_token, process_images, get_model_name_from_path
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN


class LlavaInference:
    def __init__(self, model_path, model_base=None):
        self.model_path = os.path.expanduser(model_path)
        self.model_base = model_base

        disable_torch_init()
        model_name = get_model_name_from_path(self.model_path)
        self.tokenizer, self.model, self.image_processor, _ = load_pretrained_model(
            self.model_path, self.model_base, model_name, device="cuda"
        )
        self.model.generation_config.pad_token_id = self.tokenizer.pad_token_id

    def analyze(self, image_bytes, prompt, temperature=0.2, conv_mode="qwen_2"):
        image = Image.open(BytesIO(image_bytes)).convert('RGB')

        # Construct prompt
        if self.model.config.mm_use_im_start_end:
            qs = DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_TOKEN + DEFAULT_IM_END_TOKEN + '\n' + prompt
        else:
            qs = DEFAULT_IMAGE_TOKEN + '\n' + prompt

        conv = conv_templates[conv_mode].copy()
        conv.append_message(conv.roles[0], qs)
        conv.append_message(conv.roles[1], None)
        full_prompt = conv.get_prompt()

        input_ids = tokenizer_image_token(full_prompt, self.tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).to("cuda")
        image_tensor = process_images([image], self.image_processor, self.model.config)[0]

        with torch.inference_mode():
            output_ids = self.model.generate(
                input_ids,
                images=image_tensor.unsqueeze(0).half(),
                image_sizes=[image.size],
                do_sample=True if temperature > 0 else False,
                temperature=temperature,
                num_beams=1,
                max_new_tokens=256,
                use_cache=True
            )

        output_text = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()
        return output_text, image.size
