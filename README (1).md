# FossilFinder · Field Edition

> *"Reading the record of life written in stone since the dawn of time"*

**A field paleontology web application for fossil identification, biostratigraphy, and geologic timeline exploration.**

Built by **Serhoudji** · Petroleum Geology · Algeria

🌐 **Live App:** [fossilfinder.streamlit.app](https://fossilfinder-g8q9axqcn9a9wozvd6clty.streamlit.app)

---

## What is FossilFinder?

FossilFinder is an interactive reference tool designed for **field geologists, geology students, and paleontology enthusiasts**. It allows you to explore 15 major fossil groups filtered by geologic age, depositional environment, preservation quality, and taxonomic group.

Each fossil entry includes:
- A specimen photograph
- Detailed field description
- Fun and memorable field fact
- Biostratigraphic significance for field use
- Known global occurrence localities
- Depositional environment tags

---

## Features

### Fossil Gallery
Browse all 15 fossil groups with full descriptions, field observations, and biostratigraphic notes. Filter by era, environment, preservation quality, or search by name. Discover a random fossil with one click.

### Global Distribution Map
An interactive world map showing the principal field localities for each fossil group, coloured by geologic era — Paleozoic, Mesozoic, and Cenozoic.

### Stratigraphic Timeline
A visual range chart showing the total temporal extent of each fossil group across 541 million years of Earth history, with mass extinction markers at the End-Permian, K-Pg, and End-Triassic boundaries.

### Environment Finder
Select a depositional environment — marine shallow, reef, terrestrial, fluvial, and more — and instantly see which fossil groups are typically encountered there. Includes an Environment × Group occurrence heatmap matrix.

---

## Fossil Groups Covered

| Fossil | Era | Preservation |
|--------|-----|-------------|
| Trilobita (Trilobite) | Paleozoic | Excellent |
| Ammonoidea (Ammonite) | Mesozoic | Excellent |
| Graptolithina (Graptolite) | Paleozoic | Good |
| Brachiopoda (Brachiopod) | Paleozoic | Excellent |
| Foraminifera | Cenozoic | Excellent |
| Echinoidea (Sea Urchin) | Mesozoic | Good |
| Belemnoidea (Belemnite) | Mesozoic | Good |
| Crinoidea (Sea Lily) | Paleozoic | Good |
| Rugosa (Rugose Coral) | Paleozoic | Good |
| Selachii (Shark Tooth) | Cenozoic | Excellent |
| Pollen and Spores (Palynomorphs) | Cenozoic | Excellent |
| Dinosauria (Dinosaur) | Mesozoic | Rare |
| Nummulites (Nummulite) | Cenozoic | Excellent |
| Ichthyosauria (Ichthyosaur) | Mesozoic | Rare |
| Mammalia (Fossil Mammal) | Cenozoic | Variable |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web application framework |
| [Plotly](https://plotly.com) | Interactive charts, maps, and heatmaps |
| Python | Core language |

No database, no backend, no cloud infrastructure — just Python, deployed for free on Streamlit Cloud.

---

## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/serhoudjisouhil93-alt/fossilfinder.git
cd fossilfinder

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## Project Structure

```
fossilfinder/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── images/
    ├── trilobite.jpg
    ├── ammonite.jpg
    ├── graptolite.jpg
    ├── brachiopod.jpg
    ├── foraminifera.jpg
    ├── echinoid.jpg
    ├── belemnite.jpg
    ├── crinoid.jpg
    ├── rugose_coral.jpg
    ├── shark_tooth.jpg
    ├── palynomorphs.jpg
    ├── dinosaur.jpg
    ├── nummulite.jpg
    ├── ichthyosaur.jpg
    └── mammal.jpg
```

---

## About the Author

**Serhoudji** is a petroleum geology student from Algeria, building practical tools that bridge fundamental geology, paleontology, and data science.

This project was built as part of a portfolio demonstrating skills in:
- Applied geology and paleontology
- Python programming and data visualization
- Web application development
- Biostratigraphy and sedimentary environments

---

## Roadmap

- [ ] Field identification key (step-by-step identification guide)
- [ ] Size reference for each fossil group
- [ ] Confusion species warnings (what each fossil is mistaken for)
- [ ] Regional filter for North Africa and Algeria
- [ ] Quiz mode for field preparation
- [ ] Downloadable PDF field cards
- [ ] Additional fossil groups

---

## License

This project is open source and available under the [MIT License](LICENSE).

Fossil images are sourced from public domain and Creative Commons licensed collections.

---

*FossilFinder v2.0 · Field Edition · 15 fossil groups · 3 geologic eras · 541 Ma of Earth history*
