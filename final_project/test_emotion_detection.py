import unittest  
from EmotionDetection import emotion_detector  

class TestEmotionDetector(unittest.TestCase):  
    def test_emotion_detection(self):  
        test_cases = [  
            ("Me alegra que esto haya sucedido", "joy"),  
            ("Estoy realmente enojado por esto", "anger"),  
            ("Me siento disgustado solo de oír sobre esto", "disgust"),  
            ("Estoy tan triste por esto", "sadness"),  
            ("Tengo mucho miedo de que esto suceda", "fear"),  
        ]  
        
        for affirmation, expected_dominant in test_cases:  
            with self.subTest(affirmation=affirmation):  
                result = emotion_detector(affirmation)  
                self.assertEqual(result['dominant_emotion'], expected_dominant)  

if __name__ == '__main__':  
    unittest.main()