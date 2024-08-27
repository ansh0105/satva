import os 
import sys
satva_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])
sys.path.insert(0, satva_dir_path)
from streamlit_authenticator.views.authentication_view import Authenticate

from streamlit_option_menu import option_menu

from streamlit_package.streamlit_genai import genai_analysis
from streamlit_package.streamlit_account import account_setting

def app(auth: Authenticate, config: dict):
    """
    This function is used to display option menu for Analysis and Account setting in streamlit application 
    """
    selected_nav = option_menu(
            menu_title=None,
            options=["Analysis","Account"],
            icons = ["kanban","person-gear"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={"container": {"padding": "0.1!important","width":"100% !important"}}
                )

    if selected_nav == "Analysis":
        genai_analysis()
    if selected_nav == "Account":
        account_setting(auth, config)
        
    
