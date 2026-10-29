import os,json
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE="https://thehomedeskguide.com"
def page(path,title,desc,main):
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}/{path}">
<link rel="icon" href="/favicon.svg"><meta name="p:domain_verify" content="3c62c34cb81e9f502e93caeccf102331"/><link rel="alternate" type="application/rss+xml" title="The Home Desk Guide" href="/feed.xml"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="stylesheet" href="/style.css"></head><body>
<header class="site-header"><div class="wrap"><a class="brand" href="/"><img src="/img/logo.svg" alt="The Home Desk Guide logo"><span>The Home <em>Desk</em> Guide</span></a>
<nav class="nav"><a href="/#guides">Guides</a><a href="/about/">About</a><a href="/contact/">Contact</a></nav></div></header>
{main}
<footer><div class="wrap"><div><strong>The Home Desk Guide</strong><br>Practical advice for a better home office.</div>
<div>As an Amazon Associate we earn from qualifying purchases.<br><a href="/disclosure/">Affiliate disclosure</a> · <a href="/privacy/">Privacy</a> · <a href="/contact/">Contact</a> · © 2026<br>Photos: <a href=\"https://unsplash.com\">Unsplash</a></div></div></footer></body></html>'''
    d=os.path.join(R,path);os.makedirs(d,exist_ok=True);open(os.path.join(d,'index.html'),'w').write(html)
