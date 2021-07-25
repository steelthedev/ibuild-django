from django.conf import settings
import json
import requests

class PayStack:
    PAYSTACK_SECRET_KEY = "sk_test_b1630e59eb70f2592023210935c7894455b9ac1b"
    base_url = 'https://api.paystack.co'

    def verify_payment(self, ref , *args, **kwargs):
        path = f"/transaction/verify/{ref}"


        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}" ,
            "Content-Type":'application/json',
        }

        url = self.base_url + path
        response = requests.get(url, headers = headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']

