# 🚀 NEURO-VERIFY AI - Complete Setup Guide

## Step-by-Step Installation & Launch Instructions

This guide will walk you through setting up and running the NEURO-VERIFY AI frontend from scratch.

---

## 📋 Prerequisites Check

Before starting, ensure you have:

1. **Node.js** installed (version 18.0.0 or higher)
   ```powershell
   node --version
   # Should output: v18.x.x or higher
   ```

2. **npm** installed (usually comes with Node.js)
   ```powershell
   npm --version
   # Should output: 9.x.x or higher
   ```

3. **Backend API** running (optional for development)
   - Default expects backend at `http://localhost:8000`
   - You can configure this later with environment variables

---

## 🎯 Quick Start (3 Commands)

Open PowerShell in the `neuro-verify` directory and run:

```powershell
# 1. Install all dependencies
npm install

# 2. Start development server
npm run dev

# 3. Open browser to http://localhost:3000
```

**That's it!** The app should now be running.

---

## 📦 Detailed Installation Steps

### Step 1: Navigate to Project Directory

```powershell
cd "c:\Users\saif7\OneDrive\Desktop\Fake news Detector\neuro-verify"
```

### Step 2: Install Dependencies

This will install all required packages (React, TypeScript, Tailwind, Framer Motion, etc.):

```powershell
npm install
```

**Expected output:**
```
added 523 packages, and audited 524 packages in 45s
```

**Troubleshooting:**
- If you see `WARN` messages, that's normal
- If you see `ERR!` messages:
  - Try deleting `node_modules` and `package-lock.json`
  - Run `npm install` again
  - Check internet connection

### Step 3: Configure Environment (Optional)

Create a `.env` file in the `neuro-verify` directory to configure the backend API URL:

```powershell
# Create .env file
New-Item .env -ItemType File

# Add API URL (edit this file with Notepad)
notepad .env
```

Add this line to `.env`:
```
VITE_API_BASE_URL=http://localhost:8000
```

**Default values if you skip this step:**
- API URL: `http://localhost:8000`

### Step 4: Start Development Server

```powershell
npm run dev
```

**Expected output:**
```
VITE v5.0.12  ready in 1234 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: http://192.168.0.100:3000/
  ➜  press h to show help
```

### Step 5: Open in Browser

Open your browser and navigate to:
- **Computer**: http://localhost:3000
- **Phone (same WiFi)**: http://192.168.0.100:3000

---

## 🎨 What You Should See

After launching, you should see:

1. ✨ **Animated Header** with "NEURO-VERIFY AI" logo
2. 🌌 **Honeycomb Background Pattern** (subtle, sci-fi)
3. 💎 **Glass Panel Hero Section** with URL input
4. 🔍 **"ANALYZE" Button** with neon gradient
5. ⚡ **Smooth Animations** when hovering over elements

---

## 🛠️ Development Commands

### Hot Reload Development

```powershell
npm run dev
```
- Starts server at http://localhost:3000
- **Auto-reloads** when you save files
- Press `q` to quit
- Press `r` to restart
- Press `o` to open browser

### Production Build

```powershell
npm run build
```
- Creates optimized build in `dist/` folder
- Minifies JavaScript and CSS
- Code-splits for faster loading
- Output is ready for deployment

### Preview Production Build

```powershell
npm run preview
```
- Previews the production build locally
- Runs on http://localhost:4173

### Lint Code

```powershell
npm run lint
```
- Checks for TypeScript errors
- Checks for code style issues
- Shows warnings and errors

### Format Code

```powershell
npm run format
```
- Auto-formats all `.ts`, `.tsx`, `.css` files
- Uses Prettier configuration

---

## 🔌 Connecting to Backend

### Backend Requirements

Your backend must have a `POST /api/analyze` endpoint that:

1. **Accepts JSON**:
   ```json
   {
     "url": "https://example.com/article"
   }
   ```

2. **Returns JSON** (see types in `src/types/index.ts`):
   ```json
   {
     "url": "...",
     "trust_score": 75,
     "explanation": "...",
     "claim_reviews": [...],
     "claimbuster": {...},
     "virustotal": {...}
   }
   ```

### Testing Without Backend

