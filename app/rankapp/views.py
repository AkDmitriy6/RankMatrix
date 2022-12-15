from django.http import HttpResponse
from rankapp.funcs import rank


def main(request):
    cols = request.GET.get("cols")  # Происходить чтение того, что пользователь запишет в поисковой запрос (столбцы)
    rows = request.GET.get("rows")  # Происходить чтение того, что пользователь запишет в поисковой запрос (строки)
    args = request.GET.get("args")  # Происходить чтение того, что пользователь запишет в поисковой запрос (аргументы)
    r = rank(cols=cols, rows=rows, args=args)
    return HttpResponse(f"Ранг Матрицы: {r}") # Вывод ранга матрицы

# from django.shortcuts import render
# import numpy as np
