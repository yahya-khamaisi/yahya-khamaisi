"""Builds the light and dark SVGs used by README.md.

Run `python3 assets/build.py` after editing the copy or colours below.
"""

from pathlib import Path

OUT = Path(__file__).parent

THEMES = {
    "dark": {
        "bg1": "#0B1020", "bg2": "#111A2E", "grid": "#1C2740",
        "text": "#F1F5F9", "muted": "#94A3B8", "line": "#26324D",
        "a1": "#2DD4BF", "a2": "#A78BFA", "chip": "#151F36",
    },
    "light": {
        "bg1": "#FFFFFF", "bg2": "#F1F5F9", "grid": "#E2E8F0",
        "text": "#0F172A", "muted": "#475569", "line": "#CBD5E1",
        "a1": "#0D9488", "a2": "#7C3AED", "chip": "#FFFFFF",
    },
}

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Graph on the right of the header: the system I build, end to end.
NODES = {
    "client": (820, 92, "portal"),
    "api": (960, 92, "api"),
    "agent": (1100, 92, "agents"),
    "rag": (1030, 196, "retrieval"),
    "cloud": (1170, 196, "azure"),
    "model": (890, 196, "llm"),
}
EDGES = [
    ("client", "api"), ("api", "agent"), ("agent", "rag"),
    ("rag", "model"), ("model", "api"), ("agent", "cloud"), ("rag", "cloud"),
]

STATS = [
    ("6+", "years shipping"),
    ("5", "companies"),
    ("4", "publications"),
    ("PhD", "applied AI"),
]


def header(t):
    edges = []
    for i, (a, b) in enumerate(EDGES):
        x1, y1, _ = NODES[a]
        x2, y2, _ = NODES[b]
        edges.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="edge"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="flow" '
            f'style="animation-delay:{i * 0.45:.2f}s"/>'
        )
    nodes = []
    for i, (x, y, label) in enumerate(NODES.values()):
        w = len(label) * 8.4 + 28
        nodes.append(
            f"<g>"
            f'<rect x="{x - w / 2:.1f}" y="{y - 17}" width="{w:.1f}" height="34" rx="17" class="chip"/>'
            f'<circle cx="{x - w / 2 + 15:.1f}" cy="{y}" r="4" class="dot"/>'
            f'<text x="{x + 6:.1f}" y="{y + 5}" class="mono" text-anchor="middle">{label}</text>'
            f"</g>"
        )
    stats = []
    for i, (big, small) in enumerate(STATS):
        x = 64 + i * 150
        stats.append(
            f'<text x="{x}" y="276" class="stat">{big}</text>'
            f'<text x="{x}" y="298" class="small">{small}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="340" viewBox="0 0 1280 340" role="img" aria-label="Yahya Khamayseh, Full-Stack AI Engineer">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/>
  </linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{t['a1']}"/><stop offset="1" stop-color="{t['a2']}"/>
  </linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="{t['grid']}" stroke-width="1"/>
  </pattern>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".55" stop-color="#fff" stop-opacity=".9"/>
  </linearGradient>
  <mask id="gridmask"><rect width="1280" height="340" fill="url(#fade)"/></mask>
  <clipPath id="frame"><rect width="1280" height="340" rx="20"/></clipPath>
</defs>
<style>
  .name {{ font: 700 54px {SANS}; fill: {t['text']}; letter-spacing: -1.5px; }}
  .role {{ font: 600 17px {MONO}; fill: url(#accent); letter-spacing: 2px; }}
  .tag  {{ font: 400 20px {SANS}; fill: {t['muted']}; }}
  .stat {{ font: 700 26px {SANS}; fill: {t['text']}; }}
  .small {{ font: 400 13px {MONO}; fill: {t['muted']}; }}
  .mono {{ font: 500 14px {MONO}; fill: {t['text']}; }}
  .chip {{ fill: {t['chip']}; stroke: {t['line']}; stroke-width: 1.2; }}
  .dot  {{ fill: {t['a1']}; }}
  .edge {{ stroke: {t['line']}; stroke-width: 2; }}
  .flow {{ stroke: url(#accent); stroke-width: 2.4; stroke-linecap: round;
           stroke-dasharray: 18 400; stroke-dashoffset: 418;
           animation: flow 3.2s linear infinite; }}
  .rule {{ stroke: {t['line']}; stroke-width: 1; }}
  @keyframes flow {{ to {{ stroke-dashoffset: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{ .flow {{ display: none; }} }}
</style>
<g clip-path="url(#frame)">
  <rect width="1280" height="340" fill="url(#bg)"/>
  <rect width="1280" height="340" fill="url(#grid)" mask="url(#gridmask)"/>
  <rect x="0" y="0" width="1280" height="4" fill="url(#accent)"/>
  <text x="64" y="74" class="role">FULL-STACK AI ENGINEER · DUBAI</text>
  <text x="64" y="138" class="name">Yahya Khamayseh</text>
  <text x="64" y="180" class="tag">I build AI systems for production: agents, retrieval,</text>
  <text x="64" y="208" class="tag">the APIs around them, and the cloud they run on.</text>
  <line x1="64" y1="238" x2="640" y2="238" class="rule"/>
  {''.join(stats)}
  {''.join(edges)}
  {''.join(nodes)}
</g>
</svg>
"""


for name, theme in THEMES.items():
    (OUT / f"header-{name}.svg").write_text(header(theme))
    print(f"wrote header-{name}.svg")
