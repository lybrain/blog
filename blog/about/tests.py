from rest_framework.test import APITestCase
from rest_framework import status
from about.models import WishMessage
from django.urls import reverse
from user.models import User

class BaseWishMessageTest(APITestCase):
     def setUp(self):
        self.superuser = User.objects.create_superuser('test@gmail.com', 'secret')
        self.client.login(username='test@gmail.com', password='secret')
        self.data = {
               "first_name": "string",
               "last_name": "string",
               "message": "string",
               "email": "user@example.com",
               "allow_mailing": True
          }
        self.id = WishMessage.objects.create(**self.data).id

     def check_objs_equality(self, data, stored_data):
           for key, value  in data.items():
               self.assertEqual(value, stored_data[key]) 

class CreateWishMessageTest(BaseWishMessageTest):
    def setUp(self):
        self.superuser = User.objects.create_superuser('test@gmail.com', 'secret')
        self.client.login(username='test@gmail.com', password='secret')
        self.data = {
               "first_name": "string",
               "last_name": "string",
               "message": "string",
               "email": "user@example.com",
               "allow_mailing": True
          }

    def test_post_wish_message(self):
        response = self.client.post(reverse('wish-message-list'), self.data)
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.check_objs_equality(self.data,response_data)
        
class ReadWishMessageTest(BaseWishMessageTest):
    def setUp(self):
         super().setUp()
         WishMessage.objects.create(**self.data)
         self.CREATED_OBJECTS = 2

    def test_list_wish_message(self):
        response = self.client.get(reverse('wish-message-list'))
        results = response.data['results']
        self.assertEqual(len(results), self.CREATED_OBJECTS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_wish_message(self):
        response = self.client.get(reverse('wish-message-detail', args=[self.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateWishMessageTest(BaseWishMessageTest):
    def setUp(self):
         super().setUp()
         

         self.update_data = self.data.copy()
         self.update_data['message'] = 'updated msg'

         self.partial_data = self.data.copy()
         self.partial_data['message'] = 'updated partial msg'

    def test_can_update_wish_message(self):
        response = self.client.put(reverse('wish-message-detail', args=[self.id]), self.update_data)
        self.check_objs_equality(self.update_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
    def test_can_partial_update_wish_message(self):
        response = self.client.patch(reverse('wish-message-detail', args=[self.id]), self.partial_data)
        self.check_objs_equality(self.partial_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteWishMessageTest(BaseWishMessageTest):
    def test_delete_wish_message(self):
        response = self.client.delete(reverse('wish-message-detail', args=[self.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)