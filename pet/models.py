from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категории питомцев')
    is_active = models.BooleanField(default=True, verbose_name='Активная категория')

    class Meta:
        verbose_name = "Категория питомца"
        verbose_name_plural = "Категории питомцев"

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название породы')
    is_active = models.BooleanField(default=True, verbose_name='Активная категория')

    class Meta:
        verbose_name = "Порода питомца"
        verbose_name_plural = "Породы питомцев"

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=255, verbose_name='Кличка', help_text="Шарик")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория питомца')
    age = models.CharField(max_length=255, default='0', verbose_name='Возраст питомца', help_text='2 года 10 месяцев')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    content = models.TextField(verbose_name="Описание о питомце", help_text="Умный, ласковый, ищет дом")
    meta_title = models.CharField(max_length=255, verbose_name="Meta-заголовок")
    meta_keywords = models.CharField(max_length=255, verbose_name="Meta-ключевые слова")
    meta_description = models.TextField(verbose_name="Meta-описание")
    is_active = models.BooleanField(default=True, verbose_name='Активная категория')

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return self.name


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images', verbose_name="Питомец")
    image = models.ImageField(upload_to="pets/", verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение питомца"
        verbose_name_plural = "Изображения питомцев"

    def __str__(self):
        return f"Изображение для {self.pet.name}"