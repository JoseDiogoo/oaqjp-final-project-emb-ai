"""Unit tests for emotion detection."""

from EmotionDetection import emotion_detector


def test_emotion_detector():
    """Test the emotion detector for expected dominant emotions."""
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected_emotion in test_cases.items():
        response = emotion_detector(statement)
        assert response["dominant_emotion"] == expected_emotion


if __name__ == "__main__":
    test_emotion_detector()
    print("All tests passed.")