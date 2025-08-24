# ===== Natasha Main with DeepSeek (OpenRouter) + LangChain Memory + AI Notes =====
# WolframAlpha removed. DeepSeek handles all "who is", "what is", "calculate", and general chat.
# API key is kept directly in code (⚠️ don't upload to GitHub with your real key).

import os
import datetime
import pathlib

# === Natasha modules ===
import stop_listening
import whatsapp
import location
import news
import remember
import about_natasha
import basic
import chrome
import commands as cmd
import cpu
import notes
import screenshot
import songs
import wiki
import speak
import applications as app
import editables

# === LangChain / OpenRouter ===
try:
    from langchain_openai import ChatOpenAI
except Exception:
    from langchain.chat_models import ChatOpenAI  # fallback

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# ----------- Config -----------
# 👇 PASTE YOUR OPENROUTER API KEY HERE
OPENROUTER_API_KEY = "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"

# Model slug (check with curl if needed)
DEEPSEEK_MODEL = "deepseek-ai/chat"

SYSTEM_PERSONA = (
    "You are Natasha, a concise, helpful voice assistant running locally for a student-CEO. "
    "Keep answers crisp, speak-ready, and correct. For notes, produce clean Markdown with headings and bullets."
)

def build_llm_chain():
    llm = ChatOpenAI(
        model=DEEPSEEK_MODEL,
        temperature=0.3,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )
    memory = ConversationBufferMemory(return_messages=True)
    chain = ConversationChain(llm=llm, memory=memory, verbose=False)
    return chain

AI_CHAIN = build_llm_chain()

def ai_chat_reply(user_text: str) -> str:
    try:
        if not AI_CHAIN.memory.chat_memory.messages:
            AI_CHAIN.memory.chat_memory.add_user_message(SYSTEM_PERSONA)
        resp = AI_CHAIN.predict(input=user_text)
        return (resp or "").strip()
    except Exception as e:
        print(f"[AI ERROR] {e}")
        return "Sorry, I will try again."

def ai_make_notes(topic: str) -> str:
    prompt = (
        f"Create tight, exam-friendly notes on: '{topic}'. "
        "Output in Markdown with H2/H3 headings, bullet points, definitions, key formulas, tiny examples, and a recap. "
        "Make it beginner-friendly, concise, and accurate."
    )
    try:
        if not AI_CHAIN.memory.chat_memory.messages:
            AI_CHAIN.memory.chat_memory.add_user_message(SYSTEM_PERSONA)
        resp = AI_CHAIN.predict(input=prompt)
        return (resp or "").strip()
    except Exception as e:
        print(f"[AI NOTES ERROR] {e}")
        return f"# {topic}\n\nSorry, I couldn't generate notes right now."

def save_notes_ai(topic: str, content_md: str) -> str:
    safe_topic = "".join(c for c in topic if c.isalnum() or c in (" ", "-", "_")).strip().replace(" ", "_")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    notes_dir = pathlib.Path("notes_ai")
    notes_dir.mkdir(exist_ok=True)
    path = notes_dir / f"{safe_topic}_{stamp}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content_md)
    return str(path)

# -------- Natasha settings --------
name = editables.name
real_name = editables.real_name
real_password = editables.real_password

if __name__ == "__main__":
    basic.greeting(name, real_name)

    while True:
        query = cmd.takeCommand().lower()

        # ---------- Hardcoded Natasha commands ----------
        if 'date' in query:
            basic.tell_date()

        elif 'time' in query:
            basic.tell_time()

        elif 'thanks' in query or 'thank you' in query:
            speak.speak('Pleasure to help you')

        elif 'bye bye' in query or 'go offline' in query:
            basic.go_offline(name, real_name)

        elif 'shutdown' in query or 'turn off computer' in query:
            basic.shutdown()

        elif 'restart' in query or 'reboot' in query:
            basic.restart()

        elif 'logout' in query or 'sign out' in query:
            basic.logout()

        elif 'what is your name' in query or "what's your name" in query:
            about_natasha.say_name()

        elif 'introduce' in query or 'who are you' in query or 'tell me about you' in query:
            about_natasha.introduce()

        elif 'wikipedia' in query:
            wiki.wikipedia_search(query, name, real_name)

        elif 'open google' in query or 'open chrome' in query:
            chrome.open_google()

        elif 'google' in query:
            chrome.search_google(query)

        elif 'open youtube' in query:
            chrome.open_youtube()

        elif 'youtube' in query:
            chrome.search_youtube(query)

        elif 'open whatsapp' in query:
            chrome.open_whatsapp()

        elif 'open facebook' in query or 'open fb' in query:
            chrome.open_facebook()
        elif 'facebook' in query or 'fb' in query:
            chrome.search_facebook(query)

        elif 'cpu' in query:
            cpu.cpu_battery()

        elif 'open firefox' in query:
            app.open_firefox()
        elif 'open android studio' in query:
            app.open_android_studio()
        elif 'open telegram' in query or 'open tg' in query:
            app.open_telegram()

        elif 'note' in query and ('make notes on' not in query and 'write notes on' not in query):
            notes.write_note()

        elif 'story' in query:
            notes.read_note()

        elif 'screenshot' in query:
            screenshot.screenshot()

        elif 'sinhala song' in query or 'sinhala songs' in query:
            songs.play_sinhala_song()
        elif 'english song' in query or 'english songs' in query:
            songs.play_english_song()
        elif 'song' in query or 'songs' in query:
            songs.play_song()

        elif 'read remember' in query or 'what do you remember' in query:
            remember.read_remember()

        elif 'remember' in query:
            remember.remember()

        elif 'news' in query:
            news.news()

        elif 'where is' in query:
            location.location(query)

        elif 'stop listening' in query or 'sleep' in query:
            stop_listening.stopListening()

        elif 'whatsapp' in query:
            whatsapp.sendwhatsapp()

        elif 'hello natasha' in query:
            basic.greeting(name, real_name)
        elif 'natasha' in query:
            about_natasha.natasha()

        # ---------- AI Notes ----------
        elif 'make notes on' in query or 'write notes on' in query:
            topic = query
            for key in ['make notes on', 'write notes on', 'notes on']:
                if key in topic:
                    topic = topic.split(key, 1)[1].strip()
                    break
            if not topic:
                topic = "general"
            speak.speak(f"Creating concise notes on {topic}.")
            content_md = ai_make_notes(topic)
            path = save_notes_ai(topic, content_md)
            speak.speak("Notes saved. Do you want me to read a short summary?")
            preview = content_md.replace('\n', ' ')[:500]
            if preview:
                speak.speak(preview)

        # ---------- AI fallback (everything else) ----------
        else:
            reply = ai_chat_reply(query)
            print("Natasha (AI):", reply)
            speak.speak(reply)
