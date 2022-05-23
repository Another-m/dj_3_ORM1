from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, verbose_name="Модель")
    price = models.IntegerField(verbose_name="Цена")
    image = models.ImageField(upload_to="image/", verbose_name="Фото")
    release_date = models.DateField(verbose_name="Дата выхода")
    lte_exists = models.BooleanField(verbose_name="Поддержка ЛТЕ")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


