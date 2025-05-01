#  AI Virtual Interviewer

Welcome to **AI Virtual Interviewer** – a smart, text-based interview simulation tool designed to help job seekers and students practice interview questions, receive feedback, and improve their confidence.

This project uses **Natural Language Processing (NLP)** and **semantic similarity models** to analyze and score user responses to commonly asked interview questions.

---

## 📌 Project Objective

The goal is to simulate real-world interview experiences through a user-friendly interface that:
- Presents randomized interview questions
- Accepts text-based answers from the user
- Evaluates the response based on relevance, sentiment, and clarity
- Provides constructive feedback and a performance score

---

## 🧠 How It Works

1. A question is randomly selected from a predefined list.
2. The user types their answer in the input box.
3. The system:
   - Processes the answer using `spaCy` and `TextBlob`
   - Evaluates relevance using `Sentence-BERT`
   - Checks tone/sentiment
4. Feedback is generated:
   - A score (e.g., 78/100)
   - Suggestions for clarity or improvement

---

## 🛠️ Built With

- **Python 3.9+**
- **Streamlit** – for building the web interface
- **TextBlob** – for sentiment analysis and grammar checking
- **spaCy** – for text preprocessing
- **Sentence-Transformers (BERT)** – for semantic similarity
- **Optional**: `language-tool-python`, `transformers`, `openai`

---

## 🚀 Getting Started

📷 Screenshots
![Screenshot from 2025-05-01 23-50-24](https://github.com/user-attachments/assets/5dea616a-93d3-4000-a64f-bbdf368003b0)
![Screenshot from 2025-05-01 23-50-31](https://github.com/user-attachments/assets/2d554cae-2887-494e-9a10-0362973f23d5)

**Output**
![Screenshot from 2025-05-01 23-50-15](https://github.com/user-attachments/assets/ea0aed72-a949-4322-af23-67e00f506d27)


💡 Features
📋 Dynamic question generation

✍️ Text-based user input

🤖 NLP-based answer evaluation

📊 Scoring with feedback

🧠 Semantic understanding using Sentence-BERT

🔍 Sentiment and grammar analysis

🔄 Easy deployment via Streamlit

🧪 Sample Questions Used
Tell me about yourself

What are your strengths?

How do you handle criticism?

Why do you want this job?

Tell me about a time you led a team

(Add or modify questions in questions.json or questions.txt)

🧱 Folder Structure

ai-virtual-interviewer/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── questions.json        # List of interview questions
└── utils.py              # Optional helper functions
🌐 Live Demo: 
🌟 https://aivirtualintervieweredunetinternship-5rvkuhx86etuhtpfhqrpx4.streamlit.app/

📌 Future Improvements
🎤 Add speech input using SpeechRecognition

🧠 Integrate GPT for advanced feedback

🧾 Track user session history and progress

😃 Emotion analysis from webcam (OpenCV)

🌐 Add resume-based question tailoring

🤝 Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

📫 Contact
Author: Settipalle Pradeep Reddy
Email: pradeepreddysettipalle@gmail.com
