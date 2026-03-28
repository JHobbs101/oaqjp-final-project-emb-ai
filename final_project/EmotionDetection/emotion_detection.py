import requests
import json

def emotion_detector(text_to_analyze):
# Define request body contents
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json =  { "raw_document": { "text": text_to_analyze } }

    # Pass the request for the relevant response
    response = requests.post(url=url,headers=header,json=json)

    formatted_response = response.json()

    # Pull out the relevant emotions and their scores from the result
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Create the dictionary
    results = {
        'anger':anger_score,
        'disgust':disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Find the dominant emotion by finding the label with the highest score
    dominant_emotion = max(results, key=results.get)

    # Insert into the dictionary
    results['dominant_emotion'] = dominant_emotion
    
    return results
