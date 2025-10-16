# 🤖 Hugging Face API Integration Guide

## How AI Models Work in This App

Your app uses **Hugging Face Transformers** for AI-powered detection. There are **two ways** to use Hugging Face models:

---

## ✅ Option 1: Direct Model Access (Current - FREE) 

**Status:** ✅ Already configured and working!

### How It Works:
- Models download **automatically** on first use
- Stored locally in: `C:\Users\saif7\.cache\huggingface\`
- **No API key needed** for public models
- **100% FREE** forever
- Works **offline** after first download

### What Happens:
1. First time you analyze text → Downloads text model (~500 MB)
2. First time you analyze image/video → Downloads image model (~500 MB)
3. Models cached locally → Instant loading next time
4. No internet needed after initial download (except URL scraping)

---

## 🔑 Option 2: Using Hugging Face API Token (Optional)

### When You Need a Token:
- ✅ Using **private/gated models**
- ✅ Avoiding **rate limits** on heavy usage
- ✅ Accessing **premium models**
- ✅ Better **download speeds**

### How to Add Your Token:

#### Step 1: Get Your FREE Token

1. **Sign up** at: https://huggingface.co/
2. Go to **Settings** → **Access Tokens**
3. Click **"New token"**
4. Name it: `truthlens-app`
5. Permissions: Select **"Read"**
6. Click **"Generate"**
7. **Copy** your token (starts with `hf_...`)

#### Step 2: Add Token to `.env` File

Open the **`.env`** file in your project folder:

```
c:\Users\saif7\OneDrive\Desktop\Fake news Detector\.env
```

Edit this line:
```bash
# Before:
HUGGINGFACE_TOKEN=

# After (paste your token):
HUGGINGFACE_TOKEN=hf_YourActualTokenHere
```

#### Step 3: Restart the App

```powershell
# Stop the current app (Ctrl+C in terminal)
# Then restart:
.\launch.ps1
```

**That's it!** The app will now use your token automatically.

---

## 🔄 Changing AI Models

You can use **any** Hugging Face model! Edit the `.env` file:

### For Text Detection (Fake News):
```bash
# Current model:
TEXT_MODEL=jy46604790/Fake-News-Bert-Detect

# Alternative models:
TEXT_MODEL=hamzab/roberta-fake-news-classification
TEXT_MODEL=mrm8488/bert-mini-finetuned-fake-news-detection
```

### For Image/Video Detection (Deepfake):
```bash
# Current model:
IMAGE_MODEL=prithivMLmods/Deep-Fake-Detector-v2-Model

# Alternative models:
IMAGE_MODEL=dima806/deepfake_vs_real_image_detection
IMAGE_MODEL=umm-maybe/AI-image-detector
```

**Browse models at:** https://huggingface.co/models

---

## 🧪 Testing Your Configuration

### Test 1: Check if .env is loaded

```powershell
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Token:', 'SET' if os.getenv('HUGGINGFACE_TOKEN') else 'NOT SET')"
```

### Test 2: Test model loading with token

```powershell
python -c "from detectors import fake_news; pipe = fake_news.load_text_model(); print('Model loaded successfully!')"
```

---

## 📁 File Locations

### Configuration File:
```
c:\Users\saif7\OneDrive\Desktop\Fake news Detector\.env
```

### Code Files (where token is used):
```
detectors/fake_news.py    - Text detection model
detectors/deepfake.py     - Image/video detection model
app.py                    - Main application
```

### Cached Models:
```
C:\Users\saif7\.cache\huggingface\hub\
```

---

## 🛠️ Advanced Configuration

### Using Different Devices:

Edit `app.py` and change device settings:

```python
# CPU (default - works everywhere)
device = -1

# GPU (if you have NVIDIA GPU with CUDA)
device = 0

