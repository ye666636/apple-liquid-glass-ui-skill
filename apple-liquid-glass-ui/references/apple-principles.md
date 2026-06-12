# Apple Principles for Liquid Glass Web UI

Official sources checked on 2026-06-12:

- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- Materials: https://developer.apple.com/design/human-interface-guidelines/materials
- Color: https://developer.apple.com/design/human-interface-guidelines/color
- Layout: https://developer.apple.com/design/human-interface-guidelines/layout
- Liquid Glass overview: https://developer.apple.com/documentation/technologyoverviews/liquid-glass
- Adopting Liquid Glass: https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass

Use these notes as a condensed working guide. Apple Developer pages may require JavaScript in a browser, so treat the links above as official source anchors and browse or inspect the live docs before answering questions about exact current Apple behavior, SDK-specific APIs, or exact HIG wording.

## Core HIG Translation

- Hierarchy: make controls and navigation visibly distinct from content. Elevation must communicate function, not just style.
- Harmony: use rounded geometry, spacing, and motion that feel related to the device or viewport shape.
- Consistency: follow platform conventions and keep layouts adaptive across window sizes.
- Content first: the app's content and task are the center of the experience. Glass is a supporting material.

## Liquid Glass Placement

Use Liquid Glass-like treatment for:

- Global and local navigation.
- Toolbars, tab bars, sidebars, floating action clusters, and command surfaces.
- Popovers, sheets, menus, and contextual controls.
- Active or transient controls such as sliders, toggles, segmented controls, scrubbers, and inspectors.

Avoid Liquid Glass-like treatment for:

- Main content cards repeated in grids.
- Tables, documents, forms, charts, feeds, and dense data panels.
- Background sections whose role is only decorative.
- Large surfaces where blur makes text or data harder to read.

## Visual Behavior

- Let content show through subtly; never let it compete with labels, icons, or data.
- Use a translucent fill, background blur, a fine highlight border, and a quiet shadow as a combined material.
- Adapt the material to light and dark mode instead of using one fixed opacity.
- Prefer one prominent glass system per viewport. If a top bar, bottom tab bar, and floating inspector are all glass, make the secondary ones calmer.
- Keep backgrounds behind glass varied enough to reveal depth, but not so busy that the glass fails.

## Layout

- Respect safe areas, sticky toolbars, bottom tabs, and scroll edges.
- Let content extend underneath chrome only when the chrome remains legible and the scroll behavior is intentional.
- Support arbitrary viewport widths. Avoid designs that only work at one desktop breakpoint.
- Use split views and sidebars for wide screens; collapse to bottom tabs, drawers, or segmented views on small screens.
- Keep controls near the content or object they affect.

## Motion

- Use short, responsive transitions for glass surfaces: hover, press, focus, sheet enter/exit, tab switching, toolbar compression, and scroll-edge changes.
- Avoid idle shimmer or constant background motion in productivity interfaces.
- Disable or simplify nonessential motion under `prefers-reduced-motion: reduce`.
- Keep animation duration short enough that repeated tool use feels fast.

## Color and Contrast

- Liquid Glass can pick up surrounding color, so test it over multiple content states.
- Avoid placing similar foreground and background colors across glass.
- Use dynamic tokens for text, icons, fill, stroke, and shadows.
- Provide stronger scrims or more opaque fills when the background is visually complex.
- Test high contrast and forced colors modes when the app has important workflows.

## Accessibility

- Always provide visible focus rings on glass controls.
- Maintain target sizes suitable for pointer and touch input.
- Use semantic buttons, navigation, dialogs, and form fields rather than div-only controls.
- Pair icons with accessible names and tooltips when meaning is not universal.
- Provide a non-blur fallback for browsers or settings that reduce transparency.

## Brand and Legal Boundaries

- Describe the result as Apple-inspired or Liquid Glass-inspired web UI unless building with official Apple SDKs.
- Do not redistribute Apple design assets, SF Symbols, product images, or logos unless the user supplies them and confirms permission.
- Do not claim compliance with Apple's review process; say the UI follows a practical interpretation of Apple HIG principles.
