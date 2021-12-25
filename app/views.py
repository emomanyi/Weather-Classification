from django.shortcuts import render
from django.http import HttpResponse
from .forms import WeatherForm
from .models import UploadModel
from .dnn import get_weather
from django.conf import settings
import os
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            save = form.save(commit=True)
            primary_key = save.pk
            image_obj = UploadModel.objects.get(pk=primary_key)
            image_path = os.path.join(settings.MEDIA_ROOT,str(image_obj.file))
            results = get_weather(image_path)
            results['img_url'] = str(image_obj.file.url)
            return render(request,'app/index.html', {'form': form, 'results': results})
    form = WeatherForm()
    mapppings = {
        'form': form
    }
    return render(request, 'app/index.html', mapppings)