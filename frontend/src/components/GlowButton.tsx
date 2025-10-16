import { ButtonHTMLAttributes, ReactNode } from 'react'
import { motion } from 'framer-motion'
import { cn } from '@/lib/utils'

interface GlowButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode
  variant?: 'primary' | 'secondary' | 'danger'
  isLoading?: boolean
}

/**
 * GlowButton Component
 * 
 * Futuristic button with:
 * - Neon glow effect on hover
 * - Ripple animation on click
 * - Loading state with spinner
 * - Multiple color variants
 */
const GlowButton = ({ 
  children, 
  variant = 'primary', 
  isLoading = false,
  className,
  disabled,
  ...props 
}: GlowButtonProps) => {
  const variants = {
    primary: 'bg-cyber-blue hover:bg-cyber-cyan shadow-neon-blue hover:shadow-neon-cyan',
    secondary: 'bg-cyber-purple hover:bg-cyber-pink shadow-neon-purple',
    danger: 'bg-cyber-red hover:bg-red-600 shadow-neon-red',
  }

  return (
    <motion.button
      className={cn(
        'relative px-8 py-4 rounded-lg font-orbitron font-bold text-lg',
        'transition-all duration-300 transform',
        'disabled:opacity-50 disabled:cursor-not-allowed',
        variants[variant],
        className
      )}
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      disabled={disabled || isLoading}
      {...props}
    >
      {/* Glow effect overlay */}
      <div className="absolute inset-0 rounded-lg bg-white/10 opacity-0 hover:opacity-100 transition-opacity duration-300" />
      
      {/* Button content */}
      <span className="relative z-10 flex items-center justify-center gap-2">
        {isLoading && (
          <motion.div
            className="w-5 h-5 border-2 border-white border-t-transparent rounded-full"
            animate={{ rotate: 360 }}
            transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
          />
        )}
        {children}
      </span>

      {/* Animated border */}
      <div className="absolute inset-0 rounded-lg opacity-50 holo-border" />
    </motion.button>
  )
}

export default GlowButton
