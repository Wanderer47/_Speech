import speech_recognition as speech_recog
import pathlib
import os

# make object
r = speech_recog.Recognizer()
# take audio file
audio_fail_Directory = pathlib.Path("Audio_Input_Ru")
audio_list = os.listdir(audio_fail_Directory)

for audio_name in audio_list:
    audio_In = speech_recog.AudioFile(f'{audio_fail_Directory}/{audio_name}')
# convert audio to text
    with audio_In as audio_fail:
        audio = r.record(audio_fail)
#line = r.recognize_sphinx(audio, language='en-US')
    line = r.recognize_google(audio, language='ru-RU')
# writ line to file
    text_Out = os.path.join(pathlib.Path("Text_Output_Ru"), f'{audio_name}.txt')
    with open(text_Out, 'w') as text:
        text.write(line)