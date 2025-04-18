import sqlite3
import random

# Connect to SQLite
conn = sqlite3.connect("posts.db")
cursor = conn.cursor()

# Topics pool
topics = [
    "Python", "Django", "Flask", "Machine Learning", "AI", "Cybersecurity", "React",
    "Streamlit", "NLP", "Deep Learning", "Blockchain", "DevOps", "FastAPI", "SQL", "Cloud",
    "OpenCV", "YOLOv5", "Chatbots", "Pandas", "Data Science", "JavaScript", "TensorFlow",
    "Kubernetes", "Docker", "APIs", "Authentication", "Scraping", "Face Recognition",
    "GANs", "Data Analysis", "Transformers", "Hugging Face", "Vision AI","tableau","Generative AI", "Artificial Intelligence"
]

verbs = [
    "Learn", "Master", "Build", "Explore", "Understand", "Develop", "Get Started With",
    "Create", "Deploy", "Optimize", "Analyze", "Secure", "Test", "Implement", "Automate"
]

details = [
    "real-world projects", "step-by-step tutorials", "industry examples", "interactive dashboards",
    "production-level code", "hands-on experience", "best practices", "advanced techniques",
    "modern architecture", "cloud-native tools", "cutting-edge frameworks", "full-stack integration"
]

# Generate 1000 unique posts
posts = []
for i in range(1000):
    topic = random.choice(topics)
    verb = random.choice(verbs)
    detail = random.choice(details)
    post = f"{verb} {topic} with {detail}."
    posts.append(post)

# Insert into DB
for post in posts:
    cursor.execute("INSERT INTO posts (content) VALUES (?)", (post,))

conn.commit()
conn.close()

print("✅ Successfully added 1000+ AI & tech-related posts!")
