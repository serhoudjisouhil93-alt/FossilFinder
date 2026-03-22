import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title="FossilFinder · Field Edition", layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family:'Inter',sans-serif; background:#f8f7f4; color:#2c2c2c; }
.stApp { background:#f8f7f4; }
section[data-testid="stSidebar"] { background:#fff; border-right:1px solid #e8e4dc; }
section[data-testid="stSidebar"] * { color:#2c2c2c !important; }

.site-header { background:#fff; border-bottom:2px solid #c8a96e; padding:28px 0 22px; margin-bottom:36px; }
.site-header-inner { display:flex; align-items:flex-end; justify-content:space-between; }
.site-title { font-family:'Playfair Display',serif; font-size:38px; font-weight:700; color:#1a1a1a; margin:0; }
.site-title span { color:#8a6830; }
.site-sub { font-size:11px; color:#9a8a6a; letter-spacing:0.22em; text-transform:uppercase; margin-top:6px; }
.site-author { font-size:12px; color:#9a8a6a; text-align:right; line-height:1.6; }
.site-author strong { color:#5a3a10; font-weight:700; font-size:15px; display:block; font-family:'Playfair Display',serif; }

.sec-title { font-family:'Playfair Display',serif; font-size:22px; font-weight:600; color:#1a1a1a;
             border-bottom:1px solid #e0d8cc; padding-bottom:10px; margin-bottom:6px; }
.sec-sub { font-size:12px; color:#9a8a6a; margin-bottom:22px; }

.kpi { flex:1; min-width:120px; background:#fff; border:1px solid #e8e4dc; border-top:3px solid #c8a96e;
       border-radius:6px; padding:16px 20px; }
.kpi-n { font-family:'Playfair Display',serif; font-size:30px; font-weight:700; color:#8a6830; }
.kpi-l { font-size:10px; color:#9a8a6a; letter-spacing:0.16em; text-transform:uppercase; margin-top:4px; font-weight:500; }

.fcard { background:#fff; border:1px solid #e8e4dc; border-radius:8px; overflow:hidden; margin-bottom:24px;
         transition:box-shadow 0.2s,border-color 0.2s; }
.fcard:hover { box-shadow:0 4px 20px rgba(140,100,40,0.10); border-color:#c8a96e; }
.fcard-body { padding:20px 22px 22px; }
.fcard-era { font-size:10px; letter-spacing:0.18em; color:#9a8a6a; text-transform:uppercase; margin-bottom:5px; font-weight:500; }
.fcard-name { font-family:'Playfair Display',serif; font-size:20px; font-weight:700; font-style:italic; color:#1a1a1a; margin-bottom:2px; }
.fcard-common { font-size:13px; color:#8a6830; margin-bottom:14px; font-weight:500; }
.fcard-desc { font-size:13px; color:#4a4a4a; line-height:1.75; margin-bottom:16px; }
.fact-box { background:#faf7f0; border-left:3px solid #c8a96e; padding:12px 16px; margin-bottom:14px; border-radius:0 5px 5px 0; }
.fact-label { font-size:9px; color:#9a8a6a; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:5px; font-weight:600; }
.fact-text { font-size:12px; color:#5a4a2a; line-height:1.65; font-style:italic; }
.sig-box { background:#f5f3ef; border:1px solid #e8e4dc; border-radius:5px; padding:10px 14px;
           font-size:12px; color:#5a5040; margin-bottom:14px; line-height:1.6; }
.sig-label { font-size:9px; color:#9a8a6a; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:4px; font-weight:600; }
.tag { display:inline-block; background:#f5f3ef; border:1px solid #e0d8cc; border-radius:3px;
       padding:3px 9px; font-size:10px; color:#7a6a4a; margin:2px 2px 2px 0; font-weight:500; }
.tag-env { background:#f0f5f0; border-color:#c8dcc8; color:#3a6a3a; }
.tag-loc { background:#f5f0ea; border-color:#d8c8a8; color:#6a4a1a; }

.stTabs [data-baseweb="tab-list"] { background:transparent; border-bottom:2px solid #e8e4dc; gap:0; }
.stTabs [data-baseweb="tab"] { font-family:'Inter',sans-serif; font-size:12px; font-weight:500;
  letter-spacing:0.08em; text-transform:uppercase; color:#9a8a6a; background:transparent; border:none; padding:10px 22px; }
.stTabs [aria-selected="true"] { color:#5a3a10 !important; border-bottom:2px solid #c8a96e !important;
  background:transparent !important; margin-bottom:-2px; }

.stSelectbox>div>div, .stMultiSelect>div>div, .stTextInput>div>div>input {
  background:#fff !important; border:1px solid #e0d8cc !important; color:#2c2c2c !important;
  font-family:'Inter',sans-serif !important; font-size:13px !important; border-radius:5px !important; }
.stButton>button { background:#fff !important; border:1px solid #c8a96e !important; color:#5a3a10 !important;
  font-family:'Inter',sans-serif !important; font-size:12px !important; font-weight:500 !important;
  letter-spacing:0.08em; border-radius:5px !important; padding:8px 18px !important; }
.stButton>button:hover { background:#faf7f0 !important; border-color:#8a6830 !important; }

.result-banner { background:#faf7f0; border:1px solid #e8e4dc; border-left:3px solid #c8a96e;
  border-radius:0 5px 5px 0; padding:10px 16px; margin-bottom:24px; font-size:13px; color:#5a4a2a; }
.footer { border-top:1px solid #e8e4dc; padding:20px 0 10px; margin-top:40px;
  display:flex; justify-content:space-between; align-items:center; font-size:11px; color:#9a8a6a; }
.footer-name { font-family:'Playfair Display',serif; font-size:16px; font-weight:700; color:#5a3a10; }
hr { border-color:#e8e4dc !important; }
</style>
""", unsafe_allow_html=True)

PLOT_LAYOUT = dict(paper_bgcolor="#ffffff", plot_bgcolor="#faf7f0",
                   font=dict(family="Inter, sans-serif", color="#2c2c2c", size=11),
                   margin=dict(l=50, r=20, t=50, b=50))
ERA_COLORS = {"Paleozoic":"#6a9a5a","Mesozoic":"#4a8a8a","Cenozoic":"#c8973a"}

FOSSILS = [
    dict(name="Trilobita", common="Trilobite",
         period="Cambrian–Permian", age_start=521, age_end=252, era="Paleozoic",
         environments=["Marine shallow","Marine deep","Reef"], group="Arthropod", preservation="Excellent",
         description="Among Earth's most successful early animals, trilobites dominated Paleozoic seas for nearly 270 million years. Their calcite exoskeletons preserve exceptionally well — rolled specimens indicate a stress response still visible 500 million years later.",
         fact="Over 20,000 species have been described — more diverse than all modern mammals combined. Some had eyes made of calcite crystals that required no focusing.",
         significance="Primary zone fossil for Cambrian–Ordovician. Rolled specimens indicate storm events or predator pressure.",
         locations=["Morocco (Anti-Atlas)","USA (Utah, Ohio)","Russia","China","Canada (Burgess Shale)","Algeria (Saharan platform)"],
         coords=[(31.5,-7.0),(39.3,-111.0),(55.7,37.6),(30.0,110.0),(51.4,-116.5)],
         image_url="images/trilobite.jpg"),
    dict(name="Ammonoidea", common="Ammonite",
         period="Devonian–Cretaceous", age_start=419, age_end=66, era="Mesozoic",
         environments=["Marine shallow","Marine open water","Marine deep"], group="Cephalopod", preservation="Excellent",
         description="The ultimate biostratigraphic tool. Ammonites evolved so rapidly that each species existed for less than 1 million years on average. Their coiled chambered shells allowed neutral buoyancy like a submarine. Suture patterns on weathered specimens identify genus and species.",
         fact="The largest ammonite ever found — Parapuzosia seppenradensis from Germany — reached 1.8 meters in diameter. Most field specimens fit in one hand.",
         significance="Primary biozone fossil for Jurassic and Cretaceous. Suture complexity increases through time — useful for relative age dating in the field.",
         locations=["UK (Whitby, Dorset)","Morocco (Erfoud)","Madagascar","France (Normandy)","Germany","Tunisia","Algeria (Tlemcen)"],
         coords=[(54.4,-0.6),(31.4,-4.0),(-20.0,47.0),(49.1,-0.4),(51.3,10.4)],
         image_url="images/ammonite.jpg"),
    dict(name="Graptolithina", common="Graptolite",
         period="Cambrian–Carboniferous", age_start=510, age_end=320, era="Paleozoic",
         environments=["Marine deep","Marine open water"], group="Hemichordate", preservation="Good",
         description="Flattened carbon films on black shales — easily missed by untrained eyes. Their rapid evolution makes them the primary zone fossil for Ordovician and Silurian rocks worldwide. Look for saw-blade patterns on dark fine-grained shales.",
         fact="Graptolites were once classified as plants — their name means 'written rock' in Greek. They were only recognized as animals in the 20th century.",
         significance="Primary zone fossil for Ordovician–Silurian globally. Black shale hosting indicates anoxic deep water paleoenvironment.",
         locations=["Wales (type locality)","Scotland","Canada (Quebec)","China","Australia","Czech Republic"],
         coords=[(52.3,-3.7),(56.0,-4.2),(47.0,-71.0),(30.0,110.0),(-25.0,133.0)],
         image_url="images/graptolite.jpg"),
    dict(name="Brachiopoda", common="Brachiopod",
         period="Cambrian–Present", age_start=530, age_end=0, era="Paleozoic",
         environments=["Marine shallow","Reef","Marine deep"], group="Brachiopod", preservation="Excellent",
         description="Superficially similar to bivalves but biologically unrelated. The key field distinction: brachiopods have one plane of symmetry through the shell top-to-bottom, bivalves through left-right. They were the dominant shelled organisms of Paleozoic seas and still exist today.",
         fact="Living brachiopods called Lingula are nearly identical to specimens from 500 million years ago — the slowest-evolving animals on Earth.",
         significance="Useful for Devonian biostratigraphy. Abundance indicates normal marine salinity. Must be distinguished from bivalves for accurate paleoenvironment interpretation.",
         locations=["Germany (Rhine)","USA (Devonian of New York)","UK (Silurian)","China","Australia","Algeria"],
         coords=[(50.9,6.9),(42.9,-76.0),(52.3,-1.5),(30.0,110.0),(-25.0,133.0)],
         image_url="images/brachiopod.jpg"),
    dict(name="Foraminifera", common="Foraminifera",
         period="Cambrian–Present", age_start=530, age_end=0, era="Cenozoic",
         environments=["Marine shallow","Marine deep","Marine open water","Lagoon"], group="Protist", preservation="Excellent",
         description="Microscopic single-celled organisms visible only under hand lens or microscope. Despite their size, they are the primary biostratigraphic tool for Cenozoic marine sections globally. Foram-bearing limestones often have a sugary or granular texture. Nummulites are visible to the naked eye.",
         fact="The Great Pyramid of Giza is built almost entirely from nummulitic limestone — billions of foram shells quarried and stacked by ancient Egyptians.",
         significance="Primary Cenozoic biozone tool. Planktonic/benthic ratio indicates paleodepth. Oxygen isotopes from shells reconstruct ancient ocean temperatures.",
         locations=["Global oceans","Egypt (Eocene)","North Sea","Caribbean","Algeria (Saharan platform)","Tunisia"],
         coords=[(29.9,31.1),(56.0,3.0),(15.0,-75.0),(36.8,10.2),(28.0,2.0)],
         image_url="images/foraminifera.jpg"),
    dict(name="Echinoidea", common="Sea Urchin (Fossil)",
         period="Ordovician–Present", age_start=480, age_end=0, era="Mesozoic",
         environments=["Marine shallow","Reef","Lagoon"], group="Echinoderm", preservation="Good",
         description="Regular and irregular echinoids are common in Cretaceous chalks and Jurassic limestones. Irregular forms like Micraster are classic zone fossils for the Cretaceous chalk of NW Europe. In the field, five-fold symmetry and ambulacral grooves are diagnostic.",
         fact="Medieval Europeans called echinoid tests 'shepherd's crowns' or 'fairy loaves' and kept them as good luck charms. Neolithic humans buried them with the dead.",
         significance="Micraster is a zone fossil for Cretaceous chalk. Irregular echinoids indicate infaunal life and soft muddy seafloor conditions.",
         locations=["UK (chalk downs)","France (Normandy chalk)","North Africa","Egypt","Israel","Denmark"],
         coords=[(51.2,0.5),(49.1,0.3),(27.0,20.0),(29.5,31.2),(31.0,35.0)],
         image_url="images/echinoid.jpg"),
    dict(name="Belemnoidea", common="Belemnite",
         period="Carboniferous–Eocene", age_start=360, age_end=34, era="Mesozoic",
         environments=["Marine shallow","Marine open water"], group="Cephalopod", preservation="Good",
         description="The bullet-shaped calcite guard is what preserves — the soft squid-like body rarely fossilizes. Belemnite guards are common in Jurassic and Cretaceous marine rocks worldwide. Dense accumulations called 'belemnite battlefields' may represent mass mortality events.",
         fact="In medieval Scandinavia, belemnites were called 'thunderbolts' — people believed they fell from the sky during lightning storms and had magical protective properties.",
         significance="Useful index fossil for Jurassic–Cretaceous marine sequences. Guards indicate normal marine, moderate-energy conditions.",
         locations=["UK (Jurassic Coast)","Germany (Solnhofen)","Russia","Poland","Algeria (Tlemcen region)","Tunisia"],
         coords=[(50.6,-2.4),(48.8,11.0),(55.0,40.0),(52.0,20.0),(34.8,-1.3)],
         image_url="images/belemnite.jpg"),
    dict(name="Crinoidea", common="Crinoid (Sea Lily)",
         period="Ordovician–Present", age_start=480, age_end=0, era="Paleozoic",
         environments=["Marine shallow","Reef","Marine deep"], group="Echinoderm", preservation="Good",
         description="Crinoidal stem discs — small circular plates with a central hole — are among the most common Paleozoic fossils. Intact calyces are rare and valuable. Crinoidal limestones are economically important as reservoir rocks in some oil fields. Look for button-like discs on bedding planes.",
         fact="Native American tribes used crinoid stem discs as beads — they are perfectly circular with a natural central hole, requiring no drilling.",
         significance="Crinoidal limestones are an important petroleum reservoir rock (e.g. Mississippian plays, USA). Abundance indicates clear, well-oxygenated shallow seas.",
         locations=["USA (Indiana, Illinois)","UK (Carboniferous)","Germany","Belgium","Russia","China"],
         coords=[(39.7,-86.1),(53.5,-1.5),(51.1,10.4),(50.5,4.4),(55.0,40.0)],
         image_url="images/crinoid.jpg"),
    dict(name="Rugosa", common="Rugose Coral",
         period="Ordovician–Permian", age_start=480, age_end=252, era="Paleozoic",
         environments=["Reef","Marine shallow","Lagoon"], group="Cnidarian", preservation="Good",
         description="Solitary horn-shaped and colonial reef-building corals of the Paleozoic. Their internal septa show a characteristic 4-fold symmetry — distinct from modern 6-fold corals. Rugose corals were wiped out in the end-Permian extinction, the largest mass extinction in Earth history.",
         fact="Growth rings inside rugose corals show that Devonian years had approximately 400 days, confirming that Earth's rotation has slowed over geological time due to tidal friction.",
         significance="Reef facies indicator. Four-fold septal symmetry distinguishes from modern corals. Extinction at the Permian–Triassic boundary is a key global stratigraphic marker.",
         locations=["UK (Carboniferous)","Belgium","USA (Great Lakes)","Germany","Algeria","China"],
         coords=[(53.5,-1.5),(50.5,4.4),(43.0,-83.0),(51.1,10.4),(28.0,2.0)],
         image_url="images/rugose_coral.jpg"),
    dict(name="Selachii", common="Shark Tooth",
         period="Devonian–Present", age_start=400, age_end=0, era="Cenozoic",
         environments=["Marine shallow","Marine open water","Marine deep","Coastal"], group="Fish", preservation="Excellent",
         description="Sharks continuously shed and replace teeth throughout their lives — one shark produces up to 50,000 teeth. Teeth are coated in fluorapatite, making them extremely resistant to dissolution. In the field, shark teeth are identified by their triangular shape, serrated edges, and glossy enameloid surface.",
         fact="Black phosphatized teeth are millions of years old. White or grey teeth on a beach are geologically recent. Color alone can provide a rough age estimate in the field.",
         significance="Common marine fossil useful for Cenozoic age estimation. Black coloration indicates Miocene or older; tan suggests Pliocene; white or grey indicates Pleistocene to Recent.",
         locations=["Morocco (phosphate beds)","USA (South Carolina, Maryland)","Malta","Belgium (Antwerp)","Egypt","Libya"],
         coords=[(32.0,-6.0),(33.8,-79.0),(35.9,14.5),(51.2,4.4),(27.0,30.0)],
         image_url="images/shark_tooth.jpg"),
    dict(name="Pollen and Spores", common="Palynomorphs",
         period="Silurian–Present", age_start=430, age_end=0, era="Cenozoic",
         environments=["Terrestrial","Swamp","Deltaic","Lacustrine","Marine shallow","Fluvial"], group="Plant", preservation="Excellent",
         description="Microscopic plant reproductive structures with an almost indestructible outer wall (sporopollenin). Palynomorph-bearing rocks are typically dark grey or black organic-rich shales and coals. Samples require laboratory processing but yield powerful biostratigraphic results across all environments.",
         fact="Fossil pollen preserved in amber retains its original chemistry — scientists have recovered molecular signatures of ancient flower scents from specimens 40 million years old.",
         significance="Universal biozone tool across all environments — marine and non-marine. Essential for correlating coal measures, deltaic and lacustrine sequences where marine fossils are absent.",
         locations=["Global","Coal basins worldwide","North Sea (subsurface)","Algeria (Sahara, subsurface)","Nigeria (Niger Delta)"],
         coords=[(56.0,3.0),(28.0,2.0),(5.0,6.0),(52.0,5.0)],
         image_url="images/palynomorphs.jpg"),
    dict(name="Dinosauria", common="Dinosaur",
         period="Triassic–Cretaceous", age_start=243, age_end=66, era="Mesozoic",
         environments=["Terrestrial","Fluvial","Deltaic","Coastal"], group="Reptile", preservation="Rare",
         description="Dinosaur bones require rapid burial in sediment-rich environments. Most are known from fluvial and deltaic deposits. In the field, bones often weather out of soft mudstones and appear as dark brown fragments with a honeycomb-like internal texture. Isolated teeth and vertebrae are far more common than complete skeletons.",
         fact="Birds are technically dinosaurs — specifically avian theropods that survived the end-Cretaceous mass extinction event 66 million years ago.",
         significance="Biostratigraphic marker for Mesozoic continental deposits. In situ specimens preserve original orientation and articulation, confirming autochthonous burial.",
         locations=["Argentina (Patagonia)","USA (Montana, Utah)","China (Liaoning)","Mongolia (Gobi)","Tanzania (Tendaguru)","Morocco (Kem Kem)"],
         coords=[(-45.0,-67.0),(47.0,-109.0),(41.0,122.0),(44.0,103.0),(-9.0,35.0),(31.0,-5.0)],
         image_url="images/dinosaur.jpg"),
    dict(name="Nummulites", common="Nummulite",
         period="Paleocene–Oligocene", age_start=56, age_end=34, era="Cenozoic",
         environments=["Marine shallow","Reef","Lagoon"], group="Protist", preservation="Excellent",
         description="Large coin-shaped benthic foraminifera clearly visible to the naked eye. They built entire limestone formations across the ancient Tethys seaway. Nummulitic limestones are important reservoir and aquifer rocks across North Africa and the Middle East.",
         fact="Napoleon's soldiers in Egypt thought nummulite fossils in pyramid limestone were petrified lentils eaten by the ancient pyramid builders.",
         significance="Key marker for Eocene in Tethyan realm. Nummulitic limestones are petroleum reservoir rock in North Africa and the Middle East. Field-identifiable without a microscope.",
         locations=["Algeria (Atlas)","Egypt (Giza)","Libya","Tunisia","France (Paris Basin)","Spain","India (Gujarat)","Pakistan"],
         coords=[(36.0,3.0),(29.9,31.1),(27.0,17.0),(34.0,9.0),(48.8,2.3),(40.4,-3.7)],
         image_url="images/nummulite.jpg"),
    dict(name="Ichthyosauria", common="Ichthyosaur",
         period="Triassic–Cretaceous", age_start=250, age_end=90, era="Mesozoic",
         environments=["Marine open water","Marine shallow"], group="Reptile", preservation="Rare",
         description="Dolphin-shaped marine reptiles that convergently evolved an identical body plan to modern dolphins 250 million years before dolphins existed. In the field, isolated vertebrae (circular discs) and paddle bones are the most common finds. Some specimens preserve soft tissue as carbon films.",
         fact="Several ichthyosaur specimens have been found with babies preserved mid-birth — confirming live birth tail-first, identical to the strategy used by modern dolphins.",
         significance="Marker for Triassic–Jurassic marine deposits. Isolated vertebral discs are often misidentified as fish vertebrae — compare size and internal trabecular structure.",
         locations=["UK (Lyme Regis, Jurassic Coast)","Germany (Holzmaden)","Canada (British Columbia)","Chile","Nevada (USA)"],
         coords=[(50.7,-2.9),(48.4,9.4),(54.0,-120.0),(-38.0,-71.0),(39.5,-116.0)],
         image_url="images/ichthyosaur.jpg"),
    dict(name="Mammalia", common="Fossil Mammal",
         period="Triassic–Present", age_start=225, age_end=0, era="Cenozoic",
         environments=["Terrestrial","Fluvial","Cave","Deltaic","Lacustrine"], group="Mammal", preservation="Variable",
         description="Mammal teeth are the most common mammal fossil — their enamel is the hardest biological material and resists decay the longest. A single tooth can reveal species, approximate age, diet, and paleoclimate. In the field, look for isolated teeth and bone fragments weathering out of Cenozoic red beds and cave breccias.",
         fact="A skilled paleontologist can identify a mammal species, age-at-death, and even season of death from a single isolated molar tooth.",
         significance="Primary biostratigraphy tool for Cenozoic continental deposits. Teeth enamel geochemistry provides paleoclimate data and is essential for correlating non-marine sequences.",
         locations=["USA (Badlands, South Dakota)","China (Yunnan)","Kenya (Turkana)","France (Quercy)","Algeria (Sahara, Gour Lazib)","Pakistan (Siwaliks)"],
         coords=[(43.8,-102.3),(25.0,102.0),(4.0,36.0),(44.4,1.5),(29.0,2.0),(33.0,72.0)],
         image_url="images/mammal.jpg"),
]

ENVIRONMENTS = sorted(set(e for f in FOSSILS for e in f["environments"]))
ERAS   = ["All","Paleozoic","Mesozoic","Cenozoic"]
GROUPS = ["All"] + sorted(set(f["group"] for f in FOSSILS))

def section_header(title, sub=""):
    st.markdown(f'<div class="sec-title">{title}</div>', unsafe_allow_html=True)
    if sub: st.markdown(f'<div class="sec-sub">{sub}</div>', unsafe_allow_html=True)

def fossil_card(f, show_image=True):
    tags_env = "".join(f'<span class="tag tag-env">{e}</span>' for e in f["environments"])
    tags_loc = "".join(f'<span class="tag tag-loc">{l}</span>' for l in f["locations"][:4])
    pres_color = {"Excellent":"#2a7a3a","Good":"#8a6830","Variable":"#8a5820","Rare":"#8a2020"}.get(f["preservation"],"#8a6830")
    st.markdown('<div class="fcard">', unsafe_allow_html=True)
    if show_image:
        try:
            st.image(f["image_url"], use_container_width=True)
        except Exception:
            st.markdown('<div style="background:#f5f3ef;padding:28px;text-align:center;font-size:12px;color:#9a8a6a;border-bottom:1px solid #e8e4dc">Image not available</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="fcard-body">
      <div class="fcard-era">{f['period']} &nbsp;·&nbsp; {f['age_start']}–{f['age_end']} Ma &nbsp;·&nbsp; {f['era']}</div>
      <div class="fcard-name">{f['name']}</div>
      <div class="fcard-common">{f['common']}</div>
      <div class="fcard-desc">{f['description']}</div>
      <div class="fact-box"><div class="fact-label">Field Fact</div><div class="fact-text">{f['fact']}</div></div>
      <div class="sig-box"><div class="sig-label">Biostratigraphic Significance</div>{f['significance']}</div>
      <div style="margin-bottom:8px">{tags_env}</div>
      <div style="margin-bottom:10px">{tags_loc}</div>
      <span class="tag" style="color:{pres_color};border-color:{pres_color}33;background:#fafaf8">Preservation: {f['preservation']}</span>
    </div></div>""", unsafe_allow_html=True)

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""<div style="padding:20px 0 12px">
      <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1a1a1a">FossilFinder</div>
      <div style="font-size:9px;color:#9a8a6a;letter-spacing:0.22em;text-transform:uppercase;margin-top:4px">Field Edition</div>
    </div><hr>""", unsafe_allow_html=True)
    st.markdown("**Find by Age & Environment**")
    age_min, age_max = st.slider("Geologic age (Ma)", 0, 541, (0,541), step=5, help="Ma = millions of years ago")
    sel_envs  = st.multiselect("Depositional environment", ENVIRONMENTS, placeholder="Any environment")
    st.markdown("<br>**More Filters**", unsafe_allow_html=True)
    sel_era   = st.selectbox("Geologic era", ERAS)
    sel_group = st.selectbox("Fossil group", GROUPS)
    sel_pres  = st.selectbox("Preservation", ["Any","Excellent","Good","Variable","Rare"])
    search    = st.text_input("Search", placeholder="e.g. Ammonite")
    st.markdown("<hr>", unsafe_allow_html=True)
    show_images = st.toggle("Show images", value=True)
    rnd_btn = st.button("Random Fossil", use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""<div style="font-size:11px;color:#9a8a6a;line-height:1.8">
      <div style="font-family:'Playfair Display',serif;font-size:14px;font-weight:700;color:#5a3a10">Serhoudji</div>
      FossilFinder v2.0<br>Petroleum Geology · Algeria</div>""", unsafe_allow_html=True)

def apply_filters(fossils):
    out = fossils
    if search:
        q = search.lower()
        out = [f for f in out if q in f["name"].lower() or q in f["common"].lower()]
    if sel_era != "All":
        out = [f for f in out if f["era"] == sel_era]
    if sel_envs:
        out = [f for f in out if any(e in f["environments"] for e in sel_envs)]
    if sel_group != "All":
        out = [f for f in out if f["group"] == sel_group]
    if sel_pres != "Any":
        out = [f for f in out if f["preservation"] == sel_pres]
    out = [f for f in out if f["age_start"] >= age_min and f["age_end"] <= age_max]
    return out

filtered = apply_filters(FOSSILS)

# ── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="site-header">
  <div class="site-header-inner">
    <div>
      <div class="site-title">Fossil<span>Finder</span></div>
      <div class="site-sub">Field Paleontology &nbsp;·&nbsp; Biostratigraphy &nbsp;·&nbsp; Earth History</div>
    </div>
    <div class="site-author">Developed by<strong>Serhoudji</strong>Petroleum Geology · Algeria</div>
  </div>
</div>""", unsafe_allow_html=True)

# ── KPI ────────────────────────────────────────────────────────────────────────
k1,k2,k3,k4,k5 = st.columns(5)
with k1: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(FOSSILS)}</div><div class="kpi-l">Fossil Groups</div></div>', unsafe_allow_html=True)
with k2: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(filtered)}</div><div class="kpi-l">Matching</div></div>', unsafe_allow_html=True)
with k3: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(set(f["era"] for f in filtered)) if filtered else 0}</div><div class="kpi-l">Eras</div></div>', unsafe_allow_html=True)
with k4: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(ENVIRONMENTS)}</div><div class="kpi-l">Environments</div></div>', unsafe_allow_html=True)
with k5: st.markdown(f'<div class="kpi"><div class="kpi-n">541</div><div class="kpi-l">Ma Coverage</div></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if rnd_btn:
    pick = random.choice(FOSSILS)
    section_header(f"Random — {pick['common']}")
    c1, _ = st.columns(2)
    with c1: fossil_card(pick, show_image=show_images)
    st.markdown("<hr>", unsafe_allow_html=True)

tab1,tab2,tab3,tab4 = st.tabs(["FOSSIL GALLERY","DISTRIBUTION MAP","TIMELINE","ENVIRONMENTS"])

# ── TAB 1 ──────────────────────────────────────────────────────────────────────
with tab1:
    if not filtered:
        st.warning("No fossils match your current filters. Try widening the age range or removing environment filters.")
    else:
        st.markdown(f'<div class="result-banner">Showing <strong>{len(filtered)}</strong> fossil group{"s" if len(filtered)!=1 else ""} matching your filters</div>', unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        for i,f in enumerate(filtered):
            with col1 if i%2==0 else col2: fossil_card(f, show_image=show_images)

# ── TAB 2 ──────────────────────────────────────────────────────────────────────
with tab2:
    section_header("Global Distribution Map","Classic reference localities for each fossil group — marker color indicates geologic era")
    map_fossils = filtered if filtered else FOSSILS
    fig_map = go.Figure()
    for f in map_fossils:
        if not f.get("coords"): continue
        lats=[c[0] for c in f["coords"]]; lons=[c[1] for c in f["coords"]]
        fig_map.add_trace(go.Scattergeo(lat=lats, lon=lons, mode="markers", name=f["common"],
            marker=dict(size=10, color=ERA_COLORS.get(f["era"],"#8a6830"), opacity=0.85, line=dict(width=1.5,color="#ffffff")),
            hovertemplate=f"<b>{f['common']}</b><br>{f['name']}<br>Age: {f['age_start']}–{f['age_end']} Ma<br>Era: {f['era']}<extra></extra>"))
    fig_map.update_layout(**PLOT_LAYOUT, height=500,
        geo=dict(bgcolor="#ffffff",landcolor="#f0ece4",oceancolor="#e8f0f5",lakecolor="#e8f0f5",
                 showland=True,showocean=True,showcountries=True,countrycolor="#d0c8b8",
                 showcoastlines=True,coastlinecolor="#b8a888",showframe=False,projection_type="natural earth"),
        title=dict(text="Global Fossil Occurrence Localities",font=dict(size=14,color="#1a1a1a",family="Playfair Display, serif")),
        legend=dict(bgcolor="#ffffff",bordercolor="#e8e4dc",borderwidth=1,font=dict(size=10),itemsizing="constant"))
    st.plotly_chart(fig_map, use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    section_header("Classic Field Localities")
    for f in map_fossils[:8]:
        with st.expander(f"{f['common']}  ({f['name']})  ·  {f['era']}"):
            for loc in f["locations"]: st.markdown(f"- {loc}")
            st.caption(f"Preservation: {f['preservation']}  ·  Age: {f['age_start']}–{f['age_end']} Ma")

# ── TAB 3 ──────────────────────────────────────────────────────────────────────
with tab3:
    section_header("Stratigraphic Ranges","Horizontal bars show the total time span of each fossil group — dashed lines indicate mass extinctions")
    sf = sorted(filtered if filtered else FOSSILS, key=lambda x: -x["age_start"])
    fig_tl = go.Figure()
    for f in sf:
        d = f["age_start"]-f["age_end"]
        fig_tl.add_trace(go.Bar(x=[d],y=[f["common"]],base=f["age_end"],orientation="h",name=f["era"],
            marker=dict(color=ERA_COLORS.get(f["era"],"#8a6830"),opacity=0.65,line=dict(width=1,color=ERA_COLORS.get(f["era"],"#8a6830"))),
            hovertemplate=f"<b>{f['common']}</b><br>{f['age_start']}–{f['age_end']} Ma ({d} My)<br>Era: {f['era']}<extra></extra>",showlegend=False))
    for era_n,(s,e) in [("Cenozoic",(0,66)),("Mesozoic",(66,252)),("Paleozoic",(252,541))]:
        fig_tl.add_vrect(x0=e,x1=s,fillcolor=ERA_COLORS[era_n],opacity=0.04,layer="below",line_width=0,
                         annotation_text=era_n,annotation_position="top",annotation_font=dict(size=10,color=ERA_COLORS[era_n]))
    for age,label,clr in [(252,"End-Permian (96% sp.)","#c04040"),(66,"K-Pg extinction","#c07040"),(201,"End-Triassic","#c06040")]:
        if age_min<=age<=age_max:
            fig_tl.add_vline(x=age,line_color=clr,line_dash="dot",line_width=1.2,
                             annotation_text=label,annotation_font=dict(size=9,color=clr),annotation_position="top right")
    fig_tl.update_layout(**PLOT_LAYOUT,height=max(380,len(sf)*32+80),barmode="overlay",
        xaxis=dict(title="Age (Ma)",autorange="reversed",gridcolor="#e8e4dc",linecolor="#e8e4dc"),
        yaxis=dict(gridcolor="#e8e4dc",linecolor="#e8e4dc"),
        title=dict(text="Fossil Stratigraphic Ranges — Coloured by Era",font=dict(size=14,color="#1a1a1a",family="Playfair Display, serif")))
    st.plotly_chart(fig_tl, use_container_width=True)

# ── TAB 4 ──────────────────────────────────────────────────────────────────────
with tab4:
    section_header("Environment Finder","Select a depositional environment to see which fossil groups are typically present")
    sel_env = st.selectbox("Depositional environment", ENVIRONMENTS, key="env_detail")
    env_results = [f for f in FOSSILS if sel_env in f["environments"]]
    if env_results:
        st.markdown(f'<div class="result-banner"><strong>{len(env_results)}</strong> fossil group{"s" if len(env_results)!=1 else ""} expected in <em>{sel_env}</em> settings</div>', unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        for i,f in enumerate(env_results):
            with col1 if i%2==0 else col2: fossil_card(f,show_image=show_images)
    else:
        st.info("No fossils in the database for this environment.")
    st.markdown("<hr>", unsafe_allow_html=True)
    section_header("Environment × Group Matrix","Heatmap showing which fossil groups occur in which depositional environments")
    groups_all = sorted(set(f["group"] for f in FOSSILS))
    matrix = [[sum(1 for f in FOSSILS if env in f["environments"] and f["group"]==g) for g in groups_all] for env in ENVIRONMENTS]
    fig_hm = go.Figure(go.Heatmap(z=matrix,x=groups_all,y=ENVIRONMENTS,
        colorscale=[[0,"#f8f7f4"],[0.4,"#d4b870"],[1,"#8a6020"]],
        hovertemplate="Env: %{y}<br>Group: %{x}<br>Count: %{z}<extra></extra>",
        colorbar=dict(title="Count",thickness=12,len=0.7,tickfont=dict(size=9),title_font=dict(size=10))))
    fig_hm.update_layout(**PLOT_LAYOUT,height=450,
        xaxis=dict(title="Fossil Group",tickangle=-35,gridcolor="#e8e4dc"),
        yaxis=dict(title="Environment",gridcolor="#e8e4dc"),
        title=dict(text="Fossil Occurrence Matrix",font=dict(size=14,color="#1a1a1a",family="Playfair Display, serif")))
    st.plotly_chart(fig_hm, use_container_width=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div><div class="footer-name">Serhoudji</div>Petroleum Geology · Algeria</div>
  <div style="text-align:center">FossilFinder · Field Edition v2.0<br>15 fossil groups · 3 eras · 541 Ma of Earth history</div>
  <div style="text-align:right">Built with Streamlit and Plotly<br>Paleontology · Biostratigraphy</div>
</div>""", unsafe_allow_html=True)