The frontend will show a network error modal if the backend isn't running. To test the UI:

1. Comment out the API call in `src/App.tsx`
2. Use mock data for development
3. Or run the Streamlit backend from the parent directory

---

## 📱 Accessing on Phone

### Same WiFi Required

1. **Find your computer's local IP**:
   ```powershell
   ipconfig
   # Look for "IPv4 Address" under your WiFi adapter
   # Example: 192.168.0.100
   ```

2. **Start the dev server**:
   ```powershell
   npm run dev
   ```

3. **On your phone's browser**, navigate to:
   ```
   http://YOUR_IP:3000
   # Example: http://192.168.0.100:3000
   ```

### Firewall Issues

If phone can't connect:

```powershell
# Allow Node.js through Windows Firewall (run as Administrator)
New-NetFirewallRule -DisplayName "Node.js Dev Server" -Direction Inbound -Program "C:\Program Files\nodejs\node.exe" -Action Allow
```

---

## 🐛 Common Issues & Solutions

### Issue: Port 3000 Already in Use

**Solution 1** - Kill existing process:
```powershell
# Find process using port 3000
netstat -ano | findstr :3000

# Kill process (replace PID with actual number)
taskkill /PID <PID> /F
```

**Solution 2** - Use different port:
```powershell
# Edit vite.config.ts, change:
server: {
  port: 3001,  # Change to any available port
}
```

### Issue: Dependencies Not Installing

```powershell
# Clear npm cache
npm cache clean --force

# Delete node_modules and lock file
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json

# Reinstall
npm install
```

### Issue: TypeScript Errors

```powershell
# Check TypeScript configuration
npx tsc --noEmit

# If errors persist, check:
# 1. Node version (should be 18+)
node --version

# 2. TypeScript version
npx tsc --version
```

### Issue: Blank White Screen

**Check browser console** (Press F12):

1. **Red errors?** - Check the error message
2. **No errors?** - Hard refresh: `Ctrl + Shift + R`
3. **Still blank?** - Check if `dist/` folder exists (run `npm run build`)

---

## 🎯 Performance Tips

### Faster Development

```powershell
# Use --host flag to expose to network
npm run dev -- --host

# Use --open flag to auto-open browser
npm run dev -- --open
```

### Faster Builds

```powershell
# Build without source maps (smaller, faster)
npm run build -- --minify terser
```

---

## 📂 Project File Overview

```
neuro-verify/
├── src/                    # Source code
│   ├── api/               # API integration
│   ├── components/        # React components
│   ├── types/             # TypeScript types
│   ├── App.tsx            # Main app
│   ├── main.tsx           # Entry point
│   └── index.css          # Global styles
├── public/                # Static assets
├── dist/                  # Build output (after npm run build)
├── node_modules/          # Dependencies (after npm install)
├── index.html             # HTML template
├── package.json           # Project metadata
├── vite.config.ts         # Vite configuration
├── tsconfig.json          # TypeScript config
├── tailwind.config.js     # Tailwind theme
└── .env                   # Environment variables (create this)
```

---

## 🚀 Deployment Checklist

Before deploying to production:

- [ ] Run `npm run build` successfully
- [ ] Test production build with `npm run preview`
- [ ] Set `VITE_API_BASE_URL` to production backend URL
- [ ] Run `npm run lint` with no errors
- [ ] Test on multiple devices (mobile, tablet, desktop)
- [ ] Test with screen reader for accessibility
- [ ] Check Lighthouse scores (Performance ≥85)

---

## 📞 Getting Help

1. **Check the browser console** (F12 → Console tab)
2. **Check the terminal output** where `npm run dev` is running
3. **Read error messages carefully** - they usually tell you what's wrong
4. **Review the README.md** for API integration details

---

## ✅ Success Checklist

Your setup is complete when:

- [ ] `npm install` runs without errors
- [ ] `npm run dev` starts successfully
- [ ] Browser shows the NEURO-VERIFY AI interface
- [ ] Animations are smooth (no lag)
- [ ] Input field accepts text
- [ ] Button hover effects work
- [ ] Console has no red errors (F12)

---

**You're all set!** Enjoy building with NEURO-VERIFY AI 🎉

*For additional help, see README.md or check the component documentation in src/components/*
