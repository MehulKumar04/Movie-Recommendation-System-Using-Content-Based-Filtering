🎬 Movie Recommendation System Using Content-Based Filtering

This project is a Movie Recommendation System that suggests movies similar to the ones you like using Content-Based Filtering. It analyzes movie features such as genres, cast, director, and plot keywords to find and recommend movies with similar content.

🧠 Project Overview

Content-based recommendation systems work by comparing the attributes of items rather than user behavior. This system uses Cosine Similarity to measure how similar two movies are based on their textual features.

By providing a movie title as input, the system returns a list of movies that share similar content characteristics.

🚀 Features

Suggests similar movies based on content attributes.

Uses TF-IDF Vectorization and Cosine Similarity for similarity scoring.

Simple and efficient recommendation logic.

Easy-to-understand Python implementation.

🧩 Tech Stack

Programming Language: Python

Libraries Used:

pandas — data manipulation

numpy — numerical operations

scikit-learn — TF-IDF vectorization & cosine similarity

nltk (optional) — text preprocessing

📁 Dataset

The system uses the TMDB movie dataset (or any similar dataset) containing features like:

Title

Overview

Genre

Cast

Director

You can use a dataset like tmdb_5000_movies.csv
 and tmdb_5000_credits.csv
 from Kaggle.

⚙️ Installation & Setup

Clone this repository:

git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system


Install dependencies:

pip install -r requirements.txt


Run the script:

python main.py


Enter a movie title to get recommendations!

🧮 How It Works

Data Preprocessing:
Clean and combine relevant features (e.g., genre, cast, overview).

Feature Extraction:
Convert text data into vectors using TF-IDF Vectorizer.

Similarity Calculation:
Use Cosine Similarity to find movies with the highest similarity score.

Recommendation Output:
Return top N similar movies for a given input title.

💡 Example Output

Input: “Inception”
Recommendations:

Interstellar

The Prestige

Memento

Shutter Island

The Matrix

📊 Future Enhancements

Add Collaborative Filtering for hybrid recommendations.

Integrate Flask or Streamlit for a web interface.

Include poster images and additional metadata in the output.

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or raise an issue.

🧾 License

This project is licensed under the MIT License — see the LICENSE
 file for details.

🌟 Acknowledgements

TMDB Movie Dataset

Scikit-learn Documentation
