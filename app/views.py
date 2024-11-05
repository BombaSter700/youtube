from django.shortcuts import render, redirect
from pytube import YouTube
import pytube.exceptions

def index(request):
    data = {'message': '', 'flag': False}
    if request.method == 'POST':
        link = request.POST.get('link')  # Получаем ссылку из формы
        if link:
            try:
                video = YouTube(link)  # Создаем объект видео
                stream = video.streams.get_lowest_resolution()  # Получаем поток с минимальным разрешением
                stream.download()  # Скачиваем видео
                data = {'message': 'Видео успешно загружено!', 'flag': True}
            except pytube.exceptions.RegexMatchError:
                data = {'message': 'Ссылка неверная', 'flag': True}
            except Exception as e:
                data = {'message': f'Ошибка: {str(e)}', 'flag': True}
        else:
            data = {'message': 'Введите корректную ссылку.', 'flag': True}

    return render(request, 'index.html', context=data)

