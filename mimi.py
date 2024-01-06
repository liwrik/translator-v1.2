import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def lang_trans():
    print("Добро пожаловать в переводчик")
    saied = input("Введите язык, на котором вы будете говорить: ")
    if saied.lower() == "русский":
        return "ru-RU"
    elif saied.lower() == "английский":
        return "en-EN"
    elif saied.lower() == "немецкий":
        return "de-DE"
    elif saied.lower() == "китайский":
        return "zh-ZH"
    elif saied.lower() == "японский":
        return "ja-JA"
    elif saied.lower() == "испанский":
        return "es-ES"
    else:
        print("Ошибка! Данного языка нет среди доступных.")
        return None

def translate_speech(sa_lang):
    print("Доступные языки: английский, немецкий, китайский, японский, испанский, русский.")
    lang = input("Выберите язык для перевода: ")

    translator = Translator()

    if lang == "английский":
        dest_lang = "en"
    elif lang == "немецкий":
        dest_lang = "de"
    elif lang == "китайский":
        dest_lang = "zh-CN"
    elif lang == "японский":
        dest_lang = "ja"
    elif lang == "испанский":
        dest_lang = "es"
    elif lang == "русский":
        dest_lang = "ru"
    else:
        print("Выбран неподдерживаемый язык.")
        return

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=sa_lang)
        print(f"Распознан текст: {text}")

        try:
            translation = translator.translate(text, dest=dest_lang)
            translated_text = translation.text

            print(f"Переведённый текст: {translated_text}")

            engine = pyttsx3.init()

            engine.say(translated_text)
            engine.runAndWait()
        
        except Exception as translate_error:
            print(f"Ошибка при переводе: {translate_error}")

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    sa_lang = lang_trans()
    if sa_lang:
        translate_speech(sa_lang)
