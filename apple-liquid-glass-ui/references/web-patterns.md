# Web Implementation Patterns

Use these patterns when writing HTML, CSS, React, Vue, Svelte, Tailwind, or similar web UI. Adapt naming to the existing codebase.

## Material Tokens

Define material tokens once and use them through components.

```css
:root {
  --lg-radius-xl: 28px;
  --lg-radius-lg: 20px;
  --lg-radius-md: 14px;
  --lg-blur: 22px;
  --lg-saturation: 1.35;
  --lg-fill: rgba(255, 255, 255, 0.56);
  --lg-fill-strong: rgba(255, 255, 255, 0.74);
  --lg-stroke: rgba(255, 255, 255, 0.62);
  --lg-stroke-dark: rgba(20, 24, 31, 0.12);
  --lg-shadow: 0 18px 44px rgba(18, 23, 34, 0.18);
  --lg-highlight: inset 0 1px 0 rgba(255, 255, 255, 0.72);
}

@media (prefers-color-scheme: dark) {
  :root {
    --lg-fill: rgba(24, 28, 36, 0.50);
    --lg-fill-strong: rgba(32, 37, 48, 0.72);
    --lg-stroke: rgba(255, 255, 255, 0.18);
    --lg-stroke-dark: rgba(0, 0, 0, 0.35);
    --lg-shadow: 0 18px 44px rgba(0, 0, 0, 0.38);
    --lg-highlight: inset 0 1px 0 rgba(255, 255, 255, 0.20);
  }
}
```

## Glass Chrome Class

Use this for navigation and controls, not ordinary content cards.

```css
.glass-chrome {
  background:
    linear-gradient(135deg, rgba(255, 255, 255, 0.38), transparent 42%),
    var(--lg-fill);
  border: 1px solid var(--lg-stroke);
  border-bottom-color: var(--lg-stroke-dark);
  border-radius: var(--lg-radius-xl);
  box-shadow: var(--lg-shadow), var(--lg-highlight);
  color: var(--text-primary);
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-chrome {
    -webkit-backdrop-filter: blur(var(--lg-blur)) saturate(var(--lg-saturation));
    backdrop-filter: blur(var(--lg-blur)) saturate(var(--lg-saturation));
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-chrome {
    background: var(--lg-fill-strong);
  }
}
```

## Accessibility Fallbacks

```css
@media (prefers-reduced-transparency: reduce), (prefers-contrast: more) {
  .glass-chrome {
    background: var(--lg-fill-strong);
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.001ms !important;
  }
}

@media (forced-colors: active) {
  .glass-chrome {
    background: Canvas;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```

## Component Recipes

Top navigation:

- Keep it sticky or fixed only when repeated actions matter.
- Let content scroll underneath if text remains legible.
- Use icon buttons for frequent actions and a concise title or segmented switch for context.

Bottom tab bar:

- Use for 3 to 5 primary destinations on mobile.
- Float above the safe area with a glass pill or rounded slab.
- Keep labels short and provide active state through shape, weight, and contrast.

Sidebar:

- Use on desktop and tablet for persistent navigation or source lists.
- Make the sidebar material calmer than popovers or floating toolbars.
- Collapse to a rail, drawer, or bottom tabs on narrow screens.

Sheets and popovers:

- Anchor contextual surfaces near the initiating control.
- Increase opacity behind dense forms or destructive actions.
- Keep corner radius and padding consistent with the trigger surface.

Cards and content panels:

- Use standard solid or subtly tinted surfaces for repeated content.
- Reserve glass for selected, hovered, or floating controls inside the content layer.
- Keep tables and charts crisp; do not blur behind data-heavy rows.

## Responsive Checks

- At 360px width, no toolbar label, tab label, or button text should overflow.
- At tablet width, navigation should not fight content for horizontal space.
- At desktop width, avoid giant empty hero-like areas for apps and dashboards.
- Sticky glass elements must not cover final rows, form actions, or toast messages.

## Implementation Review

Before finishing a UI task:

- Inspect screenshots or run the app at mobile and desktop sizes when possible.
- Confirm that glass is limited to functional chrome.
- Check hover, active, focus, disabled, loading, empty, and error states.
- Confirm text contrast over glass with realistic backgrounds.
- Confirm keyboard navigation reaches every interactive control in a sensible order.
