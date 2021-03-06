from django.db import models
from django.conf import settings
from django.core.serializers import serialize


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):

     def serialize(self):
        list_values = list(self.values("user","content","image"))
        return final_array

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
    user        =models.ForeignKey(settings.AUTH_USER_MODEL)
    content     =models.TextField(blank= True, null= True)
    image       =models.ImageField(upload_to = upload_update_image, blank =True, null = True)
    updated     =models.DateTimeField(auto_now=True)
    timestamp   =models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content  or ""

    def serialize(self):
        image = self.image
        if image:
            image = self.image.url
        data = {
            "content":self.content,
            "user":self.user.id,
            "image":image
            }
        data = json.dumps(data)
        return data
