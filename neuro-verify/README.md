# NEURO-VERIFY AI 🚀

**Premium Sci-Fi URL Fake News Analyzer** - Hollywood-grade UI/UX with production-ready TypeScript + React

A visually striking, fully accessible, and responsive fake news analysis platform featuring neon/honeycomb sci-fi aesthetics, professional polish, and zero runtime errors.

---

## ✨ Features

- 🎬 **Hollywood-Grade UI/UX** - Premium sci-fi design with neon gradients, glassmorphism, and animated effects
- 🔒 **Fully Accessible** - WCAG AA compliant with keyboard navigation and screen reader support
- 📱 **Responsive Design** - Mobile → Tablet → Desktop → 4K (breakpoints: 640px, 1024px, 1440px+)
- ⚡ **Zero Console Errors** - Production-ready with complete TypeScript typing
- 🎨 **Custom Design System** - Comprehensive button variants, animations, and reusable components
- 🔄 **Retry Logic** - Exponential backoff for failed API requests (max 3 attempts)
- 🎭 **Framer Motion** - Smooth sci-fi animations with `cubic-bezier(.16,.84,.26,1)` easing
- 📊 **Trust Score Visualization** - Animated radar charts and progress indicators
- 🌐 **API Integration** - Connects to backend POST `/api/analyze` endpoint

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | React 18, TypeScript, Vite |
| **Styling** | TailwindCSS, PostCSS, Custom CSS Variables |
| **Animation** | Framer Motion |
| **Charts** | Recharts |
| **HTTP Client** | Axios |
| **Testing** | Vitest |
| **Linting** | ESLint, Prettier |

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** >= 18.0.0
- **npm** >= 9.0.0 or **yarn** >= 1.22.0
- Backend API running on `http://localhost:8000` (or configure `VITE_API_BASE_URL`)

### Installation

```powershell
# Navigate to project directory
cd neuro-verify

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will be available at **http://localhost:3000**

---

## 📦 Available Scripts

```powershell
# Development
npm run dev          # Start Vite dev server with hot reload

# Production Build
npm run build        # TypeScript check + production build
npm run preview      # Preview production build locally

# Code Quality
npm run lint         # Run ESLint checks
npm run format       # Format code with Prettier

# Testing
npm run test         # Run Vitest unit tests
```

---

## 🎨 Design System

### Color Palette

```css
--bg: #0A0F14                      /* Deep space black */
--panel: #0F1720                   /* Panel slate */
--glass: rgba(255,255,255,0.04)    /* Glass overlay */
--neon-primary: #00E5FF            /* Electric cyan */
--neon-accent: #7C4DFF             /* Electric purple */
--neon-warn: #FF6B35               /* Amber alert */
--text-primary: #E6F7FF            /* Pale cyan */
--muted: #99A3AD                   /* Muted gray */
--glass-border: rgba(0,229,255,0.12) /* Subtle neon border */
```

### Typography

- **Headlines**: `Orbitron, Rajdhani, sans-serif` (weight: 700)
- **Body**: `Inter, system-ui, sans-serif` (weight: 400-600)

### Animation Timing

- **Fast**: 160ms (buttons, hover states)
- **Medium**: 320ms (cards, lists)
- **Slow**: 680ms (background, holographic effects)
- **Easing**: `cubic-bezier(.16,.84,.26,1)` (smooth sci-fi feel)

### Button Variants

| Variant | Use Case | Example |
|---------|----------|---------|
| `primary` | Main actions | Analyze button |
| `secondary` | Supporting actions | Share, Copy |
| `ghost` | Inline actions | View Details |
| `danger` | Destructive actions | Delete |
| `icon` | Icon-only buttons | Settings, History |
| `fab` | Floating action button | Quick analyze |

---

## 🔌 API Integration

### Backend Endpoint

```typescript
POST /api/analyze
Content-Type: application/json

{
  "url": "https://example.com/article"
}
```

### Response Type

```typescript
interface AnalyzeResponse {
  url: string;
  title?: string;
  snippet?: string;
  publish_date?: string;
  author?: string;
  claim_reviews: ClaimReview[];
  claimbuster: { top_sentences: ClaimBusterSentence[] };
  virustotal: VirusTotalSummary | null;
  source_reputation?: SourceReputation;
  trust_score: number; // 0-100
  explanation: string;
}
```

### Environment Configuration

Create `.env` file in project root:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

## 📁 Project Structure

```
neuro-verify/
├── src/
│   ├── api/
│   │   └── client.ts           # API client with retry logic
│   ├── components/
│   │   ├── Button.tsx          # Button component system
│   │   ├── Header.tsx          # Fixed top navigation
│   │   ├── HeroPanel.tsx       # URL input panel
│   │   ├── ResultsDashboard.tsx # Analysis results
│   │   ├── TrustScoreGauge.tsx # Animated trust score
│   │   ├── ClaimReviewCard.tsx # Claim review list item
│   │   ├── BackgroundEffects.tsx # Sci-fi backgrounds
│   │   ├── ErrorModal.tsx      # Error handling modal
│   │   └── Footer.tsx          # App footer
│   ├── types/
│   │   └── index.ts            # TypeScript definitions
│   ├── App.tsx                 # Main app component
│   ├── main.tsx                # React entry point
│   └── index.css               # Global styles
├── public/                     # Static assets
├── index.html                  # HTML template
├── package.json                # Dependencies
├── tsconfig.json               # TypeScript config
├── vite.config.ts              # Vite configuration
├── tailwind.config.js          # Tailwind theme
├── postcss.config.js           # PostCSS config
└── README.md                   # This file
```

---

## 🎯 Accessibility Features

- ✅ **Keyboard Navigation** - All interactive elements reachable via Tab
- ✅ **Focus Indicators** - Visible focus outlines (WCAG 2.1 AA)
- ✅ **ARIA Labels** - Screen reader support for all actions
- ✅ **Color Contrast** - Minimum 4.5:1 for normal text
- ✅ **Semantic HTML** - Proper landmarks and headings
- ✅ **Live Regions** - `aria-live="polite"` for dynamic content
- ✅ **Modal Focus Trap** - ESC to close, focus restoration
- ✅ **Reduced Motion** - Respects `prefers-reduced-motion`

---

## 🧪 Testing

```powershell
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch

# Generate coverage report
npm run test:coverage
```

---

## 📊 Performance Targets

| Metric | Target | Actual |
|--------|--------|--------|
| Lighthouse Performance | ≥85 | 🎯 |
| Accessibility | ≥90 | 🎯 |
| Best Practices | ≥90 | 🎯 |
| First Contentful Paint | <1.5s | 🎯 |
| Time to Interactive | <3.5s | 🎯 |

---

## 🚢 Production Build

```powershell
# Build for production
npm run build

# Output directory: dist/
# Files are minified, code-split, and optimized
```

### Deployment

```powershell
# Preview production build locally
npm run preview

# Deploy to static hosting (Netlify, Vercel, AWS S3, etc.)
# Just upload the dist/ folder
```

---

## 🐛 Troubleshooting

### Port Already in Use

```powershell
# Change port in vite.config.ts or use environment variable
PORT=3001 npm run dev
```

### TypeScript Errors

```powershell
# Check TypeScript configuration
npx tsc --noEmit

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Build Fails

```powershell
# Clear Vite cache
rm -rf node_modules/.vite
npm run build
```

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 💬 Support

For issues, questions, or feature requests, please open an issue on GitHub.

---

**Built with ❤️ using React, TypeScript, and Tailwind CSS**

*NEURO-VERIFY AI - Truth in the age of misinformation*
