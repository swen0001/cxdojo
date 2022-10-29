from django.shortcuts import render

from .models import MyUser, Files
from .forms import FilesModelForm
from .parsing import parsing_csv, parsing_xml


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
        list_csv = parsing_csv(obj.file_csv.path)
        list_xml = parsing_xml(obj.file_xml.path)
        i = -1
        user_list = []
        for lx in list_xml:
            i += 1
            for lc in list_csv:
                if lx[1] in lc[0]:
                    y = list_csv.index(lc)
                    user_list.append(list_xml[i] + list_csv[y])
                else:
                    pass
        for row in user_list:
            first_name = row[0]
            last_name = row[1]
            avatar = row[2]
            username = row[3]
            password = row[4]
            date_joined = row[5]
            MyUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                avatar=avatar,
                username=username,
                password=password,
                date_joined=date_joined,
            )
        obj.activated = True
        obj.save()
    return render(request, 'upload_users/upload.html', {'form': form})
