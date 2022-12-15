from django.urls import reverse
from rest_framework.test import APITestCase

class RankappTests(APITestCase):
    def test_rankapp_incorrect(self):
        """
        Проверка на ввод некорректных данных
        :return:
        """
        url = "/api/2/3/1_2_3_4_5_6_7_8_9" #Тестируемый запрос
        responce = self.client.get(url) #Вызов функции
        self.assertEqual(responce.data, {
            "cols": 2,
            "rows": 3,
            "args": '1_2_3_4_5_6_7_8_9',
            "result": "EROR! Please correct your ARGS! Amount doesn't match!",
        }) #соответствует ли ответ тому что я ожидаю
        #Предположил что будет ошибка и ошибка выдалась, следовательно тест успешен

    def test_rankapp_correct(self):
        """
        Проверка на ввод ккоректных данных
        :return:
        """
        url = "/api/3/3/1_2_3_4_5_6_7_8_9"  #Тестируемый запрос
        responce = self.client.get(url)  #Вызов функции
        self.assertEqual(responce.data, {
            "cols": 3,
            "rows": 3,
            "args": '1_2_3_4_5_6_7_8_9',
            "result": 2,
        })  # соответствует ли ответ тому что я ожидаю
        # Предположил что ошибки не будет, и соответственно ошибки нет