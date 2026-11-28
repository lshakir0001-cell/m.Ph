import json, os, html
import pathlib
OUT=str(pathlib.Path(__file__).resolve().parent.parent/'APP'/'catalog')
os.makedirs(OUT+'/img',exist_ok=True)
# id, english, arabic, cat, form, colour, strength line, search words (generic names etc.)
P=[
# ---- medicines (أدوية) ----
('panadol-500','Panadol 500mg','بنادول ٥٠٠','med','box','#d71920','500mg','paracetamol باراسيتامول مسكن حرارة'),
('panadol-extra','Panadol Extra','بنادول إكسترا','med','box','#d71920','Extra','paracetamol caffeine باراسيتامول كافيين'),
('panadol-night','Panadol Night','بنادول نايت','med','box','#1f3a93','Night','paracetamol باراسيتامول نوم'),
('panadol-baby','Panadol Baby Syrup','بنادول للأطفال شراب','med','syrup','#d71920','Baby','paracetamol باراسيتامول اطفال'),
('adol-500','Adol 500mg','أدول ٥٠٠','med','box','#0072bc','500mg','paracetamol باراسيتامول ادول'),
('adol-syrup','Adol Syrup for Children','أدول شراب للأطفال','med','syrup','#0072bc','Syrup','paracetamol باراسيتامول ادول اطفال'),
('fevadol-500','Fevadol 500mg','فيفادول ٥٠٠','med','box','#e4701e','500mg','paracetamol باراسيتامول'),
('fevadol-syrup','Fevadol Syrup','فيفادول شراب','med','syrup','#e4701e','Syrup','paracetamol باراسيتامول اطفال'),
('brufen-400','Brufen 400mg','بروفين ٤٠٠','med','box','#7a1f5c','400mg','ibuprofen ايبوبروفين'),
('brufen-syrup','Brufen Syrup','بروفين شراب','med','syrup','#7a1f5c','Syrup','ibuprofen ايبوبروفين اطفال'),
('nurofen-kids','Nurofen for Children','نيوروفين للأطفال','med','syrup','#c8102e','Kids','ibuprofen ايبوبروفين'),
('voltaren-50','Voltaren 50mg','فولتارين ٥٠','med','box','#00857c','50mg','diclofenac ديكلوفيناك'),
('voltaren-gel','Voltaren Emulgel','فولتارين جل','med','tube','#00857c','Emulgel','diclofenac ديكلوفيناك مرهم'),
('augmentin-1g','Augmentin 1g','أوجمنتين ١ جم','med','box','#5b2c83','1g','amoxicillin clavulanate اموكسيسيلين مضاد حيوي'),
('augmentin-syrup','Augmentin Suspension','أوجمنتين شراب','med','syrup','#5b2c83','Suspension','amoxicillin اموكسيسيلين مضاد حيوي ثلاجة'),
('amoxil-syrup','Amoxil Syrup','أموكسيل شراب','med','syrup','#2e7d32','Syrup','amoxicillin اموكسيسيلين مضاد حيوي'),
('zithromax','Zithromax 250mg','زيثروماكس ٢٥٠','med','box','#0057a8','250mg','azithromycin ازيثرومايسين مضاد حيوي'),
('flagyl','Flagyl 500mg','فلاجيل ٥٠٠','med','box','#a6192e','500mg','metronidazole ميترونيدازول'),
('nexium-40','Nexium 40mg','نيكسيوم ٤٠','med','box','#6d2077','40mg','esomeprazole اسوميبرازول معدة حموضة'),
('gaviscon','Gaviscon Liquid','جافيسكون شراب','med','syrup','#00a3e0','Liquid','حموضة معدة'),
('buscopan','Buscopan 10mg','بسكوبان ١٠','med','box','#008a5e','10mg','hyoscine هيوسين مغص'),
('imodium','Imodium 2mg','إيموديوم ٢','med','box','#00539f','2mg','loperamide لوبيراميد اسهال'),
('motilium','Motilium 10mg','موتيليوم ١٠','med','box','#e30613','10mg','domperidone دومبيريدون غثيان'),
('zyrtec','Zyrtec 10mg','زيرتك ١٠','med','box','#00788a','10mg','cetirizine سيتريزين حساسية'),
('claritine','Claritine 10mg','كلاريتين ١٠','med','box','#0a6ab6','10mg','loratadine لوراتادين حساسية'),
('telfast-180','Telfast 180mg','تلفاست ١٨٠','med','box','#7b2a8e','180mg','fexofenadine فيكسوفينادين حساسية'),
('ventolin','Ventolin Inhaler','فنتولين بخاخ','med','inhaler','#00a0df','100mcg','salbutamol سالبوتامول ربو'),
('otrivin','Otrivin Nasal Spray','أوتريفين بخاخ أنف','med','spray','#0089cf','0.1%','xylometazoline زيلوميتازولين انف'),
('strepsils','Strepsils','ستربسلز','med','box','#e2001a','Lozenges','حلق'),
('vicks','Vicks VapoRub','فيكس','med','jar','#005a2b','VapoRub','زكام'),
('glucophage-500','Glucophage 500mg','جلوكوفاج ٥٠٠','med','box','#6e2c8c','500mg','metformin ميتفورمين سكر'),
('lantus','Lantus SoloStar','لانتوس سولوستار','med','pen','#6a1b9a','SoloStar','insulin glargine انسولين سكر ثلاجة'),
('novorapid','NovoRapid FlexPen','نوفورابيد فليكس بن','med','pen','#f36f21','FlexPen','insulin aspart انسولين سكر ثلاجة'),
('ozempic','Ozempic Pen','أوزمبيك','med','pen','#0d7c8c','Pen','semaglutide سيماجلوتايد سكر ثلاجة'),
('concor-5','Concor 5mg','كونكور ٥','med','box','#c8102e','5mg','bisoprolol بيسوبرولول ضغط'),
('lipitor-20','Lipitor 20mg','ليبيتور ٢٠','med','box','#0a4c97','20mg','atorvastatin اتورفاستاتين كوليسترول'),
('aspocid','Aspocid 81mg','أسبوسيد ٨١','med','box','#e41f26','81mg','aspirin اسبرين'),
('eltroxin','Eltroxin 50mcg','التروكسين ٥٠','med','box','#00539b','50mcg','levothyroxine ليفوثيروكسين غدة'),
('systane','Systane Eye Drops','سيستين قطرة عين','med','drops','#0067b1','Ultra','قطرة عين جفاف'),
('fucidin','Fucidin Cream','فيوسيدين كريم','med','tube','#e4002b','Cream','fusidic acid فيوسيديك مرهم'),
('bepanthen','Bepanthen Ointment','بيبانثين مرهم','med','tube','#0a5ea8','Ointment','dexpanthenol مرهم حفاض'),
('daktarin','Daktarin Cream','دكتارين كريم','med','tube','#e2231a','Cream','miconazole ميكونازول فطريات'),
('betadine','Betadine Solution','بيتادين','med','syrup','#7b3f00','10%','povidone iodine مطهر'),
('prospan','Prospan Syrup','بروسبان شراب','med','syrup','#1b8a3a','Syrup','ivy leaf كحة سعال'),
('mucosolvan','Mucosolvan Syrup','ميوكوسولفان شراب','med','syrup','#0067a6','Syrup','ambroxol امبروكسول كحة بلغم'),
('centrum','Centrum Multivitamin','سنتروم','med','bottle','#004b87','Multi','فيتامين vitamins'),
('vitd3','Vitamin D3 Drops','فيتامين د قطرات','med','drops','#f2a900','D3','vitamin d فيتامين دال'),
('omega3','Omega 3','أوميغا ٣','med','bottle','#f39c12','1000mg','fish oil زيت السمك'),
('lacteol','Lacteol','لاكتيول','med','box','#0098d4','Probiotic','بروبيوتيك ثلاجة'),
# ---- skincare (عناية بالبشرة) ----
('cerave-cream','CeraVe Moisturizing Cream','سيرافي كريم مرطب','skin','jar','#0060a9','Moisturizing','سيرافي مرطب'),
('cerave-foaming','CeraVe Foaming Cleanser','سيرافي غسول رغوي','skin','pump','#0060a9','Foaming','غسول سيرافي'),
('cerave-hydrating','CeraVe Hydrating Cleanser','سيرافي غسول مرطب','skin','pump','#0060a9','Hydrating','غسول سيرافي'),
('lrp-effaclar-duo','La Roche-Posay Effaclar Duo','لاروش بوزيه إيفاكلار ديو','skin','tube','#1b75bb','Effaclar Duo+','لاروش حبوب'),
('lrp-anthelios','La Roche-Posay Anthelios SPF50','لاروش بوزيه واقي شمس','skin','tube','#f39200','SPF50+','لاروش واقي شمس'),
('lrp-cicaplast','La Roche-Posay Cicaplast Baume B5','لاروش بوزيه سيكابلاست','skin','tube','#1b75bb','Baume B5','لاروش مرطب'),
('ordinary-niacinamide','The Ordinary Niacinamide 10% + Zinc','ذا أوردينري نياسيناميد','skin','serum','#222222','Niacinamide','اوردينري سيروم'),
('ordinary-ha','The Ordinary Hyaluronic Acid 2% + B5','ذا أوردينري هيالورونيك','skin','serum','#222222','Hyaluronic','اوردينري سيروم'),
('ordinary-retinol','The Ordinary Retinol 0.5%','ذا أوردينري ريتينول','skin','serum','#222222','Retinol 0.5%','اوردينري ريتينول ثلاجة'),
('vitc-serum','Vitamin C Serum','سيروم فيتامين سي','skin','serum','#f28c00','Vitamin C','فيتامين سي سيروم ثلاجة'),
('retinol-cream','Retinol Cream','كريم ريتينول','skin','jar','#8e44ad','Retinol','ريتينول'),
('bioderma-sensibio','Bioderma Sensibio H2O','بيوديرما ميسيلار','skin','bottle','#e5007e','H2O','ميسيلار مزيل مكياج'),
('avene-water','Avène Thermal Spring Water','أفين ماء حراري','skin','spray','#e6007e','Thermal Water','افين بخاخ'),
('cetaphil','Cetaphil Gentle Skin Cleanser','سيتافيل غسول لطيف','skin','pump','#0067b1','Gentle','غسول سيتافيل'),
('vichy-m89','Vichy Minéral 89','فيشي مينرال ٨٩','skin','serum','#00205b','Minéral 89','فيشي سيروم'),
('neutrogena-hb','Neutrogena Hydro Boost','نيتروجينا هيدرو بوست','skin','jar','#0071ce','Hydro Boost','نيتروجينا مرطب'),
('nivea-creme','NIVEA Creme','نيفيا كريم','skin','jar','#0e2a6b','Creme','نيفيا'),
('eucerin-urea','Eucerin UreaRepair','يوسيرين يوريا','skin','tube','#003e7e','UreaRepair','يوسيرين'),
('garnier-micellar','Garnier Micellar Water','غارنييه ميسيلار','skin','bottle','#e5007d','Micellar','قارنييه مزيل مكياج'),
('vaseline-lip','Vaseline Lip Therapy','فازلين شفايف','skin','jar','#5aa0d0','Lip','فازلين شفايف'),
]
DARK=lambda c:c
def esc(s):return html.escape(s,quote=True)
def label(x,y,w,txt,size,col='#fff',weight=800):
    # shrink long words so they fit
    size=min(size, w/(0.58*max(1,len(txt))))
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="{weight}" font-size="{size:.1f}" fill="{col}">{esc(txt)}</text>'
def brand(name):
    # first word(s) as the big brand label
    n=name.replace('La Roche-Posay','LRP').replace('The Ordinary','The Ordinary')
    w=n.split()
    if w[0] in ('The','Vitamin','Retinol') and len(w)>1: return ' '.join(w[:2])
    return w[0]
