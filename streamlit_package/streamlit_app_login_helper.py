import os 
import sys
import yaml
satva_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])
sys.path.insert(0, satva_dir_path)
print("\n \n ",satva_dir_path, "\n \n")
from PIL import Image
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator import Hasher
from streamlit_option_menu import option_menu
from streamlit_authenticator.views.authentication_view import Authenticate

def update_config_file(config: dict):
    """
    Login helper function to update config.yaml file
    """
    with open(os.path.join(os.getcwd(),'config.yaml'),'w') as file:
        yaml.dump(config, file, default_flow_style=False)


def forget_username(auth: Authenticate,config: dict):
    """
    Login helper function to retrieve username using registered email address 
    """
    try:
        username_of_forgotten_username, email_of_forgotten_username = auth.forgot_username()
        if username_of_forgotten_username:
            update_config_file(config)
            st.success('Username retrieved sucessfully')
            st.info(f"Your username is: {username_of_forgotten_username}")
            # The developer should securely transfer the username to the user.
        elif username_of_forgotten_username == False:
            st.error('Email not found')
    except Exception as e:
        st.error(f"Cannot change username due to error: {e}")


def forget_password(auth: Authenticate,config: dict):
    """
    Login helper function to retrieve password using registered email address 
    """
    try:
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = auth.forgot_password()
        if username_of_forgotten_password:
            update_config_file(config)
            st.success('Password retrieved sucessfully')
            st.info(f"Your new temporary password is: {new_random_password} \n Please reset your password")
            # The developer should securely transfer the new password to the user.
        elif username_of_forgotten_password == False:
            st.error('Username not found')
    except Exception as e:
        st.error(f"Cannot change password due to error: {e}")



if __name__ == '__main__':
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

    # Pre-hashing all plain text passwords once
    Hasher.hash_passwords(config['credentials'])

    authenticator = stauth.Authenticate(
        config["credentials"],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized'],
        auto_hash=False
        )
    
    with st.container():
        col1,col2=st.columns([0.20,0.80],gap="large")
        with col1:
            add_vertical_space(4)
            selected_nav = option_menu(
                    menu_title=None,
                    options=["Forget Username","Forget Password"],
                    icons = ["person-lock","shield-lock"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="vertical",
                    styles={"container": {"padding": "0.1!important","width":"100% !important"}}
                    )
        with col2:
            add_vertical_space(3)
            if selected_nav == "Forget Username":
                forget_username(authenticator, config)
            if selected_nav == "Forget Password":
                forget_password(authenticator, config)

            




