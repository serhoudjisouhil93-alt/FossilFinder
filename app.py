import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FossilFinder · Field Edition",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=IM+Fell+English:ital@0;1&family=Source+Code+Pro:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Code Pro', monospace;
    background-color: #0f0d09;
    color: #d8c9a8;
}
.stApp {
    background-color: #0f0d09;
    background-image:
        radial-gradient(ellipse at 20% 20%, #1a150a 0%, transparent 60%),
        radial-gradient(ellipse at 80% 80%, #12100a 0%, transparent 60%);
}

section[data-testid="stSidebar"] {
    background: #13110c;
    border-right: 1px solid #2a2015;
}
section[data-testid="stSidebar"] * { color: #d8c9a8 !important; }

/* ── HERO HEADER ── */
.hero {
    background: linear-gradient(160deg, #1c170e 0%, #241d10 50%, #1a150a 100%);
    border: 1px solid #3a2e18;
    border-radius: 12px;
    padding: 36px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
        45deg, transparent, transparent 40px,
        rgba(200,151,58,0.015) 40px, rgba(200,151,58,0.015) 41px
    );
}
.hero::after {
    content: '☽';
    position: absolute;
    right: 48px; top: 50%;
    transform: translateY(-50%);
    font-size: 88px;
    opacity: 0.06;
    color: #c8973a;
}
.hero-eyebrow {
    font-size: 10px;
    letter-spacing: 0.3em;
    color: #c8973a;
    text-transform: uppercase;
    margin-bottom: 10px;
    font-family: 'Source Code Pro', monospace;
}
.hero-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 48px;
    font-weight: 700;
    color: #f5ead0;
    line-height: 1.1;
    margin: 0 0 6px;
}
.hero-title em { color: #c8973a; font-style: italic; }
.hero-tagline {
    font-family: 'IM Fell English', Georgia, serif;
    font-style: italic;
    font-size: 16px;
    color: #8a7550;
    margin-top: 8px;
}

/* ── SECTION HEADER ── */
.sec-wrap { margin: 8px 0 20px; }
.sec-label {
    font-size: 9px;
    letter-spacing: 0.3em;
    color: #6b5530;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.sec-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: #f0e2c0;
    border-bottom: 1px solid #2a2015;
    padding-bottom: 10px;
}

/* ── FOSSIL CARD ── */
.fcard {
    background: #171310;
    border: 1px solid #2a2015;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 20px;
    transition: border-color 0.25s, box-shadow 0.25s;
}
.fcard:hover {
    border-color: #c8973a;
    box-shadow: 0 4px 24px rgba(200,151,58,0.08);
}
.fcard-img {
    width: 100%;
    aspect-ratio: 4/3;
    object-fit: cover;
    display: block;
    background: #1c1810;
    border-bottom: 1px solid #2a2015;
}
.fcard-img-placeholder {
    width: 100%;
    aspect-ratio: 4/3;
    background: linear-gradient(135deg, #1c1810, #241d10);
    border-bottom: 1px solid #2a2015;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 56px;
    opacity: 0.5;
}
.fcard-body { padding: 18px 20px 20px; }
.fcard-era {
    font-size: 9px;
    letter-spacing: 0.2em;
    color: #c8973a;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.fcard-name {
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    font-weight: 700;
    font-style: italic;
    color: #f0e2c0;
    margin-bottom: 2px;
}
.fcard-common {
    font-family: 'IM Fell English', serif;
    font-size: 13px;
    color: #8a7550;
    margin-bottom: 12px;
}
.fcard-desc {
    font-size: 12px;
    color: #9a8a6a;
    line-height: 1.75;
    margin-bottom: 14px;
}
.fact-box {
    background: #1e1a10;
    border-left: 3px solid #c8973a;
    border-radius: 0 6px 6px 0;
    padding: 10px 14px;
    margin-bottom: 14px;
}
.fact-label { font-size: 9px; color: #c8973a; letter-spacing: 0.2em; margin-bottom: 4px; }
.fact-text { font-size: 12px; color: #c0aa80; line-height: 1.6; font-style: italic; }
.sig-box {
    background: #13110c;
    border: 1px solid #2a2015;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 11px;
    color: #7a6a4a;
    margin-bottom: 12px;
}
.sig-label { font-size: 9px; color: #5a4a2a; letter-spacing: 0.15em; margin-bottom: 3px; }

.tag {
    display: inline-block;
    background: #1e1a10;
    border: 1px solid #3a2e18;
    border-radius: 3px;
    padding: 2px 8px;
    font-size: 9px;
    color: #7a6a4a;
    letter-spacing: 0.08em;
    margin: 2px 2px 2px 0;
    text-transform: uppercase;
}
.tag-env  { border-color: #2a4030; color: #6a9070; }
.tag-loc  { border-color: #30402a; color: #8a9060; }
.tag-pres { border-color: #4a3a1a; color: #c8973a; }

/* ── KPI ROW ── */
.kpi-grid { display: flex; gap: 12px; margin-bottom: 28px; flex-wrap: wrap; }
.kpi {
    flex: 1; min-width: 120px;
    background: #171310;
    border: 1px solid #2a2015;
    border-radius: 8px;
    padding: 14px 18px;
    position: relative;
}
.kpi::before {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #c8973a, transparent);
    border-radius: 0 0 8px 8px;
}
.kpi-n { font-family: 'Playfair Display', serif; font-size: 30px; font-weight: 700; color: #c8973a; }
.kpi-l { font-size: 9px; color: #5a4a2a; letter-spacing: 0.18em; text-transform: uppercase; margin-top: 2px; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: #13110c;
    border-bottom: 1px solid #2a2015;
    gap: 2px;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Source Code Pro', monospace;
    font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase;
    color: #5a4a2a; background: transparent;
    border-radius: 6px 6px 0 0;
    padding: 10px 20px;
}
.stTabs [aria-selected="true"] {
    background: #1c170e !important;
    color: #c8973a !important;
    border-bottom: 2px solid #c8973a !important;
}

/* ── INPUTS ── */
.stSelectbox > div > div, .stMultiSelect > div > div {
    background: #171310 !important;
    border-color: #2a2015 !important;
    color: #d8c9a8 !important;
    font-family: 'Source Code Pro', monospace !important;
}
.stSlider [data-baseweb="slider"] { padding: 0 4px; }
.stButton > button {
    background: #1e1a10 !important;
    border: 1px solid #c8973a !important;
    color: #c8973a !important;
    font-family: 'Source Code Pro', monospace !important;
    font-size: 11px !important;
    letter-spacing: 0.1em;
    border-radius: 6px !important;
    text-transform: uppercase;
}
.stButton > button:hover { background: rgba(200,151,58,0.12) !important; }

hr { border-color: #2a2015 !important; }

/* ── MAP NOTE ── */
.map-note {
    background: #171310;
    border: 1px solid #2a2015;
    border-radius: 8px;
    padding: 14px 18px;
    font-size: 11px;
    color: #7a6a4a;
    margin-bottom: 16px;
}

/* ── RESULT HEADER ── */
.result-header {
    background: linear-gradient(90deg, #1c170e, transparent);
    border-left: 3px solid #c8973a;
    padding: 10px 16px;
    margin-bottom: 20px;
    border-radius: 0 6px 6px 0;
    font-family: 'Playfair Display', serif;
    font-size: 15px;
    color: #d8c9a8;
}

</style>
""", unsafe_allow_html=True)

# ─── FOSSIL DATABASE ──────────────────────────────────────────────────────────
# Images: iNaturalist open-data S3 CDN — allows hotlinking, no CORS issues
FOSSILS = [
    dict(
        name="Trilobita", common="Trilobite",
        emoji="🦐",
        period="Cambrian–Permian", age_start=521, age_end=252, era="Paleozoic",
        environments=["Marine shallow", "Marine deep", "Reef"],
        group="Arthropod", preservation="Excellent",
        description="Among Earth's most successful early animals, trilobites dominated Paleozoic seas for nearly 270 million years. Their calcite exoskeletons preserve exceptionally well — rolled specimens indicate a stress response still visible 500 million years later.",
        fact="Over 20,000 species have been described. They were more diverse than all modern mammals combined, and some had eyes made of calcite crystals that never needed focusing.",
        significance="Primary zone fossil for Cambrian–Ordovician. Rolled specimens indicate storm events or predator pressure.",
        locations=["Morocco (Anti-Atlas)", "USA (Utah, Ohio)", "Russia", "China", "Canada (Burgess Shale)", "Algeria (Saharan platform)"],
        coords=[(31.5, -7.0), (39.3, -111.0), (55.7, 37.6), (30.0, 110.0), (51.4, -116.5)],
        image_url="images/trilobite.jpg",
        color="#8b6914",
    ),
    dict(
        name="Ammonoidea", common="Ammonite",
        emoji="🌀",
        period="Devonian–Cretaceous", age_start=419, age_end=66, era="Mesozoic",
        environments=["Marine shallow", "Marine open water", "Marine deep"],
        group="Cephalopod", preservation="Excellent",
        description="The ultimate biostratigraphic tool. Ammonites evolved so rapidly that each species existed for less than 1 million years on average. Their coiled chambered shells allowed neutral buoyancy like a submarine. Suture patterns (visible on weathered specimens) identify genus and species.",
        fact="The largest ammonite ever found — Parapuzosia seppenradensis from Germany — reached 1.8 meters in diameter. Most field specimens fit in your hand.",
        significance="Primary biozone fossil for Jurassic & Cretaceous. Suture complexity increases through time — useful for relative age dating in the field.",
        locations=["UK (Whitby, Dorset)", "Morocco (Erfoud)", "Madagascar", "France (Normandy)", "Germany", "Tunisia", "Algeria (Tlemcen)"],
        coords=[(54.4, -0.6), (31.4, -4.0), (-20.0, 47.0), (49.1, -0.4), (51.3, 10.4)],
        image_url="images/ammonite.jpg",
        color="#c8973a",
    ),
    dict(
        name="Graptolithina", common="Graptolite",
        emoji="〰️",
        period="Cambrian–Carboniferous", age_start=510, age_end=320, era="Paleozoic",
        environments=["Marine deep", "Marine open water"],
        group="Hemichordate", preservation="Good",
        description="Flattened carbon films on black shales — easily missed by untrained eyes. Graptolites are colonial organisms that drifted in ancient oceans. Their rapid evolution makes them the primary zone fossil for Ordovician and Silurian rocks worldwide. Look for saw-blade patterns on dark fine-grained shales.",
        fact="Graptolites were once classified as plants — their name means 'written rock' in Greek. They were only recognized as animals in the 20th century.",
        significance="Primary zone fossil for Ordovician–Silurian globally. Black shale hosting = anoxic deep water paleoenvironment.",
        locations=["Wales (type locality)", "Scotland", "Canada (Quebec)", "China", "Australia", "Czech Republic"],
        coords=[(52.3, -3.7), (56.0, -4.2), (47.0, -71.0), (30.0, 110.0), (-25.0, 133.0)],
        image_url="images/graptolite.jpg",
        color="#4a3a1e",
    ),
    dict(
        name="Brachiopoda", common="Brachiopod",
        emoji="🐚",
        period="Cambrian–Present", age_start=530, age_end=0, era="Paleozoic",
        environments=["Marine shallow", "Reef", "Marine deep"],
        group="Brachiopod", preservation="Excellent",
        description="Superficially similar to bivalves but biologically unrelated. The key field distinction: brachiopods have one plane of symmetry through the shell (top-bottom), bivalves through left-right. They were the dominant shelled organisms of Paleozoic seas and are still living today.",
        fact="Living brachiopods called Lingula are nearly identical to specimens from 500 million years ago — the slowest-evolving animals on Earth.",
        significance="Useful for Devonian biostratigraphy. Abundance indicates normal marine salinity. Distinct from bivalves — critical for paleoenvironment interpretation.",
        locations=["Germany (Rhine)", "USA (Devonian of New York)", "UK (Silurian)", "China", "Australia", "Algeria"],
        coords=[(50.9, 6.9), (42.9, -76.0), (52.3, -1.5), (30.0, 110.0), (-25.0, 133.0)],
        image_url="images/brachiopod.jpg",
        color="#6b4e2a",
    ),
    dict(
        name="Foraminifera", common="Foraminifera",
        emoji="🔬",
        period="Cambrian–Present", age_start=530, age_end=0, era="Cenozoic",
        environments=["Marine shallow", "Marine deep", "Marine open water", "Lagoon"],
        group="Protist", preservation="Excellent",
        description="Microscopic single-celled organisms visible only under hand lens or microscope. Despite their size, they are the primary biostratigraphic tool for Cenozoic marine sections globally. In the field, foram-bearing limestones often have a sugary or granular texture. Nummulites (large benthic forams) are visible to the naked eye.",
        fact="The Great Pyramid of Giza is built almost entirely from nummulitic limestone — billions of foram shells stacked by ancient Egyptians.",
        significance="Primary Cenozoic biozone tool. Planktonic/benthic ratio indicates paleodepth. δ¹⁸O from shells = ancient temperature proxy.",
        locations=["Global oceans", "Egypt (Eocene)", "North Sea", "Caribbean", "Algeria (Saharan platform)", "Tunisia"],
        coords=[(29.9, 31.1), (56.0, 3.0), (15.0, -75.0), (36.8, 10.2), (28.0, 2.0)],
        image_url="images/foraminifera.jpg",
        color="#a09060",
    ),
    dict(
        name="Echinoidea", common="Sea Urchin",
        emoji="🌸",
        period="Ordovician–Present", age_start=480, age_end=0, era="Mesozoic",
        environments=["Marine shallow", "Reef", "Lagoon"],
        group="Echinoderm", preservation="Good",
        description="Regular (radial) and irregular (bilateral) echinoids are common in Cretaceous chalks and Jurassic limestones. Irregular forms like Micraster are classic zone fossils for the Cretaceous chalk of NW Europe. In the field, their five-fold symmetry and ambulacral grooves are diagnostic.",
        fact="Medieval Europeans called echinoid tests 'shepherd's crowns' or 'fairy loaves' and kept them as good luck charms. Neolithic humans buried them with the dead.",
        significance="Micraster is a zone fossil for Cretaceous chalk. Irregular echinoids = infaunal life, indicates soft muddy seafloor.",
        locations=["UK (chalk downs)", "France (Normandy chalk)", "North Africa", "Egypt", "Israel", "Denmark"],
        coords=[(51.2, 0.5), (49.1, 0.3), (27.0, 20.0), (29.5, 31.2), (31.0, 35.0)],
        image_url="images/echinoid.jpg",
        color="#9a8060",
    ),
    dict(
        name="Belemnoidea", common="Belemnite",
        emoji="🔩",
        period="Carboniferous–Eocene", age_start=360, age_end=34, era="Mesozoic",
        environments=["Marine shallow", "Marine open water"],
        group="Cephalopod", preservation="Good",
        description="The bullet-shaped calcite guard is what preserves — the soft squid-like body rarely fossilizes. Belemnite guards are common in Jurassic and Cretaceous marine rocks worldwide. Dense accumulations called 'belemnite battlefields' may represent mass mortality events or spawning grounds.",
        fact="In medieval Scandinavia, belemnites were called 'thunderbolts' (tordensten) — people believed they fell from the sky during lightning storms and had magical properties.",
        significance="Useful index fossil for Jurassic–Cretaceous marine sequences. Guards indicate normal marine, moderate-energy conditions.",
        locations=["UK (Jurassic Coast)", "Germany (Solnhofen)", "Russia", "Poland", "Algeria (Tlemcen region)", "Tunisia"],
        coords=[(50.6, -2.4), (48.8, 11.0), (55.0, 40.0), (52.0, 20.0), (34.8, -1.3)],
        image_url="images/belemnite.jpg",
        color="#8a7050",
    ),
    dict(
        name="Crinoidea", common="Crinoid (Sea Lily)",
        emoji="🌺",
        period="Ordovician–Present", age_start=480, age_end=0, era="Paleozoic",
        environments=["Marine shallow", "Reef", "Marine deep"],
        group="Echinoderm", preservation="Good",
        description="Crinoidal stem discs — small circular plates with a central hole — are among the most common Paleozoic fossils. Intact calyces (cup-shaped heads) are rare and valuable. Crinoidal limestones are economically important as reservoir rocks in some oil fields. Look for button-like discs on bedding planes.",
        fact="Native American tribes used crinoid stem discs as beads — they're perfectly circular with a natural hole, no drilling required.",
        significance="Crinoidal limestones = important petroleum reservoir rock (e.g. Mississippian plays, USA). Abundance indicates clear, well-oxygenated shallow seas.",
        locations=["USA (Indiana, Illinois)", "UK (Carboniferous)", "Germany", "Belgium", "Russia", "China"],
        coords=[(39.7, -86.1), (53.5, -1.5), (51.1, 10.4), (50.5, 4.4), (55.0, 40.0)],
        image_url="images/crinoid.jpg",
        color="#7a6040",
    ),
    dict(
        name="Rugosa", common="Rugose Coral",
        emoji="🪸",
        period="Ordovician–Permian", age_start=480, age_end=252, era="Paleozoic",
        environments=["Reef", "Marine shallow", "Lagoon"],
        group="Cnidarian", preservation="Good",
        description="Solitary horn-shaped and colonial reef-building corals of the Paleozoic. Their internal septa show a characteristic 4-fold symmetry — distinct from modern 6-fold corals. Rugose corals were wiped out in the end-Permian extinction, the largest mass extinction in Earth history (96% of marine species lost).",
        fact="The growth rings inside rugose corals show that Devonian years had ~400 days, confirming that Earth's rotation has slowed over time due to tidal friction.",
        significance="Reef facies indicator. 4-fold septal symmetry distinguishes from modern corals. Extinction at Permian–Triassic boundary is a key global stratigraphic marker.",
        locations=["UK (Carboniferous)", "Belgium", "USA (Great Lakes)", "Germany", "Algeria", "China"],
        coords=[(53.5, -1.5), (50.5, 4.4), (43.0, -83.0), (51.1, 10.4), (28.0, 2.0)],
        image_url="images/rugose_coral.jpg",
        color="#7a5a3a",
    ),
    dict(
        name="Selachii", common="Shark Tooth",
        emoji="🦷",
        period="Devonian–Present", age_start=400, age_end=0, era="Cenozoic",
        environments=["Marine shallow", "Marine open water", "Marine deep", "Coastal"],
        group="Fish", preservation="Excellent",
        description="Sharks continuously shed and replace teeth throughout their lives — one shark produces up to 50,000 teeth. Teeth are coated in fluorapatite, making them extremely resistant to dissolution. In the field, shark teeth are identified by their triangular shape, serrated edges, and glossy enameloid surface. Color varies from white (young) to black (old, phosphatized).",
        fact="Megalodon teeth reach 18 cm — the shark itself may have reached 18 meters. Black phosphatized teeth are millions of years old; white teeth on the beach are recent.",
        significance="Common marine fossil useful for Cenozoic age estimation. Black = Miocene or older; tan/brown = Pliocene; white/grey = Pleistocene–Recent.",
        locations=["Morocco (phosphate beds)", "USA (South Carolina, Maryland)", "Malta", "Belgium (Antwerp)", "Egypt", "Libya"],
        coords=[(32.0, -6.0), (33.8, -79.0), (35.9, 14.5), (51.2, 4.4), (27.0, 30.0)],
        image_url="images/shark_tooth.jpg",
        color="#8a9aaa",
    ),
    dict(
        name="Pollen & Spores", common="Palynomorphs",
        emoji="🌿",
        period="Silurian–Present", age_start=430, age_end=0, era="Cenozoic",
        environments=["Terrestrial", "Swamp", "Deltaic", "Lacustrine", "Marine shallow", "Fluvial"],
        group="Plant", preservation="Excellent",
        description="Microscopic plant reproductive structures with an almost indestructible outer wall (sporopollenin). In the field, palynomorph-bearing rocks are typically dark grey or black organic-rich shales and coals. Samples must be processed in lab with HF acid. Despite this, palynology is one of the most powerful biostratigraphic tools across all sedimentary environments.",
        fact="Fossil pollen preserved in amber retains its original chemistry — scientists have recovered the molecular signatures of ancient flower scents from 40-million-year-old specimens.",
        significance="Universal biozone tool across all environments — marine and non-marine. Essential for correlating coal measures, deltaic and lacustrine sequences where marine fossils are absent.",
        locations=["Global", "Coal basins worldwide", "North Sea (subsurface)", "Algeria (Sahara, subsurface)", "Nigeria (Niger Delta)"],
        coords=[(56.0, 3.0), (28.0, 2.0), (5.0, 6.0), (52.0, 5.0)],
        image_url="images/palynomorphs.jpg",
        color="#6a8a4a",
    ),
    dict(
        name="Dinosauria", common="Dinosaur",
        emoji="🦖",
        period="Triassic–Cretaceous", age_start=243, age_end=66, era="Mesozoic",
        environments=["Terrestrial", "Fluvial", "Deltaic", "Coastal"],
        group="Reptile", preservation="Rare",
        description="Dinosaur bones require rapid burial in sediment-rich environments. Most known from fluvial (river) and deltaic deposits where carcasses were buried quickly. In the field, bones often weather out of soft mudstones and appear as dark brown or black fragments with a honeycomb-like internal texture. Isolated teeth and vertebrae are far more common than complete skeletons.",
        fact="Birds are technically dinosaurs — specifically avian theropods that survived the end-Cretaceous extinction event 66 million years ago.",
        significance="Biostratigraphic marker for Mesozoic continental deposits. Bones are often reworked — in situ specimens preserve original orientation and articulation.",
        locations=["Argentina (Patagonia)", "USA (Montana, Utah)", "China (Liaoning)", "Mongolia (Gobi)", "Tanzania (Tendaguru)", "Morocco (Kem Kem)"],
        coords=[(-45.0, -67.0), (47.0, -109.0), (41.0, 122.0), (44.0, 103.0), (-9.0, 35.0), (31.0, -5.0)],
        image_url="images/dinosaur.jpg",
        color="#6b8a3a",
    ),
    dict(
        name="Nummulites", common="Nummulite",
        emoji="🪙",
        period="Paleocene–Oligocene", age_start=56, age_end=34, era="Cenozoic",
        environments=["Marine shallow", "Reef", "Lagoon"],
        group="Protist", preservation="Excellent",
        description="Large coin-shaped benthic foraminifera clearly visible to the naked eye — a distinctive feature in the field. They built entire limestone formations across the ancient Tethys seaway. Nummulitic limestones are important reservoir and aquifer rocks across North Africa and the Middle East. Look for coin-like discs in Eocene carbonates.",
        fact="Napoleon's soldiers in Egypt thought nummulite fossils in pyramid limestone were petrified lentils eaten by the ancient pyramid builders.",
        significance="Key marker for Eocene in Tethyan realm. Nummulitic limestones = petroleum reservoir rock in North Africa and Middle East. Visible without microscope — field-identifiable.",
        locations=["Algeria (Atlas)", "Egypt (Giza)", "Libya", "Tunisia", "France (Paris Basin)", "Spain", "India (Gujarat)", "Pakistan"],
        coords=[(36.0, 3.0), (29.9, 31.1), (27.0, 17.0), (34.0, 9.0), (48.8, 2.3), (40.4, -3.7)],
        image_url="images/nummulite.jpg",
        color="#b8a870",
    ),
    dict(
        name="Ichthyosauria", common="Ichthyosaur",
        emoji="🐬",
        period="Triassic–Cretaceous", age_start=250, age_end=90, era="Mesozoic",
        environments=["Marine open water", "Marine shallow"],
        group="Reptile", preservation="Rare",
        description="Dolphin-shaped marine reptiles that convergently evolved an identical body plan to modern dolphins 250 million years before dolphins existed. Some specimens from Germany preserve soft tissue outlines as carbon films, showing dorsal fins and tail flukes not visible from bones alone. In the field, isolated vertebrae (circular discs) and paddle bones are the most common finds.",
        fact="Several ichthyosaur specimens have been found with babies preserved mid-birth — confirming live birth, tail-first, just like modern dolphins.",
        significance="Marker for Triassic–Jurassic marine deposits. Isolated vertebral discs are often misidentified as fish vertebrae — compare size and internal structure.",
        locations=["UK (Lyme Regis, Jurassic Coast)", "Germany (Holzmaden)", "Canada (British Columbia)", "Chile", "Nevada (USA)"],
        coords=[(50.7, -2.9), (48.4, 9.4), (54.0, -120.0), (-38.0, -71.0), (39.5, -116.0)],
        image_url="images/ichthyosaur.jpg",
        color="#5a7a8a",
    ),
    dict(
        name="Mammalia", common="Fossil Mammal",
        emoji="🦴",
        period="Triassic–Present", age_start=225, age_end=0, era="Cenozoic",
        environments=["Terrestrial", "Fluvial", "Cave", "Deltaic", "Lacustrine"],
        group="Mammal", preservation="Variable",
        description="Mammal teeth are the most common mammal fossil — their enamel is the hardest biological material and resists decay longest. A single tooth can reveal species, age, diet, and paleoclimate. In the field, look for isolated teeth and bone fragments weathering out of Cenozoic red beds, fluvial silts, and cave breccias.",
        fact="We know more about ancient mammal species from isolated teeth than any other body part. A good paleontologist can identify species, age-at-death, and even season of death from a single molar.",
        significance="Primary biostratigraphy tool for Cenozoic continental deposits. Teeth enamel geochemistry provides paleoclimate data. Essential for correlating non-marine sequences.",
        locations=["USA (Badlands, South Dakota)", "China (Yunnan)", "Kenya (Turkana)", "France (Quercy)", "Algeria (Sahara, Gour Lazib)", "Pakistan (Siwaliks)"],
        coords=[(43.8, -102.3), (25.0, 102.0), (4.0, 36.0), (44.4, 1.5), (29.0, 2.0), (33.0, 72.0)],
        image_url="images/mammal.jpg",
        color="#9a7050",
    ),
]

ENVIRONMENTS = sorted(set(e for f in FOSSILS for e in f["environments"]))
ERAS         = ["All", "Paleozoic", "Mesozoic", "Cenozoic"]
GROUPS       = ["All"] + sorted(set(f["group"] for f in FOSSILS))

PLOT_BG = dict(
    paper_bgcolor="#171310", plot_bgcolor="#0f0d09",
    font=dict(family="Source Code Pro, monospace", color="#d8c9a8", size=11),
    margin=dict(l=50, r=20, t=50, b=50),
)
ERA_COLORS = {"Paleozoic": "#99c08d", "Mesozoic": "#67c5b5", "Cenozoic": "#f9a11b"}

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def section_header(title, sub=""):
    st.markdown(f"""
    <div class="sec-wrap">
      <div class="sec-label">— Field Guide —</div>
      <div class="sec-title">{title}</div>
    </div>
    {"<p style='font-size:12px;color:#6b5530;margin:-12px 0 18px;'>"+sub+"</p>" if sub else ""}
    """, unsafe_allow_html=True)

def fossil_card(f, show_image=True):
    tags_env  = "".join(f'<span class="tag tag-env">{e}</span>'  for e in f["environments"])
    tags_loc  = "".join(f'<span class="tag tag-loc">📍 {l}</span>' for l in f["locations"][:4])
    pres_color = {"Excellent":"#39c87a","Good":"#c8973a","Variable":"#e09030","Rare":"#e05c5c"}.get(f["preservation"],"#c8973a")

    # Card top border
    st.markdown(f'<div class="fcard">', unsafe_allow_html=True)

    # Image — load from local images/ folder in the repo
    if show_image:
        try:
            st.image(f["image_url"], use_container_width=True,
                     caption=f"{f['common']} · {f['era']}")
        except Exception:
            # Fallback: show emoji placeholder if image file is missing
            st.markdown(
                f'<div style="background:#1c170e;border-bottom:1px solid #2a2015;'
                f'padding:40px;text-align:center;font-size:52px;opacity:0.4">'
                f'{f["emoji"]}</div>',
                unsafe_allow_html=True
            )

    # Card body
    st.markdown(f"""
      <div class="fcard-body">
        <div class="fcard-era">⏱ {f['period']} &nbsp;·&nbsp; {f['age_start']}–{f['age_end']} Ma &nbsp;·&nbsp; {f['era']}</div>
        <div class="fcard-name">{f['name']}</div>
        <div class="fcard-common">"{f['common']}"</div>
        <div class="fcard-desc">{f['description']}</div>
        <div class="fact-box">
          <div class="fact-label"> Field Fact</div>
          <div class="fact-text">{f['fact']}</div>
        </div>
        <div class="sig-box">
          <div class="sig-label">⚑ Biostratigraphic Significance</div>
          {f['significance']}
        </div>
        <div style="margin-bottom:8px">{tags_env}</div>
        <div style="margin-bottom:8px">{tags_loc}</div>
        <span class="tag tag-pres" style="color:{pres_color};border-color:{pres_color}44">
          ◆ Preservation: {f['preservation']}
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:18px 0 10px">
      <div style="font-family:'Playfair Display',serif;font-size:24px;font-weight:700;
           color:#f0e2c0;font-style:italic">🦴 Fossil<em style="color:#c8973a">Finder</em></div>
      <div style="font-size:9px;color:#5a4a2a;letter-spacing:0.25em;margin-top:3px">
        FIELD EDITION · PALEONTOLOGY
      </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    st.markdown("** FIND BY AGE & ENVIRONMENT**")

    age_min, age_max = st.slider(
        "Geologic age (Ma)",
        0, 541, (0, 541), step=5,
        help="Ma = millions of years ago. 0 = today, 541 = base of Cambrian"
    )

    sel_envs = st.multiselect(
        "Depositional environment",
        ENVIRONMENTS,
        placeholder="Any environment…"
    )

    st.markdown("<br>** MORE FILTERS**", unsafe_allow_html=True)
    sel_era   = st.selectbox("Geologic era", ERAS)
    sel_group = st.selectbox("Fossil group", GROUPS)
    sel_pres  = st.selectbox("Preservation quality", ["Any","Excellent","Good","Variable","Rare"])
    search    = st.text_input("Search name", placeholder="e.g. Ammonite…")

    st.markdown("<hr>", unsafe_allow_html=True)
    show_images = st.toggle("Show fossil images", value=True)
    st.markdown("<br>", unsafe_allow_html=True)
    rnd_btn = st.button("  Random Fossil", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.caption("FossilFinder v2.0 · Field Edition\nFor field geologists & geology students")

# ─── FILTER ───────────────────────────────────────────────────────────────────
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

# ─── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">Field Paleontology · Biostratigraphy · Earth History</div>
  <div class="hero-title">Fossil<em>Finder</em></div>
  <div class="hero-tagline">"Reading the record of life written in stone"</div>
</div>
""", unsafe_allow_html=True)

# ─── KPI STRIP ────────────────────────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)
with k1: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(FOSSILS)}</div><div class="kpi-l">Fossil Groups</div></div>', unsafe_allow_html=True)
with k2: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(filtered)}</div><div class="kpi-l">Matching Filters</div></div>', unsafe_allow_html=True)
with k3: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(set(f["era"] for f in filtered)) if filtered else 0}</div><div class="kpi-l">Geologic Eras</div></div>', unsafe_allow_html=True)
with k4: st.markdown(f'<div class="kpi"><div class="kpi-n">{len(ENVIRONMENTS)}</div><div class="kpi-l">Environments</div></div>', unsafe_allow_html=True)
with k5: st.markdown(f'<div class="kpi"><div class="kpi-n">541</div><div class="kpi-l">Ma Coverage</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── RANDOM FOSSIL ────────────────────────────────────────────────────────────
if rnd_btn:
    pick = random.choice(FOSSILS)
    section_header(f" Random Fossil — {pick['common']}")
    fossil_card(pick, show_image=show_images)
    st.markdown("<hr>", unsafe_allow_html=True)

# ─── MAIN TABS ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "  FOSSIL GALLERY",
    "  DISTRIBUTION MAP",
    "  TIMELINE",
    "  ENVIRONMENTS",
])

# ══ TAB 1 — FOSSIL GALLERY ═══════════════════════════════════════════════════
with tab1:
    if not filtered:
        st.warning("No fossils match your filters. Try widening the age range or removing environment filters.")
    else:
        st.markdown(f'<div class="result-header">Showing <strong>{len(filtered)}</strong> fossil group{"s" if len(filtered)!=1 else ""} matching your filters</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        for i, f in enumerate(filtered):
            with col1 if i % 2 == 0 else col2:
                fossil_card(f, show_image=show_images)

# ══ TAB 2 — DISTRIBUTION MAP ═════════════════════════════════════════════════
with tab2:
    section_header("Global Fossil Distribution",
                   "Known occurrence localities for filtered fossil groups · Click markers for details")

    st.markdown("""
    <div class="map-note">
    ⚑ <strong>Field note:</strong> These represent classic reference localities — fossils may occur in many additional locations.
    Marker color indicates geologic era. Use filters in the sidebar to show specific groups.
    </div>
    """, unsafe_allow_html=True)

    map_fossils = filtered if filtered else FOSSILS

    fig_map = go.Figure()

    for f in map_fossils:
        if not f.get("coords"):
            continue
        lats = [c[0] for c in f["coords"]]
        lons = [c[1] for c in f["coords"]]
        color = ERA_COLORS.get(f["era"], "#c8973a")

        fig_map.add_trace(go.Scattergeo(
            lat=lats, lon=lons,
            mode="markers",
            name=f["common"],
            marker=dict(
                size=10,
                color=color,
                opacity=0.85,
                line=dict(width=1.5, color="#0f0d09"),
                symbol="circle",
            ),
            hovertemplate=(
                f"<b>{f['common']}</b><br>"
                f"<i>{f['name']}</i><br>"
                f"Age: {f['age_start']}–{f['age_end']} Ma<br>"
                f"Era: {f['era']}<br>"
                f"Preservation: {f['preservation']}<extra></extra>"
            ),
            showlegend=True,
        ))

    fig_map.update_layout(
        **PLOT_BG,
        height=520,
        geo=dict(
            bgcolor="#0f0d09",
            landcolor="#1c170e",
            oceancolor="#0a0d12",
            lakecolor="#0a0d12",
            showland=True, showocean=True, showlakes=True,
            showcountries=True, countrycolor="#2a2015",
            showcoastlines=True, coastlinecolor="#3a3020",
            showframe=False,
            projection_type="natural earth",
        ),
        title=dict(
            text="Global Fossil Occurrence Localities",
            font=dict(size=14, color="#f0e2c0", family="Playfair Display, serif"),
        ),
        legend=dict(
            bgcolor="#171310", bordercolor="#2a2015", borderwidth=1,
            font=dict(size=10), itemsizing="constant",
        ),
    )
    st.plotly_chart(fig_map, use_container_width=True)

    # Location table
    st.markdown("<br>", unsafe_allow_html=True)
    section_header("Classic Field Localities")
    for f in map_fossils[:8]:
        with st.expander(f"**{f['common']}** ({f['name']}) · {f['era']}"):
            for loc in f["locations"]:
                st.markdown(f"- 📍 {loc}")
            st.markdown(f"*Preservation: {f['preservation']} · Age: {f['age_start']}–{f['age_end']} Ma*")

# ══ TAB 3 — TIMELINE ═════════════════════════════════════════════════════════
with tab3:
    section_header("Stratigraphic Ranges",
                   "Horizontal bars show the total time span of each fossil group · Dashed lines = mass extinctions")

    show_fossils = filtered if filtered else FOSSILS
    sorted_fossils = sorted(show_fossils, key=lambda x: -x["age_start"])

    fig_tl = go.Figure()

    for f in sorted_fossils:
        color = ERA_COLORS.get(f["era"], "#c8973a")
        duration = f["age_start"] - f["age_end"]
        fig_tl.add_trace(go.Bar(
            x=[duration],
            y=[f["common"]],
            base=f["age_end"],
            orientation="h",
            name=f["era"],
            marker=dict(color=color, opacity=0.70, line=dict(width=1, color=color)),
            hovertemplate=(
                f"<b>{f['common']}</b><br>"
                f"<i>{f['name']}</i><br>"
                f"{f['age_start']}–{f['age_end']} Ma ({duration} My duration)<br>"
                f"Era: {f['era']}<br>"
                f"Group: {f['group']}<extra></extra>"
            ),
            showlegend=False,
        ))

    # Era bands
    for era_info, (start, end) in [("Cenozoic",(0,66)),("Mesozoic",(66,252)),("Paleozoic",(252,541))]:
        fig_tl.add_vrect(x0=end, x1=start,
                         fillcolor=ERA_COLORS[era_info], opacity=0.035,
                         layer="below", line_width=0,
                         annotation_text=era_info, annotation_position="top",
                         annotation_font=dict(size=10, color=ERA_COLORS[era_info]))

    # Mass extinctions
    for age, label, color in [
        (252, "End-Permian extinction (96% sp.)", "#ff4444"),
        (66,  "K-Pg extinction (non-avian dinos)", "#ff8844"),
        (201, "End-Triassic extinction", "#ff6644"),
        (444, "End-Ordovician extinction", "#ff4466"),
    ]:
        if age_min <= age <= age_max:
            fig_tl.add_vline(x=age, line_color=color, line_dash="dot", line_width=1.2,
                             annotation_text=label,
                             annotation_font=dict(size=9, color=color),
                             annotation_position="top right")

    fig_tl.update_layout(
        **PLOT_BG, height=max(380, len(sorted_fossils) * 32 + 80),
        barmode="overlay",
        xaxis=dict(title="Age (Ma)", autorange="reversed",
                   gridcolor="#2a2015", linecolor="#2a2015",
                   tickfont=dict(size=10)),
        yaxis=dict(gridcolor="#2a2015", linecolor="#2a2015",
                   tickfont=dict(size=11)),
        title=dict(text="Fossil Stratigraphic Ranges · Coloured by Era",
                   font=dict(size=14, color="#f0e2c0", family="Playfair Display, serif")),
    )
    st.plotly_chart(fig_tl, use_container_width=True)

# ══ TAB 4 — ENVIRONMENTS ═════════════════════════════════════════════════════
with tab4:
    section_header("Environment Finder",
                   "Select a depositional environment to see what fossils you might expect to find")

    sel_env = st.selectbox("Depositional environment", ENVIRONMENTS, key="env_detail")
    env_results = [f for f in FOSSILS if sel_env in f["environments"]]

    if env_results:
        st.markdown(f'<div class="result-header">📍 <strong>{len(env_results)}</strong> fossil group{"s" if len(env_results)!=1 else ""} expected in <em>{sel_env}</em> settings</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        for i, f in enumerate(env_results):
            with col1 if i % 2 == 0 else col2:
                fossil_card(f, show_image=show_images)
    else:
        st.info("No fossils in the database for this environment.")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Heatmap — environments × groups
    section_header("Environment × Group Matrix",
                   "Which fossil groups occur in which environments")

    groups_all = sorted(set(f["group"] for f in FOSSILS))
    matrix = []
    for env in ENVIRONMENTS:
        row = [sum(1 for f in FOSSILS if env in f["environments"] and f["group"] == g)
               for g in groups_all]
        matrix.append(row)

    fig_hm = go.Figure(go.Heatmap(
        z=matrix, x=groups_all, y=ENVIRONMENTS,
        colorscale=[[0,"#0f0d09"],[0.4,"#5a3a10"],[1,"#c8973a"]],
        hovertemplate="Env: %{y}<br>Group: %{x}<br>Count: %{z}<extra></extra>",
        colorbar=dict(title="Count", thickness=12, len=0.7,
                      tickfont=dict(size=9, color="#d8c9a8"),
                      title_font=dict(size=10, color="#d8c9a8")),
    ))
    fig_hm.update_layout(
        **PLOT_BG, height=450,
        xaxis=dict(title="Fossil Group", tickangle=-35, gridcolor="#2a2015"),
        yaxis=dict(title="Depositional Environment", gridcolor="#2a2015"),
        title=dict(text="Fossil Occurrence Matrix — Environments × Groups",
                   font=dict(size=13, color="#f0e2c0", family="Playfair Display, serif")),
    )
    st.plotly_chart(fig_hm, use_container_width=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="display:flex;justify-content:space-between;
     font-size:10px;color:#3a2e18;padding:10px 0;
     font-family:'Source Code Pro',monospace">
  <span> FossilFinder · Field Edition · Paleontology Explorer By SERHOUDJI </span>
  <span>15 groups · 3 eras · 541 Ma · Built for field geologists</span>
</div>
""", unsafe_allow_html=True)
