import audi_app1
import streamlit as st
import plotly.express as px
import pandas as pd


# Define a session state class
class SessionState:
    def __init__(self):
        self.recording = False

# Initialize the session state
session_state = SessionState()

# Function to toggle recording state
def toggle_recording():
    session_state.recording = not session_state.recording
    if session_state.recording:
        st.write("Recording started")
    else:
        st.write("Recording stopped")
        
def main():
    st.title("Emotion Detection App")
    
    if st.button("Start recording"):
        toggle_recording()
        data = audi_app1.au_to_sent()
        # st.write(data)

        # Convert the dictionary to a list of tuples
        data_list = [(key, value) for key, value in data.items()]

        # Create a DataFrame using the list of tuples
        df = pd.DataFrame(data_list, columns=['Sentiment', 'Score'])


        # Plot bar graph using Plotly
        fig = px.bar(df, x='Sentiment', y='Score', labels={'x': 'Sentiment', 'y': 'Score'}, title='Sentiment Analysis')
        st.plotly_chart(fig)

    

if __name__ == "__main__":
    main()
