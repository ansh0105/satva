import subprocess

command1 = ["streamlit", "run", "streamlit_login.py", "--server.port=8501"]
command2 = ["streamlit", "run", "streamlit_app_login_helper.py", "--server.port=8502"]

process1 = subprocess.Popen(command1)
process2 = subprocess.Popen(command2)

process1.wait()
process2.wait()