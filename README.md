# Annabelle — Ukrainian Voice Assistant

A voice assistant in Ukrainian designed to interact with a computer using voice commands.

The project combines speech recognition, Ukrainian language processing, fuzzy text matching, audio input/output and computer interaction.

---

## Project Goal

The goal of the project was to develop a practical voice assistant for computer interaction while exploring speech recognition, audio processing and Ukrainian language processing.

The project is continuously evolving and the current version is designed to be flexible enough for further development.

---

## System Architecture

```text
                  ┌──────────────┐
                  │  Microphone  │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ Audio Input  │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │     Vosk     │
                  │     ASR      │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ Text Filter  │
                  │    re        │
                  └──────┬───────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Command Matching │
                │    RapidFuzz     │
                └────────┬─────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ PC Command   │
                  │ / Action     │
                  └──────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ Ukrainian TTS│
                  └──────────────┘
```

---

## Software

**Programming language:**

- Python

**Libraries:**

- `ukrainian_tts` — Ukrainian speech synthesis
- `number_to_text_ua` — number-to-text conversion
- `text_to_number_ua` — conversion of written numbers back to numeric values
- `time_to_text_ua` — conversion of time into text
- `rapidfuzz` — fuzzy text comparison
- `vosk` — speech recognition
- `pyaudio` — audio streams
- `sounddevice` — audio input/output
- `wave` — WAV file processing
- `keyboard` — keyboard interaction
- `re` — text filtering and processing

**Python system modules:**

- `os`

---

## Custom Ukrainian Language Libraries

One of the main parts of the project is a set of self-developed libraries for Ukrainian language processing:

### `number_to_text_ua`

Converts numbers into Ukrainian text.

### `text_to_number_ua`

Converts Ukrainian numbers written as words back into numeric values.

### `time_to_text_ua`

Converts time values into textual Ukrainian representation.

These components can be reused independently of the voice assistant.

---

## How the Program Works

The assistant captures speech from an audio input device, converts it into text using Vosk and processes the recognized command.

The resulting text is cleaned and compared against available commands using text-processing techniques and fuzzy matching.

After identifying the required command, Annabelle performs the corresponding action on the computer.

The assistant can also generate Ukrainian speech output using the text-to-speech component.

---

## Demonstration

The current project demonstration:

https://github.com/user-attachments/assets/6b2a610d-a983-4712-a4b7-e34fb471de3a

---

## Engineering Scope

The project combines:

- speech recognition;
- speech synthesis;
- Ukrainian language processing;
- fuzzy string matching;
- real-time audio input/output;
- keyboard interaction;
- command processing.

---
## Project Status

**Status:** Active development / evolving project.
