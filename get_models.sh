#!/usr/bin/env bash

mkdir -p weights
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_0.5b_stage2.zip -P weights
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_0.5b_stage3.zip -P weights
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_1.5b_stage2.zip -P weights
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_1.5b_stage3.zip -P weights
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_7b_stage2.zip -P weights
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_7b_stage3.zip -P weights

# Extract models
cd weights
unzip -qq llava-fastvithd_0.5b_stage2.zip
unzip -qq llava-fastvithd_0.5b_stage3.zip
unzip -qq llava-fastvithd_1.5b_stage2.zip
unzip -qq llava-fastvithd_1.5b_stage3.zip
unzip -qq llava-fastvithd_7b_stage2.zip
unzip -qq llava-fastvithd_7b_stage3.zip

# Clean up
rm llava-fastvithd_0.5b_stage2.zip
rm llava-fastvithd_0.5b_stage3.zip
rm llava-fastvithd_1.5b_stage2.zip
rm llava-fastvithd_1.5b_stage3.zip
rm llava-fastvithd_7b_stage2.zip
rm llava-fastvithd_7b_stage3.zip
cd -
