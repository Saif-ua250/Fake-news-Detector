# 🎯 QUICK START: Add Hugging Face Token (Optional)

## ⚠️ IMPORTANT: Token is OPTIONAL!

Your app **already works perfectly** without a token! Only add a token if you need:
- Private/gated models
- Faster downloads
- Higher rate limits

---

## 📍 Where to Add Your Token

### Location:
```
c:\Users\saif7\OneDrive\Desktop\Fake news Detector\.env
```

### What to Edit:

**BEFORE (default - no token):**
```bash
# Optional: Add your Hugging Face token here (without quotes)
# HUGGINGFACE_TOKEN=hf_your_token_here

# Leave blank to use models without authentication (public models work fine)
HUGGINGFACE_TOKEN=
```

**AFTER (with your token):**
```bash
# Optional: Add your Hugging Face token here (without quotes)
# HUGGINGFACE_TOKEN=hf_your_token_here

# Your token is now active!
HUGGINGFACE_TOKEN=hf_abcdefghijklmnopqrstuvwxyz1234567890
```

---

## 🔑 How to Get Your FREE Token

### Step-by-Step:

1. **Go to Hugging Face:**
   ```
   https://huggingface.co/
   ```

2. **Sign Up/Login:**
   - Click "Sign Up" (top right)
   - Use email or GitHub account
   - FREE forever!

3. **Go to Settings:**
   ```
   https://huggingface.co/settings/tokens
   ```

4. **Create New Token:**
   - Click "New token" button
   - Name: `truthlens-app` (or any name)
   - Type: **Read** (default is fine)
   - Click "Generate"

5. **Copy Token:**
   - Token looks like: `hf_xxxxxxxxxxxxxxxxxxxxx`
   - Click "Copy" icon
   - **Save it somewhere safe!**

6. **Paste in `.env` File:**
   - Open: `.env` in your project folder
   - Find line: `HUGGINGFACE_TOKEN=`
   - Paste your token: `HUGGINGFACE_TOKEN=hf_your_actual_token`
   - **Save the file**

7. **Restart App:**
   ```powershell
   # Stop app (Ctrl+C)
   # Restart:
   .\launch.ps1
   ```

**Done!** ✅ Your app now uses the token automatically!

---

## 🎨 Visual Guide

```
┌─────────────────────────────────────────────┐
│   .env File Structure                        │
├─────────────────────────────────────────────┤
│                                              │
│  # Hugging Face Configuration               │
│  # Get token: huggingface.co/settings/tokens│
│                                              │
│  ⬇️ PASTE YOUR TOKEN HERE ⬇️                 │
│  HUGGINGFACE_TOKEN=hf_YourTokenHere         │
│  ⬆️ PASTE YOUR TOKEN HERE ⬆️                 │
│                                              │
│  # Model Configuration                       │
│  TEXT_MODEL=jy46604790/Fake-News-Bert-Detect│
│  IMAGE_MODEL=prithivMLmods/Deep-Fake-...    │
│                                              │
└─────────────────────────────────────────────┘
```

---

## ⚡ Quick Test

After adding token, test it:

```powershell
# Test 1: Check if token is loaded
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Token Status:', 'ACTIVE ✅' if os.getenv('HUGGINGFACE_TOKEN') else 'NOT SET ⚠️')"

# Test 2: Try loading a model
python -c "from detectors import fake_news; print('Loading model...'); pipe = fake_news.load_text_model(); print('SUCCESS! ✅')"
```

---

## 🚫 Common Mistakes

### ❌ WRONG:
```bash
# With quotes (DON'T DO THIS):
HUGGINGFACE_TOKEN="hf_abc123"

# With spaces (DON'T DO THIS):
HUGGINGFACE_TOKEN = hf_abc123

# Commented out (DON'T DO THIS):
# HUGGINGFACE_TOKEN=hf_abc123
```

