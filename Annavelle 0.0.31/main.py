from ukrainian_tts.tts import TTS, Voices, Stress
from number_to_text_ua import number_to_text_ua
from text_to_number_ua import text_to_number_ua
from time_to_text_ua import get_current_time_in_text
from rapidfuzz import fuzz
from vosk import Model, KaldiRecognizer
import sys
import json
import sounddevice as sd
import queue
import pyaudio
import wave
import os
import keyboard
import re
import time

model = Model('d:/Annabelle/vosk-model-uk-v3')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream_listen = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream_listen.start_stream()

#додати детектинг програм на компі
opts = {
    "accept": {
        "yes": ('так', 'да', 'звісно'),
        "no": ('ні')
    },
    "tbr": ('котра', 'яка', 'зараз', 'скільки', '', '', '', '', '', '', '', '',),
    "exit": (''),
    "cmds":{
        "math": ('помнож','поділи','додай','відніми'),
        "timeD": 'дата',
        "timeH": ('година', 'годину')
    },
}

def detect_command(text):
    RC = {'text': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(text, x)
            if vrt > RC['percent']:
                RC['text'] = c
                RC['percent'] = vrt

    print("Yes2")
    execute_command(RC['text'])

def execute_command(command):
    if command == 'timeH':
        play_sound_tts_ua(get_current_time_in_text())

    elif command == 'timeD':
        ...


@staticmethod
def get_full_path(filename):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder_path+'\\Sound', filename)

def get_full_path_folder(foldername):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder_path, foldername)

def improve_file_is_real(full_path):
    try:
        with open(full_path, 'r') as file:
            return 1
    except FileNotFoundError:
        return None

def detect_folder(foldername):
    full_path = get_full_path_folder(foldername)
    print(full_path)
    if os.path.isdir(full_path):
        return 1
    else:
        return 0

def create_folder(foldername):
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(rf"{path}")
    os.mkdir(foldername)
    os.chdir(r"d:/Annabelle")#зробити більш універсальним

def name_wav_file(text):
    filename = ''.join(letter for letter in text if letter.isalnum())
    return filename

def create_sound_tts_ua(text):
    filename = name_wav_file(text)
    full_path = get_full_path((filename)+'.wav')
    
    if detect_folder("Sound"):
        tts = TTS(device="cpu")
        with open(full_path, mode="wb") as file:
            _, output_text = tts.tts(text, Voices.Tetiana.value, Stress.Dictionary.value, file)# Voices.Dmytro.value Lada Tetiana
        play_sound_tts_ua(text)
    
    else: 
        create_folder("Sound")
        create_sound_tts_ua(text)
    
def play_sound_tts_ua(text):
    filename = name_wav_file(text)
    full_path = get_full_path((filename) + '.wav')

    if improve_file_is_real(full_path):
        chunk = 1024

        try:
            f = wave.open(full_path, "rb")

            # Перевірка на потік
            if not hasattr(play_sound_tts_ua, "stream") or play_sound_tts_ua.stream._stream is None or not play_sound_tts_ua.stream.is_active():
                print("Потік не відкритий або неактивний. Відкриваємо новий потік.")
                play_sound_tts_ua.stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                                                  channels=f.getnchannels(),
                                                  rate=f.getframerate(),
                                                  output=True)
                print("Потік успішно відкрито.")

            data = f.readframes(chunk)
            while data:
                play_sound_tts_ua.stream.write(data)
                data = f.readframes(chunk)

            play_sound_tts_ua.stream.stop_stream()
            play_sound_tts_ua.stream.close()
            f.close()

            # Видалення файлу, якщо його назва складається з цифр чи з'являється слово "Зараз"
            if filename.isdigit() or re.match(r'Зараз', filename):
                try:
                    os.remove(full_path)
                    print(f"Файл {full_path} видалено.")
                except PermissionError:
                    print(f"Не вдалося видалити файл {full_path}, оскільки він використовується іншим процесом.")
                except FileNotFoundError:
                    print(f"Файл {full_path} не знайдено.")
                except Exception as e:
                    print(f"Сталася помилка: {e}")

        except Exception as e:
            print(f"Сталася помилка при відтворенні звуку: {e}")
    else:
        create_sound_tts_ua(text)

def clear_text(text):
    text = re.sub(r'text|{|}|:|\n|"', '', text)
    text = re.sub(r'  ', '', text)
    return text

# Основна функція
def listen_ua():
    while keyboard.is_pressed('page down'):
        data = stream_listen.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            text = clear_text(rec.Result())
            print(f"log: {text}")

            # Перевірка на слово "аннабель" та інші варіації
            if re.match(r'аннабель|анабель|анна|а нам|абель|анапи', text):
                print("Yesss")
                for x in opts['tbr']:
                    text = text.replace(x, "").strip()

                print(text)
                detect_command(re.sub(r'аннабель|анабель|анна|а нам|абель|анапи', '', text))

#play_sound_tts_ua("10.3")
#play_sound_tts_ua("Привіт, я вмію розмовляти")

print("Start")

keyboard.add_hotkey('page down', listen_ua, args=())

keyboard.wait()