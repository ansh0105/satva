import os 
import sys
satva_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])
sys.path.insert(0, satva_dir_path)
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_authenticator.views.authentication_view import Authenticate
from streamlit_extras.add_vertical_space import add_vertical_space

from streamlit_package.streamlit_account_helper import log_out,update_user_detail,register_new_user,reset_password



def account_setting(auth, config: dict):
    """
    This function is used for adding authentication functionalities in stremlit such as:
    1. Update User Detail
    2. Register New User
    3. Reset Password
    4. Logout
    """
    with st.container():
        col1,col2=st.columns([0.20,0.80],gap="large")
        with col1:
            add_vertical_space(4)
            selected_nav = option_menu(
                    menu_title=None,
                    options=["Update Details","Add User","Reset Password","Logout"],
                    icons = ["person-up","person-add","unlock","box-arrow-right"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="vertical",
                    styles={"container": {"width":"100% !important"}}
                    )
            
        with col2:
            add_vertical_space(3)
            if selected_nav == "Update Details":
                update_user_detail(auth, config)
            
            if selected_nav == "Add User":
                register_new_user(auth,config)

            if selected_nav == "Reset Password":
                reset_password(auth,config)
            
            if selected_nav == "Logout":
                log_out(auth)

        
