/**
 * Header Component - Fixed Top Navigation
 * Premium sci-fi glass morphism design with logo and action icons
 */

import { motion } from 'framer-motion';

export default function Header() {
  return (
    <motion.header
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5, ease: [0.16, 0.84, 0.26, 1] }}
      className="fixed top-0 left-0 right-0 z-50 h-18"
    >
      <div className="glass-panel mx-4 mt-4">
        <div className="container mx-auto px-6 h-18 flex items-center justify-between">
          {/* Logo and brand name */}
          <div className="flex items-center gap-4">
            {/* Logo icon - animated hexagon */}
            <motion.div
              className="w-11 h-11 flex items-center justify-center"
              animate={{
                rotate: [0, 360],
              }}
              transition={{
                duration: 20,
                repeat: Infinity,
                ease: 'linear',
              }}
            >
              <svg
                viewBox="0 0 44 44"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                className="w-full h-full"
              >
                <path
                  d="M22 2L38.5 12V32L22 42L5.5 32V12L22 2Z"
                  stroke="url(#logo-gradient)"
                  strokeWidth="2"
                  fill="rgba(0,229,255,0.1)"
                />
                <defs>
                  <linearGradient id="logo-gradient" x1="5.5" y1="2" x2="38.5" y2="42">
                    <stop offset="0%" stopColor="#00E5FF" />
                    <stop offset="100%" stopColor="#7C4DFF" />
                  </linearGradient>
                </defs>
              </svg>
            </motion.div>

            {/* Brand name */}
            <h1 className="font-headline font-bold text-xl tracking-[0.2em] gradient-text">
              NEURO-VERIFY AI
            </h1>
          </div>

          {/* Action icons */}
          <div className="flex items-center gap-3">
            {/* History button */}
            <motion.button
              whileHover={{ scale: 1.05, boxShadow: '0 0 20px rgba(0,229,255,0.3)' }}
              whileTap={{ scale: 0.95 }}
              className="glass-panel w-14 h-14 flex items-center justify-center rounded-full transition-all duration-fast"
              aria-label="View analysis history"
              title="History"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.5}
                stroke="currentColor"
                className="w-6 h-6 text-neon-primary"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </motion.button>

            {/* Settings button */}
            <motion.button
              whileHover={{ scale: 1.05, boxShadow: '0 0 20px rgba(0,229,255,0.3)' }}
              whileTap={{ scale: 0.95 }}
              className="glass-panel w-14 h-14 flex items-center justify-center rounded-full transition-all duration-fast"
              aria-label="Open settings"
              title="Settings"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.5}
                stroke="currentColor"
                className="w-6 h-6 text-neon-primary"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z"
                />
                <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </motion.button>

            {/* Profile button */}
            <motion.button
              whileHover={{ scale: 1.05, boxShadow: '0 0 20px rgba(124,77,255,0.3)' }}
              whileTap={{ scale: 0.95 }}
              className="glass-panel w-14 h-14 flex items-center justify-center rounded-full transition-all duration-fast border-2 border-neon-accent/30"
              aria-label="View profile"
              title="Profile"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.5}
                stroke="currentColor"
                className="w-6 h-6 text-neon-accent"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
                />
              </svg>
            </motion.button>
          </div>
        </div>
      </div>
    </motion.header>
  );
}