def svg(form,c,name,sub,cat):
    bg='#e8f7ef' if cat=='med' else '#ffeef3'
    b=brand(name); body=''
    if form=='box':
        body=f'''<path d="M30 52 L50 36 H138 L118 52Z" fill="{c}" opacity=".75"/><path d="M118 52 L138 36 V120 L118 136Z" fill="{c}" opacity=".55"/>
<rect x="22" y="52" width="96" height="84" rx="3" fill="#fff" stroke="{c}" stroke-width="2"/><rect x="22" y="52" width="96" height="26" fill="{c}"/>
{label(70,71,90,b,17)}{label(70,100,88,sub,13,c)}<g fill="{c}" opacity=".85"><rect x="42" y="112" width="22" height="10" rx="5"/><circle cx="88" cy="117" r="6"/></g>'''
    elif form=='syrup':
        body=f'''<rect x="62" y="20" width="36" height="18" rx="3" fill="{c}"/><path d="M66 38h28v10c14 4 20 12 20 24v58a8 8 0 0 1-8 8H54a8 8 0 0 1-8-8V72c0-12 6-20 20-24z" fill="#b9722f" opacity=".85"/>
<rect x="50" y="78" width="60" height="50" rx="3" fill="#fff"/><rect x="50" y="78" width="60" height="14" fill="{c}"/>{label(80,89,56,b,11)}{label(80,112,54,sub,11,c)}'''
    elif form=='tube':
        body=f'''<path d="M44 24h72l-6 96H50z" fill="#fff" stroke="{c}" stroke-width="2"/><path d="M44 24h72v12H44z" fill="{c}" opacity=".5"/><rect x="62" y="120" width="36" height="22" rx="3" fill="{c}"/>
<rect x="48" y="44" width="64" height="22" fill="{c}"/>{label(80,60,60,b,14)}{label(80,88,58,sub,11,c)}'''
    elif form=='pen':
        body=f'''<g transform="rotate(-35 80 80)"><rect x="20" y="66" width="104" height="26" rx="12" fill="#fff" stroke="{c}" stroke-width="2"/><rect x="20" y="66" width="34" height="26" rx="12" fill="{c}"/>
<rect x="124" y="72" width="14" height="14" rx="3" fill="#9aa"/><rect x="138" y="77" width="10" height="4" fill="#9aa"/><rect x="60" y="72" width="40" height="14" rx="2" fill="#eef"/></g>
{label(80,138,120,b,15,c)}{label(80,152,120,sub,11,'#333',500)}'''
    elif form=='drops':
        body=f'''<path d="M74 18l-6 22h24l-6-22z" fill="{c}"/><rect x="64" y="40" width="32" height="14" rx="3" fill="{c}"/><rect x="54" y="54" width="52" height="78" rx="10" fill="#fff" stroke="{c}" stroke-width="2"/>
<rect x="54" y="74" width="52" height="18" fill="{c}"/>{label(80,87,48,b,11)}{label(80,112,48,sub,11,c)}'''
    elif form=='inhaler':
        body=f'''<rect x="58" y="16" width="36" height="96" rx="12" fill="{c}"/><path d="M58 96h36v26a8 8 0 0 1-8 8H40a8 8 0 0 1-8-8v-14a8 8 0 0 1 8-8h18z" fill="#cfd8dc" stroke="#90a4ae"/>
<rect x="64" y="34" width="24" height="40" rx="3" fill="#fff"/>{label(80,146,120,b,15,c)}'''
    elif form=='spray':
        body=f'''<path d="M72 14h16l4 26H68z" fill="#fff" stroke="{c}" stroke-width="2"/><rect x="62" y="40" width="36" height="10" rx="2" fill="{c}"/><rect x="54" y="50" width="52" height="88" rx="10" fill="#fff" stroke="{c}" stroke-width="2"/>
<rect x="54" y="70" width="52" height="22" fill="{c}"/>{label(80,85,48,b,12)}{label(80,114,48,sub,10,c)}'''
    elif form=='jar':
        body=f'''<rect x="30" y="54" width="100" height="20" rx="6" fill="{c}"/><path d="M34 74h92v44a10 10 0 0 1-10 10H44a10 10 0 0 1-10-10z" fill="#fff" stroke="{c}" stroke-width="2"/>
{label(80,98,86,b,16,c)}{label(80,118,86,sub,11,'#333',500)}'''
    elif form=='pump':
        body=f'''<path d="M70 14h26v8H78v10h-8z" fill="#ddd" stroke="#999"/><rect x="66" y="32" width="28" height="14" rx="3" fill="#eee" stroke="#999"/><rect x="48" y="46" width="64" height="94" rx="10" fill="#fff" stroke="{c}" stroke-width="2"/>
<rect x="48" y="66" width="64" height="22" fill="{c}"/>{label(80,82,60,b,13)}{label(80,110,58,sub,11,c)}'''
    elif form=='serum':
        body=f'''<rect x="72" y="12" width="16" height="22" rx="7" fill="#333"/><rect x="66" y="34" width="28" height="14" rx="2" fill="#555"/><rect x="56" y="48" width="48" height="90" rx="6" fill="#d9a35e" opacity=".55" stroke="#9c6b2f"/>
<rect x="58" y="70" width="44" height="40" fill="#fff"/>{label(80,86,40,b,9,'#111')}{label(80,100,40,sub,8,c,600)}'''
    elif form=='bottle':
        body=f'''<rect x="64" y="20" width="32" height="18" rx="3" fill="{c}"/><rect x="48" y="38" width="64" height="100" rx="12" fill="#fff" stroke="{c}" stroke-width="2"/>
<rect x="48" y="62" width="64" height="24" fill="{c}"/>{label(80,79,60,b,13)}{label(80,108,58,sub,11,c)}'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160"><rect width="160" height="160" fill="{bg}"/>{body}</svg>\n'
cat=[]
for (i,en,ar,c,form,col,sub,kw) in P:
    open(f'{OUT}/img/{i}.svg','w').write(svg(form,col,en,sub,c))
    ar=ar.translate(str.maketrans('٠١٢٣٤٥٦٧٨٩','0123456789'))
    cat.append({'id':i,'en':en,'ar':ar,'cat':c,'img':f'catalog/img/{i}.svg','kw':kw,'gtin':[]})
with open(f'{OUT}/catalog.js','w') as f:
    f.write('''/* Mini Pharmacy built-in catalog: common medicines and skincare in Saudi Arabia.
   Each entry: id, en (English name), ar (Arabic name), cat (med|skin), img (picture path),
   kw (extra search words, e.g. the generic/scientific name), gtin (box barcodes, GTIN-14, if known).
   The pictures in catalog/img are simple drawings, not the companies' real box photos.
   To use a real photo: save it as catalog/img/<id>.jpg and change img to that path.
   To add a product: copy one line and change it. */
window.MPH_CATALOG=[\n''')
    f.write(',\n'.join(json.dumps(x,ensure_ascii=False) for x in cat))
    f.write('\n];\n')
print(len(cat))
