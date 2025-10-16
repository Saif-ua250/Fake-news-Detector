# 🎨 NEURO-VERIFY AI - Visual Layout Guide

This document shows the exact layout structure and component placement.

---

## 📐 Desktop Layout (1440px)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         HEADER (72px, Fixed, Glass)                        │
│  [LOGO] NEURO-VERIFY AI              [History] [Settings] [Profile]       │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐ │
│  │              HERO PANEL (180px, Glass with Honeycomb)               │ │
│  │  ┌─────────────────────────────────────────┐  ┌─────────────────┐  │ │
│  │  │ 🔗 Paste article URL or drop link...    │  │  🔍 ANALYZE     │  │ │
│  │  │ [URL Input Field - 56px height]         │  │  [Neon Button]  │  │ │
│  │  └─────────────────────────────────────────┘  └─────────────────┘  │ │
│  │                                                                      │ │
│  │  [Last Analysis Quick Stat]                                         │ │
│  └──────────────────────────────────────────────────────────────────────┘ │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐ │
│  │                      RESULTS DASHBOARD                               │ │
│  │                                                                      │ │
│  │  ┌─────────────────────┐  ┌───────────────────────────────────────┐ │ │
│  │  │                     │  │  CLAIM REVIEWS                        │ │ │
│  │  │   TRUST SCORE       │  │  ┌─────────────────────────────────┐ │ │ │
│  │  │      GAUGE          │  │  │ ✓ Publisher: XYZ News           │ │ │ │
│  │  │                     │  │  │   Verdict: MIXED                │ │ │ │
│  │  │       [75]          │  │  │   "Article contains..."         │ │ │ │
│  │  │      ╱─────╲        │  │  └─────────────────────────────────┘ │ │ │
│  │  │     │       │       │  │  ┌─────────────────────────────────┐ │ │ │
│  │  │     │  75%  │       │  │  │ ✓ Publisher: ABC Fact           │ │ │ │
│  │  │     │       │       │  │  │   Verdict: FALSE                │ │ │ │
│  │  │      ╲─────╱        │  │  │   "Claims are not..."           │ │ │ │
│  │  │                     │  │  └─────────────────────────────────┘ │ │ │
│  │  │  [Explanation]      │  │                                       │ │ │
│  │  │                     │  │  CLAIMBUSTER TOP SENTENCES           │ │ │
│  │  │  [Why? Accordion]   │  │  ┌─────────────────────────────────┐ │ │ │
│  │  │                     │  │  │ "The president announced..."    │ │ │ │
│  │  └─────────────────────┘  │  │ [████████░░] 0.87               │ │ │ │
│  │                            │  └─────────────────────────────────┘ │ │ │
│  │                            │  ┌─────────────────────────────────┐ │ │ │
│  │                            │  │ "According to sources..."       │ │ │ │
│  │                            │  │ [██████░░░░] 0.65               │ │ │ │
│  │                            │  └─────────────────────────────────┘ │ │ │
│  │                            │                                       │ │ │
│  │                            │  SOURCE REPUTATION                   │ │ │
│  │                            │  ┌─────────────────────────────────┐ │ │ │
│  │                            │  │ Domain: example.com             │ │ │ │
│  │                            │  │ Age: 2,451 days                 │ │ │ │
│  │                            │  │ VirusTotal: 2/89 flagged        │ │ │ │
│  │                            │  │ Rating: ██████████ Trustworthy  │ │ │ │
│  │                            │  └─────────────────────────────────┘ │ │ │
│  │                            └───────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────────────────┘ │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                           FOOTER (48px, Thin)                              │
│   🤖 AI-Powered  ⚡ Real-Time  🔒 Secure  🌐 Open Source                   │
│   © 2025 NEURO-VERIFY AI • Built with React • Powered by Transformers     │
└────────────────────────────────────────────────────────────────────────────┘

                                                     [FAB Button]
                                                        ╱───╲
                                                       │  🔍 │  ← Floating
                                                        ╲───╱     64×64px
```

---

## 📱 Mobile Layout (375px)

```
┌──────────────────────────────┐
│         HEADER               │
│ [LOGO] NEURO-VERIFY         │
│           [≡] [Profile]      │
└──────────────────────────────┘

┌──────────────────────────────┐
│      HERO PANEL              │
│  ┌────────────────────────┐  │
│  │ 🔗 Paste URL...        │  │
│  │ [Input]                │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  🔍 ANALYZE            │  │
│  │  [Full Width Button]   │  │
│  └────────────────────────┘  │
└──────────────────────────────┘

