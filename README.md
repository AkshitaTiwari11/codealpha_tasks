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

## 📈 Task 2: 
