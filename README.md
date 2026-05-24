# 🇮🇳 India Geo Analytics Dashboard

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Geospatial-purple?style=for-the-badge&logo=plotly)
![Analytics](https://img.shields.io/badge/Analytics-Geospatial-green?style=for-the-badge)
![Dashboard](https://img.shields.io/badge/Dashboard-Interactive-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

</p>

---

# 🌐 Live Application

🚀 **Streamlit Deployment:**  
https://india-geo-analytics-1135.streamlit.app/

---

# 📌 Project Overview

The **India Geo Analytics Dashboard** is an interactive geospatial analytics system built using:

- Streamlit
- Plotly Mapbox
- Pandas
- PyYAML
- Python

The application enables users to explore **state-wise district-level indicators across India** through interactive geospatial visualization.

Users can:
- select a state
- compare district-level metrics
- analyze geographic distributions
- identify regional patterns visually

The system transforms structured tabular datasets into an interactive analytical dashboard using geospatial encoding techniques.

---

# 🎯 What This Dashboard Actually Does

The dashboard performs:

```text
State Selection
        ↓
District Filtering
        ↓
Parameter Selection
        ↓
Geospatial Visualization
        ↓
Interactive Analytics
```

Users can:

1. Select a state (or Overall India)
2. Choose:
   - Bubble Size Metric
   - Bubble Color Metric
3. Generate an interactive geospatial visualization
4. Explore district-level regional patterns

---

# 📊 Understanding The Visualization

Each point on the map represents a district.

The visualization uses multiple visual dimensions simultaneously.

| Visual Feature | Meaning |
|---|---|
| Bubble Size | Primary selected metric |
| Bubble Color | Secondary selected metric |
| Geographic Position | District location |

---

## 📌 Example Interpretation

Suppose:

- Bubble Size Metric = Population
- Bubble Color Metric = Literacy Rate

Then:

- Larger bubbles → districts with higher population
- Darker color intensity → districts with higher literacy rate
- Geographic clustering → regional concentration patterns

This enables users to identify:

- socio-economic disparities
- urban concentration
- digital infrastructure distribution
- literacy distribution patterns
- regional inequality
- demographic clustering

through a single interactive visualization.

---

# 🧠 Analytical Value

This project demonstrates how geospatial visualization systems can convert structured datasets into:

- interactive insights
- exploratory analytics tools
- geographic intelligence dashboards
- regional comparison systems

The architecture forms a foundation for future:
- GIS analytics systems
- ML-powered geospatial intelligence
- policy analytics dashboards
- population intelligence systems
- smart-city analytics applications

---

# 🏗️ System Architecture

```text
Dataset (india.csv)
        ↓
Data Processing Layer (Pandas / NumPy)
        ↓
State & Parameter Filtering
        ↓
Geospatial Visualization Engine (Plotly Mapbox)
        ↓
Streamlit Dashboard Application
        ↓
Interactive Browser-Based Analytics
```

---

# ⚙️ Architecture Breakdown

## 📂 Data Layer

The system uses:

```text
india.csv
```

which contains:
- district-level indicators
- geographic coordinates
- numerical attributes
- state mappings

---

## 🧹 Data Processing Layer

Implemented using:

- Pandas
- NumPy

Responsibilities:
- state filtering
- parameter extraction
- district segmentation
- user-selected feature handling

---

## 🌍 Geospatial Visualization Layer

Built using:

- Plotly Mapbox

Responsible for:
- district plotting
- geographic rendering
- bubble encoding
- color scaling
- interactive exploration

---

## 🖥️ Streamlit UI Layer

Responsible for:
- sidebar interaction
- state selection
- parameter selection
- dashboard rendering
- visualization updates

---

# ✨ Core Features

## 🇮🇳 State-Wise District Analytics

Users can:
- select individual states
- compare district-level indicators
- analyze geographic distributions

---

## 🌍 Interactive Geospatial Visualization

- Mapbox-powered district visualization
- Interactive hover exploration
- Dynamic rendering

---

## 📊 Multi-Dimensional Encoding

The dashboard simultaneously encodes:

- size
- color
- location

to visualize multiple variables in a single analytical view.

---

## ⚡ Dynamic Dashboard Controls

Sidebar controls enable:
- real-time parameter selection
- state filtering
- interactive exploration workflows

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Dashboard framework |
| Plotly | Geospatial visualization |
| Pandas | Data processing |
| NumPy | Numerical computation |
| PyYAML | Configuration management |

---

# 📂 Project Structure

```text
India-geo-analytics-dashboard/
|-- app.py
|-- config.yaml
|-- india.csv
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- src/
|   |-- config.py
|   |-- data.py
|   |-- ui.py
|   `-- visualization.py
`-- .venv/
```

---

# 🎮 How To Use

## Step 1

Select a state:

- Overall India
- or any individual Indian state

---

## Step 2

Choose:

- Bubble Size Metric
- Bubble Color Metric

Example metrics:
- Population
- Literacy Rate
- Sex Ratio
- Households with Internet

---

## Step 3

The dashboard updates automatically when filters are changed.

---

## Step 4

Analyze:
- district distributions
- bubble size variation
- color intensity patterns
- geographic clustering

---

# 📊 Engineering Highlights

- Interactive geospatial analytics system
- Plotly Mapbox integration
- Multi-dimensional data encoding
- Dynamic state-wise filtering
- User-driven exploration workflows
- District-level geographic visualization
- Streamlit cloud deployment
- Interactive dashboard architecture
- Real-time visualization rendering

---

# ⚙️ Local Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/RudraTyagi1135/India-geo-analytics-dashboard.git
cd India-geo-analytics-dashboard
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The application is deployed using:

- Streamlit Cloud

Deployment link:

https://india-geo-analytics-1135.streamlit.app/

---

# 📈 Potential Future Improvements

Planned enhancements include:

- Time-series analytics support
- Real-world API integration
- ML-based geographic clustering
- Geographic anomaly detection
- Backend API integration
- AWS cloud deployment
- Dynamic Mapbox styling
- Geospatial ML pipelines
- Real-time analytics ingestion

---

# 🎯 What This Project Demonstrates

This project demonstrates practical understanding of:

- Geospatial analytics systems
- Interactive dashboard engineering
- Plotly Mapbox visualization
- Multi-dimensional data encoding
- User-driven analytics workflows
- Geographic intelligence visualization
- Production dashboard deployment
- Interactive analytics architecture

---

# 📌 Strategic Engineering Value

This project demonstrates significantly more engineering depth than static notebook visualizations because it includes:

- interactive deployment
- real-time user-driven filtering
- scalable visualization workflows
- geospatial analytics systems
- multi-variable encoding architecture
- production-ready dashboard design

---

# 📸 Recommended Screenshot Section

Add application screenshots here for stronger recruiter impact:

```markdown
![Dashboard Overview](your-image-link)
![India Visualization](your-image-link)
![State Analytics](your-image-link)
```

---

# 👨‍💻 Author

## Rudra Tyagi

### Focus Areas

- ML Systems
- MLOps
- AI Infrastructure
- Geospatial Analytics Systems
- Data Analytics Engineering

---

# ⭐ Recruiter Notes

This repository demonstrates:

- Geospatial analytics engineering
- Interactive dashboard development
- Plotly visualization systems
- Geographic intelligence workflows
- User-driven analytical exploration
- Production deployment capability

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
