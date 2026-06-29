# CodeAlpha Internship Tasks

Welcome to my repository for the CodeAlpha Internship! This repository contains my completed technical tasks, showcasing my approach to data collection, analysis, and clean engineering practices.

---

## 📊 Task 1: Web Scraper (Books to Scrape)
A Python-based web scraper that extracts book titles and pricing from an e-commerce site, cleans currency encoding anomalies, and exports the data to a structured CSV file.

### 🛠️ Technologies Used
* **Python 3.14**
* **BeautifulSoup4** (HTML Parsing)
* **Requests** (HTTP Requests)
* **Pandas** (Data Manipulation & Exporting)

### 🚀 Technical Challenges & Solutions
* **The Encoding Bug:** Encountered character misinterpretations (`Â£`) during currency parsing due to standard console encoding differences. 
* **The Solution:** Implemented a robust string replacement logic (`.replace('Â£', '$').replace('£', '$')`) to format all prices into clean, uniform USD values before exporting.

---

## 🔍 Task 2: Exploratory Data Analysis (EDA)

A data profiling script designed to investigate the structural integrity, quality, and core metrics of the raw web-scraped dataset. It automates data preprocessing and outputs statistical summaries directly to the terminal console to validate data before visualization or downstream pipelines.

### 🛠️ Technologies Used
* **Python 3.14**
* **Pandas** (Data Inspection, Manipulation & Mathematical Summary)

### 🚀 Technical Challenges & Solutions
* **The Float Casting Bug:** Raw data from the CSV originally contained string formatting, symbols, and whitespace, which threw execution exceptions during standard mathematical analysis blocks.
* **The Solution:** Implemented a robust data type-casting step using `.str.replace()` and `.astype(float)` to isolate numeric arrays, enabling seamless generation of foundational metrics such as count, mean, and standard deviation.

---

## 📉 Task 3: Data Visualization Dashboard

An interactive visualization dashboard built to clean and analyze the e-commerce book data harvested in Task 1. This script parses raw records and dynamically creates statistical distributions and ranking charts to uncover product insights.

### 🛠️ Technologies Used
* **Python 3.14**
* **Pandas** (Data Manipulation)
* **Matplotlib** (Plot Window Layouts)
* **Seaborn** (Statistical Data Visualization Density Plots)

### 📊 Dashboard Features
* **Price Distribution Analytics:** Implements a Seaborn Kernel Density Estimate (KDE) histogram to map out market price frequencies.
* **Top 5 Rankings:** Dynamically processes and displays horizontal bar charts identifying the most premium pricing thresholds.

### 🚀 Technical Challenges & Solutions
* **The Deprecation Warning:** Ran into syntax notices regarding explicit `hue` attributes and unmapped tick coordinates while managing categorical bar labels.
* **The Solution:** Patched the pipeline by defining `hue='Book Title'`, suppressing unnecessary legend tags with `legend=False`, and explicitly setting tick locations using `axes[1].set_yticks()` before drawing labels. This eliminated all terminal alerts.
