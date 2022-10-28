import csv

from django.shortcuts import render
from .models import MyUser, Files
from .forms import FilesModelForm
import csv


def index(request):
    users = MyUser.objects.all()
    data = {'users': users}
    return render(request, 'upload_users/index.html', data)


def upload(request):
    form = FilesModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = FilesModelForm()
        obj = Files.objects.get(activated=False)
        with open(obj.file_csv.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    if row[0] == '' or row[1] == '' or row[2] == '':
                        pass
                    else:
                        username = row[0]
                        password = row[1]
                        date_joined = row[2]
                        MyUser.objects.create(
                            username=username,
                            password=password,
                            date_joined=date_joined,
                        )
            obj.activated = True
    return render(request, 'upload_users/upload.html', {'form': form})
