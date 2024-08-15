import speech_recognition as sr
import librosa
import soundfile as sf
import scipy.signal

def recognize_speech(kana, romaji):
    recognizer = sr.Recognizer()  # Renomeie a variável para evitar conflitos
    
    # Gravar áudio
    with sr.Microphone() as source:
        
        print(f"Qual é esse Kana? {kana}")                
        audio = recognizer.listen(source)
        
        # Salvar o áudio gravado em um arquivo WAV
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
     
    # Reconhecimento de fala
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        if text.lower() == romaji.lower():
            return 'correto'
        else:
            return 'errado'
    except sr.UnknownValueError:
        print("Não consegui entender o áudio")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")

