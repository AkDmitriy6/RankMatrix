from rest_framework import serializers
from rest_framework.serializers import Field
import numpy as np

class MyField(Field): # Корректный вывод
    def to_representation(self, value):
        if isinstance(value, np.integer): #Если тип данных число, происходит вывод числа
            return value
        elif isinstance(value, str): #Если тип данных строка, происходит вывод строки
            return value

class RankSerializer(serializers.Serializer): #
    cols = serializers.IntegerField()
    rows = serializers.IntegerField()
    args = serializers.CharField()
    result = MyField()