### ✅ CORRECT:
```bash
# No quotes, no spaces, not commented:
HUGGINGFACE_TOKEN=hf_abc123
```

---

## 🔄 What Happens After Adding Token

### Before Token:
```
Loading model...
Downloading from Hugging Face...
⏳ Slower download speeds
✅ Works fine, just takes longer
```

### After Token:
```
Loading model...
Using Hugging Face authentication token ✅
Downloading from Hugging Face...
⚡ Faster download speeds
🔓 Access to private models
✅ Better rate limits
```

---

## 📝 Example `.env` File

Here's a complete example:

```bash
# ================================================
# Hugging Face Configuration for TRUTH LENS
# ================================================

# Your Hugging Face Token (Optional but recommended)
# Get free token: https://huggingface.co/settings/tokens
# Benefits: Faster downloads, private models, no rate limits
HUGGINGFACE_TOKEN=hf_abcdefghijklmnopqrstuvwxyz1234567890

# AI Model Configuration
# Browse models: https://huggingface.co/models
TEXT_MODEL=jy46604790/Fake-News-Bert-Detect
IMAGE_MODEL=prithivMLmods/Deep-Fake-Detector-v2-Model

# ================================================
# That's it! Save and restart app with .\launch.ps1
# ================================================
```

---

## 🎯 Different Scenarios

### Scenario 1: No Token (Current Setup)
```bash
HUGGINGFACE_TOKEN=
```
**Result:** ✅ Works perfectly! Uses public models without authentication.

### Scenario 2: With Token (Enhanced)
```bash
HUGGINGFACE_TOKEN=hf_YourActualToken
```
**Result:** ✅ Faster downloads + access to private models!

### Scenario 3: Different Models
```bash
HUGGINGFACE_TOKEN=hf_YourToken
TEXT_MODEL=hamzab/roberta-fake-news-classification
IMAGE_MODEL=dima806/deepfake_vs_real_image_detection
```
**Result:** ✅ Uses your custom models!

---

## 🆘 Troubleshooting

### Problem: "Token not working"

**Check 1:** File saved?
```powershell
# View .env file:
type .env
```

**Check 2:** Token format correct?
```bash
# Should start with hf_:
HUGGINGFACE_TOKEN=hf_...
```

**Check 3:** App restarted?
```powershell
# Restart required after .env changes:
.\launch.ps1
```

### Problem: "Module 'dotenv' not found"

**Solution:**
```powershell
pip install python-dotenv
```

### Problem: "403 Forbidden"

**Cause:** Model is private/gated

**Solution:** 
1. Visit model page on Hugging Face
2. Click "Request Access" if needed
3. Add your token to `.env`
4. Restart app

---

## 💡 Pro Tips

1. **Keep Token Private:** Never share or commit to GitHub
2. **Use Read-Only:** Don't need write permissions
3. **Multiple Tokens:** Create different tokens for different projects
4. **Regenerate if Exposed:** Can delete and create new token anytime
5. **Monitor Usage:** Check https://huggingface.co/settings/tokens

---

## 📞 Need Help?

### Can't find `.env` file?
```powershell
# Navigate to project:
cd "c:\Users\saif7\OneDrive\Desktop\Fake news Detector"

# List all files (including hidden):
ls -Force

# Open in notepad:
notepad .env
```

### Token not loading?
```powershell
# Test environment loading:
python -c "from dotenv import load_dotenv; import os; load_dotenv(); token = os.getenv('HUGGINGFACE_TOKEN'); print(f'Token length: {len(token) if token else 0}')"
```

---

## ✅ Summary

**Your app is fully functional WITHOUT a token!**

**To add token (optional):**
1. Get from: https://huggingface.co/settings/tokens
2. Open: `.env` file in project folder
3. Edit: `HUGGINGFACE_TOKEN=hf_YourToken`
4. Save file
5. Restart: `.\launch.ps1`

**That's all!** 🚀

---

**See detailed guide:** `HUGGINGFACE_API_GUIDE.md`
