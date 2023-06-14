import unittest
import json
from app.server import app
from unittest.mock import Mock, patch

class FlaskUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        app.testing = True
        self.client = app.test_client()

    @patch('app.server.joblib.load')
    def test_test_endpoint(self, mock_load):
        # Set up mock for joblib.load to return a mock model
        mock_model = Mock()
        mock_model.predict.return_value = [5]  # Mock the prediction result
        mock_load.return_value = mock_model

        data = {
            'fixed-acidity': 7.5,
            'volatile-acidity': 0.5,
            'citric-acid': 0.36,
            'residual-sugar': 6.1,
            'chlorides': 0.029,
            'free-sulfur-dioxide': 32.0,
            'total-sulfur-dioxide': 160.0,
            'density': 0.994,
            'ph': 3.3,
            'sulphates': 0.5,
            'alcohol': 9.7
        }
        response = self.client.post('/test', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertIn('quality', response_data)
        self.assertIsInstance(response_data['quality'], int)

    def test_test_get_endpoint(self):
        response = self.client.get('/test_get', json={})  # Send an empty JSON payload
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertIn('name', response_data)
        self.assertEqual(response_data['name'], 'bruh')

if __name__ == '__main__':
    unittest.main()
