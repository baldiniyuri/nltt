from django.test import TestCase
from rest_framework.test import APIClient


class TestUsersView(TestCase):
    def setUp(self):
        self.client = APIClient()
     
        self.user_data = {"email": "marie@test.com","password": "123456",}

        self.login_user_wrong_password = {"email": "marie@test.com", "password": "654321"}

        self.login_inexistent_user = {"email": "ghost@phanton.com", "password": "00000"}


    def test_post_user(self):
        post_user = self.client.post("/api/register/", self.user_data, format="json")
            
        self.assertEqual(post_user.status_code, 201)

        token = self.client.post("/api/login/", self.user_data, format="json").json()["token"]
        
        expected_response = {'data': {'id': 3, 'email': 'marie@test.com', 'is_staff': False, 'is_superuser': False}, 'token': token}

        token_from_post = post_user.json()['token']
        self.assertEqual(token_from_post, token)
        self.assertEqual(post_user.json(), expected_response)

  
        post_same_user = self.client.post("/api/register/", self.user_data, format="json")

        self.assertEqual(post_same_user.status_code, 409)


    def test_login_user(self): 
        self.client.post("/api/register/", self.user_data, format="json")

        login_user = self.client.post("/api/login/", self.user_data, format="json")

        token_user = self.client.post("/api/login/", self.user_data, format="json").json()["token"]

        expected_response_fisica = {"token": token_user}
        
        self.assertEqual(login_user.status_code, 200)
        
        self.assertEqual(login_user.json(), expected_response_fisica)

        login_user_wrong_password = self.client.post("/api/login/", self.login_user_wrong_password, format="json")
        
        self.assertEqual(login_user_wrong_password.status_code, 401)

        login_inexistent_user = self.client.post("/api/login/", self.login_inexistent_user, format="json")
        
        self.assertEqual(login_inexistent_user.status_code, 404)


    def test_delete_user(self):
        self.client.post("/api/register/", self.user_data, format="json")

        token_fisica = self.client.post("/api/login/", self.user_data, format="json").json()["token"]

        delete_user = self.client.delete("/api/delete-account/1/", self.user_data, format="json", HTTP_AUTHORIZATION="Token " + token_fisica)

        self.assertEqual(delete_user.status_code, 204)
        
        delete_same_user = self.client.delete("/api/delete-account/1/", self.user_data, format="json", HTTP_AUTHORIZATION="Token " + token_fisica)

        self.assertEqual(delete_same_user.status_code, 401)



