import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="AI Virtual Interviewer", layout="centered")

st.title(" AI Virtual Interviewer")
st.write("Practice your interview skills by answering randomly selected questions. Get instant feedback based on your responses!")

# Load questions from CSV
def load_questions(file_path='questions_dataset.csv'):
    try:
        df = pd.read_csv(file_path)
        if 'question' not in df.columns:
            st.error("❌ 'question' column not found in the CSV.")
            return []
        return df['question'].tolist()
    except Exception as e:
        st.error(f"❌ Error loading CSV file: {e}")
        return []

# Select random questions
def select_random_questions(all_questions, num_questions=5):
    return random.sample(all_questions, num_questions)

# Plot results
def plot_results(questions, scores):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(questions, scores, color='skyblue')
    ax.set_xlabel('Score (out of 10)')
    ax.set_title('Interview Performance')
    ax.set_xlim(0, 10)
    ax.invert_yaxis()
    st.pyplot(fig)

# Generate feedback
def generate_feedback(scores):
    total = sum(scores)
    average = total / len(scores)
    feedback = f"🎯 **Total Score:** {total}/50\n📊 **Average Score:** {average:.2f}/10\n\n"
    if average >= 8:
        feedback += "✅ Excellent performance!"
    elif average >= 6:
        feedback += "⚡ Good performance, but there are areas to improve."
    else:
        feedback += "🔴 Needs improvement. Keep practicing!"
    return feedback

# Load and store questions
questions = load_questions()
if questions:
    if "selected_questions" not in st.session_state:
        st.session_state.selected_questions = select_random_questions(questions)

    selected_questions = st.session_state.selected_questions

    st.subheader("📋 Answer the following questions:")
    answers = []
    for i, question in enumerate(selected_questions, 1):
        answer = st.text_area(f"Q{i}: {question}", height=100, key=f"q{i}")
        answers.append(answer.strip())

    if st.button("✅ Finish Interview"):
        if '' in answers:
            st.warning("⚠️ Please answer all questions before submitting.")
        else:
            scores = [random.randint(6, 10) for _ in selected_questions]  # Placeholder scoring
            plot_results(selected_questions, scores)
            st.markdown("### 📄 Feedback")
            st.markdown(generate_feedback(scores))

    if st.button("🔄 Restart Interview"):
        st.session_state.clear()
        st.experimental_rerun()
else:
    st.warning("No questions loaded. Please check your CSV file.")
