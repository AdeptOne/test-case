from django.db import models

from .services import create_shortened_link


class Link(models.Model):
    full_link = models.URLField(unique=True)
    short_link = models.URLField(unique=True, blank=True)
    clicks = models.IntegerField('Кол-во кликов', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def get_absolute_url(self):
        pass

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
