import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title="FossilFinder · Serhoudji", layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=IM+Fell+English:ital@0;1&family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Crimson Text', Georgia, serif;
    background-color: #12100b;
    color: #d4c49a;
}
.stApp {
    background-color: #12100b;
    background-image:
        radial-gradient(ellipse at 0% 0%, #1e1a0e 0%, transparent 55%),
        radial-gradient(ellipse at 100% 100%, #1a1208 0%, transparent 55%);
}
section[data-testid="stSidebar"] { background:#0e0c08; border-right:1px solid #3a2e14; }
section[data-testid="stSidebar"] * { color:#c8b87a !important; }

.hero {
    background: linear-gradient(160deg, #1c1608 0%, #241e0c 40%, #1a1408 100%);
    border:1px solid #4a3a18; border-top:3px solid #c8973a;
    border-radius:4px; padding:40px 48px 56px; margin-bottom:36px; position:relative; overflow:hidden;
}
.hero::before {
    content:'';position:absolute;inset:0;
    background: repeating-linear-gradient(0deg,transparent,transparent 39px,rgba(184,150,12,0.03) 39px,rgba(184,150,12,0.03) 40px),
                repeating-linear-gradient(90deg,transparent,transparent 39px,rgba(184,150,12,0.03) 39px,rgba(184,150,12,0.03) 40px);
}
.hero-eyebrow { font-family:'Cinzel',serif; font-size:10px; letter-spacing:0.45em; color:#6a5a2a; text-transform:uppercase; margin-bottom:14px; }
.hero-rule { width:60px;height:1px; background:linear-gradient(90deg,#c8973a,transparent); margin-bottom:14px; }
.hero-title { font-family:'Cinzel',serif; font-size:52px; font-weight:700; color:#f0dfa0; line-height:1; letter-spacing:0.06em; margin:0 0 8px; text-shadow:0 2px 20px rgba(200,151,58,0.2); }
.hero-title em { color:#c8973a; font-style:normal; }
.hero-tagline { font-family:'IM Fell English',serif; font-style:italic; font-size:17px; color:#7a6a3a; margin-top:10px; }
.hero-author { position:absolute; bottom:28px; right:48px; text-align:right; font-family:'Cinzel',serif; font-size:9px; letter-spacing:0.2em; color:#5a4a1a; text-transform:uppercase; }
.hero-author strong { display:block; font-size:14px; color:#c8973a; letter-spacing:0.12em; margin-top:3px; }

.kpi { flex:1; min-width:110px; background:linear-gradient(135deg,#1a1608,#221c0a); border:1px solid #3a2e14; border-top:2px solid #c8973a; border-radius:3px; padding:16px 18px; }
.kpi-n { font-family:'Cinzel',serif; font-size:32px; font-weight:700; color:#c8973a; line-height:1; }
.kpi-l { font-family:'Cinzel',serif; font-size:8px; color:#6a5a2a; letter-spacing:0.22em; text-transform:uppercase; margin-top:5px; }

.sec-wrap { margin:4px 0 22px; }
.sec-pre { font-family:'Cinzel',serif; font-size:9px; color:#5a4a1a; letter-spacing:0.35em; text-transform:uppercase; margin-bottom:6px; }
.sec-title { font-family:'Cinzel',serif; font-size:20px; font-weight:600; color:#e8d080; border-bottom:1px solid #3a2e14; padding-bottom:10px; }
.sec-sub { font-family:'Crimson Text',serif; font-style:italic; font-size:14px; color:#6a5a2a; margin:6px 0 0 2px; }

.fcard { background:linear-gradient(160deg,#1a1608 0%,#1e1a0a 100%); border:1px solid #3a2e14; border-radius:4px; overflow:hidden; margin-bottom:26px; position:relative; transition:border-color 0.25s,box-shadow 0.25s; }
.fcard::before { content:''; position:absolute; top:0;left:0;right:0;height:2px; background:linear-gradient(90deg,#c8973a,#8a6020,transparent); }
.fcard:hover { border-color:#c8973a; box-shadow:0 6px 32px rgba(200,151,58,0.12); }
.fcard-body { padding:22px 24px 24px; }
.fcard-era { font-family:'Cinzel',serif; font-size:9px; letter-spacing:0.25em; color:#5a4a1a; text-transform:uppercase; margin-bottom:6px; }
.fcard-name { font-family:'Playfair Display',serif; font-size:22px; font-weight:700; font-style:italic; color:#f0dfa0; margin-bottom:2px; }
.fcard-common { font-family:'Cinzel',serif; font-size:11px; color:#c8973a; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:14px; }
.fcard-divider { width:40px;height:1px; background:linear-gradient(90deg,#c8973a,transparent); margin-bottom:14px; }
.fcard-desc { font-family:'Crimson Text',serif; font-size:15px; color:#a09060; line-height:1.75; margin-bottom:18px; }

.fact-box { background:#0e0c08; border:1px solid #3a2e14; border-left:3px solid #c8973a; padding:16px 18px; margin-bottom:16px; border-radius:0 3px 3px 0; position:relative; }
.fact-ornament { position:absolute; top:-8px;left:14px; background:#0e0c08; padding:0 6px; font-family:'Cinzel',serif; font-size:8px; color:#c8973a; letter-spacing:0.2em; text-transform:uppercase; }
.fact-text { font-family:'IM Fell English',serif; font-style:italic; font-size:14px; color:#c8a860; line-height:1.7; }

.sig-box { background:#0e0c08; border:1px solid #2e2410; border-radius:3px; padding:12px 16px; margin-bottom:16px; font-family:'Crimson Text',serif; font-size:14px; color:#907848; line-height:1.6; }
.sig-label { font-family:'Cinzel',serif; font-size:8px; color:#4a3a10; letter-spacing:0.22em; text-transform:uppercase; margin-bottom:5px; }

.tag { display:inline-block; background:#0e0c08; border:1px solid #3a2e14; border-radius:2px; padding:3px 10px; font-family:'Cinzel',serif; font-size:8px; color:#6a5a2a; margin:2px 2px 2px 0; letter-spacing:0.1em; text-transform:uppercase; }
.tag-env { border-color:#2a4020; color:#4a7030; }
.tag-loc { border-color:#3a2e14; color:#806020; }

.stTabs [data-baseweb="tab-list"] { background:transparent; border-bottom:1px solid #3a2e14; gap:0; }
.stTabs [data-baseweb="tab"] { font-family:'Cinzel',serif; font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#4a3a10; background:transparent; border:none; padding:12px 24px; }
.stTabs [aria-selected="true"] { color:#c8973a !important; border-bottom:2px solid #c8973a !important; background:transparent !important; margin-bottom:-1px; }

.stSelectbox>div>div, .stMultiSelect>div>div, .stTextInput>div>div>input {
    background:#0e0c08 !important; border:1px solid #3a2e14 !important; color:#c8b87a !important;
    font-family:'Cinzel',serif !important; font-size:11px !important; border-radius:3px !important; }
.stButton>button { background:#0e0c08 !important; border:1px solid #c8973a !important; color:#c8973a !important;
    font-family:'Cinzel',serif !important; font-size:10px !important; font-weight:600 !important;
    letter-spacing:0.2em; text-transform:uppercase; border-radius:3px !important; padding:10px 20px !important; }
.stButton>button:hover { background:#c8973a18 !important; }

.result-banner { background:#0e0c08; border:1px solid #3a2e14; border-left:3px solid #c8973a; border-radius:0 3px 3px 0;
    padding:12px 18px; margin-bottom:26px; font-family:'Crimson Text',serif; font-style:italic; font-size:15px; color:#907848; }

.footer { border-top:1px solid #3a2e14; padding:28px 0 16px; margin-top:48px; display:flex; justify-content:space-between; align-items:center; }
.footer-name { font-family:'Cinzel',serif; font-size:18px; font-weight:700; color:#c8973a; letter-spacing:0.1em; }
.footer-sub { font-family:'Crimson Text',serif; font-style:italic; font-size:13px; color:#4a3a10; margin-top:2px; }
.footer-center { text-align:center; font-family:'Cinzel',serif; font-size:9px; color:#4a3a10; letter-spacing:0.2em; text-transform:uppercase; line-height:2.2; }
.footer-right { text-align:right; font-family:'Crimson Text',serif; font-style:italic; font-size:13px; color:#4a3a10; line-height:1.8; }
hr { border-color:#3a2e14 !important; }
</style>
""", unsafe_allow_html=True)

PLOT_LAYOUT = dict(
    paper_bgcolor="#1a1608", plot_bgcolor="#12100b",
    font=dict(family="Crimson Text, serif", color="#c8b87a", size=12),
    margin=dict(l=50, r=20, t=50, b=50))
ERA_COLORS = {"Paleozoic":"#6a9a5a","Mesozoic":"#4a8aaa","Cenozoic":"#c8973a"}

FOSSILS = [
    dict(name="Trilobita",common="Trilobite",period="Cambrian–Permian",age_start=521,age_end=252,era="Paleozoic",
         environments=["Marine shallow","Marine deep","Reef"],group="Arthropod",preservation="Excellent",
         description="Among Earth's most successful early animals, trilobites dominated Paleozoic seas for nearly 270 million years. Their calcite exoskeletons preserve exceptionally well — rolled specimens indicate a stress response still visible 500 million years later.",
         fact="Over 20,000 species have been described — more diverse than all modern mammals combined. Some possessed eyes of calcite crystals that required no focusing whatsoever.",
         significance="Primary zone fossil for Cambrian–Ordovician. Rolled specimens indicate storm events or predator pressure.",
         locations=["Morocco (Anti-Atlas)","USA (Utah, Ohio)","Russia","China","Canada (Burgess Shale)","Algeria (Saharan platform)"],
         coords=[(31.5,-7.0),(39.3,-111.0),(55.7,37.6),(30.0,110.0),(51.4,-116.5)],
         image_url="images/trilobite.jpg"),
    dict(name="Ammonoidea",common="Ammonite",period="Devonian–Cretaceous",age_start=419,age_end=66,era="Mesozoic",
         environments=["Marine shallow","Marine open water","Marine deep"],group="Cephalopod",preservation="Excellent",
         description="The supreme biostratigraphic instrument of the Mesozoic. Ammonites evolved with such rapidity that each species persisted for less than one million years. Their coiled chambered architecture permitted neutral buoyancy. Suture patterns on weathered specimens betray genus and species to the trained eye.",
         fact="The greatest ammonite yet recovered — Parapuzosia seppenradensis of Germany — measured 1.8 metres in diameter. Most specimens recovered in the field fit comfortably within one hand.",
         significance="Primary biozone fossil for the Jurassic and Cretaceous. Suture complexity increases through time — of direct utility for relative age determination in the field.",
         locations=["UK (Whitby, Dorset)","Morocco (Erfoud)","Madagascar","France (Normandy)","Germany","Tunisia","Algeria (Tlemcen)"],
         coords=[(54.4,-0.6),(31.4,-4.0),(-20.0,47.0),(49.1,-0.4),(51.3,10.4)],
         image_url="images/ammonite.jpg"),
    dict(name="Graptolithina",common="Graptolite",period="Cambrian–Carboniferous",age_start=510,age_end=320,era="Paleozoic",
         environments=["Marine deep","Marine open water"],group="Hemichordate",preservation="Good",
         description="Flattened carbon films upon black shales — readily overlooked by the untrained observer. These colonial organisms once drifted through ancient oceans. Their prodigious rate of evolution renders them the primary zone fossil for Ordovician and Silurian successions worldwide.",
         fact="Graptolites were long classified among the plants — their very name signifies 'written rock' in the Greek tongue. Their animal nature was not established until the twentieth century.",
         significance="Primary zone fossil for Ordovician–Silurian globally. Black shale hosting denotes an anoxic deep water paleoenvironment.",
         locations=["Wales (type locality)","Scotland","Canada (Quebec)","China","Australia","Czech Republic"],
         coords=[(52.3,-3.7),(56.0,-4.2),(47.0,-71.0),(30.0,110.0),(-25.0,133.0)],
         image_url="images/graptolite.jpg"),
    dict(name="Brachiopoda",common="Brachiopod",period="Cambrian–Present",age_start=530,age_end=0,era="Paleozoic",
         environments=["Marine shallow","Reef","Marine deep"],group="Brachiopod",preservation="Excellent",
         description="Superficially resembling the bivalve yet biologically unrelated. The essential field distinction: brachiopods possess a single plane of symmetry from apex to margin; bivalves through left and right. They reigned as the dominant shelled organisms of Paleozoic seas and persist into the present age.",
         fact="Living brachiopods of the genus Lingula are virtually indistinguishable from specimens 500 million years of age — the most slowly evolving creatures known to science.",
         significance="Of utility for Devonian biostratigraphy. Abundance signifies normal marine salinity. Must be distinguished from bivalves for accurate paleoenvironment interpretation.",
         locations=["Germany (Rhine)","USA (Devonian of New York)","UK (Silurian)","China","Australia","Algeria"],
         coords=[(50.9,6.9),(42.9,-76.0),(52.3,-1.5),(30.0,110.0),(-25.0,133.0)],
         image_url="images/brachiopod.jpg"),
    dict(name="Foraminifera",common="Foraminifera",period="Cambrian–Present",age_start=530,age_end=0,era="Cenozoic",
         environments=["Marine shallow","Marine deep","Marine open water","Lagoon"],group="Protist",preservation="Excellent",
         description="Single-celled organisms of microscopic dimension, visible only beneath hand lens or microscope. Despite their diminutive scale, they constitute the primary biostratigraphic instrument for Cenozoic marine successions throughout the globe. Foram-bearing limestones often present a sugary or granular texture.",
         fact="The Great Pyramid of Giza is constructed almost entirely from nummulitic limestone — billions upon billions of foram shells quarried from the Egyptian desert by ancient hands.",
         significance="Primary Cenozoic biozone instrument. The planktonic to benthic ratio indicates paleodepth. Oxygen isotopes from their tests reconstruct the temperatures of vanished oceans.",
         locations=["Global oceans","Egypt (Eocene)","North Sea","Caribbean","Algeria (Saharan platform)","Tunisia"],
         coords=[(29.9,31.1),(56.0,3.0),(15.0,-75.0),(36.8,10.2),(28.0,2.0)],
         image_url="images/foraminifera.jpg"),
    dict(name="Echinoidea",common="Sea Urchin (Fossil)",period="Ordovician–Present",age_start=480,age_end=0,era="Mesozoic",
         environments=["Marine shallow","Reef","Lagoon"],group="Echinoderm",preservation="Good",
         description="Regular and irregular echinoids are found in abundance within Cretaceous chalks and Jurassic limestones. Irregular forms such as Micraster serve as classical zone fossils for the Cretaceous chalk of northwestern Europe. Five-fold symmetry and ambulacral grooves are the diagnostic characters in the field.",
         fact="Medieval Europeans named echinoid tests 'shepherd's crowns' or 'fairy loaves' and preserved them as charms against misfortune. Neolithic peoples interred them with their honoured dead.",
         significance="Micraster constitutes a zone fossil for the Cretaceous chalk. Irregular echinoids denote infaunal existence and a soft, muddy seafloor.",
         locations=["UK (chalk downs)","France (Normandy chalk)","North Africa","Egypt","Israel","Denmark"],
         coords=[(51.2,0.5),(49.1,0.3),(27.0,20.0),(29.5,31.2),(31.0,35.0)],
         image_url="images/echinoid.jpg"),
    dict(name="Belemnoidea",common="Belemnite",period="Carboniferous–Eocene",age_start=360,age_end=34,era="Mesozoic",
         environments=["Marine shallow","Marine open water"],group="Cephalopod",preservation="Good",
         description="The bullet-shaped calcite guard is the portion that survives — the soft, squid-like body rarely submits to fossilisation. Belemnite guards are encountered in abundance throughout Jurassic and Cretaceous marine successions. Dense accumulations known as 'belemnite battlefields' may record episodes of mass mortality.",
         fact="In the medieval Scandinavian tradition, belemnites were denominated 'thunderbolts' — believed to descend from the heavens during tempests, carrying protective power.",
         significance="A serviceable index fossil for Jurassic–Cretaceous marine sequences. Guards indicate normal marine, moderate-energy conditions.",
         locations=["UK (Jurassic Coast)","Germany (Solnhofen)","Russia","Poland","Algeria (Tlemcen region)","Tunisia"],
         coords=[(50.6,-2.4),(48.8,11.0),(55.0,40.0),(52.0,20.0),(34.8,-1.3)],
         image_url="images/belemnite.jpg"),
    dict(name="Crinoidea",common="Crinoid (Sea Lily)",period="Ordovician–Present",age_start=480,age_end=0,era="Paleozoic",
         environments=["Marine shallow","Reef","Marine deep"],group="Echinoderm",preservation="Good",
         description="Crinoidal stem discs — small circular ossicles pierced at their centre — rank among the most abundant of all Paleozoic fossils. Intact calyces are rare and prized. Crinoidal limestones hold economic importance as petroleum reservoir rocks. Seek the characteristic button-like discs upon bedding planes.",
         fact="The indigenous peoples of North America employed crinoid stem discs as beads — perfectly circular, naturally perforated, requiring no labour of the drill.",
         significance="Crinoidal limestones constitute an important petroleum reservoir rock, as in the Mississippian plays of the United States. Abundance signals clear, well-oxygenated shallow seas.",
         locations=["USA (Indiana, Illinois)","UK (Carboniferous)","Germany","Belgium","Russia","China"],
         coords=[(39.7,-86.1),(53.5,-1.5),(51.1,10.4),(50.5,4.4),(55.0,40.0)],
         image_url="images/crinoid.jpg"),
    dict(name="Rugosa",common="Rugose Coral",period="Ordovician–Permian",age_start=480,age_end=252,era="Paleozoic",
         environments=["Reef","Marine shallow","Lagoon"],group="Cnidarian",preservation="Good",
         description="Solitary horn-shaped and colonial reef-building corals of the Paleozoic world. Their internal septa exhibit a characteristic four-fold symmetry entirely distinct from the six-fold arrangement of modern corals. The Rugosa were extinguished in the end-Permian catastrophe — the most devastating mass extinction in the chronicle of life.",
         fact="The growth rings within rugose corals demonstrate that the Devonian year contained approximately 400 days — proof, written in ancient stone, that Earth's rotation has slowed through geological time.",
         significance="An indicator of reef facies. Four-fold septal symmetry distinguishes from modern corals. Extinction at the Permian–Triassic boundary is a critical global stratigraphic marker.",
         locations=["UK (Carboniferous)","Belgium","USA (Great Lakes)","Germany","Algeria","China"],
         coords=[(53.5,-1.5),(50.5,4.4),(43.0,-83.0),(51.1,10.4),(28.0,2.0)],
         image_url="images/rugose_coral.jpg"),
    dict(name="Selachii",common="Shark Tooth",period="Devonian–Present",age_start=400,age_end=0,era="Cenozoic",
         environments=["Marine shallow","Marine open water","Marine deep","Coastal"],group="Fish",preservation="Excellent",
         description="The shark sheds and replaces its teeth without cessation — a single individual may produce fifty thousand teeth across its lifetime. The fluorapatite enameloid renders them extraordinarily resistant to dissolution. In the field, triangular form, serrated margins, and a lustrous surface are the diagnostic characters.",
         fact="Teeth of black phosphatised aspect are of great antiquity — millions of years old. White or grey teeth upon the strand are geologically recent. Colour alone furnishes a field estimate of age.",
         significance="A common marine fossil of utility for Cenozoic age estimation. Black coloration indicates Miocene or older; tan suggests Pliocene; white or grey indicates Pleistocene to Recent.",
         locations=["Morocco (phosphate beds)","USA (South Carolina, Maryland)","Malta","Belgium (Antwerp)","Egypt","Libya"],
         coords=[(32.0,-6.0),(33.8,-79.0),(35.9,14.5),(51.2,4.4),(27.0,30.0)],
         image_url="images/shark_tooth.jpg"),
    dict(name="Pollen and Spores",common="Palynomorphs",period="Silurian–Present",age_start=430,age_end=0,era="Cenozoic",
         environments=["Terrestrial","Swamp","Deltaic","Lacustrine","Marine shallow","Fluvial"],group="Plant",preservation="Excellent",
         description="Microscopic reproductive structures armoured with a wall of sporopollenin that borders upon the indestructible. Palynomorph-bearing strata are typically dark grey or black organic-rich shales and coals. Laboratory preparation with hydrofluoric acid is required, yet the biostratigraphic yield is unrivalled across all environments.",
         fact="Pollen preserved within amber retains its original chemistry — investigators have recovered the molecular signatures of the perfumes of ancient flowers from specimens forty million years of age.",
         significance="A universal biozone instrument across all environments, marine and continental alike. Indispensable for correlating coal measures, deltaic and lacustrine sequences where marine fossils are wholly absent.",
         locations=["Global","Coal basins worldwide","North Sea (subsurface)","Algeria (Sahara, subsurface)","Nigeria (Niger Delta)"],
         coords=[(56.0,3.0),(28.0,2.0),(5.0,6.0),(52.0,5.0)],
         image_url="images/palynomorphs.jpg"),
    dict(name="Dinosauria",common="Dinosaur",period="Triassic–Cretaceous",age_start=243,age_end=66,era="Mesozoic",
         environments=["Terrestrial","Fluvial","Deltaic","Coastal"],group="Reptile",preservation="Rare",
         description="The remains of dinosaurs demand rapid burial within sediment-rich environments for their preservation. Most known occurrences derive from fluvial and deltaic deposits. In the field, bones weather from soft mudstones presenting as dark brown fragments with a characteristic honeycomb interior. Isolated teeth and vertebrae vastly exceed complete skeletons in frequency.",
         fact="Birds are in scientific truth dinosaurs — specifically avian theropods that survived the terminal Cretaceous catastrophe 66 million years before the present.",
         significance="A biostratigraphic marker for Mesozoic continental deposits. Specimens preserved in articulation within their original matrix confirm autochthonous burial.",
         locations=["Argentina (Patagonia)","USA (Montana, Utah)","China (Liaoning)","Mongolia (Gobi)","Tanzania (Tendaguru)","Morocco (Kem Kem)"],
         coords=[(-45.0,-67.0),(47.0,-109.0),(41.0,122.0),(44.0,103.0),(-9.0,35.0),(31.0,-5.0)],
         image_url="images/dinosaur.jpg"),
    dict(name="Nummulites",common="Nummulite",period="Paleocene–Oligocene",age_start=56,age_end=34,era="Cenozoic",
         environments=["Marine shallow","Reef","Lagoon"],group="Protist",preservation="Excellent",
         description="Great coin-shaped benthic foraminifera conspicuous to the naked eye — a most distinctive character in the field. They constructed entire limestone formations across the ancient Tethys seaway. Nummulitic limestones serve as important reservoir and aquifer rocks throughout North Africa and the Middle East.",
         fact="The soldiers of Napoleon's Egyptian campaign supposed the nummulite fossils within the pyramid limestone to be the petrified lentils consumed by the ancient builders — the coinage of a civilisation swallowed by time.",
         significance="The primary marker for the Eocene within the Tethyan realm. Nummulitic limestones constitute petroleum reservoir rock across North Africa and the Middle East. Identifiable without a microscope.",
         locations=["Algeria (Atlas)","Egypt (Giza)","Libya","Tunisia","France (Paris Basin)","Spain","India (Gujarat)","Pakistan"],
         coords=[(36.0,3.0),(29.9,31.1),(27.0,17.0),(34.0,9.0),(48.8,2.3),(40.4,-3.7)],
         image_url="images/nummulite.jpg"),
    dict(name="Ichthyosauria",common="Ichthyosaur",period="Triassic–Cretaceous",age_start=250,age_end=90,era="Mesozoic",
         environments=["Marine open water","Marine shallow"],group="Reptile",preservation="Rare",
         description="Marine reptiles of dolphin form that evolved, by convergence, a body plan identical to the modern dolphin — 250 million years before that creature existed. In the field, isolated vertebral discs and paddle elements are the most frequently encountered remains. Certain specimens from Germany preserve soft tissues as carbonaceous films.",
         fact="Several specimens have been recovered with young preserved in the act of birth — confirming live birth, tail-first, precisely as the dolphin accomplishes today.",
         significance="A marker for Triassic–Jurassic marine deposits. Isolated vertebral discs are frequently misidentified as fish vertebrae — the internal trabecular structure provides the distinction.",
         locations=["UK (Lyme Regis, Jurassic Coast)","Germany (Holzmaden)","Canada (British Columbia)","Chile","Nevada (USA)"],
         coords=[(50.7,-2.9),(48.4,9.4),(54.0,-120.0),(-38.0,-71.0),(39.5,-116.0)],
         image_url="images/ichthyosaur.jpg"),
    dict(name="Mammalia",common="Fossil Mammal",period="Triassic–Present",age_start=225,age_end=0,era="Cenozoic",
         environments=["Terrestrial","Fluvial","Cave","Deltaic","Lacustrine"],group="Mammal",preservation="Variable",
         description="The teeth of mammals are their most durable and frequently recovered remains — the enamel is the last to yield to decay. A single isolated tooth may reveal species, approximate age at death, diet, and the climate of a vanished world. Seek teeth and bone fragments weathering from Cenozoic red beds and cave breccias.",
         fact="A skilled paleontologist may determine a mammal's species, age at death, and even the season of that death from a single isolated molar — more intelligence than any other fossil class may yield.",
         significance="The primary biostratigraphy instrument for Cenozoic continental deposits. Enamel geochemistry furnishes paleoclimate data indispensable for correlating non-marine sequences.",
         locations=["USA (Badlands, South Dakota)","China (Yunnan)","Kenya (Turkana)","France (Quercy)","Algeria (Sahara, Gour Lazib)","Pakistan (Siwaliks)"],
         coords=[(43.8,-102.3),(25.0,102.0),(4.0,36.0),(44.4,1.5),(29.0,2.0),(33.0,72.0)],
         image_url="images/mammal.jpg"),
]

ENVIRONMENTS = sorted(set(e for f in FOSSILS for e in f["environments"]))
ERAS   = ["All","Paleozoic","Mesozoic","Cenozoic"]
GROUPS = ["All"] + sorted(set(f["group"] for f in FOSSILS))

def section_header(title, sub=""):
    st.markdown(f'<div class="sec-wrap"><div class="sec-pre">— Field Compendium —</div><div class="sec-title">{title}</div>{"<div class=sec-sub>"+sub+"</div>" if sub else ""}</div>', unsafe_allow_html=True)

def fossil_card(f, show_image=True):
    tags_env = "".join(f'<span class="tag tag-env">{e}</span>' for e in f["environments"])
    tags_loc = "".join(f'<span class="tag tag-loc">{l}</span>' for l in f["locations"][:4])
    pres_c = {"Excellent":"#4a9a5a","Good":"#c8973a","Variable":"#b07030","Rare":"#c04040"}.get(f["preservation"],"#c8973a")
    st.markdown('<div class="fcard">', unsafe_allow_html=True)
    if show_image:
        try:
            st.image(f["image_url"], use_container_width=True)
        except Exception:
            st.markdown('<div style="background:#0e0c08;padding:28px;text-align:center;font-family:Cinzel,serif;font-size:9px;color:#3a2e14;letter-spacing:0.2em;border-bottom:1px solid #2e2410">IMAGE NOT AVAILABLE</div>', unsafe_allow_html=True)
    st.markdown(f"""<div class="fcard-body">
      <div class="fcard-era">{f['period']} &nbsp;·&nbsp; {f['age_start']}–{f['age_end']} Ma &nbsp;·&nbsp; {f['era']}</div>
      <div class="fcard-name">{f['name']}</div>
      <div class="fcard-common">{f['common']}</div>
      <div class="fcard-divider"></div>
      <div class="fcard-desc">{f['description']}</div>
      <div class="fact-box"><div class="fact-ornament">Field Observation</div><div class="fact-text">{f['fact']}</div></div>
      <div class="sig-box"><div class="sig-label">Biostratigraphic Significance</div>{f['significance']}</div>
      <div style="margin-bottom:8px">{tags_env}</div>
      <div style="margin-bottom:12px">{tags_loc}</div>
      <span class="tag" style="color:{pres_c};border-color:{pres_c}44">Preservation &nbsp;·&nbsp; {f['preservation']}</span>
    </div></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""<div style="padding:22px 0 14px">
      <div style="font-family:'Cinzel',serif;font-size:9px;color:#4a3a10;letter-spacing:0.35em;text-transform:uppercase;margin-bottom:8px">Field Edition</div>
      <div style="font-family:'Playfair Display',serif;font-size:24px;font-weight:700;font-style:italic;color:#e8d080">FossilFinder</div>
      <div style="width:40px;height:1px;background:linear-gradient(90deg,#c8973a,transparent);margin:10px 0"></div>
      <div style="font-family:'Crimson Text',serif;font-style:italic;font-size:13px;color:#4a3a10;line-height:1.6">A compendium of fossil groups<br>for the field geologist</div>
    </div><hr>""", unsafe_allow_html=True)
    st.markdown("**Search by Age & Environment**")
    age_min, age_max = st.slider("Geologic Age (Ma)", 0, 541, (0,541), step=5)
    sel_envs  = st.multiselect("Depositional Environment", ENVIRONMENTS, placeholder="Any environment")
    st.markdown("<br>**Refine Results**", unsafe_allow_html=True)
    sel_era   = st.selectbox("Era", ERAS)
    sel_group = st.selectbox("Group", GROUPS)
    sel_pres  = st.selectbox("Preservation", ["Any","Excellent","Good","Variable","Rare"])
    search    = st.text_input("Search", placeholder="e.g. Ammonite")
    st.markdown("<hr>", unsafe_allow_html=True)
    show_images = st.toggle("Show Images", value=True)
    rnd_btn = st.button("Random Fossil", use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""<div style="font-family:'Cinzel',serif;font-size:9px;color:#4a3a10;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:6px">Author</div>
    <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#c8973a;letter-spacing:0.08em">Serhoudji</div>
    <div style="font-family:'Crimson Text',serif;font-style:italic;font-size:13px;color:#4a3a10;margin-top:3px">Petroleum Geology · Algeria</div>""", unsafe_allow_html=True)

def apply_filters(fossils):
    out = fossils
    if search:
        q = search.lower()
        out = [f for f in out if q in f["name"].lower() or q in f["common"].lower()]
    if sel_era != "All":  out = [f for f in out if f["era"] == sel_era]
    if sel_envs:           out = [f for f in out if any(e in f["environments"] for e in sel_envs)]
    if sel_group != "All": out = [f for f in out if f["group"] == sel_group]
    if sel_pres != "Any":  out = [f for f in out if f["preservation"] == sel_pres]
    out = [f for f in out if f["age_start"] >= age_min and f["age_end"] <= age_max]
    return out

filtered = apply_filters(FOSSILS)

st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">Paleontology &nbsp;·&nbsp; Biostratigraphy &nbsp;·&nbsp; Earth History</div>
  <div class="hero-rule"></div>
  <div class="hero-title">FOSSIL<em>FINDER</em></div>
  <div class="hero-tagline">"Reading the record of life written in stone since the dawn of time"</div>
  <div class="hero-author">Developed by<strong>Serhoudji</strong>Petroleum Geology · Algeria</div>
</div>""", unsafe_allow_html=True)

k1,k2,k3,k4,k5 = st.columns(5)
with k1: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(FOSSILS)}</div><div class="kpi-l">Fossil Groups</div></div>', unsafe_allow_html=True)
with k2: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(filtered)}</div><div class="kpi-l">Matching</div></div>', unsafe_allow_html=True)
with k3: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(set(f["era"] for f in filtered)) if filtered else 0}</div><div class="kpi-l">Eras</div></div>', unsafe_allow_html=True)
with k4: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(ENVIRONMENTS)}</div><div class="kpi-l">Environments</div></div>', unsafe_allow_html=True)
with k5: st.markdown(f'<div class="kpi"><div class="kpi-n">541</div><div class="kpi-l">Ma Coverage</div></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if rnd_btn:
    pick = random.choice(FOSSILS)
    section_header(f"Random Selection — {pick['common']}")
    c1,_ = st.columns(2)
    with c1: fossil_card(pick, show_image=show_images)
    st.markdown("<hr>", unsafe_allow_html=True)

tab1,tab2,tab3,tab4 = st.tabs(["FOSSIL GALLERY","DISTRIBUTION MAP","TIMELINE","ENVIRONMENTS"])

with tab1:
    if not filtered:
        st.warning("No fossils match your current filters. Try widening the age range or removing environment filters.")
    else:
        n = len(filtered)
        st.markdown(f'<div class="result-banner">Displaying <strong>{n}</strong> fossil group{"s" if n!=1 else ""} corresponding to your criteria</div>', unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        for i,f in enumerate(filtered):
            with col1 if i%2==0 else col2: fossil_card(f, show_image=show_images)

with tab2:
    section_header("Global Distribution of Occurrences","Principal reference localities — colour of marker denotes geologic era")
    mf = filtered if filtered else FOSSILS
    fig_map = go.Figure()
    for f in mf:
        if not f.get("coords"): continue
        fig_map.add_trace(go.Scattergeo(lat=[c[0] for c in f["coords"]],lon=[c[1] for c in f["coords"]],mode="markers",name=f["common"],
            marker=dict(size=10,color=ERA_COLORS.get(f["era"],"#c8973a"),opacity=0.85,line=dict(width=1.5,color="#12100b")),
            hovertemplate=f"<b>{f['common']}</b><br>{f['name']}<br>Age: {f['age_start']}–{f['age_end']} Ma<br>Era: {f['era']}<extra></extra>"))
    fig_map.update_layout(**PLOT_LAYOUT,height=520,
        geo=dict(bgcolor="#12100b",landcolor="#1e1a0e",oceancolor="#0e0c0a",lakecolor="#0e0c0a",
                 showland=True,showocean=True,showcountries=True,countrycolor="#2e2410",
                 showcoastlines=True,coastlinecolor="#3a2e14",showframe=False,projection_type="natural earth"),
        title=dict(text="Global Fossil Occurrence Localities",font=dict(size=14,color="#e8d080",family="Cinzel, serif")),
        legend=dict(bgcolor="#1a1608",bordercolor="#3a2e14",borderwidth=1,font=dict(size=10),itemsizing="constant"))
    st.plotly_chart(fig_map, use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    section_header("Principal Field Localities")
    for f in mf[:8]:
        with st.expander(f"{f['common']}  ·  {f['name']}  ·  {f['era']}"):
            for loc in f["locations"]: st.markdown(f"- {loc}")
            st.caption(f"Preservation: {f['preservation']}  ·  Age: {f['age_start']}–{f['age_end']} Ma")

with tab3:
    section_header("Stratigraphic Ranges Through Time","Horizontal bars denote the total temporal extent of each fossil group — broken lines mark mass extinctions")
    sf = sorted(filtered if filtered else FOSSILS, key=lambda x: -x["age_start"])
    fig_tl = go.Figure()
    for f in sf:
        d=f["age_start"]-f["age_end"]; c=ERA_COLORS.get(f["era"],"#c8973a")
        fig_tl.add_trace(go.Bar(x=[d],y=[f["common"]],base=f["age_end"],orientation="h",name=f["era"],
            marker=dict(color=c,opacity=0.65,line=dict(width=1,color=c)),
            hovertemplate=f"<b>{f['common']}</b><br>{f['age_start']}–{f['age_end']} Ma ({d} My)<br>Era: {f['era']}<extra></extra>",showlegend=False))
    for era_n,(s,e) in [("Cenozoic",(0,66)),("Mesozoic",(66,252)),("Paleozoic",(252,541))]:
        fig_tl.add_vrect(x0=e,x1=s,fillcolor=ERA_COLORS[era_n],opacity=0.04,layer="below",line_width=0,
                         annotation_text=era_n,annotation_position="top",annotation_font=dict(size=10,color=ERA_COLORS[era_n],family="Cinzel, serif"))
    for age,label,clr in [(252,"End-Permian (96% sp.)","#c04040"),(66,"K-Pg Extinction","#c07040"),(201,"End-Triassic","#c06040")]:
        if age_min<=age<=age_max:
            fig_tl.add_vline(x=age,line_color=clr,line_dash="dot",line_width=1.2,
                             annotation_text=label,annotation_font=dict(size=9,color=clr),annotation_position="top right")
    fig_tl.update_layout(**PLOT_LAYOUT,height=max(400,len(sf)*34+80),barmode="overlay",
        xaxis=dict(title="Age (Ma)",autorange="reversed",gridcolor="#2e2410",linecolor="#2e2410"),
        yaxis=dict(gridcolor="#2e2410",linecolor="#2e2410"),
        title=dict(text="Fossil Stratigraphic Ranges — Coloured by Era",font=dict(size=14,color="#e8d080",family="Cinzel, serif")))
    st.plotly_chart(fig_tl, use_container_width=True)

with tab4:
    section_header("Environment Finder","Select a depositional environment to consult which fossil groups are habitually encountered therein")
    sel_env = st.selectbox("Depositional Environment", ENVIRONMENTS, key="env_detail")
    env_results = [f for f in FOSSILS if sel_env in f["environments"]]
    if env_results:
        st.markdown(f'<div class="result-banner"><strong>{len(env_results)}</strong> fossil group{"s" if len(env_results)!=1 else ""} anticipated within <em>{sel_env}</em> settings</div>', unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        for i,f in enumerate(env_results):
            with col1 if i%2==0 else col2: fossil_card(f,show_image=show_images)
    else:
        st.info("No fossils in the database for this environment.")
    st.markdown("<hr>", unsafe_allow_html=True)
    section_header("Environment × Group Occurrence Matrix","Distribution of fossil groups across depositional environments")
    groups_all = sorted(set(f["group"] for f in FOSSILS))
    matrix = [[sum(1 for f in FOSSILS if env in f["environments"] and f["group"]==g) for g in groups_all] for env in ENVIRONMENTS]
    fig_hm = go.Figure(go.Heatmap(z=matrix,x=groups_all,y=ENVIRONMENTS,
        colorscale=[[0,"#12100b"],[0.35,"#3a2a0a"],[0.7,"#8a6020"],[1,"#c8973a"]],
        hovertemplate="Environment: %{y}<br>Group: %{x}<br>Count: %{z}<extra></extra>",
        colorbar=dict(title="Count",thickness=12,len=0.7,tickfont=dict(size=9,color="#c8b87a"),title_font=dict(size=10,color="#c8b87a"))))
    fig_hm.update_layout(**PLOT_LAYOUT,height=460,
        xaxis=dict(title="Fossil Group",tickangle=-35,gridcolor="#2e2410",linecolor="#2e2410"),
        yaxis=dict(title="Environment",gridcolor="#2e2410",linecolor="#2e2410"),
        title=dict(text="Fossil Occurrence Matrix",font=dict(size=14,color="#e8d080",family="Cinzel, serif")))
    st.plotly_chart(fig_hm, use_container_width=True)

st.markdown("""
<div class="footer">
  <div>
    <div class="footer-name">Serhoudji</div>
    <div class="footer-sub">Petroleum Geology · Algeria</div>
  </div>
  <div class="footer-center">
    FossilFinder · Field Edition · v2.0<br>
    ✦<br>
    15 Fossil Groups · 3 Eras · 541 Ma of Earth History
  </div>
  <div class="footer-right">
    Constructed with Streamlit and Plotly<br>
    Paleontology · Biostratigraphy<br>
    Field Geology
  </div>
</div>""", unsafe_allow_html=True)
