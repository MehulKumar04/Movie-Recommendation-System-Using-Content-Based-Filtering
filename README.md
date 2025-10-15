# 🎬 Movie Recommendation System Using Content-Based Filtering

This project is a **Movie Recommendation System** that suggests movies similar to the ones you like using **Content-Based Filtering**. It analyzes movie features such as **genres, cast, director, and plot keywords** to find and recommend movies with similar content.  

---

## 🧠 Project Overview

Content-based recommendation systems work by comparing the **attributes of items** rather than user behavior.  
This system uses **Cosine Similarity** to measure how similar two movies are based on their textual features.  

By providing a movie title as input, the system returns a list of movies that share similar content characteristics.

---

## 🚀 Features

- Suggests similar movies based on content attributes  
- Uses **TF-IDF Vectorization** and **Cosine Similarity** for similarity scoring  
- Simple and efficient recommendation logic  
- Easy-to-understand Python implementation  

---

## 🧩 Tech Stack

- **Programming Language:** Python  
- **Libraries Used:**  
  - `pandas` — data manipulation  
  - `numpy` — numerical operations  
  - `scikit-learn` — TF-IDF vectorization & cosine similarity  
  - `nltk` (optional) — text preprocessing  

---

## 📁 Dataset

The system uses the **TMDB movie dataset** (or any similar dataset) containing features like:  
- Title  
- Overview  
- Genre  
- Cast  
- Director  

You can use a dataset like [`tmdb_5000_movies.csv`](https://www.kaggle.com/tmdb/tmdb-movie-metadata) and [`tmdb_5000_credits.csv`](https://www.kaggle.com/tmdb/tmdb-movie-metadata) from Kaggle.

---

## ⚙️ Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
