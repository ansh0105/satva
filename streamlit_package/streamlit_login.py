import os 
import sys
import yaml
satva_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])
sys.path.insert(0, satva_dir_path)
from PIL import Image
import streamlit as st

from streamlit_extras.add_vertical_space import add_vertical_space

from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator import Hasher

from streamlit_package.streamlit_app import app



st.set_page_config(page_title="SATVA",page_icon="🟢",layout="wide")

st.markdown("""
        <style>
            .block-container {
                    padding-top: 2.4rem;
                    padding-bottom: 0rem;
                    padding-left: 2.5rem;
                    padding-right: 2.5rem;
                } 
            
            .div.css-10qvep2.e1f1d6gn1 {
             height=10px !important;
            }
            div.st-emotion-cache-njprtr.e1f1d6gn3 {
            padding-top: 2rem;
            }
            
        </style>
        """, unsafe_allow_html=True)
        

with st.container():
    col1,col2 = st.columns([0.15, 0.85] ,gap="small")
    with col1:
        logo_image = Image.open(os.path.join(satva_dir_path,"assets/satva_logo.png"))
        resized_logo = logo_image.resize((180,165))
        # Get the dimensions of the logo image
        logo_width, logo_height = resized_logo.size
        logo= st.image(resized_logo, use_column_width=False, output_format="auto") 
        
    with col2:
        add_vertical_space(1)
        st.title("Spam Analysis and Tagging with Virtual Assistant")
        st.divider()
    
with open(os.path.join(os.getcwd(),'config.yaml')) as file:
    config = yaml.load(file, Loader=SafeLoader)

Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config["credentials"],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized'],
    auto_hash=False
    )

authenticator.login(location="main")

if st.session_state['authentication_status']:
    app(authenticator,config)

elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
    
elif st.session_state['authentication_status'] is None:
    st.markdown("[Forget Username & Password](http://localhost:8502)")
    st.warning('Please enter your username and password')


