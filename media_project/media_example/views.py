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
            instance = form.save()
    else:
        form = UploadForm()
    return render(request, "media-example.html", {"form": form, "instance": instance})

def update_view(request, pk):
    if request.method == "POST":
        instance = ExampleModel.objects.get(pk=pk)
        form = UploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()

