import azure.cognitiveservices.speech as speechsdk
import time

speech_config = speechsdk.SpeechConfig(subscription="c037e8631a6b42ec87f18c2aec901ba5", region="eastus")

audio_input = speechsdk.AudioConfig(filename="./audio/reinhardt3.wav")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

def handle_final_result(evt):
    with open('./txt/transcript_7.txt', 'a') as f:
        print(evt.result.text, file=f)

speech_recognizer.recognized.connect(handle_final_result)

speech_recognizer.start_continuous_recognition()

time.sleep(1000)

speech_recognizer.stop_continuous_recognition()
