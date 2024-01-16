from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=100, verbose_name="Задача")
    content = models.TextField(null=True, blank=True, verbose_name="Описание", default="Описание: ")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Задачи"
        verbose_name = "Задача"
        ordering = ["published"]

