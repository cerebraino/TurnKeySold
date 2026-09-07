import csv, re, os

# ---------- LOADERS ----------
def load_base():
    with open('DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv', newline='') as f:
        r = csv.reader(f); h = next(r)
        return {row[0]: row for row in r if row and row[0].strip()}
def load_appr():
    d = {}
    with open('PORTFOLIO/full_appraisal.csv', newline='') as f:
        r = csv.reader(f); h = next(r)
        for row in r:
            if row and row[0].strip(): d[row[0]] = dict(zip(h,row))
    return d

base = load_base()
appr = load_appr()

def parseval(s):
    m = re.search(r'\$([\d,]+)', s)
    return int(m.group(1).replace(',','')) if m else None

# ---------- PRIORITY ----------
items = [(parseval(base[d][1]), i, d) for i,d in enumerate(base)]
items.sort(key=lambda x: (-x[0], x[1]))
p36 = {d for _,_,d in items[:36]}

SOLD = {'leanmeds.com'}
EXPG = {'curebyketo.com','fusebot.ai','weputt.com','paretobuddy.com'}
priority = p36 - SOLD - EXPG

def status_of(d):
    if d in SOLD: return 'SOLD'
    if d in EXPG: return 'EXPANSION-READY'
    if d in priority: return 'PRIORITY'
    return 'ACTIVE'

# ---------- PORTFOLIO GROUP ----------
BP_GROUP = {
    'topsex.ai':'Adult','whorehouse.ai':'Adult','aisexshops.com':'Adult','puticlub.ai':'Adult',
    'burdel.ai':'Adult','putasexo.com':'Adult','putero.ai':'Adult','puticlub.online':'Adult','putero.online':'Adult',
    'buyslimmeds.com':'Weight Loss','bestslimmeds.com':'Weight Loss','cheapslimmeds.com':'Weight Loss',
    'curebyketo.com':'Weight Loss','amoketo.com':'Weight Loss','tipsketo.com':'Weight Loss','bajapanza.com':'Weight Loss',
    'leanmeds.com':'Weight Loss',
    'lavoiture.ai':'Core','knowlaw.ai':'Core','hispanoabogado.com':'Core',
}
def group_from_cat(cat):
    if not cat: return None
    c = cat.lower()
    if 'adult' in c: return 'Adult'
    if 'weight loss' in c or 'keto' in c: return 'Weight Loss'
    if 'auto' in c: return 'Automotive'
    if 'betting' in c: return 'Betting/Gambling'
    if 'real estate' in c or 'mortgage' in c: return 'Real Estate/Mortgage'
    if 'hispanic' in c: return 'Hispanic Market'
    if 'legal' in c: return 'Legal'
    if 'health' in c or 'medical' in c or 'wellness' in c: return 'Health/Wellness'
    if 'field' in c or 'logistics' in c: return 'Field Service/Logistics'
    if 'payment' in c or 'pay' in c: return 'Payments/Fintech'
    if 'beer' in c or 'drink' in c: return 'Beer/Beverage'
    if 'cannabis' in c or 'mota' in c: return 'Cannabis'
    if 'spanish' in c or 'mexico' in c: return 'Spanish/LatAm'
    if 'spiritual' in c or 'fitness' in c: return 'Lifestyle'
    if 'tech' in c: return 'Tech/General'
    if 'general' in c or 'brand' in c or 'productivity' in c: return 'General'
    if 'reliability' in c or 'safety' in c or 'ai' in c: return 'AI/SaaS'
    return 'General'

def group_of(d):
    if d in BP_GROUP: return BP_GROUP[d]
    if d in appr: return group_from_cat(appr[d]['Category'])
    return ''

# ---------- LANGUAGE ----------
def lang_of(d):
    if d in appr:
        c = appr[d]['Category'].lower()
        if 'french' in c: return 'FR'
        if 'spanish' in c or 'mexico' in c or 'hispanic' in c or 'latin' in c: return 'ES'
        if 'portuguese' in c: return 'PT'
    s = d.lower()
    if 'voiture' in s or d=='lavoiture.ai': return 'FR'
    if any(x in s for x in ['hispano','latino','latinomedico','bajapanza','muy','paga','pagatu','pague','paguesu','suacasa','quitesu','teapuesto','apuesto','platicar','bailar','cantar','reir','infancia','hipoteca','la','comprarcasita','bajaturenta','adelgaza','comodejar','pararde','cancelar','rentahumanos','rentapersona','pruebade','mex','mota']) and 'net' not in s[-3:]: return 'ES'
    if 'automovel' in s or 'automoveis' in s: return 'PT'
    return 'EN'

# ---------- SPECIAL: vivamucho truncated category cell cleanup from leads §2 ----------
# leads_vivamucho.com.md §2: Spanish-language longevity/wellness clinics, doctors, creators
VIVAMUCHO_CATS = "Spanish-language longevity/wellness clinics & doctors; health/fitness content creators (Dr. Carlos Jaramillo, Dr. Bayter, Patry Jordan); premium wellness travel/lifestyle brands"

