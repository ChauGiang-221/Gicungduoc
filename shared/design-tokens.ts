// Shared Design Tokens
// Dùng chung cho Web, Mobile, Desktop

export const colors = {
  primary: '#3B82F6',
  primaryDark: '#2563EB',
  background: '#F5F5F5',
  surface: '#FFFFFF',
  text: '#333333',
  textSecondary: '#888888',
  border: '#E5E5E5',
  error: '#EF4444',
  success: '#22C55E',
} as const

export const spacing = {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px',
} as const

export const borderRadius = {
  sm: '8px',
  md: '12px',
  lg: '16px',
  full: '9999px',
} as const

export const fontSize = {
  sm: '14px',
  md: '16px',
  lg: '18px',
  xl: '20px',
} as const
