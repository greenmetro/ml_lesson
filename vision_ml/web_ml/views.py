from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings

def first_view(request):
  return render(request, 'web_ml/first_view.html', {})

def uimage(request):
  if request.method == 'POST':
      form = UploadImageForm(request.POST, request.FILES)
      if form.is_valid():
         myfile = request.FILES['image']
         fs = FileSystemStorage()
         filename = fs.save(myfile.name, myfile)
         uploaded_file_url = fs.url(filename)
         return render(request, 'web_ml/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
  else:
      form = UploadImageForm()
      return render(request, 'web_ml/uimage.html', {'form': form})


def dface(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            # opencv_dface(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'web_ml/dface.html', {'form': form, 'post': post})
    else:
        form = ImageUploadForm()
    return render(request, 'web_ml/dface.html', {'form': form})