from django.shortcuts import render, redirect
from .forms import ImageDownloadForm
from .bg_remover import remove_bg
from .models import ImageModel
from django.http import FileResponse
from django.conf import settings


def main(request):

    if request.method == 'POST':
        form = ImageDownloadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            file = ImageModel.objects.create(image_nobg=image)
            file.save()
            remove_bg(str(file.image_nobg))
            response = FileResponse(open(settings.MEDIA_ROOT + str(file.image_nobg), 'rb'), as_attachment=True)
            return response
    else:
        form = ImageDownloadForm
    return render(request, 'main/index.html', context={'form': form})