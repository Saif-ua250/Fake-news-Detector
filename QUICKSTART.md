# 🚀 Quick Start Guide

## ⚡ Fast Setup (5 Steps)

### 1️⃣ Open Terminal (PowerShell)
```powershell
cd "c:\Users\saif7\OneDrive\Desktop\Fake news Detector"
```

### 2️⃣ Create Virtual Environment
```powershell
python -m venv venv
```

### 3️⃣ Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```

If you get an error about execution policy, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4️⃣ Install Dependencies
```powershell
pip install -r requirements.txt
```

⏳ This will take 5-10 minutes (downloads ~2GB of packages)

### 5️⃣ Run the App
```powershell
streamlit run app.py
```

🎉 **Your app will open at:** http://localhost:8501

---

## 📱 Using the App

### Text/URL Analysis
1. Click **"📝 Text/URL"** in sidebar
2. Paste text OR enter a URL
3. Click **"🔍 Analyze"**

### Image Analysis
1. Click **"🖼️ Image"** in sidebar
2. Upload a JPG/PNG image
3. Click **"🔍 Analyze Image"**

### Video Analysis
1. Click **"🎥 Video"** in sidebar
2. Upload an MP4 video
3. Adjust sampling rate (1-5 fps)
4. Click **"🔍 Analyze Video"**

---

## 🐛 Common Issues

### "Module not found" error
```powershell
# Make sure venv is activated (you should see (venv) in prompt)
.\venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt
```

### "streamlit: command not found"
```powershell
# Use full Python module syntax
python -m streamlit run app.py
```

### Slow first run
- ✅ Normal! Models download on first run (~5-15 min)
- ✅ Subsequent runs are much faster (models cached)

### Out of memory
- Reduce video sampling rate to 1
- Use smaller images/videos
- Close other applications

---

## 🧪 Test the Installation

Run tests to verify everything works:

```powershell
pytest tests/ -v
```

---

## 📚 More Help

- **Full Documentation**: See `README.md`
- **Code Documentation**: Check docstrings in each `.py` file
- **Model Info**: Visit Hugging Face model cards

---

## 🎯 Example Usage

### Test with Sample Text
```
The Earth is flat and NASA has been lying to us for decades.
Scientists around the world are covering up the truth about our planet.
```
Expected: **Fake** (high confidence)

### Test with Real News
```
According to a new study published in Nature, researchers have found 
that regular exercise can improve cognitive function in older adults.
```
Expected: **Real** (high confidence)

---

**Happy Analyzing! 🔍✨**
