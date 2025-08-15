import streamlit as st 
from gtts import gTTS
import tempfile 
import os 

st.title('AI Text-to-speech')
st.subheader("Write text to be read aloud...")
languageChoices = st.selectbox("Select Language:", options=[("English", "en"), ("French", "fr"), ("Portuguese", "pt")], format_func=lambda x:x[0])

text_input = st.text_area("Oi, tudo bem, Escreve os seus palavras: ", "Voce pode escreve aqui")

if st.button("Convert to speech"):
    if text_input.strip():
        tts = gTTS(text_input, lang=languageChoices[1])
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            audio_path = tmpfile.name
        # play audio 
        audio_file = open(audio_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        
        #audio file handling
        audio_file.close()
        os.remove(audio_path)
        
    else: 
        # no text to read
        st.warning("Please enter some text first")
        
        
        