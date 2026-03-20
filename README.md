# 🎓 AI-Powered-Student-Assistant-Chatbot

An intelligent chatbot system designed to analyze **teacher effectiveness** using **Machine Learning + RAG (Retrieval-Augmented Generation)**.

---

## 🚀 Features

- 💬 ChatGPT-like interactive UI (Streamlit)
- 📘 RAG-based knowledge retrieval (no API required)
- 📊 Machine Learning prediction of teacher effectiveness
- 🔄 Concise & Detailed response modes
- 🌐 Web search fallback for unknown queries
- 🎛️ Dynamic user inputs (class size & student score)

---

## 🧠 How It Works

User Input →  
1️⃣ ML Prediction (if query includes "predict")  
2️⃣ Knowledge Retrieval (RAG)  
3️⃣ Rule-Based Response  
4️⃣ Web Search Fallback  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- Pickle  

---

## 📂 Project Structure

project/
│── app.py
│── train_model.py
│
├── model/
│ └── model.pkl
│
├── utils/
│ ├── ml_utils.py
│ ├── rag_utils.py
│ └── web_utils.py
│
├── data/
│ └── knowledge.txt



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
cd AI-Powered-Student-Assistant-Chatbot


2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
streamlit run app.py
