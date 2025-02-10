import streamlit as st
import nltk
from transformers import pipeline   
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

chatbot = pipeline("text-generation", model="distilgpt2")

def health_chatbot(user_input):
    if "symptoms" in user_input:
        return "Please consult a doctor for better advice."
    elif "Appointment" in user_input:
        return "Would you like to book an appointment with the doctor?"
    elif "Medication" in user_input:  # Fixed typo from "Madication"
        return "It is important to take medicines as prescribed by the doctor. If you have concerns, please consult the doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1) 
        return response[0]["generated_text"]
    return ""

def main():
    st.title("Healthcare Chatbot")
    user_input = st.text_input("How can I help you today?")
    
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your request..., please wait"):
                response = health_chatbot(user_input)  
            st.write("HealthCare Chatbot:", response) 
            print(response)  
        else:
            st.write("Please enter a message to get a response.")

main()
