# 🚀 LLaVA-FastVLM: One-Click Visual Language API
![Vizualization](https://github.com/Shohruh72/FastVLM/blob/main/static/demo.gif)

## One-click web interface for Apple's FastVLM vision models

## ✨ What Makes This Special
Built on **Apple's FastVLM (CVPR 2025)** - the breakthrough vision model that's 85x faster than traditional approaches. Bayonic Vision brings this cutting-edge technology to your browser with a beautiful, simple interface.


## 🎯 Key Features

* **⚡ Lightning Fast:** 85x faster Time-to-First-Token than LLaVA-OneVision
* **🎨 Drag & Drop:** Beautiful web interface - just drop your image and go
* **🧠 Multiple Models:** 0.5B, 1.5B, and 7B parameter variants
* **📱 Production Ready:** Flask-powered backend with REST API
* **🔧 Zero Config:** Works out of the box

🚀 Quick Start

### Install


```bash
    # Download FastVLM models
    bash get_models.sh
```

``` bash
    # Clone and setup
    conda create -n bayonic python=3.10
    conda activate bayoninc
    pip install -e .
```

```bash 
  # Launch the web interface
  python app.py
```

Open http://localhost:5000 → Drop an image → Get instant AI analysis ✨

## 🎪 Demo
### Drop any image and ask questions like:

* "What's happening in this image?"
* "Count the objects you see"
* "Describe the scene in detail"
* "What emotions do you detect?"

### 🔧 Tech Stack

* FastVLM - Apple's state-of-the-art vision encoder (CVPR 2025)
* Flask - Lightweight Python web framework
* LLaVA - Advanced vision-language understanding
* Modern UI - Responsive interface that works everywhere

#### Reference
https://github.com/apple/ml-fastvlm

## 🔥 Try it now. Star if you like instant AI magic! ⭐️
