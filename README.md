# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python**, **Scikit-learn**, and **Streamlit**. The application recommends similar movies by analyzing movie descriptions using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Live Demo

🔗 **Streamlit App:** https://your-streamlit-link.streamlit.app

> *(Replace with your deployed Streamlit URL after deployment.)*

---

## 📌 Project Overview

This project demonstrates a simple content-based recommendation engine. Instead of relying on user ratings, it compares movie descriptions to identify similar movies and provides personalized recommendations based on textual similarity.

---

## ✨ Features

- 🎬 Recommend similar movies instantly
- 📖 Uses movie descriptions for recommendations
- 🔍 TF-IDF Vectorization for feature extraction
- 📊 Cosine Similarity to measure movie similarity
- ⚡ Interactive Streamlit web application
- 🖥️ Beginner-friendly recommendation system

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📂 Project Structure

```
Movie_Recommendation/
│
├── Movie_Recommendation.ipynb
├── app.py
├── movie_data.pkl
├── similarity_matrix.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Create a movie dataset containing movie titles and descriptions.
2. Convert descriptions into numerical vectors using TF-IDF.
3. Calculate similarity scores using Cosine Similarity.
4. Select a movie from the Streamlit interface.
5. Display the Top 5 most similar movie recommendations.

---

## 📊 Sample Recommendation

**Selected Movie**

```
Interstellar
```

**Recommended Movies**

| Movie | Similarity Score |
|--------|-----------------:|
| The Martian | 0.662 |
| Avatar | 0.445 |
| Arrival | 0.414 |
| The Matrix | 0.210 |
| Inception | 0.197 |

> *Similarity scores may vary slightly depending on the Scikit-learn version.*

---

## ▶️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Supriyaraj13/Movie-Recommendation-System
```

### 2️⃣ Navigate to the project

```bash
cd Movie_Recommendation
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

- Add a larger movie dataset
- Include movie posters
- Search movies by keyword
- Filter recommendations by genre
- Hybrid recommendation system using user ratings

---

## 👩‍💻 Author

**Supriya Raj**

GitHub: https://github.com/Supriyaraj13