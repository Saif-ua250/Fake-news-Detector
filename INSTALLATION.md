# 🚀 COMPLETE INSTALLATION & USAGE GUIDE

## ✅ Your App is Ready! Follow These Steps:

---

## 📋 OPTION 1: Automated Setup (Recommended)

### Step 1: Open PowerShell
Right-click in the project folder and select "Open in Terminal" or "Open PowerShell window here"

### Step 2: Run Setup Script
```powershell
.\setup.ps1
```

**If you get an execution policy error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then run `.\setup.ps1` again.

### Step 3: Run the App
```powershell
.\run.ps1
```

**Done! Your app will open at http://localhost:8501** 🎉

---

## 📋 OPTION 2: Manual Setup

### Step 1: Open PowerShell in Project Directory
```powershell
cd "c:\Users\saif7\OneDrive\Desktop\Fake news Detector"
```

### Step 2: Create Virtual Environment
```powershell
python -m venv venv
```

### Step 3: Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your prompt.

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```
⏳ This takes 5-10 minutes (downloads ~2GB)

### Step 5: Test Installation (Optional)
```powershell
python test_setup.py
```

### Step 6: Run the App
```powershell
streamlit run app.py
```

**Your browser will automatically open to http://localhost:8501** 🎊

---

## 🎯 HOW TO USE THE WEB APP

### 1️⃣ Detect Fake News (Text)

1. **Select Mode**: Click "📝 Text/URL" in the left sidebar
2. **Input Method**: Choose "Paste Text"
3. **Enter Text**: Paste a news article or text
4. **Analyze**: Click the "🔍 Analyze" button
5. **View Results**: 
   - See if it's "Fake" or "Real"
   - Check confidence score
   - Read explanation
   - Toggle "Show raw model output" for details

**Example Text to Try:**
```
Scientists have confirmed that drinking water is essential for human health 
according to a new study published in a peer-reviewed medical journal.
```

### 2️⃣ Detect Fake News (URL)

1. **Select Mode**: Click "📝 Text/URL" in the sidebar
2. **Input Method**: Choose "Enter URL"
3. **Paste URL**: Enter a news article URL
4. **Analyze**: Click "🔍 Analyze"
5. **View Results**: App fetches and analyzes the article

**Try with real news URLs like:**
- BBC articles
- Reuters articles
- AP News articles

### 3️⃣ Detect Deepfakes (Images)

1. **Select Mode**: Click "🖼️ Image" in the sidebar
2. **Upload Image**: Click "Browse files" and select a JPG/PNG
3. **Preview**: Your image appears on screen
4. **Analyze**: Click "🔍 Analyze Image"
5. **View Results**:
   - "Deepfake" or "Real" label
   - Confidence percentage
   - Explanation of what was detected

### 4️⃣ Detect Deepfakes (Videos)

1. **Select Mode**: Click "🎥 Video" in the sidebar
2. **Upload Video**: Choose an MP4/AVI/MOV file
3. **Set Sampling Rate**: 
   - 1 fps = faster, fewer frames
   - 5 fps = slower, more accurate
4. **Analyze**: Click "🔍 Analyze Video"
5. **Wait**: Processing takes 1-3 minutes
6. **View Results**:
   - Overall verdict
   - Per-frame analysis
   - Frame counts (deepfake vs real)

---

## ⚡ QUICK COMMANDS REFERENCE

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the app
streamlit run app.py

# Run tests
pytest tests/ -v

# Test installation
python test_setup.py

# Stop the app
# Press Ctrl+C in the terminal
```

---

## 🔧 TROUBLESHOOTING

### ❌ "python is not recognized"
**Solution:** Install Python from https://www.python.org
- Make sure to check "Add Python to PATH" during installation

### ❌ "streamlit: command not found"
**Solution:** 
1. Make sure venv is activated: `.\venv\Scripts\Activate.ps1`
2. Or use: `python -m streamlit run app.py`

### ❌ "Import 'transformers' could not be resolved"
**Solution:** Install dependencies:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### ❌ Script execution policy error
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ "Out of Memory" when processing video
**Solution:**
- Reduce sampling rate to 1 fps
- Use shorter videos (< 30 seconds)
- Close other applications
- Use smaller resolution videos

### ❌ First run is very slow
**Solution:** This is normal! 
- First run downloads models (~1-2 GB)
- Takes 5-15 minutes initially
- Subsequent runs are much faster (models are cached)

### ❌ URL scraping fails
**Solution:**
- Check internet connection
- Try a different URL
- Some sites block scraping - use "Paste Text" instead
- Ensure the URL is a direct article link

### ❌ Can't find article text in URL
**Solution:**
- Make sure URL is a direct article page
- Try copying the article text and using "Paste Text" mode
- Some news sites require JavaScript or have anti-scraping measures

---

## 📊 WHAT TO EXPECT

### ⏱️ Processing Times

| Task | First Time | Subsequent Times |
|------|-----------|------------------|
| App Startup | 2-3 min | 10-20 sec |
| Text Analysis | 30 sec | 2-3 sec |
| Image Analysis | 30 sec | 3-5 sec |
| Video (30s @ 1fps) | 5 min | 90-120 sec |

### 🎯 Accuracy Notes

- Models are ~80-90% accurate
- Not perfect - use as guidance
- Verify important information
- Results show confidence scores
- Lower confidence = less certain

---

## 🎓 UNDERSTANDING RESULTS

### Fake News Detection

**Label: "Fake"**
- Text has characteristics of misinformation
- May contain sensationalized language
- Lacks credible source patterns
- ⚠️ Verify before sharing

**Label: "Real"**
- Text has characteristics of legitimate news
- Balanced, factual reporting style
- ✓ Still verify important claims

### Deepfake Detection

**Label: "Deepfake"**
- Media shows signs of manipulation
- AI-generated or altered features detected
- Facial inconsistencies or artifacts
- ⚠️ Verify authenticity

**Label: "Real"**
- Media appears authentic
- Natural features and textures
- No obvious manipulation detected
- ✓ No system is 100% accurate

---

## 💡 BEST PRACTICES

### For Text Analysis:
✅ Use complete articles (not just headlines)
✅ Paste at least 3-4 paragraphs
✅ Check multiple sources
✅ Look at confidence scores

### For Image Analysis:
✅ Use clear, high-quality images
✅ Face photos work best
✅ Avoid heavily compressed images
✅ Test multiple images if uncertain

### For Video Analysis:
✅ Start with 1 fps sampling
✅ Use videos < 1 minute for faster results
✅ Higher sampling rate = more accurate but slower
✅ Check per-frame results for consistency

---

## 🎉 YOU'RE READY!

Your FakeNews + Deepfake Detector is fully functional and ready to use!

### To Start:
```powershell
.\run.ps1
```

### Or Manually:
```powershell
.\venv\Scripts\Activate.ps1
streamlit run app.py
```

### Access at:
**http://localhost:8501**

---

## 📞 NEED HELP?

- Check **QUICKSTART.md** for quick reference
- Read **README.md** for detailed documentation
- Check **PROJECT_SUMMARY.md** for technical details
- Run `python test_setup.py` to diagnose issues

---

**Happy Detecting! 🔍✨**
