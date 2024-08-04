#import necessary libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#load the datasets
credits = pd.read_csv(r"C:\Users\91983\OneDrive\Desktop\movies\tmdb_5000_credits.csv")
movies = pd.read_csv(r"C:\Users\91983\OneDrive\Desktop\movies\tmdb_5000_movies.csv")

#fill the missing values in the 'overview' column with an empty string
movies['overview'] = movies['overview'].fillna(" ")

#initialize the TF-IDF vectorizer with english stop words
tfidf = TfidfVectorizer(stop_words = "english")

#fit and transform the 'overview' column to create the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(movies['overview'])

#compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix , tfidf_matrix)

#create a series with movie titles
indices = pd.Series(movies.index, index=movies['original_title']).drop_duplicates()

#function to get movie recommendations based on the title
def get_recommendations(title, cosine_sim = cosine_sim):
    print(f"Top 10 Suggestions for '{title}': \n")
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    sim_index = [i[0] for i in sim_scores]
    print(movies["original_title"].iloc[sim_index])

get_recommendations('Spider-Man 3')