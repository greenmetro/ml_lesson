from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_dface import opencv_detector
from .models import ImageUploadModel

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


def objectDector_html(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        ImageUploadModel.objList
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            opencv_detector(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'web_ml/objectDector.html', {'form': form, 'post': post,'objListNm': ImageUploadModel.objList})
    else:
        form = ImageUploadForm()
    return render(request, 'web_ml/objectDector.html', {'form': form})