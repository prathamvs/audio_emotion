from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

recognizer = sr.Recognizer()

def au_to_sent():
    with sr.Microphone() as source:
        print('Cleaning background noise....')
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print('Waiting for your message...')
        recordedaudio = recognizer.listen(source)
        print('Done recording...')
        
    try:
        print('Printing message...')
        text = recognizer.recognize_google(recordedaudio,language='en-US')
        Sentence = [str(text)]
        print('Your message:{}'.format(text))
        
    except Exception as ex:
        print(ex)
        
    ## Sentiment analysis
    # Sentence = [str(text)]

    analyser = SentimentIntensityAnalyzer()
    for i in Sentence:
        v =analyser.polarity_scores(i)
        
    return v
    
