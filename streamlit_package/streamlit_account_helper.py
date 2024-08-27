import yaml
import os
import streamlit as st
from streamlit_authenticator.views.authentication_view import Authenticate

def update_config_file(config: dict):
    """
    Account helper function to update config.yaml file
    """
    with open(os.path.join(os.getcwd(),'config.yaml'),'w') as file:
        yaml.dump(config, file, default_flow_style=False)
        

def reset_password(auth: Authenticate,config: dict): 
    """
    Account helper function to reset the password
    """
    try:
        if auth.reset_password(st.session_state['username']):
            update_config_file(config)
            st.success('Password modified successfully')
    except Exception as e:
        st.error(f"Cannot Reset password due to error: {e}")


def register_new_user(auth: Authenticate,config: dict):
    """
    Account helper function to add/register new user
    """
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = auth.register_user(clear_on_submit=True,pre_authorization=False)
        if email_of_registered_user:
            update_config_file(config)
            st.success('User registered successfully')
    except Exception as e:
        st.error(f"Cannot Register the user due to error: {e}")


def update_user_detail(auth:Authenticate, config:dict):
    """
    Account helper function to update details of existing user
    """
    try:
        if auth.update_user_details(st.session_state['username']):
            update_config_file(config)
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(f"Cannot update user details due to error: {e}")


def log_out(auth: Authenticate):
    """
    Account helper function to logout the session
    """
    auth.logout()