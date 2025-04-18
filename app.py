import streamlit as st
import sqlite3
import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Connect to SQLite DB
conn = sqlite3.connect("posts.db", check_same_thread=False)
cursor = conn.cursor()

# Create posts table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
''')
conn.commit()

# Preprocess text using spaCy
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Fetch posts from DB and preprocess
def fetch_and_preprocess_posts():
    df = pd.read_sql("SELECT * FROM posts", conn)
    df['processed'] = df['content'].apply(preprocess)
    return df

# Recommend posts
def recommend(query, df, top_n=3):
    query_proc = preprocess(query)
    texts = df['processed'].tolist()
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts + [query_proc])
    cosine_sim = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    return df.iloc[top_indices], cosine_sim[top_indices]

# Add new post to DB
def add_post(content):
    cursor.execute("INSERT INTO posts (content) VALUES (?)", (content,))
    conn.commit()

# ----------------- Streamlit UI ------------------


st.title("🧠 Intelligent Post Recommendation System")
menu = ["Recommend", "Add Post", "View All Posts"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Recommend":
    st.subheader("🔍 Recommend Similar Posts")
    user_query = st.text_area("Enter your post/query:")
    if st.button("Get Recommendations"):
        if user_query.strip():
            df = fetch_and_preprocess_posts()
            if df.empty:
                st.warning("No posts available. Please add some posts first.")
            else:
                results, scores = recommend(user_query, df)
                st.success("Top Recommendations:")
                for i, (idx, row) in enumerate(results.iterrows()):
                    st.markdown(f"**{i+1}. {row['content']}**  \nScore: {scores[i]:.2f}")
                    st.write(f"https://www.google.com/search?q={row['content'].replace(' ', '+')}")
        else:
            st.warning("Please enter a query.")

elif choice == "Add Post":
    st.subheader("➕ Add a New Post")
    new_post = st.text_area("Post Content:")
    if st.button("Add to Database"):
        if new_post.strip():
            add_post(new_post)
            st.success("Post added successfully!")
        else:
            st.warning("Post cannot be empty.")

elif choice == "View All Posts":
    st.subheader("📋 All Posts in Database")
    df = pd.read_sql("SELECT * FROM posts", conn)
    st.dataframe(df[['id', 'content']])

