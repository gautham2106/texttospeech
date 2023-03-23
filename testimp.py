import openai
import gradio as gr
from playsound import playsound

import speech_recognition as sr
import os
from gtts import gTTS
import io

from textgpt import response

openai.api_key = "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"
model_engine = "text-davinci-003"

def recognize_speech(audio):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Sorry, I could not understand what you said."
    except sr.RequestError:
        text = "Sorry, my speech recognition service is down."
    return text
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    text1 = response.choices[0].text
    tts = gTTS(text=text1, lang='en')
    import os

    # Save the audio file to the current working directory
    tts.save("hello.mp3")

    # Get the full path to the audio file
    audio_path = os.path.abspath("hello.mp3")

    # Play the audio file
    playsound(audio_path)
    return response.choices[0].text


iface=gr.Interface(
    fn=generate_response,
    inputs=gr.inputs.Textbox("Enter your prompt here...", type="text"),

    outputs=gr.Textbox("Prompt output will appear here..."),
    title="GPT-3 Text Davinci-003 Prompt Generator",
    description="Enter a prompt and generate a response using the GPT-3 Text Davinci-003 model.",

)
iface.launch(share=True)