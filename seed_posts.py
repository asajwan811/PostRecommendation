import sqlite3

sample_posts = [
    "How to implement authentication in a Django app.",
    "Understanding convolutional neural networks in deep learning.",
    "A beginner's guide to React components and state management.",
    "The future of artificial intelligence in healthcare.",
    "Getting started with AWS for cloud deployments.",
    "Top 10 VS Code extensions for productivity.",
    "Build a real-time chat application using WebSocket and Node.js.",
    "Secure your APIs using OAuth 2.0 and JWT.",
    "Implementing object detection using YOLOv5 and OpenCV.",
    "Deploy your ML model using Streamlit and Docker.",
    "Fine-tuning BERT for sentiment analysis on movie reviews.",
    "Automate Excel reports using Python and Pandas.",
    "Introduction to GraphQL for frontend developers.",
    "How to build an AI-powered chatbot using Rasa.",
    "Monitoring Kubernetes clusters with Prometheus and Grafana.",
    "Creating interactive dashboards with Plotly and Dash.",
    "Understanding the basics of blockchain technology.",
    "Build a blog application using Django and SQLite.",
    "Text summarization using Hugging Face Transformers.",
    "Integrating payment gateway with Django e-commerce site.",
    "Cybersecurity fundamentals for ethical hacking beginners.",
    "Deploying a FastAPI application on Heroku.",
    "Data preprocessing techniques for machine learning.",
    "Web scraping with BeautifulSoup and Selenium.",
    "Analyzing stock prices using LSTM models.",
    "Building an AI assistant using OpenAI GPT API.",
    "Multi-language support in Django applications.",
    "Creating RESTful APIs with Flask and SQLAlchemy.",
    "Face recognition system using dlib and OpenCV.",
    "Developing PWA with React and Service Workers."
]

conn = sqlite3.connect("posts.db")
cursor = conn.cursor()

for post in sample_posts:
    cursor.execute("INSERT INTO posts (content) VALUES (?)", (post,))

conn.commit()
conn.close()

print("✅ Sample posts added!")
