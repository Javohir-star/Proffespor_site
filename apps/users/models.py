from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class Media(BaseModel):
    file = models.FileField(_("File URL"), max_length=500, upload_to="media/")

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("media")

    def __str__(self):

        return f"{self.file.url}"
    

class User(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


