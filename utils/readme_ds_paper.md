# DS Paper Universe

<div align="center">

![DS Paper Universe](https://img.shields.io/badge/DS%20Paper%20Universe-Literature%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A comprehensive literature retrieval and visualization platform powered by network analysis**

[Demo Video](https://www.youtube.com/watch?v=vBVPZlLWp8o&t=1s) • [Report Bug](../../issues) • [Request Feature](../../issues)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Screenshots](#-screenshots)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

DS Paper Universe is an intelligent literature analysis platform that helps researchers discover insights from academic papers through interactive visualizations and network analysis. The platform processes literature data from academic databases and provides:

- 📊 Interactive visualizations of publication trends
- 🕸️ Keyword and citation co-occurrence networks
- 👥 Author collaboration analysis
- 🌍 Geographic distribution of research
- 📈 Impact factor rankings

---

## ✨ Key Features

### 🔍 Smart Literature Search
- Fast keyword-based paper retrieval
- Real-time filtering and sorting
- Detailed publication metadata display

### 📊 Data Visualization
- **Author Analysis**: Affiliation rankings, productivity metrics, collaboration networks
- **Publication Trends**: Yearly publication patterns, source title analysis
- **Impact Metrics**: Citation rankings, influence factor analysis
- **Geographic Insights**: World heatmap of author distributions

### 🕸️ Network Analysis
- **Keyword Co-occurrence Network**: Discover research themes and connections
- **Paper Citation Network**: Understand reference relationships
- Dynamic force-directed graph layouts with interactive exploration

### 🎨 User Interface
- Clean, modern Bootstrap 5 design
- Responsive layout for all devices
- Intuitive navigation with sidebar menu
- Sortable data tables

---

## 📸 Screenshots

<div align="center">
<img src="path/to/homepage-screenshot.png" alt="Homepage" width="45%">
<img src="path/to/network-screenshot.png" alt="Network View" width="45%">
</div>

---

## 🛠️ Technology Stack

### Backend
- **Flask** - Web framework
- **Pandas** - Data processing
- **NetworkX** - Graph analysis
- **GeoPandas** - Geographic data handling

### Frontend
- **Bootstrap 5** - UI framework
- **ECharts/PyEcharts** - Interactive visualizations
- **jQuery** - DOM manipulation

### Visualization
- **Matplotlib** - Static plots
- **Seaborn** - Statistical graphics
- **PyEcharts** - Interactive charts

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ds-paper-universe.git
cd ds-paper-universe
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
```txt
Flask==2.3.0
pandas==2.0.0
networkx==3.1
geopandas==0.13.0
matplotlib==3.7.1
seaborn==0.12.2
pyecharts==2.0.3
icecream==2.1.3
tqdm==4.65.0
```

### Step 4: Prepare Data

Place your CSV data files in the `database/` folder:
- `literature_data.csv`
- `author_data.csv`
- `author_publication_data.csv`

**CSV format requirements:**
- Literature data: Title, Year, Source title, Author Keywords, References, Cited by, EID, etc.
- Author data: Author(s) ID, Author Name, Affiliations, country
- Publication data: Author(s) ID, PublicationEID

---

## 🚀 Quick Start

### Development Mode

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

### Production Mode (Gunicorn)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🌐 Deployment

### Option 1: Home Server Deployment

#### Using systemd (Linux)

1. **Create service file:**

```bash
sudo nano /etc/systemd/system/ds-paper-universe.service
```

2. **Add configuration:**

```ini
[Unit]
Description=DS Paper Universe Flask App
After=network.target

[Service]
User=youruser
WorkingDirectory=/path/to/ds-paper-universe
Environment="PATH=/path/to/ds-paper-universe/venv/bin"
ExecStart=/path/to/ds-paper-universe/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

3. **Enable and start:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable ds-paper-universe
sudo systemctl start ds-paper-universe
sudo systemctl status ds-paper-universe
```

#### Configure Nginx Reverse Proxy

```bash
sudo nano /etc/nginx/sites-available/ds-paper-universe
```

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        alias /path/to/ds-paper-universe/static;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/ds-paper-universe /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Option 2: Docker Deployment

1. **Create Dockerfile:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

2. **Build and run:**

```bash
docker build -t ds-paper-universe .
docker run -d -p 5000:5000 -v $(pwd)/database:/app/database ds-paper-universe
```

### Option 3: Docker Compose

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./database:/app/database
      - ./static:/app/static
    environment:
      - FLASK_ENV=production
    restart: always
```

```bash
docker-compose up -d
```

---

## 📖 Usage Guide

### 1. Search for Literature

- Enter keywords in the search box on the homepage
- View results in an organized table
- Sort by title, year, or source

### 2. Explore Visualizations

Click "Visualize" in the sidebar to generate:
- Author affiliation charts
- Publication productivity rankings
- Geographic heatmaps
- Citation and impact factor rankings
- Yearly publication trends

### 3. Analyze Networks

**Keyword Network:**
- View keyword co-occurrence patterns
- Identify research themes
- Explore connections between topics

**Paper Network:**
- Analyze citation relationships
- Discover influential papers
- Track knowledge flow

### 4. Customize Analysis

Modify parameters in `app.py`:
```python
top_n_keyword = 300  # Number of keywords in network
top_n_paper = 10     # Number of papers in network
```

---

## 📁 Project Structure

```
ds-paper-universe/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── database/                   # Data files
│   ├── literature_data.csv
│   ├── author_data.csv
│   ├── author_publication_data.csv
│   ├── keyword/               # Generated keyword data
│   └── paper/                 # Generated paper data
├── static/                    # Static assets
│   ├── css/
│   ├── image/
│   └── images/vision/        # Generated visualizations
├── templates/                 # HTML templates
│   ├── index.html
│   ├── search.html
│   ├── Papers.html
│   ├── visualize.html
│   ├── keywordsNetwork.html
│   ├── paperNetwork.html
│   └── direction.html
└── utils/                     # Utility modules
    ├── exploratory_data_analysis.py
    ├── social_network.py
    └── visualization/
        ├── author_analysis.py
        ├── publication_analysis.py
        ├── network_visu.py
        └── network_visu_paper.py
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- ECharts for powerful visualization capabilities
- Flask community for excellent documentation

---

## 📞 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/ds-paper-universe](https://github.com/yourusername/ds-paper-universe)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Your Name]

</div>
