import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
df = pd.read_csv('product_data.csv')

# Create a TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['product_description'])

# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

# Make recommendations
def recommend_products(target_product, num_recommendations=5):
    product_index = df[df['product_name'] == target_product].index[0]
    similar_products = similarity_matrix[product_index].argsort()[::-1][1:num_recommendations+1]
    return df.iloc[similar_products]['product_name'].tolist()

recommendations = recommend_products('Product A', num_recommendations=5)
print(recommendations)