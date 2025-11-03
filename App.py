import subprocess
import sys
import os

def clone_repo():
    repo_url = "https://github.com/samuraimitti-art/streamlit-app-deploy.git"
    subprocess.run(["git", "clone", repo_url])

def create_venv():
    venv_dir = "env"
    subprocess.run([sys.executable, "-m", "venv", venv_dir])
    print(f"Virtual environment created at ./{venv_dir}")

def activate_venv():
    activate_script = os.path.join("env", "Scripts", "activate.bat")
    if os.path.exists(activate_script):
        print(f"To activate the virtual environment, run:\n{activate_script}")
    else:
        print("Activation script not found. Make sure the virtual environment was created successfully.")

def install_streamlit():
    pip_executable = os.path.join("env", "Scripts", "pip.exe")
    if os.path.exists(pip_executable):
        subprocess.run([pip_executable, "install", "streamlit==1.41.1"])
        print("streamlit==1.41.1 installed successfully.")
    else:
        print("pip executable not found. Make sure the virtual environment was created successfully.")

def show_git_config():
    result = subprocess.run(["git", "config", "-l"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Git configuration:\n", result.stdout)
    else:
        print("Failed to retrieve git configuration.")

def freeze_requirements():
    pip_executable = os.path.join("env", "Scripts", "pip.exe")
    if os.path.exists(pip_executable):
        with open("requirements.txt", "w") as req_file:
            subprocess.run([pip_executable, "freeze"], stdout=req_file)
        print("requirements.txt generated successfully.")
    else:
        print("pip executable not found. Cannot generate requirements.txt.")

def set_git_user_name(user_name):
    result = subprocess.run(["git", "config", "--global", "user.name", user_name])
    if result.returncode == 0:
        print(f"Global git user.name set to '{user_name}'.")
    else:
        print("Failed to set global git user.name.")

def set_git_user_email(user_email):
    result = subprocess.run(["git", "config", "--global", "user.email", user_email])
    if result.returncode == 0:
        print(f"Global git user.email set to '{user_email}'.")
    else:
        print("Failed to set global git user.email.")

def git_commit(message):
    result = subprocess.run(["git", "commit", "-m", message])
    if result.returncode == 0:
        print(f"Committed with message: '{message}'")
    else:
        print("Git commit failed. Make sure you have staged changes.")

def git_push():
    result = subprocess.run(["git", "push", "-u", "origin", "main"])
    if result.returncode == 0:
        print("Pushed to origin main successfully.")
    else:
        print("Git push failed. Make sure you have committed changes and set the remote correctly.")

if __name__ == "__main__":
    # Ensure app.py exists in the correct location
    if not os.path.exists("app.py"):
        # Create a simple app.py if it doesn't exist
        with open("app.py", "w", encoding="utf-8") as f:
            f.write(
                'import streamlit as st\n\n'
                'st.title("WorkTalk - AI英語パーソナルトレーナー")\n'
                'st.write("このアプリはビジネス英語を短時間で実践的に学ぶためのAIトレーナーです。")\n'
            )
        print("app.py was not found and has been created with a basic Streamlit app.")
        # Add, commit, and push app.py
        subprocess.run(["git", "add", "app.py"])
        subprocess.run(["git", "commit", "-m", "Add main app file"])
        subprocess.run(["git", "push"])
        # Generate requirements.txt using pip freeze
        pip_executable = os.path.join("env", "Scripts", "pip.exe")
        if os.path.exists(pip_executable):
            with open("requirements.txt", "w") as req_file:
                subprocess.run([pip_executable, "freeze"], stdout=req_file)
            print("requirements.txt generated successfully.")
        else:
            print("pip executable not found. Cannot generate requirements.txt.")
    else:
        print("app.py found in repository root.")
