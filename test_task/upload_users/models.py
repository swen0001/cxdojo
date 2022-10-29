from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_joined = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.URLField()


class Files(models.Model):
    file_csv = models.FileField(upload_to='csv')
    file_xml = models.FileField(upload_to='xml')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File CSV: {self.file_csv}'
