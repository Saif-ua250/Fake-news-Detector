/**
 * Button Component - Premium Sci-Fi Design System
 * Fully typed, accessible, and keyboard-navigable button with multiple variants
 */

import React from 'react';
import { motion, type HTMLMotionProps } from 'framer-motion';
import type { ButtonVariant, ButtonSize } from '@/types';

/**
 * Button component props extending motion.button props
 */
export interface ButtonProps extends Omit<HTMLMotionProps<'button'>, 'size'> {
  /** Visual variant of the button */
  variant?: ButtonVariant;
  /** Size of the button */
  size?: ButtonSize;
  /** Button content */
  children: React.ReactNode;
  /** Loading state */
  isLoading?: boolean;
  /** Full width button */
  fullWidth?: boolean;
  /** Icon element to display before text */
  leftIcon?: React.ReactNode;
  /** Icon element to display after text */
  rightIcon?: React.ReactNode;
}

/**
 * Get button style classes based on variant
 */
const getVariantClasses = (variant: ButtonVariant): string => {
  const variants: Record<ButtonVariant, string> = {
    primary:
      'bg-gradient-to-r from-neon-primary to-neon-accent text-bg font-bold shadow-neon-accent hover:brightness-105 hover:shadow-glow disabled:opacity-45 disabled:cursor-not-allowed',
    secondary:
      'bg-transparent border border-glass-border text-neon-primary hover:bg-glass hover:border-neon-primary/30 disabled:opacity-45',
    ghost:
      'bg-transparent text-neon-primary hover:underline hover:text-neon-accent disabled:opacity-45',
    danger:
      'bg-gradient-to-r from-neon-warn to-red-600 text-white font-bold shadow-neon-warn hover:brightness-105 disabled:opacity-45',
    icon:
      'glass-panel w-14 h-14 flex items-center justify-center text-neon-primary hover:bg-glass hover:shadow-glow rounded-full',
    fab:
      'fixed bottom-8 right-8 w-16 h-16 rounded-full bg-gradient-to-r from-neon-primary to-neon-accent text-bg shadow-neon-primary hover:scale-105 hover:shadow-glow z-50 animate-float',
  };

  return variants[variant];
};

/**
 * Get button size classes
 */
const getSizeClasses = (size: ButtonSize, variant: ButtonVariant): string => {
  // Icon and FAB buttons don't use size classes
  if (variant === 'icon' || variant === 'fab') return '';

  const sizes: Record<ButtonSize, string> = {
    sm: 'px-3.5 py-2.5 text-sm',
    md: 'px-5 py-4 text-base',
    lg: 'px-7 py-5 text-base tracking-wider',
  };

  return sizes[size];
};

/**
 * Animation variants for button interactions
 */
const buttonVariants = {
  initial: { scale: 1 },
  hover: {
    scale: 1.02,
    y: -2,
    transition: { duration: 0.16, ease: [0.16, 0.84, 0.26, 1] },
  },
  tap: {
    scale: 0.995,
    y: 0,
    transition: { duration: 0.1 },
  },
};

/**
 * Button Component
 * 
 * @example
 * ```tsx
 * <Button variant="primary" size="lg" onClick={handleAnalyze}>
 *   ANALYZE
 * </Button>
 * ```
 */
export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = 'primary',
      size = 'md',
      children,
      isLoading = false,
      fullWidth = false,
      leftIcon,
      rightIcon,
      disabled,
      className = '',
      ...props
    },
    ref
  ) => {
    const variantClasses = getVariantClasses(variant);
    const sizeClasses = getSizeClasses(size, variant);
    const widthClass = fullWidth ? 'w-full' : '';

    return (
      <motion.button
        ref={ref}
        variants={buttonVariants}
        initial="initial"
        whileHover={!disabled && !isLoading ? 'hover' : undefined}
        whileTap={!disabled && !isLoading ? 'tap' : undefined}
        disabled={disabled || isLoading}
        className={`
          relative inline-flex items-center justify-center gap-2
          rounded-xl font-body font-semibold uppercase
          transition-all duration-fast ease-sci-fi
          focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-neon-primary focus-visible:ring-offset-2 focus-visible:ring-offset-bg
          ${variantClasses}
          ${sizeClasses}
          ${widthClass}
          ${className}
        `}
        {...props}
      >
        {/* Loading spinner */}
        {isLoading && (
          <svg
            className="animate-spin h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
          </svg>
        )}

        {/* Left icon */}
        {!isLoading && leftIcon && <span aria-hidden="true">{leftIcon}</span>}

        {/* Button text */}
        <span>{children}</span>

        {/* Right icon */}
        {!isLoading && rightIcon && <span aria-hidden="true">{rightIcon}</span>}
      </motion.button>
    );
  }
);

Button.displayName = 'Button';

export default Button;