# ---------- NOTES (explicit flags) ----------
# Ketoned Bodies = gambling-spam domain exclusion (curebyketo lead), Routine dead site, Voiceflow implied-email
NOTES = {
  'curebyketo.com': 'Lead Ketoned Bodies EXCLUDED (gambling-spam domain); Routine EXCLUDED (dead site); Ketone-IQ is top expansion lead (Geoffrey Woo).',
  'fusebot.ai': 'Gumloop (Max Brodeur-Urbas) top NEW lead; Voiceflow = LinkedIn-DM channel only (implied email, owner judgment pending).',
  'weputt.com': 'Golf-tech expansion leads (TrackMan sales@, Toptracer info@, SwingU support@ fireable).',
  'paretobuddy.com': 'Pareto/personal-finance expansion leads (Sunsama Travis Meyer, Any.do, TickTick, Toggl).',
  'lavoiture.ai': '5 CEO changes caught 2026-09-04: Stellantis=Filosa, Renault=Provost, ACC=Swan, Verkor=Debrue, Einride=Charli. FR-first market; Quebec expansion rounds 1-2 complete (MTL-10 file 2026-09-05).',
  'knowlaw.ai': 'Pilot strongest yield (7 NEW). Exec: Lan Francis co-founder (verify title before use).',
  'nofail.ai': 'Pilot yield 6 NEW. PagerDuty exec = John DiLullo (NOT Tejada - stale-row fix applied 2026-09-05).',
  'nobreak.ai': 'PagerDuty exec = John DiLullo (stale-row fix 2026-09-05).',
  'burdel.ai': 'Stripchat CEO = Breeze Dennis (blank filled 2026-09-05).',
  'topsex.ai': 'Blueheart/Dr. Sachin Raoul alt lead (health/ed) DMPS 92, $25-35K ask.',
  'leanmeds.com': 'SOLD via Spaceship (Trinity HealthCare Supply). No outreach.',
  'hispanoabogado.com': 'Pilot weakest yield (1 NEW) - already saturated.',
  'payauto.ai': 'Pilot weakest yield (1 NEW) - already saturated.',
  'onegal.net': 'Base CSV lists as part of General/Other; low value domain.',
  'theaicustomeracquisition.com': '16.5K value; AI marketing category.',
}

# ---------- DEFENSIBLE VALUE NOTE: keep base string as-is ----------
# ---------- APPRAISAL FIELDS ----------
def int_or_blank(s):
    if s is None or str(s).strip()=='' : return ''
    try:
        v = str(s).replace(',','').strip()
        return str(int(v))
    except: return ''

# ---------- BUILD ROWS ----------
cols = ['domain','status','portfolio_group','language_market','est_value_low_usd','est_value_high_usd',
        'defensible_value_note','brandability_1_10','sale_potential','buyer_categories_top3',
        'top_buyers_with_dmps','sample_micro_message','notes']

rows = []
for d in base:
    base_row = base[d]
    value_note = base_row[1]
    cats_raw = base_row[2]
    buyers = base_row[3]
    micro = base_row[4]
    a = appr.get(d, {})
    # buyer categories top3
    if d == 'vivamucho.com':
        cats_top3 = VIVAMUCHO_CATS
    else:
        cats_top3 = cats_raw if cats_raw and cats_raw.strip() and cats_raw != 'not yet researched' else ''
    # top buyers w/ dmps: keep base col 4 verbatim unless "not yet researched"
    buyers_out = buyers if buyers and buyers.strip() and buyers != 'not yet researched' else ''
    micro_out = micro if micro and micro.strip() else ''
    notes = NOTES.get(d,'')
    row = [
        d,
        status_of(d),
        group_of(d) or '',
        lang_of(d),
        int_or_blank(a.get('Est. Low','')),
        int_or_blank(a.get('Est. High','')),
        value_note.strip(),
        a.get('Brandability (1-10)','') if d in appr else '',
        a.get('Sale Potential','') if d in appr else '',
        cats_top3,
        buyers_out,
        micro_out,
        notes,
    ]
    rows.append(row)

# order: keep base CSV original order? or value desc? For collaborator hand-off, value desc is clearer.
# We'll sort by status (SOLD last) then value desc, but keep base order for stable ties.
rows.sort(key=lambda r: (r[1]=='SOLD', -(parseval(dict((rr[0],rr) for rr in rows)[r[0]][5] if False else 0) if False else 0)))
# status rank: PRIORITY/EXPANSION(0) < ACTIVE(1) < SOLD(2); then value desc
def status_rank(r):
    if r[1] == 'SOLD': return 2
    if r[1] in ('PRIORITY','EXPANSION-READY'): return 0
    return 1
vmap = {r[0]: parseval(r[6]) or 0 for r in rows}
rows.sort(key=lambda r: (status_rank(r), -vmap[r[0]]))

out = '/home/team/shared/MASTER-DOMAIN-INVENTORY_2026-09-06.csv'
with open(out,'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(cols)
    for row in rows:
        w.writerow(row)
print("WROTE", len(rows), "rows ->", out)
