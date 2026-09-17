import mermaid from 'mermaid';

var config = {
  startOnLoad: false,
  theme: 'default',
  fontFamily: '"Jost", -apple-system, blinkmacsystemfont, "Segoe UI", roboto, "Helvetica Neue", arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";',
};

mermaid.initialize(config);

function renderMermaid() {
  // The {{< mermaid >}} shortcode emits <div class="mermaid">…</div>.
  mermaid.run({ querySelector: '.mermaid' });
}

if (document.readyState !== 'loading') {
  renderMermaid();
} else {
  document.addEventListener('DOMContentLoaded', renderMermaid);
}
