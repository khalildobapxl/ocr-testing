# OCR Models Comparison and Testing

This repository contains a comprehensive evaluation of different Optical Character Recognition (OCR) models. The primary goal is to assess their performance on various photos of labels captured under different conditions including varying angles, lighting, and backgrounds.

## 📋 Project Overview

- **Objective**: Evaluate OCR model performance on real-world label images
- **Test Images**: Located in `testImages/` directory
- **Image Categories**: Good quality, medium quality, and poor quality samples
- **Testing Approach**: Raw images without preprocessing to simulate real-world conditions

## 🔧 Tested Models

| Model | Status | Recommendation |
|-------|--------|----------------|
| [Tesseract OCR](#tesseract-ocr) | ❌ | Not Recommended |
| [EasyOCR](#easyocr) | ✅ | Recommended |
| [PaddleOCR](#paddleocr) | ✅ | Recommended |
| [DocTR](#doctr) | ⭐ | Highly Recommended |

---

## 📸 Test Image Structure

```
testImages/
├── good1.jpg, good2.jpg, good3.jpg    # High quality images
├── mid1.png, mid2.png, mid3.png        # Medium quality images
└── bad1.jpg, bad2.jpg, bad3.png        # Poor quality images
```

---

## 🧪 Model Evaluations

### Tesseract OCR

**Installation:**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

**Performance Analysis:**
- ✅ **Strengths**: Performs well on clean, high-contrast text
- ❌ **Weaknesses**: 
  - Struggles with complex backgrounds
  - Poor performance on angled images
  - Difficulty with images containing multiple objects
- **Overall Rating**: ❌ **NOT RECOMMENDED**

---

### PaddleOCR

**Installation:**
```bash
# Install PaddlePaddle (CPU version for testing, GPU version available)
pip install paddlepaddle

# Install PaddleOCR
pip install paddleocr
```

**Performance Analysis:**
- ✅ **Strengths**: 
  - Exceptional accuracy across all test images
  - Extracts text invisible to human eye with high precision
  - Robust performance on poor quality images
- ⚠️ **Considerations**: Requires both PaddlePaddle and PaddleOCR packages
- **Overall Rating**: ✅ **RECOMMENDED**

---

### EasyOCR

**Installation:**
```bash
# Install PyTorch dependencies
pip install torch torchvision torchaudio

# Install EasyOCR
pip install easyocr
```

**Performance Analysis:**
- ✅ **Strengths**: 
  - Good performance on most images with default settings
  - Supports 80+ languages
  - Potential for improvement with preprocessing
- ⚠️ **Considerations**: 
  - Requires significant storage space
  - CUDA support increases package size
- **Overall Rating**: ✅ **RECOMMENDED**

---

### DocTR

**Installation:**
```bash
pip install python-doctr[tensorflow]
```

**Performance Analysis:**
- ⭐ **Strengths**: 
  - Exceptional performance across all test images
  - Best overall results among tested models
  - Efficient and reliable
- 🔧 **Potential**: Could be further optimized with parameter tuning
- **Overall Rating**: ⭐ **HIGHLY RECOMMENDED**

---


## 📊 Results Summary

Based on our testing across various image qualities:

1. **🏆 Best Overall**: DocTR - Consistent high performance
2. **🥈 High Accuracy**: PaddleOCR - Excellent on challenging images  
3. **🥉 Versatile**: EasyOCR - Good performance with language variety
4. **📝 Basic**: Tesseract - Limited to clean, simple text