# Multiple GPUs
device = 1  # second GPU
```

### Using Local Models:

If you download models manually:

```bash
# In .env file:
TEXT_MODEL=/path/to/local/model/folder
```

---

## 🔍 Troubleshooting

### Issue 1: "403 Forbidden" Error

**Cause:** Model is private/gated or rate-limited

**Solution:** 
1. Get Hugging Face token (see Step 1 above)
2. Add to `.env` file
3. Restart app

### Issue 2: "Token not found" Error

**Cause:** `.env` file not loaded

**Solution:**
```powershell
# Reinstall python-dotenv:
pip install python-dotenv

# Verify .env file exists:
ls .env
```

### Issue 3: Slow Model Downloads

**Cause:** No token = slower download servers

**Solution:** Add token for faster downloads

### Issue 4: Models Won't Download

**Cause:** Internet connection or firewall

**Solution:**
```powershell
# Test connection:
ping huggingface.co

# Check firewall:
# Allow Python in Windows Firewall

# Try manual download:
python -c "from transformers import pipeline; pipeline('text-classification', model='jy46604790/Fake-News-Bert-Detect')"
```

---

## 📊 Token Usage Monitoring

### Check Your Token Usage:

1. Go to: https://huggingface.co/settings/tokens
2. View your tokens
3. See usage statistics

### Free Tier Limits:
- ✅ Unlimited public model downloads
- ✅ Unlimited local model usage
- ✅ No rate limits with token

---

## 🌟 Best Practices

### Security:
- ✅ **Never commit** `.env` to Git
- ✅ Keep token **private**
- ✅ Use **read-only** tokens
- ✅ Regenerate if exposed

### Performance:
- ✅ Download models once, use offline
- ✅ Use token for faster downloads
- ✅ Cache models locally
- ✅ Use CPU for compatibility, GPU for speed

### Model Selection:
- ✅ Test different models for accuracy
- ✅ Choose lighter models for speed
- ✅ Use specialized models for specific tasks

---

## 🎯 Quick Reference

### Current Configuration:
```bash
# Text Model (Fake News Detection)
jy46604790/Fake-News-Bert-Detect

# Image Model (Deepfake Detection)
prithivMLmods/Deep-Fake-Detector-v2-Model

# Token: Not required (optional)
# Works: ✅ Yes, fully functional
```

### To Add Token:
1. Get from: https://huggingface.co/settings/tokens
2. Edit: `.env` file
3. Add line: `HUGGINGFACE_TOKEN=hf_YourToken`
4. Restart: `.\launch.ps1`

### To Change Models:
1. Browse: https://huggingface.co/models
2. Edit: `.env` file
3. Update: `TEXT_MODEL=` or `IMAGE_MODEL=`
4. Restart: `.\launch.ps1`

---

## ❓ FAQ

**Q: Do I need a Hugging Face account?**  
A: No, for public models. Yes, for private models or better speeds.

**Q: Is Hugging Face free?**  
A: Yes! Free tier includes unlimited model downloads.

**Q: Will my token expire?**  
A: No, tokens don't expire unless you delete them.

**Q: Can I use multiple tokens?**  
A: Yes, but only one per app. Good for team setups.

**Q: What if I exceed rate limits?**  
A: Add a token to remove most limits. Free tier is generous.

**Q: Can I use paid models?**  
A: Some models require subscriptions. Check model page.

**Q: How do I know if a model needs a token?**  
A: Gated models show "Request Access" button on Hugging Face.

---

## 📞 Support

### Hugging Face Resources:
- 📚 Docs: https://huggingface.co/docs
- 🤝 Forum: https://discuss.huggingface.co/
- 💬 Discord: https://discord.gg/hugging-face

### Project Documentation:
- `README.md` - Project overview
- `INSTALLATION_COMPLETE.md` - Setup guide
- `HOW_TO_RUN.md` - Usage instructions

---

## ✅ Summary

**Current Status:** ✅ Your app works perfectly **WITHOUT a token!**

**To add token (optional):**
1. Get token from https://huggingface.co/settings/tokens
2. Edit `.env` file: `HUGGINGFACE_TOKEN=hf_YourToken`
3. Restart app: `.\launch.ps1`

**That's it!** Your AI integration is complete! 🎉
