import os.path
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings
from PIL import Image
from .forms import UploadForm
from .models import ExampleModel


def media_example(request):
    if request.method == "POST":
        instance = None
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ExampleModel()
            instance.image_field = form.cleaned_data['image_upload']
            instance.file_field = form.cleaned_data['file_upload']
            instance.save()
    else:
        form = UploadForm()
    return render(request, "media-example.html", {"form": form, "instance": instance}, )
