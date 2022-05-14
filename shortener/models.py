from django.contrib.auth.models import User
from django.db import models

from .utils import create_shortened_link


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    full_link = models.URLField(max_length=300)
    short_link = models.URLField(unique=True, blank=True)
    clicks = models.IntegerField('Кол-во кликов', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_link:
            self.short_link = create_shortened_link(self)

        super().save(*args, **kwargs)

    def clicked(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return f"{self.full_link} сокращена до {self.short_link}"

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['-created_at']
