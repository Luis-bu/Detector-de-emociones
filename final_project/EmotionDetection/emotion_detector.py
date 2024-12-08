import requests  

def emotion_detector(text_to_analyze):  
    if not text_to_analyze.strip():  
        return {  
            'anger': None,  
            'disgust': None,  
            'fear': None,  
            'joy': None,  
            'sadness': None,  
            'dominant_emotion': None  
        }  

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    input_json = {"raw_document": {"text": text_to_analyze}}  

    try:  
        response = requests.post(url, headers=headers, json=input_json, timeout=10)  
        response.raise_for_status()  
        result = response.json()  

        emotions = result.get('emotion', {})  
        anger_score = emotions.get('anger', 0)  
        disgust_score = emotions.get('disgust', 0)  
        fear_score = emotions.get('fear', 0)  
        joy_score = emotions.get('joy', 0)  
        sadness_score = emotions.get('sadness', 0)  

        scores = {  
            'anger': anger_score,  
            'disgust': disgust_score,  
            'fear': fear_score,  
            'joy': joy_score,  
            'sadness': sadness_score  
        }  
        dominant_emotion = max(scores, key=scores.get)  

        output = {  
            'anger': anger_score,  
            'disgust': disgust_score,  
            'fear': fear_score,  
            'joy': joy_score,  
            'sadness': sadness_score,  
            'dominant_emotion': dominant_emotion  
        }  

        return output  

    except requests.exceptions.RequestException as e:  
        return f"Error: {e}"