arts=json.load(open(os.path.join(R,'build','articles.json')))
cards=''.join(f'<a class="card" href="/guides/{a["slug"]}/"><img src="{a["img"]}" alt="{a.get("imgAlt",a["title"])}"><div class="body"><div class="tag">{a["tag"]}</div><h3>{a["title"]}</h3><p>{a["desc"]}</p></div></a>' for a in arts)
soon=[("https://images.unsplash.com/photo-1688578735352-9a6f2ac3b70a?auto=format&fit=crop&w=800&q=80","Chairs","Ergonomic chairs: what really matters","The features worth paying for, and the ones that are just marketing."),("https://images.unsplash.com/photo-1611096002616-763f16ef15f3?auto=format&fit=crop&w=800&q=80","Setup","The home office setup checklist","Monitor height, lighting and cables, step by step.")]
cards+='' and ''.join(f'<div class="card soon"><img src="{i}" alt="{h}" loading="lazy"><div class="body"><div class="tag">Coming soon · {t}</div><h3>{h}</h3><p>{p}</p></div></div>' for i,t,h,p in soon if not any(a["img"]==i for a in arts))
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
<h1>{a["title"]}</h1><div class="meta"><span>By <a href="/about/">Lucas</a>, founder</span><span>·</span><span>Updated {a["updated"]}</span></div>
<p class="disclosure-note">Some links may be affiliate links. We may earn a commission at no extra cost to you. <a href="/disclosure/">Learn more</a>.</p>
<img class="cover" src="{a["img"]}" alt="{a.get("imgAlt",a["title"])}"><p style="font-size:1.15rem">{a["intro"]}</p>
<nav class="toc"><strong>In this guide</strong><ol>{toc}</ol></nav>{secs}</article>''')
simple={'about':("About",'<p>Hi, I\'m Lucas, the founder and editor of The Home Desk Guide.</p>\n<p>I started this site because choosing home office gear online is harder than it should be. Product pages are full of marketing claims, and many "best of" lists don\'t explain why one desk or chair is better than another. My goal is simple: help you pick the right gear for your space, your body and your budget, and buy it once.</p>\n<h2>How I research products</h2>\n<ul class="check"><li>I compare manufacturer specifications side by side: dimensions, height range, motors, weight capacity and warranty.</li><li>I read through large numbers of owner reviews, looking for recurring problems like wobble, noise or early failures.</li><li>I list the weaknesses of every product, not just the strengths.</li><li>I update guides when products, specs or prices change.</li></ul>\n<h2>What I don\'t do</h2>\n<p>I don\'t accept payment to rank products, and brands can\'t buy a spot in a guide. Unless a guide clearly says a product was tested in person, my recommendations are based on research, specifications and owner feedback, and I say so in every guide.</p>\n<h2>How the site makes money</h2>\n<p>Some links on this site are affiliate links. If you buy through them, I may earn a small commission at no extra cost to you. This keeps the site free and never changes which products I recommend. <a href="/disclosure/">Read the full disclosure</a>.</p>\n<p>Questions or spotted a mistake? <a href="/contact/">Get in touch</a>.</p>'),
'disclosure':("Affiliate Disclosure","<p>Some links on this site are affiliate links. If you buy through them, we may earn a commission at no extra cost to you. As an Amazon Associate, we earn from qualifying purchases. This never changes our recommendations.</p>"),
'contact':("Contact",'<p>Have a question about a guide, spotted an outdated spec, or want to suggest a product to compare? I\'d love to hear from you.</p>\n<div class="callout"><strong>Email:</strong> <a href="mailto:contact@thehomedeskguide.com">contact@thehomedeskguide.com</a></div>\n<p>Please note that I can\'t provide personal shopping support for every request, but every message is read and corrections are applied to the guides.</p>\n<p><strong>Brands and PR:</strong> I don\'t accept paid placements in rankings. You\'re welcome to send product information for consideration in future guides.</p>'),
'privacy':("Privacy Policy","<p>This site does not require accounts and does not sell personal data. Affiliate partners such as Amazon may use cookies to track purchases made through our links.</p>")}
for p,(t,b) in simple.items(): page(f'{p}/',f'{t} – The Home Desk Guide',t,f'<article class="article"><h1>{t}</h1>{b}</article>')
urls=['','about/','contact/','disclosure/','privacy/']+[f'guides/{a["slug"]}/' for a in arts]
open(os.path.join(R,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}/{u}</loc></url>\n' for u in urls)+'</urlset>\n')

from xml.sax.saxutils import escape as X

import re,datetime,html as H
# ---------- Pinterest: several pins per article, released gradually ----------
STATE=os.path.join(R,'data','pin-schedule.json')
try: sched=json.load(open(STATE))
except Exception: sched={}
def strip(t): return H.unescape(re.sub('<[^>]+>','',t)).strip()
def variants(a):
    allh=''.join(s[1] for s in a['sections'])
    v=[('main',a['title'],a['desc']+' Compare specs, pros and cons side by side and find the right pick for your home office.')]
    for i,m in enumerate(re.finditer(r'<div class="pick">.*?<span class="badge">(.*?)</span><h3>(.*?)</h3>.*?<ul>(.*?)</ul><p><strong>Best for:</strong>(.*?)</p>',allh,re.S)):
        badge,name,ul,best=[strip(x) for x in m.groups()]
        short=a['title'].split(' (')[0]
        v.append((f'p{i}',f'{name} – {badge} | {short}',f'{name} ({badge.lower()}). Best for: {best} See how it compares with other picks in our guide: {a["title"]}.'))
    if not a['title'].lower().startswith('how to'): v.append(('tips',f'Before you buy: {a["title"].split(" (")[0]} checklist',f'Quick checklist before you buy. {a["desc"]}'))
    return v
today=datetime.date.today()
queue=[]
for a in reversed(arts):  # oldest first
    for vid,t,d in variants(a):
        key=f"{a['slug']}|{vid}"; queue.append((key,a,vid,t,d))
# release up to 10 new pins per day, spread over days
released_today=sum(1 for k,v in sched.items() if v==str(today))
for key,a,vid,t,d in queue:
    if key in sched: continue
    if released_today>=10: break
    sched[key]=str(today); released_today+=1
os.makedirs(os.path.dirname(STATE),exist_ok=True); json.dump(sched,open(STATE,'w'),indent=0)
def item(key,a,vid,t,d):
    link=f"{SITE}/guides/{a['slug']}/?utm_source=pinterest&utm_content={vid}"
    img=f"{SITE}/pins/{a['slug']}.png?v=3&amp;variant={vid}".replace('&amp;','&')
    pub=datetime.datetime.fromisoformat(sched[key]).strftime('%a, %d %b %Y 12:00:00 +0000')
    return f"<item><title>{X(t)}</title><link>{X(link)}</link><guid>{X(link)}</guid><pubDate>{pub}</pubDate><description>{X(d)}</description><enclosure url=\"{X(img)}\" type=\"image/png\" length=\"0\"/><media:content url=\"{X(img)}\" medium=\"image\"/></item>"
live=[q for q in queue if q[0] in sched]
def feed(name,items,title):
    open(os.path.join(R,name),'w').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/"><channel><title>{X(title)}</title><link>{SITE}/</link><description>Home office buying guides</description>{"".join(item(*q) for q in items)}</channel></rss>')
feed('feed.xml',live,'The Home Desk Guide')
cats={}
for q in live:
    cats.setdefault(re.sub(r'[^a-z0-9]+','-',q[1]['tag'].lower()).strip('-'),[]).append(q)
for c,its in cats.items(): feed(f'feed-{c}.xml',its,f'The Home Desk Guide – {its[0][1]["tag"]}')

