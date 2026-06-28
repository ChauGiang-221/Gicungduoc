# Design System Handoff

## Color Palette

```css
--primary: hsl(222.2, 47.4%, 11.2%)
--secondary: hsl(210, 40%, 96.1%)
--accent: hsl(217.2, 32.6%, 17.5%)
--destructive: hsl(0, 84.2%, 60.2%)
--muted: hsl(210, 40%, 96.1%)
--border: hsl(214.3, 31.8%, 91.4%)
--ring: hsl(222.2, 84%, 4.9%)
```

## Typography

```css
font-family: Inter, system-ui, sans-serif
font-sizes:
  xs: 0.75rem
  sm: 0.875rem
  base: 1rem
  lg: 1.125rem
  xl: 1.25rem
  2xl: 1.5rem
  3xl: 1.875rem
  4xl: 2.25rem
```

## Spacing

```css
spacing:
  1: 0.25rem
  2: 0.5rem
  3: 0.75rem
  4: 1rem
  5: 1.25rem
  6: 1.5rem
  8: 2rem
  10: 2.5rem
  12: 3rem
  16: 4rem
  20: 5rem
  24: 6rem
```

## Components

### Button
- Variants: default, destructive, outline, secondary, ghost, link
- Sizes: default, sm, lg, icon
- Border radius: 0.5rem
- Padding: 0.5rem 1rem

### Card
- Background: white/dark slate
- Border: 1px solid border color
- Border radius: 0.75rem
- Padding: 1.5rem

### Input
- Border: 1px solid input color
- Border radius: 0.5rem
- Padding: 0.5rem 1rem
- Focus ring: 2px ring color

## Icons

Use Lucide React icons.

```bash
import { IconName } from 'lucide-react'
```

## Responsive Breakpoints

```css
sm: 640px
md: 768px
lg: 1024px
xl: 1280px
2xl: 1536px
```

## Vietnamese UI Notes

- Font hỗ trợ tiếng Việt: Inter, Be Vietnam Pro.
- Line height cao hơn 5-10% cho tiếng Việt.
- Text alignment: left cho paragraphs dài.
- Button text: ngắn gọn, action-oriented.
