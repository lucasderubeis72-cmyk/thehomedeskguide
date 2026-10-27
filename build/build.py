import os,json
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE="https://thehomedeskguide.com"
def page(path,title,desc,main):
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}/{path}">
<link rel="icon" href="/favicon.svg"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="stylesheet" href="/style.css"></head><body>
<header class="site-header"><div class="wrap"><a class="brand" href="/"><img src="/img/logo.svg" alt=""><span>The Home <em>Desk</em> Guide</span></a>
<nav class="nav"><a href="/#guides">Guides</a><a href="/about/">About</a><a href="/disclosure/">Disclosure</a></nav></div></header>
{main}
<footer><div class="wrap"><div><strong>The Home Desk Guide</strong><br>Practical advice for a better home office.</div>
<div>As an Amazon Associate we earn from qualifying purchases.<br><a href="/disclosure/">Affiliate disclosure</a> · <a href="/privacy/">Privacy</a> · © 2026<br>Photos: <a href=\"https://unsplash.com\">Unsplash</a></div></div></footer></body></html>'''
    d=os.path.join(R,path);os.makedirs(d,exist_ok=True);open(os.path.join(d,'index.html'),'w').write(html)
arts=json.load(open(os.path.join(R,'build','articles.json')))
cards=''.join(f'<a class="card" href="/guides/{a["slug"]}/"><img src="{a["img"]}" alt="{a["title"]}"><div class="body"><div class="tag">{a["tag"]}</div><h3>{a["title"]}</h3><p>{a["desc"]}</p></div></a>' for a in arts)
soon=[("https://images.unsplash.com/photo-1688578735352-9a6f2ac3b70a?auto=format&fit=crop&w=800&q=80","Chairs","Ergonomic chairs: what really matters","The features worth paying for, and the ones that are just marketing."),("https://images.unsplash.com/photo-1611096002616-763f16ef15f3?auto=format&fit=crop&w=800&q=80","Setup","The home office setup checklist","Monitor height, lighting and cables, step by step.")]
cards+=''.join(f'<div class="card soon"><img src="{i}" alt="{h}" loading="lazy"><div class="body"><div class="tag">Coming soon · {t}</div><h3>{h}</h3><p>{p}</p></div></div>' for i,t,h,p in soon if not any(a["img"]==i for a in arts))
page('',"The Home Desk Guide – Honest Home Office Gear Advice","Practical guides to standing desks, ergonomic chairs and desk gear for people who work from home.",f'''
<section class="hero"><div class="wrap"><div><span class="eyebrow">Home office buying guides</span><h1>Build a home office you <span>actually enjoy</span> working in</h1>
<p>Clear, no-hype guides to standing desks, ergonomic chairs and the upgrades that make long workdays easier on your body.</p>
<a class="btn" href="#guides">Browse the guides →</a><a class="btn ghost" href="/about/">How we research</a>
<div class="stats"><div><b>Specs-first</b>compared side by side</div><div><b>No sponsored</b>rankings, ever</div><div><b>Updated</b>every month</div></div></div>
<div class="shot"><img src="https://images.unsplash.com/photo-1600494603989-9650cf6ddd3d?auto=format&fit=crop&w=1400&q=80" alt="A home office with a wooden desk and chair"><div class="float"><b>5 compact desks compared</b><span>Our latest standing desk guide</span></div></div></div></section>
<section class="section" id="guides"><div class="wrap"><h2>Latest guides</h2><p class="sub">Start here if you are setting up or upgrading your workspace.</p><div class="grid">{cards}</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><h2>How we choose products</h2><p class="sub">Every recommendation follows the same simple process.</p><div class="features">
<div class="feature"><div class="ic">📐</div><h3>Specs side by side</h3><p>We compare size, height range, motors and weight limits from manufacturer listings.</p></div>
<div class="feature"><div class="ic">💬</div><h3>Real owner feedback</h3><p>We look for recurring complaints like wobble, noise and early failures before recommending anything.</p></div>
<div class="feature"><div class="ic">🔍</div><h3>Honest trade-offs</h3><p>Every pick lists its weaknesses too, so you know exactly what you are giving up.</p></div></div></div></section>''')
for a in arts:
    toc=''.join(f'<li><a href="#s{i}">{h}</a></li>' for i,(h,_) in enumerate(a["sections"]))
    secs=''.join(f'<h2 id="s{i}">{h}</h2>{b}' for i,(h,b) in enumerate(a["sections"]))
    page(f'guides/{a["slug"]}/',f'{a["title"]} – The Home Desk Guide',a["desc"],f'''<article class="article"><div class="crumbs"><a href="/">Home</a> › <a href="/#guides">{a["tag"]}</a></div>
<h1>{a["title"]}</h1><div class="meta"><span>By The Home Desk Guide team</span><span>·</span><span>Updated {a["updated"]}</span></div>
<p class="disclosure-note">Some links may be affiliate links. We may earn a commission at no extra cost to you. <a href="/disclosure/">Learn more</a>.</p>
<img class="cover" src="{a["img"]}" alt="{a["title"]}"><p style="font-size:1.15rem">{a["intro"]}</p>
<nav class="toc"><strong>In this guide</strong><ol>{toc}</ol></nav>{secs}</article>''')
simple={'about':("About","<p>The Home Desk Guide helps remote workers choose home office gear without the hype. We compare specifications, prices and real owner feedback so you can decide faster and buy once.</p>"),
'disclosure':("Affiliate Disclosure","<p>Some links on this site are affiliate links. If you buy through them, we may earn a commission at no extra cost to you. As an Amazon Associate, we earn from qualifying purchases. This never changes our recommendations.</p>"),
'privacy':("Privacy Policy","<p>This site does not require accounts and does not sell personal data. Affiliate partners such as Amazon may use cookies to track purchases made through our links.</p>")}
for p,(t,b) in simple.items(): page(f'{p}/',f'{t} – The Home Desk Guide',t,f'<article class="article"><h1>{t}</h1>{b}</article>')
urls=['','about/','disclosure/','privacy/']+[f'guides/{a["slug"]}/' for a in arts]
open(os.path.join(R,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}/{u}</loc></url>\n' for u in urls)+'</urlset>\n')
