#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Step 1: Load questions from CSV
def load_questions(file_path='questions_dataset.csv'):
    """ Load questions from a CSV file into a list """
    try:
        df = pd.read_csv(file_path)
        if 'question' not in df.columns:
            print("Error: 'question' column not found in CSV file.")
            return []
        return df['question'].tolist()
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

# Step 2: Select random questions
def select_random_questions(all_questions, num_questions=5):
    """ Select a random sample of questions from the list """
    return random.sample(all_questions, num_questions)

# Step 3: Display interview questions and collect answers
def display_interview(questions):
    """ Display the questions and collect answers from the user """
    answers = []
    answer_widgets = []

    for question in questions:
        question_widget = widgets.Label(value=f"Q: {question}")
        answer_widget = widgets.Textarea(
            placeholder="Type your answer here...",
            layout=widgets.Layout(width='600px', height='100px')
        )
        
        display(question_widget)
        display(answer_widget)
        answer_widgets.append(answer_widget)

    return answer_widgets

# Step 4: Plot results (bar chart)
def plot_results(questions, scores):
    """ Plot a bar chart for the interview results """
    print("Plotting results...")  # Debugging statement
    plt.figure(figsize=(10, 6))
    plt.barh(questions, scores, color='skyblue')
    plt.xlabel('Score (out of 10)')
    plt.title('Interview Performance')
    plt.xlim(0, 10)
    plt.gca().invert_yaxis()
    plt.show()

# Step 5: Generate feedback based on scores
def generate_feedback(scores):
    """ Generate feedback based on scores """
    total = sum(scores)
    average = total / len(scores)
    
    feedback = f"🎯 Total Score: {total}/50\n 📊 Average Score: {average:.2f}/10\n\n"

    
    
    if average >= 8:
        feedback += "✅ Excellent performance!"
    elif average >= 6:
        feedback += "⚡ Good performance, but there are areas to improve."
    else:
        feedback += "🔴 Needs improvement. Keep practicing!"
    
    return feedback

# Step 6: Handle the interview process and finish button click
def start_interview():
    """ Start the interview process """
    
    # Load questions from the CSV
    questions = load_questions()
    if not questions:
        print("No questions loaded from the CSV.")
        return
    
    # Select 5 random questions
    selected_questions = select_random_questions(questions)
    
   # print(f"Selected Questions: {selected_questions}")  # Debugging statement
    
    # Display UI to collect answers
    answer_widgets = display_interview(selected_questions)
    
    # Define the finish button and output area
    finish_button = widgets.Button(description="Finish Interview", button_style='success')
    
    output_area = widgets.Output()

    def on_finish_button_clicked(b):
        """ Handle finish button click and show results """
        with output_area:
            clear_output(wait=True)
            
            # Collect answers from textboxes
            answers = [widget.value.strip() for widget in answer_widgets]
            
            # If any answer is empty, ask user to complete it
            if '' in answers:
                print("⚠️ Please answer all questions.")
                return
            
            #print(f"Answers: {answers}")  # Debugging statement
            
            # Simulate scoring (random for now, can replace with actual logic)
            scores = [random.randint(6, 10) for _ in selected_questions]
            
            # Plot the results as a bar chart
            plot_results(selected_questions, scores)
            
            # Generate feedback based on scores
            feedback = generate_feedback(scores)
            print("\n--- Feedback ---\n")
            print(feedback)
    
    finish_button.on_click(on_finish_button_clicked)
    
    # Display the finish button and output area
    display(finish_button)
    display(output_area)



# In[9]:


start_interview()


# In[ ]:




