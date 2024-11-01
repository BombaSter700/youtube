from django.shortcuts import render, redirect
from pytube import *
import pytube
import pytube.exceptions

def index(request):
    data = {'message': '', 'flag': False}
    if request.method == 'POST':
        try:
            link = request.POST['link']
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            stream.download()
        except pytube.exceptions.RegexMatchError:
            data = {'message': 'Ссылка неверная', 'flag': True}
    return render(request, 'index.html', context=data)

