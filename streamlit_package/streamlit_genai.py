import os 
import sys
import time
satva_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])
sys.path.insert(0, satva_dir_path)
import streamlit as st
from genai_layer import generate_response
from nlp_pipeline.content_analysis import content_analyzer

from streamlit_extras.add_vertical_space import add_vertical_space


def genai_analysis():
    """
    This function is used to analyse the input text message and generate descriptive response by performing following tasks:
    1. Spam Classification
    2. Ner Extraction
    3. Sentiment Analysis
    4. Balcklisted URL Tagging
    """
    col1, col2 = st.columns([0.2,0.8])
    with col1:
        input_name = st.text_input(label = "Enter name of the sender:")
    
    n_c1, n_c2 = st.columns([0.9,0.1])
    with n_c1:
        input_msg = st.text_area(label= "Enter the message or text that you want to analyse:")

    submit_btn = st.button("Analyse", key="s1")
    if submit_btn:
        with st.status("Initializing Spam Analysis Process..........", expanded=True) as status:
            st.write("Checking Blacklisted Url...")
            time.sleep(0.5)
            st.write("Extracting Entities...")
            spam_stat, sen_stat, ner_stat, url_stat = content_analyzer(input_msg)
            st.write("Analyzing Sentiment..")
            time.sleep(0.5)
            st.write("Performing Content Analysis...")
            genai_msg = generate_response(input_name, input_msg, spam_stat, sen_stat, ner_stat, url_stat)
            st.write("Generating Response...")
            time.sleep(2)
            status.update(
                label="Process Complete!", state="complete", expanded=False
            )
        add_vertical_space(2)
        st.markdown(genai_msg)


