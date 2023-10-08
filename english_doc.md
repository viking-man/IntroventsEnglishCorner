# Introvents' English Corner

#### A spoken English education chatbot based on ChatGPT/whsiper and gTTS.

### 1.Introduction

***The program utilizes the Flask framework, uses SQLite to store audio files, converts audio to text using OpenAI's
open-source Whisper, converts text to audio using gTTS, and employs the official ChatGPT API for chat-based
conversations. Therefore, to use this project, you need an API authorization for ChatGPT.***

### 2.Basic Workflow

-> Frontend reads audio information.

-> Flask server.  

-> Converts audio to text using Whisper.  

-> Requests OpenAI's ChatCompetition API.  

-> Converts the returned text to an audio file using gTTS, stores the data, and responds with the audio.  

-> Frontend plays the audio file directly."

### 3.Usage Process
1. Download the program 
    
```
git clone https://github.com/viking-man/IntroventsEnglishCorner.git
cd IntroventsEnglishCorner
```

2. Initialize the project environment

```
python -m venv venv
. venv/bin/activate
```
   For Windows users, after creating a virtual environment using `python -m venv venv`, navigate to the Scripts directory by using the command `cd venv/Scripts/`. Then, activate the created virtual environment directly using the `activate` command.

3. Install the necessary Python packages

`pip install -r requirements.txt`

4. Initialize the corresponding database
```
flask db init
flask db migrate
flask db upgrade
```
5. Start the application   
`flask run`

6. Open the website

    `127.0.0.1:5000`

### 4. Notes  

- Replace the OPENAI_API_KEY in .flaskenv with your own OpenAI API key.
- When using Whisper for the first time, it will automatically download the small model, which is approximately 500MB in size. You may need to wait for this download to complete.
- If you find that the conversion results are not satisfactory, you can go to the WhisperModel.py file and replace 'small' with 'medium' or 'large'.