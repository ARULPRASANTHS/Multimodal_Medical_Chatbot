# 🩺 Multimodal Medical Chatbot

## 🚀 Setup Instructions

### 1. Create and activate Conda environment
```bash
conda create -n medicalbot python=3.10 -y
conda activate medicalbot

### 2. Upgrade pip, setuptools, and wheel
```bash
python -m pip install --upgrade pip setuptools wheel


### 3. Clone or download the repository
  Using Git:
```bash
git clone <your-repo-url>
cd Multimodal_Medical_Chatbot

### 4. Clean old builds (optional but recommended)
```bash
rmdir /s /q build
rmdir /s /q dist
del /q *.egg-info

### 5. Install dependencies
```bash
pip install -r requirements.txt

Or install the project package in editable mode:
```bash 
pip install -e .

### 6. Verify installation
```bash
pip list

Look for:
generative-ai-project   0.0.1

### 7. Test the package
```bash 
python


Then run:
```bash 
from helper import greet_user
print(greet_user("Arulprasanth"))


Expected output:

Hello, Arulprasanth! Welcome to the Medical Chatbot.

### 8. Run the Flask app
```bash
python app.py


Open your browser and go to:

http://127.0.0.1:5000/


You should see:

Medical Chatbot is running!

### 9. Notes for Windows Users

Make sure no Python terminals or IDEs are open in the project folder while installing.

Rename folders to avoid spaces in paths if .egg-info errors appear.

If .egg-info errors persist, try rebooting your PC to clear file locks.

📂 How to add to GitHub

Save your changes to README.md.

Commit changes:
```bash

git add README.md
git commit -m "Add setup commands"


Push to GitHub:
```bash

git push origin main


✅ Key improvements:  
- Dark headers via Markdown `#` and bold icons.  
- Commands highlighted in **code blocks** with syntax highlighting (`bash` or `python`).  
- Clear separation between instructions, expected output, and notes.  

If you want, I can also **add a Table of Contents** at the top with links to each section for eve

