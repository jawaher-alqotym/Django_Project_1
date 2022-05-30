from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class VrSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_field = models.ImageField(upload_to="images/VrImg")
    audio_field = models.FileField(default = 'xxxx', upload_to="audios/VrSound")


    def __str__(self):
        return f'{self.user}'

