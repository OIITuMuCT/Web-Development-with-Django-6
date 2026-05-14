from django.shortcuts import redirect, render
from django.conf import settings
from PIL import Image
from .forms import UploadForm


def media_example(request):

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = (settings.MEDIA_ROOT /
                request.FILES['file_upload'].name)
            image = Image.open(form.cleaned_data['file_upload'])
            image.thumbnail((50, 50))
            image.save(save_path)
            # with open(save_path, "wb") as output_file:
            #     for chunk in form.cleaned_data['file_upload'].chunks():
            #         output_file.write(chunk)
    else:
        form = UploadForm()
    return render(request, "media-example.html", {"form": form})

