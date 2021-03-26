import speech_recognition as speech_recog
import pathlib
import os
from googletrans import Translator

# make object
r = speech_recog.Recognizer()
translator = Translator()
# take audio file
audio_fail_Directory = pathlib.Path("Audio_Input_Ar")
audio_list = os.listdir(audio_fail_Directory)

for audio_name in audio_list:
    audio_In = speech_recog.AudioFile(f'{audio_fail_Directory}/{audio_name}')
# convert audio to text
    with audio_In as audio_fail:
        audio = r.record(audio_fail)
    line = r.recognize_google(audio, language='ar-EG')
# translate Ar text in Ru lenguage 
    result = translator.translate(line, dest='ru', src='ar')
# writ result to file - translate to ru
    text_Out_Ar_ru = os.path.join(pathlib.Path("Text_Output_Ar_ru"), f'{audio_name}.txt')
    with open(text_Out_Ar_ru, 'w') as text:
        text.write(result.text)
# writ line to file - ar
    text_Out_Ar_ar = os.path.join(pathlib.Path("Text_Output_Ar_ar"), f'{audio_name}.txt')
    with open(text_Out_Ar_ar, 'w', encoding="utf-8") as text:
        text.write(line)