# 🤖 Natasha – Your Personal J.A.R.V.I.S. Assistant

*"Sir, shall I run the protocol?"*  

Meet **EVO'S V1 Natasha**, a futuristic voice assistant inspired by **J.A.R.V.I.S.** from Iron Man.  
She listens, speaks, remembers, writes notes, runs commands, and thinks using **DeepSeek R1T2** via **OpenRouter API**.  

Built in Python 🐍. Runs locally on your laptop.  
She’s not Alexa. She’s not Siri. **She’s your own Jarvis.**

---

## ✨ Features

### 🎤 Voice Interaction
- Wake Natasha with your voice  
- Ask her *“Who is Tony Stark?”*, *“What is AI?”*, *“Calculate 35 × 47”*  
- She answers using **DeepSeek R1T2 AI brain**  

### 📝 AI Note Taking
- Say: *“Make notes on aldehydes”*  
- Natasha generates **exam-friendly notes in Markdown** with:
  - Headings
  - Bullet points
  - Key formulas
  - Examples
- Notes auto-saved to `notes_ai/`

### 🧠 AI Memory (LangChain)
- Natasha **remembers your last questions** in a session  
- Ask:  
  - “What is TCP?”  
  - “And what about reliability?”  
- She keeps context like a real AI companion

### 💻 System Control
- `"shutdown computer"` → shuts down  
- `"restart"` → reboots  
- `"logout"` → logs out  
- `"stop listening"` / `"sleep"` → pause listening  

### 🌐 Browsing & Search
- `"open google"` → launches Chrome  
- `"google who is Elon Musk"` → searches  
- `"open youtube"` → YouTube  
- `"youtube iron man trailer"` → search directly  

### 📲 Socials
- `"open whatsapp"`  
- `"whatsapp message"` → send WhatsApp message  
- `"open facebook"`  

### 📰 Information
- `"news"` → latest news  
- `"where is New York"` → map location  
- `"wikipedia python programming"` → summary  

### 🖼️ Utilities
- `"screenshot"` → takes screenshot  
- `"note"` → quick notes  
- `"story"` → reads saved notes  
- `"cpu"` → system performance  

### 🎶 Entertainment
- `"play sinhala songs"`  
- `"play english songs"`  
- `"play song"`  

---

## 🚀 Setup

### 1️⃣ Clone repo
```bash
git clone https://github.com/yourusername/Natasha-VoiceAssistant.git
cd Natasha-VoiceAssistant

----

## Getting Started
- Change the name in `editables.py` for pronouncing 
- Change the real_name in `editables.py` for printing
- You can enable password uncommenting lines 30-49 in `main.py`
- Change the password in `editables.py`
- Change paths in `editables.py` for Folders, Applications and Songs
- Get API key for [News](https://newsapi.org/) and change in `editables.py`
- Get API key for [Wolframalpha](https://developer.wolframalpha.com/) and change in `editables.py`
- Change names and phone numbers in `phone_book.py` for WhatsApp

---

### 2️⃣ Install requirements
```bash
pip install -r requirements.txt

---
3️⃣ API Key Setup

Natasha’s AI brain runs on DeepSeek R1T2 via OpenRouter.
You need your own API key. Get it here: 👉 https://openrouter.ai/keys

Where to paste the key

Open main.py, find this section:
# 👇 PASTE YOUR OPENROUTER API KEY HERE
OPENROUTER_API_KEY = "sk-or-xxxxxxxxxxxxxxxxxxxx"

llm = ChatOpenAI(
    model="deepseek/deepseek-r1-t2",   # confirm model slug
    temperature=0.3,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)
---
Replace sk-or-xxxxxxxxxxxxxxxxxxxx with your own key.

⚠️ Never share your API key or push it to GitHub!
---

🎮 Usage

Run Natasha:
python main.py

---
Examples:
User: Who is Anirudh Gupta?
Natasha: Anirudh Gupta is a young innovator and developer, CEO of Infinity Services Providers.

User: Calculate 25 * 34
Natasha: The answer is 850.

User: Make notes on aldehydes
Natasha: Notes saved. Do you want me to read a short summary?

----
🛡️ Notes on Privacy

Natasha runs completely locally on your laptop.

Only API calls (voice queries) go to OpenRouter → DeepSeek.

Notes are stored in notes_ai/ on your machine.
---

🧑‍💻 Tech Stack

Python 3.10+

SpeechRecognition

pyttsx3

LangChain

DeepSeek R1T2 via OpenRouter

Custom modules (search, notes, news, etc.)

---
🦾 Credits

Developer: Anirudra Gupta – aka Team Infinity 🏆

Inspiration: J.A.R.V.I.S. from Iron Man

AI Power: DeepSeek R1T2 (via OpenRouter)

----
this is V1 it will blow the mide of people V2 coming soon 

---
INFINITY SERVICES PROVIDERS 
