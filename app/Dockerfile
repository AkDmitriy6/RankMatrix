# Dockerfile

# The first instruction is what image we want to base our container on
#Загрузка Python
FROM python
#Копирование файла зависимости
COPY requirements.txt requirements.txt
#Подгрузка дополнительных пакетов
RUN pip install --no-cache-dir -r requirements.txt
#Копирование образов
COPY app app
ADD .env /app/.env
#Рабочая папки
WORKDIR /app
#Команды python
RUN python manage.py migrate
RUN python manage.py collectstatic
#Порты
EXPOSE 8000


# runs the development server
#ENTRYPOINT ["python", "./manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]