import speech_recognition as speech_recog
import pathlib
import os

print("Input audio name: ")
audio_name = input() # определяю название файла 'Q.wav' ...
audio_fail_Directory = pathlib.Path("Audio_Input")
audio_In = speech_recog.AudioFile(f'{audio_fail_Directory}/{audio_name}')

r = speech_recog.Recognizer()
with audio_In as audio_fail:
    audio = r.record(audio_fail)
#line = r.recognize_sphinx(audio, language='en-US')
line = r.recognize_google(audio, language='ru-RU')

text_Out = os.path.join(pathlib.Path("Text_Output"), f'{audio_name}.txt')
with open(text_Out, 'w') as text:
    text.write(line)