┌──────────────────────────────┐
│    TRUST SCORE GAUGE         │
│       ╱─────╲                │
│      │       │               │
│      │  75%  │               │
│      │       │               │
│       ╲─────╱                │
│                              │
│  "Moderately trustworthy"    │
│  [▼ Why?]                    │
└──────────────────────────────┘

┌──────────────────────────────┐
│    CLAIM REVIEWS             │
│  ┌────────────────────────┐  │
│  │ ✓ Publisher XYZ        │  │
│  │   MIXED verdict        │  │
│  │   [▼ Details]          │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │ ✗ Publisher ABC        │  │
│  │   FALSE verdict        │  │
│  │   [▼ Details]          │  │
│  └────────────────────────┘  │
└──────────────────────────────┘

┌──────────────────────────────┐
│    CLAIMBUSTER               │
│  ┌────────────────────────┐  │
│  │ "The president..."     │  │
│  │ [████████░] 0.87       │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │ "According to..."      │  │
│  │ [██████░░░] 0.65       │  │
│  └────────────────────────┘  │
└──────────────────────────────┘

┌──────────────────────────────┐
│    SOURCE REPUTATION         │
│  ┌────────────────────────┐  │
│  │ Domain: example.com    │  │
│  │ Age: 2,451 days        │  │
│  │ VirusTotal: 2/89       │  │
│  │ Rating: Trustworthy    │  │
│  └────────────────────────┘  │
└──────────────────────────────┘

┌──────────────────────────────┐
│          FOOTER              │
│  🤖⚡🔒🌐                    │
│  © 2025 NEURO-VERIFY AI      │
└──────────────────────────────┘

                   [FAB]
                   ╱───╲
                  │  🔍 │
                   ╲───╱
```

---

## 🎨 Component Hierarchy

```
App
├── BackgroundEffects
│   ├── HoneycombPattern
│   ├── GridOverlay
│   └── ScanLine (animated)
│
├── Header (Fixed, z-50)
│   ├── Logo (Animated hexagon)
│   ├── BrandName
│   └── ActionIcons
│       ├── HistoryButton (Icon)
│       ├── SettingsButton (Icon)
│       └── ProfileButton (Icon)
│
├── Main (Container)
│   ├── HeroPanel
│   │   ├── URLInput (56px height)
│   │   ├── AnalyzeButton (Primary, lg)
│   │   └── LastAnalysisStat (Optional)
│   │
│   └── ResultsDashboard (Conditional)
│       ├── TrustScoreModule
│       │   ├── TrustScoreGauge (320px diameter)
│       │   │   ├── AnimatedArc
│       │   │   ├── CenterScore (0-100)
│       │   │   └── Label
│       │   ├── Explanation (1-2 lines)
│       │   └── WhyAccordion (Expandable)
│       │
│       └── DataPanels (Grid/Flex)
│           ├── ClaimReviewsList
│           │   └── ClaimReviewCard[] (Map)
│           │       ├── PublisherInfo
│           │       ├── VerdictBadge
│           │       ├── Summary
│           │       └── ExpandButton
│           │
│           ├── ClaimBusterList
│           │   └── SentenceCard[] (Map)
│           │       ├── SentenceText
│           │       ├── ProgressBar (0-1)
│           │       └── ActionButtons
│           │
│           └── ReputationPanel
│               ├── DomainInfo
│               ├── VirusTotalSummary
│               └── TrustMeter
│
├── Footer (48px)
│   ├── FeatureIcons
│   ├── Links
│   └── Copyright
│
└── ErrorModal (Conditional)
    ├── ModalOverlay (Backdrop)
    ├── ModalContent
    │   ├── ErrorIcon (Red neon)
    │   ├── ErrorMessage
    │   ├── ErrorDetails
    │   └── ActionButtons
    │       ├── CloseButton (Secondary)
    │       └── RetryButton (Primary)
    └── FocusTrap
