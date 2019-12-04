from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

from pyladiesflat.settings.base.static import UPLOAD_TO


class StoryPoint(models.Model):
    date = models.DateField(
        _('Дата'), null=True, blank=True
    )
    title = models.CharField(
        _('Заголовок'), max_length=255
    )
    description = models.TextField(
        _('Описание')
    )
    image = models.ImageField(
        _('Изображение'), upload_to=UPLOAD_TO
    )

    class Meta:
        verbose_name = 'Историческое событие'
        verbose_name_plural = 'Исторические события'
        db_table = 'story_points'

    def __str__(self):
        return self.title


class Schedule(models.Model):
    date = models.DateField(
        _('Дата'), null=True, blank=True
    )
    title = models.CharField(
        _('Заголовок'), max_length=255
    )
    description = models.TextField(
        _('Описание'),
        null=True, blank=True
    )
    url = models.URLField(
        _('Ссылка на мероприятие'),
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        db_table = 'schedule'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Publication(models.Model):
    date = models.DateField(
        _('Дата'), null=True, blank=True
    )
    source = models.CharField(
        _('Ресурс'), max_length=255
    )
    title = models.CharField(
        _('Заголовок'), max_length=255
    )
    url = models.URLField(
        _('Ссылка на публикацию'),
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        db_table = 'publications'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(
        _('Заголовок'), max_length=255
    )
    text = RichTextField(
        _('Текст со ссылками'),
        blank=True, null=True
    )
    order_number = models.IntegerField(
        _('Порядковый номер'),
        default=0,
    )

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
        db_table = 'resources'
        ordering = ['order_number']

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(
        _('Имя'), max_length=255
    )
    logo = models.ImageField(
        _('Логотип'), upload_to=UPLOAD_TO
    )
    url = models.URLField(
        _('Ссылка'),
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        db_table = 'partners'

    def __str__(self):
        return self.name
