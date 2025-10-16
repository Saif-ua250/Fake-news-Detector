/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        bg: '#0A0F14',
        panel: '#0F1720',
        glass: 'rgba(255,255,255,0.04)',
        'neon-primary': '#00E5FF',
        'neon-accent': '#7C4DFF',
        'neon-warn': '#FF6B35',
        'text-primary': '#E6F7FF',
        muted: '#99A3AD',
        'glass-border': 'rgba(0,229,255,0.12)',
      },
      fontFamily: {
        headline: ['Orbitron', 'Rajdhani', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
      transitionDuration: {
        fast: '160ms',
        medium: '320ms',
        slow: '680ms',
      },
      transitionTimingFunction: {
        'sci-fi': 'cubic-bezier(.16,.84,.26,1)',
      },
      boxShadow: {
        'neon-primary': '0 12px 40px rgba(0,229,255,0.14)',
        'neon-accent': '0 12px 40px rgba(124,77,255,0.12)',
        'neon-warn': '0 8px 32px rgba(255,107,53,0.18)',
        glow: '0 0 20px rgba(0,229,255,0.3)',
      },
      backdropBlur: {
        glass: '24px',
      },
      animation: {
        'pulse-glow': 'pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'scan-line': 'scan-line 8s linear infinite',
      },
      keyframes: {
        'pulse-glow': {
          '0%, 100%': { opacity: '1', boxShadow: '0 0 20px rgba(0,229,255,0.3)' },
          '50%': { opacity: '0.8', boxShadow: '0 0 40px rgba(0,229,255,0.6)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        'scan-line': {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100vh)' },
        },
      },
    },
  },
  plugins: [],
};