```

---

## 📏 Exact Measurements

### Header
- **Height**: 72px fixed
- **Logo**: 44×44px (animated rotation)
- **Icon Buttons**: 56×56px circular
- **Padding**: 24px horizontal
- **Background**: Glass with blur(24px)

### Hero Panel
- **Height**: 140-180px (responsive)
- **Input Height**: 56px
- **Button Height**: 56px
- **Border Radius**: 12px
- **Gap**: 12px between elements
- **Desktop**: Input 65% width, Button 35%
- **Mobile**: Full width stacked, 12px margin-top

### Trust Score Gauge
- **Diameter**: 320px (desktop), 220px (tablet), 160px (mobile)
- **Stroke Width**: 12px
- **Animation**: 0→value in 680ms spring
- **Center Number**: 4rem font, 800 weight

### Claim Review Card
- **Height**: Auto (min 120px)
- **Padding**: 20px
- **Border**: 1px solid glass-border
- **Border Radius**: 16px
- **Gap**: 12px between elements
- **Favicon**: 32×32px circle

### ClaimBuster Sentence
- **Height**: Auto (min 80px)
- **Progress Bar**: Height 8px, rounded-full
- **Score Font**: 14px mono
- **Padding**: 16px

### Footer
- **Height**: 48px fixed
- **Font Size**: 12px (icons 20px)
- **Padding**: 12px horizontal
- **Gap**: 32px between features

### FAB Button
- **Size**: 64×64px circle
- **Position**: Bottom-right (32px, 32px)
- **Z-Index**: 50
- **Animation**: Float (Y-axis ±6px, 6s loop)

---

## 🎯 Spacing System

```
Micro:   4px   (xs)  → Tight elements
Small:   8px   (sm)  → Related items
Base:    12px  (base)→ Standard spacing
Medium:  16px  (md)  → Section padding
Large:   24px  (lg)  → Component margins
XLarge:  32px  (xl)  → Major sections
2XL:     48px  (2xl) → Page sections
3XL:     64px  (3xl) → Hero sections
```

---

## 🌈 Color Usage Map

| Element | Color | Usage |
|---------|-------|-------|
| Background | `#0A0F14` | App base |
| Panels | `#0F1720` | Cards, modals |
| Primary Actions | `#00E5FF` | Analyze button, links |
| Accent | `#7C4DFF` | Profile, highlights |
| Success | `#44FF44` | Positive verdicts |
| Warning | `#FF6B35` | Mixed verdicts |
| Danger | `#FF4444` | False verdicts |
| Text Primary | `#E6F7FF` | Headlines, body |
| Text Muted | `#99A3AD` | Secondary text |
| Borders | `rgba(0,229,255,0.12)` | Subtle outlines |

---

## ⚡ Animation Timing

| Element | Duration | Easing | Loop |
|---------|----------|--------|------|
| Button Hover | 160ms | sci-fi | No |
| Card Appear | 320ms | sci-fi | No |
| Gauge Fill | 680ms | spring | No |
| Logo Rotate | 20s | linear | Yes |
| FAB Float | 6s | ease-in-out | Yes |
| Scan Line | 8s | linear | Yes |
| Glow Pulse | 2s | ease-in-out | Yes |

---

## 📱 Responsive Breakpoints

```css
/* Mobile First Approach */

/* Mobile: 0-640px */
- Single column layout
- Stacked components
- Full-width buttons
- Compact padding (16px)
- Gauge: 160px diameter

/* Tablet: 641-1024px */
- 2-column grid
- Side-by-side cards
- Medium padding (20px)
- Gauge: 220px diameter

/* Desktop: 1025-1440px */
- 3-column grid
- Optimal spacing (24px)
- Max-width container (1400px)
- Gauge: 320px diameter

/* Wide: 1441px+ */
- Increased scale (1.05×)
- Wider gutters (32px)
- Enhanced shadows
- Same layout as desktop
```

---

## 🎬 Interaction States

### Button States
1. **Default** - Gradient, shadow
2. **Hover** - translateY(-2px), brightness(1.05), stronger shadow
3. **Active** - translateY(0), scale(0.995)
4. **Focus** - 2px ring, offset 2px
5. **Disabled** - opacity(0.45), cursor not-allowed
6. **Loading** - Spinner, disabled

### Card States
1. **Default** - Glass, subtle border
2. **Hover** - translateY(-5px), stronger border, glow
3. **Active** - Scale(0.98)
4. **Focus** - Ring outline

### Input States
1. **Default** - Transparent, border
2. **Focus** - Neon glow, brighter border
3. **Error** - Red border, shake animation
4. **Disabled** - Opacity(0.5)

---

This layout guide ensures pixel-perfect implementation of the NEURO-VERIFY AI design! 🎨
