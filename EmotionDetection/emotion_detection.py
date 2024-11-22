import requests


def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    res = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        json={"raw_document": {"text": text_to_analyze}},
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
    )

    res_json = res.json()

    emotions = {
        "anger": res_json.get("anger"),
        "disgust": res_json.get("disgust"),
        "fear": res_json.get("fear"),
        "joy": res_json.get("joy"),
        "sadness": res_json.get("sadness"),
    }

    dominant = None
    for emotion, score in emotions.items():
        if not dominant:
            dominant = (emotion, score)
            continue

        if score > dominant[1]:
            dominant = (emotion, score)

    emotions["dominant_emotion"] = dominant[0]

    return emotions
