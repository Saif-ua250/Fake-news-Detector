# 🔍 FakeNews + Deepfake Detector

A comprehensive AI-powered web application for detecting fake news in text/URLs and deepfakes in images/videos.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- **📝 Text & URL Analysis**: Detect fake news in articles using BERT-based NLP
- **🖼️ Image Detection**: Identify deepfakes in photos and images
- **🎥 Video Analysis**: Analyze videos frame-by-frame for deepfake detection
- **🎨 User-Friendly Interface**: Clean Streamlit UI with real-time results
- **🤖 Pre-trained Models**: Leverages state-of-the-art Hugging Face models
- **📊 Detailed Results**: Shows confidence scores and explanations

## 🧠 Models Used

- **Text/Fake News**: [`jy46604790/Fake-News-Bert-Detect`](https://huggingface.co/jy46604790/Fake-News-Bert-Detect)
- **Image/Video Deepfake**: [`prithivMLmods/Deep-Fake-Detector-v2-Model`](https://huggingface.co/prithivMLmods/Deep-Fake-Detector-v2-Model)

## 📁 Project Structure

```
Fake news Detector/
├── app.py                      # Main Streamlit application
├── detectors/
│   ├── __init__.py
│   ├── fake_news.py           # Text fake news detection
│   └── deepfake.py            # Image/video deepfake detection
├── utils/
│   ├── __init__.py
│   ├── scraper.py             # Web scraping for URLs
│   └── video_utils.py         # Video frame extraction
├── tests/
│   └── test_detectors.py      # Unit tests
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM (8GB+ recommended for video processing)
- Internet connection (for first-time model downloads)

### Installation

1. **Clone or download this repository**

```bash
cd "Fake news Detector"
```

2. **Create a virtual environment**

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> **Note**: First installation may take 5-10 minutes as it downloads ML libraries and models.

4. **Run the application**

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 💻 Usage

### Text Analysis

1. Select **📝 Text/URL** mode from the sidebar
2. Choose to paste text directly or enter a URL
3. Click **🔍 Analyze**
4. View results with confidence score and explanation

### Image Analysis

1. Select **🖼️ Image** mode from the sidebar
2. Upload a JPG, JPEG, or PNG image
3. Click **🔍 Analyze Image**
4. View deepfake detection results

### Video Analysis

1. Select **🎥 Video** mode from the sidebar
2. Upload an MP4, AVI, or MOV video
3. Adjust frame sampling rate (1-5 fps)
4. Click **🔍 Analyze Video**
5. View overall result and per-frame analysis

## 🔧 Configuration

### GPU Support

By default, the app runs on CPU. To enable GPU:

1. Install PyTorch with CUDA support:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

2. Models will automatically detect and use GPU if available

### Model Caching

Models are automatically cached after first download in:
- Windows: `C:\Users\<username>\.cache\huggingface\`
- Linux/Mac: `~/.cache/huggingface/`

## 🧪 Testing

Run unit tests with pytest:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=detectors --cov=utils

# Verbose output
pytest tests/ -v
```

## ⚠️ Troubleshooting

### Out of Memory Errors

- **Reduce video sampling rate** (use 1 fps instead of higher values)
- **Process smaller images/videos**
- **Close other applications** to free up RAM
- **Use CPU-only mode** if GPU memory is insufficient

### Slow Performance

- **First run is slow**: Models are downloaded and cached (5-15 minutes)
- **Subsequent runs are faster**: Cached models load quickly
- **Video analysis takes time**: Processing 60 frames can take 1-3 minutes on CPU

### Import Errors

```bash
# Ensure virtual environment is activated
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Model Download Issues

- **Check internet connection**
- **Use VPN if Hugging Face is blocked** in your region
- **Manually download models**:
  ```python
  from transformers import pipeline
  pipeline("text-classification", model="jy46604790/Fake-News-Bert-Detect")
  ```

### Newspaper3k SSL Errors

If you encounter SSL certificate errors when scraping URLs:

```bash
# Windows
pip install certifi
python -m certifi

# Or use environment variable
set REQUESTS_CA_BUNDLE=/path/to/cacert.pem
```

## 📊 Performance Metrics

| Task | CPU Time | GPU Time | Accuracy* |
|------|----------|----------|-----------|
| Text (500 words) | ~2-3 sec | ~1 sec | 85-90% |
| Image | ~3-5 sec | ~1-2 sec | 80-85% |
| Video (30s @ 1fps) | ~90-120 sec | ~30-45 sec | 75-85% |

*Accuracy varies based on content quality and model capabilities

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

**Important Notice:**

This tool uses AI models that are **not 100% accurate**. Results should be used as guidance, not as definitive proof.

- **False positives/negatives can occur**
- **Always verify with multiple trusted sources**
- **Use critical thinking when evaluating media**
- **Models may have biases** based on training data

This tool is for **educational and research purposes**. Do not use it as the sole basis for important decisions.

## 🙏 Acknowledgments

- **Hugging Face** for hosting the models
- **Streamlit** for the web framework
- **OpenCV** for video processing
- **newspaper3k** for web scraping
- Model creators:
  - `jy46604790` for Fake-News-Bert-Detect
  - `prithivMLmods` for Deep-Fake-Detector-v2-Model

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Documentation**: Check this README
- **Models**: Visit Hugging Face model cards for details

## 🔄 Version History

- **v1.0.0** (2025-10-15): Initial release
  - Text fake news detection
  - Image deepfake detection
  - Video deepfake detection
  - Streamlit web interface
  - URL scraping support

## 🎯 Roadmap

- [ ] Add batch processing for multiple files
- [ ] Implement result export (CSV/JSON)
- [ ] Add multi-language support
- [ ] Include audio deepfake detection
- [ ] Create REST API endpoint
- [ ] Add model fine-tuning capabilities

---

**Made with ❤️ using Python, Streamlit, and Hugging Face Transformers**
