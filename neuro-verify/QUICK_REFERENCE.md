# 🚀 NEURO-VERIFY AI - Quick Reference Card

## ⚡ Instant Commands

```powershell
# Setup & Run (Automated)
.\setup-and-run.ps1

# Manual Setup
npm install
npm run dev

# Build for Production
npm run build
npm run preview

# Code Quality
npm run lint
npm run format
```

---

## 🎨 Design Tokens Cheat Sheet

```css
/* Copy-paste into your code */
bg-bg                    /* #0A0F14 - Main background */
bg-panel                 /* #0F1720 - Card background */
text-neon-primary        /* #00E5FF - Cyan text */
text-neon-accent         /* #7C4DFF - Purple text */
border-glass-border      /* rgba(0,229,255,0.12) - Borders */

/* Spacing */
gap-3    /* 12px */
p-4      /* 16px padding */
m-6      /* 24px margin */

/* Shadows */
shadow-neon-primary      /* Cyan glow */
shadow-neon-accent       /* Purple glow */
shadow-glow              /* Intense glow */

/* Transitions */
transition-fast          /* 160ms */
transition-medium        /* 320ms */
transition-slow          /* 680ms */
ease-sci-fi              /* cubic-bezier(.16,.84,.26,1) */
```

---

## 🧩 Component Import Quick Reference

```typescript
// Buttons
import { Button } from '@/components/Button';
<Button variant="primary" size="lg" onClick={handleClick}>
  ANALYZE
</Button>

// Variants: 'primary' | 'secondary' | 'ghost' | 'danger' | 'icon' | 'fab'
// Sizes: 'sm' | 'md' | 'lg'

// API Client
import { analyzeUrl } from '@/api/client';
const result = await analyzeUrl('https://example.com');

// Types
import type { AnalyzeResponse, ApiError, LoadingState } from '@/types';
```

---

## 📁 File Locations

| What | Where |
|------|-------|
| **Components** | `src/components/*.tsx` |
| **API Client** | `src/api/client.ts` |
| **Types** | `src/types/index.ts` |
| **Global Styles** | `src/index.css` |
| **Tailwind Config** | `tailwind.config.js` |
| **Vite Config** | `vite.config.ts` |
| **Environment** | `.env` (create this) |

---

## 🔌 API Integration

```typescript
// POST /api/analyze
{
  "url": "https://example.com/article"
}

// Response
{
  "trust_score": 75,        // 0-100
  "explanation": "...",
  "claim_reviews": [...],
  "claimbuster": {...},
  "virustotal": {...}
}
```

### Configure Backend URL
```env
# .env file
VITE_API_BASE_URL=http://localhost:8000
```

---

## 🎯 Common Tasks

### Add New Component
```powershell
# Create file: src/components/MyComponent.tsx
```

```typescript
import { motion } from 'framer-motion';

export default function MyComponent() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.32 }}
      className="glass-panel p-6 rounded-xl"
    >
      {/* Your content */}
    </motion.div>
  );
}
```

### Add Animation
```typescript
<motion.div
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  transition={{ duration: 0.16 }}
>
  {/* Element */}
</motion.div>
```

### Add Responsive Classes
```typescript
<div className="
  w-full                  // Mobile: full width
  md:w-1/2                // Tablet: half width
  lg:w-1/3                // Desktop: third width
  p-4 md:p-6 lg:p-8       // Responsive padding
">
  {/* Content */}
</div>
```

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port 3000 in use** | Change port in `vite.config.ts` |
| **Dependencies fail** | `npm cache clean --force` then reinstall |
| **TypeScript errors** | Run `npm install` first |
| **Blank screen** | Check console (F12), hard refresh (Ctrl+Shift+R) |
| **API errors** | Check backend is running, verify `.env` |

---

## 📱 Access URLs

```
Computer:  http://localhost:3000
Phone:     http://YOUR_IP:3000
Preview:   http://localhost:4173 (after npm run build)
```

Find YOUR_IP:
```powershell
ipconfig
# Look for IPv4 Address
```

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Navigate elements |
| `Enter` / `Space` | Activate button |
| `Esc` | Close modal |
| `Ctrl+Shift+R` | Hard refresh browser |
| `F12` | Open dev tools |

---

## 🎨 Utility Classes

```css
/* Glass Effect */
.glass-panel              /* Pre-built glass morphism */

/* Gradient Text */
.gradient-text            /* Cyan → Purple gradient */

/* Neon Glow */
.neon-glow                /* Text shadow glow effect */

/* Animations */
.animate-float            /* Floating Y-axis */
.animate-pulse-glow       /* Pulsing glow */
.animate-spin             /* Rotation */

/* Background */
.honeycomb-bg             /* Honeycomb SVG pattern */
```

---

## 📊 Performance Checklist

- [ ] Images compressed (WebP)
- [ ] Lazy load non-critical components
- [ ] Use `React.memo` for expensive renders
- [ ] Avoid inline functions in JSX
- [ ] Use `useMemo` / `useCallback` when needed
- [ ] Code split with dynamic `import()`
- [ ] Minify production build

---

## 🔒 Accessibility Checklist

- [ ] All buttons have `aria-label`
- [ ] Focus visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Esc)
- [ ] Color contrast ≥4.5:1
- [ ] Use semantic HTML (`<button>`, `<nav>`, `<main>`)
- [ ] `alt` text on all images
- [ ] `aria-live` regions for dynamic content

---

## 📚 Documentation Links

- [Full README](./README.md)
- [Setup Guide](./SETUP_GUIDE.md)
- [Layout Guide](./LAYOUT_GUIDE.md)
- [Project Summary](./PROJECT_SUMMARY.md)

---

## 🎓 Learning Path

1. **Start**: Run `.\setup-and-run.ps1`
2. **Explore**: Open `src/App.tsx` and read comments
3. **Customize**: Edit `src/components/HeroPanel.tsx`
4. **Theme**: Modify `tailwind.config.js` colors
5. **API**: Update `src/api/client.ts` endpoint
6. **Build**: Run `npm run build` and check `dist/`

---

## 💡 Pro Tips

1. **Hot Reload**: Save files to see instant changes
2. **DevTools**: Use React DevTools extension
3. **TypeScript**: Hover over variables to see types
4. **Tailwind**: Use IntelliSense for class autocomplete
5. **Animations**: Use `prefers-reduced-motion` media query
6. **Errors**: Check both terminal AND browser console

---

## 📞 Quick Help

```powershell
# Check versions
node --version
npm --version

# Clear cache
npm cache clean --force

# Reinstall everything
Remove-Item -Recurse node_modules, package-lock.json
npm install

# Check for updates
npm outdated

# Update dependencies
npm update
```

---

## 🎯 Next Steps

1. ✅ Run `npm install`
2. ✅ Start with `npm run dev`
3. ✅ Open http://localhost:3000
4. ✅ Test URL input
5. ✅ Check mobile responsive
6. ✅ Review component code
7. ✅ Customize colors
8. ✅ Deploy to production

---

**Keep this card handy for quick reference!** 📌

*NEURO-VERIFY AI - Built for developers, designed for users* 🚀
