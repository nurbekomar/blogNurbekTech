from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL", null=True
    )
    content = RichTextUploadingField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блогы"
        ordering = ["title", "time_create"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL", null=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
