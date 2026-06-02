---
name: apple-liquid-glass-ui
description: "Design and implement web interfaces inspired by Apple's Liquid Glass and Human Interface Guidelines. Use when asked to build or refine Apple-style UI, Liquid Glass web design, 苹果液态玻璃, iOS/macOS-like dashboards, app shells, toolbars, tabs, cards, modals, navigation, responsive product interfaces, or to review UI against Apple HIG principles while preserving accessibility and web platform constraints."
---

# Apple Liquid Glass UI

## Goal

Create production-ready web interfaces with Apple-inspired hierarchy, materials, motion, and restraint. Treat Liquid Glass on the web as an approximation inspired by Apple guidance; do not present it as an official Apple component library, and do not copy Apple proprietary assets.

## Workflow

1. Identify whether the task is greenfield implementation, redesign, component creation, or UI review.
2. Preserve the product's real workflow. Build the usable app or tool screen first; apply the visual language after the information architecture is clear.
3. Load [Apple Principles](references/apple-principles.md) before making design decisions. If the user asks for exact latest Apple behavior, browse official Apple documentation first because this guidance can change.
4. Load [Web Patterns](references/web-patterns.md) when writing CSS, React, Tailwind, component APIs, or responsive layouts.
5. Put Liquid Glass treatments on the functional layer: navigation, toolbars, tab bars, floating controls, popovers, sheets, and transient controls.
6. Keep content surfaces calmer: standard backgrounds, cards, tables, lists, charts, and document areas should not all become glass.
7. Use system-like controls and platform expectations: clear hierarchy, familiar placement, adaptive layout, concise labels, and icon buttons with tooltips where appropriate.
8. Verify the result across desktop and mobile. Check contrast, legibility over changing backgrounds, reduced motion, reduced transparency, keyboard focus, and responsive overflow.

## Design Rules

- Use glass sparingly. One primary glass navigation/control system usually feels intentional; many glass cards usually feel noisy.
- Separate functional chrome from content. Glass floats above content and helps people retain a sense of place.
- Let the background matter. Glass needs real content, imagery, color, or depth behind it, but never at the cost of text contrast.
- Prefer adaptive, dense, usable layouts over decorative landing-page composition for tools, dashboards, and operational apps.
- Use concentric geometry: related rounded shapes should feel aligned, with inner elements using smaller radii than outer containers.
- Support light and dark mode with tokens instead of hard-coded single-theme colors.
- Respect accessibility settings: `prefers-reduced-motion`, `prefers-contrast`, `forced-colors`, and fallbacks when `backdrop-filter` is unavailable.
- Do not use Apple logos, SF Symbols, Apple product screenshots, or proprietary assets unless the user provides them with permission.

## Implementation Expectations

- For existing apps, follow the current stack and design system. Extend local components instead of adding a parallel UI kit.
- For new web apps, create real screens with working states, not a static mood board.
- Use CSS variables for material, shadow, tint, blur, radius, and motion tokens.
- Prefer semantic HTML, accessible labels, visible focus states, and touch targets that remain usable on mobile.
- Use `backdrop-filter` progressively with a solid or translucent fallback.
- When animation is used, keep it functional: focus changes, toolbar compression, sheet entrance, hover/press feedback, and state transitions.

## Review Checklist

- Is the UI immediately usable for the user's requested workflow?
- Does the glass layer clarify controls and navigation instead of decorating every surface?
- Are content, controls, and overlays legible over light, dark, busy, and low-contrast backgrounds?
- Does the layout adapt cleanly at mobile, tablet, and desktop widths?
- Are motion, transparency, and focus states accessible?
- Did the final answer mention any unverified Apple guidance if browsing was skipped?
