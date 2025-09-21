# Multimodal_Medical_Chatbot

Setup Instructions
1. Create and activate Conda environment

conda create -n medicalbot python=3.10 -y
conda activate medicalbot

2. Upgrade pip, setuptools, and wheel

python -m pip install --upgrade pip setuptools wheel

3. Clone or download the repository

# Using Git
git clone <your-repo-url>
cd Multimodal_Medical_Chatbot


⚠️ If your folder path has spaces (Windows), rename it:

cd "C:\Users\ARULPRASANTH S\Music"
ren "Multimodal_Medical_Chatbot" Multimodal_Medical_Chatbot_Fixed
cd Multimodal_Medical_Chatbot_Fixed

4. Clean old builds (optional but recommended)

rmdir /s /q build
rmdir /s /q dist
del /q *.egg-info

5. Install dependencies

pip install -r requirements.txt


Or install the project package in editable mode:

pip install -e .

6. Verify installation

pip list


Look for:

generative-ai-project   0.0.1

7. Test the package

python

from helper import greet_user
print(greet_user("Arulprasanth"))


Expected output:

Hello, Arulprasanth! Welcome to the Medical Chatbot.

8. Run the Flask app

python app.py


Open your browser:

http://127.0.0.1:5000/


You should see:

Medical Chatbot is running!

9. Notes for Windows Users

Make sure no Python terminals or IDEs are open in the project folder while installing.

Rename folders to avoid spaces in paths if .egg-info errors appear.

If .egg-info errors persist, try rebooting your PC to clear file locks.

How to add to GitHub

Save your changes to README.md.

Commit:

git add README.md
git commit -m "Add setup commands"


Push to GitHub:

git push origin main




