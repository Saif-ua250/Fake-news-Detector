# 🚀 QUICK START GUIDE - NEURO-VERIFY AI Frontend

## ⚡ 5-Minute Setup

### Step 1: Navigate to Frontend Directory
```powershell
cd "C:\Users\saif7\OneDrive\Desktop\Fake news Detector\frontend"
```

### Step 2: Install Dependencies
```powershell
npm install
```
*This will install all React, TypeScript, Tailwind, and animation libraries (~2-3 minutes)*

### Step 3: Start Development Server
```powershell
npm run dev
```

### Step 4: Open Browser
Navigate to: **http://localhost:3000**

---

## 🎯 What You'll See

### Landing Page (Home)
- **NEURO-VERIFY AI** glowing title
- Animated hexagon grid background
- Scan line effect moving down screen
- URL input box with holographic glow
- "ANALYZE NOW" button with neon effects

### Results Dashboard
- Circular trust score (0-100%)
- Pentagon radar chart
- Three columns:
  - 🧩 Claim Reviews
  - ⚡ ClaimBuster Sentences
  - 🛡️ Source Reputation (VirusTotal)

---

## 🔧 Configuration

### Backend API Connection

The frontend expects a backend at `http://localhost:8000/api/analyze`

**To change backend URL**, edit `vite.config.ts`:

```typescript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000', // ← Change this
      changeOrigin: true,
    },
  },
}
```

### Color Theme Customization

Edit `tailwind.config.js` → `theme.extend.colors`:

```javascript
'cyber-blue': '#00d4ff',    // Primary glow color
'cyber-cyan': '#00ffff',    // Secondary accents
'cyber-purple': '#b537ff',  // Highlights
```

---

## 🐛 Troubleshooting

### Issue: TypeScript Errors in VS Code
**Solution**: Run `npm install` first. Errors will disappear once dependencies are installed.

### Issue: "Cannot connect to backend"
**Solution**: 
1. Verify backend is running on port 8000
2. Check `vite.config.ts` proxy settings
3. Ensure backend has CORS enabled

### Issue: Slow Animations
**Solution**: Reduce animation complexity in `HexGridBackground.tsx`:
```typescript
const hexRadius = 40 // ← Decrease to 30
```

### Issue: Build Fails
**Solution**:
```powershell
rm -r node_modules
rm package-lock.json
npm install
npm run build
```

---

## 📱 Testing on Mobile

1. Start dev server: `npm run dev`
2. Note the **Network URL** (e.g., `http://192.168.1.x:3000`)
3. Open that URL on mobile device (same WiFi network)

---

## 🎨 Key Files to Customize

| File | Purpose |
|------|---------|
| `src/pages/Home.tsx` | Landing page layout |
| `src/pages/Results.tsx` | Results dashboard |
| `tailwind.config.js` | Colors, fonts, animations |
| `src/components/HexGridBackground.tsx` | Background animation |
| `src/hooks/useAnalyzeAPI.ts` | API integration |

---

## 🚀 Production Build

```powershell
# Create optimized build
npm run build

# Output: dist/ folder

# Preview build locally
npm run preview
```

**Deploy** the `dist/` folder to:
- Vercel
- Netlify
- AWS S3 + CloudFront
- Any static hosting service

---

## 📊 Performance Targets

- ✅ Lighthouse Performance: 90+
- ✅ First Contentful Paint: < 1.5s
- ✅ Time to Interactive: < 3s
- ✅ Bundle Size: ~500KB gzipped

---

## 💡 Pro Tips

1. **Disable animations on low-end devices**: Comment out `<ScanLine />` in `App.tsx`
2. **Use React DevTools**: Install browser extension for debugging
3. **Hot reload**: Saves auto-refresh browser during development
4. **TypeScript autocomplete**: VS Code provides full IntelliSense for all components

---

## 🎯 Next Steps After Setup

1. **Test URL Analysis**: Enter any news URL and click "ANALYZE NOW"
2. **Inspect Results**: Check all three data columns render correctly
3. **Test Error Handling**: Try invalid URL to see glitch error popup
4. **Customize Colors**: Tweak `cyber-blue` in tailwind config
5. **Add Backend**: Connect to your FastAPI `/api/analyze` endpoint

---

## 📞 Need Help?

- Check `README.md` for full documentation
- Review component comments (TSDoc format)
- Inspect browser console for errors
- Verify backend API response format matches `AnalysisResponse` type

---

**You're all set! Open http://localhost:3000 and enjoy your Hollywood-level sci-fi interface! 🚀✨**
