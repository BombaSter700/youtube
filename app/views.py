from django.shortcuts import render, redirect
import yt_dlp
import logging

# Настройка логгера
logger = logging.getLogger(__name__)

def index(request):
    data = {'message': '', 'flag': False}
    if request.method == 'POST':
        link = request.POST.get('link')  # Получаем ссылку из формы
        if link:
            try:
                logger.info(f"Начало загрузки с YouTube: {link}")
                
                # Настройки загрузки
                ydl_opts = {
                    'format': 'best[ext=mp4]',  # Выбираем лучший доступный формат mp4
                    'outtmpl': './downloads/%(title)s.%(ext)s',  # Путь для сохранения
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=True)  # Загружаем видео
                    title = info.get('title', 'Видео без названия')
                    logger.info(f"Загрузка завершена: {title}")
                    data = {'message': f'Видео "{title}" успешно загружено!', 'flag': True}
            except yt_dlp.utils.DownloadError as e:
                logger.error(f"Ошибка загрузки: {str(e)}")
                data = {'message': f'Ошибка загрузки: {str(e)}', 'flag': True}
            except Exception as e:
                logger.error(f"Неизвестная ошибка: {str(e)}")
                data = {'message': f'Ошибка: {str(e)}', 'flag': True}
        else:
            data = {'message': 'Введите корректную ссылку.', 'flag': True}

    return render(request, 'index.html', context=data)