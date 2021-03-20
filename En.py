import speech_recognition as speech_recog
import pathlib
import os
from googletrans import Translator

# take audio file
print("Input audio name: ")
audio_name = input() # определяю название файла 'Q.wav' ...
audio_fail_Directory = pathlib.Path("Audio_Input_En")
audio_In = speech_recog.AudioFile(f'{audio_fail_Directory}/{audio_name}')
# convert audio to text
r = speech_recog.Recognizer()
with audio_In as audio_fail:
    audio = r.record(audio_fail)
line = r.recognize_google(audio, language='en-US')
# translate En text in Ru lenguage 
translator = Translator()
result = translator.translate(line, dest='ru', src='en')
# writ result to file
text_Out = os.path.join(pathlib.Path("Text_Output_En"), f'{audio_name}.txt')
with open(text_Out, 'w') as text:
    text.write(result.text)