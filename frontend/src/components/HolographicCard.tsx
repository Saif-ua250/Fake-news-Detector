import { ReactNode } from 'react'
import { motion } from 'framer-motion'
import { cn } from '@/lib/utils'

interface HolographicCardProps {
  children: ReactNode
  className?: string
  delay?: number
}

/**
 * HolographicCard Component
 * 
 * Glassmorphism card with:
 * - Backdrop blur effect
 * - Holographic border animation
 * - Entrance animation with delay
 * - Hover glow effect
 */
const HolographicCard = ({ children, className, delay = 0 }: HolographicCardProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay }}
      className={cn(
        'glass-card p-6',
        'hover:border-cyber-cyan/50 hover:shadow-neon-cyan',
        'transition-all duration-300',
        className
      )}
    >
      {/* Holographic shine effect */}
      <div className="absolute inset-0 rounded-lg overflow-hidden pointer-events-none">
        <div className="absolute inset-0 bg-gradient-to-br from-cyber-blue/10 via-transparent to-cyber-purple/10 opacity-0 hover:opacity-100 transition-opacity duration-500" />
      </div>
      
      {/* Card content */}
      <div className="relative z-10">
        {children}
      </div>
    </motion.div>
  )
}

export default HolographicCard
