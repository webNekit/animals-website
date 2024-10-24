from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название отчета', help_text="Отчет по закупкам лекарств")
    file = models.FileField(upload_to="reports/", verbose_name="Файл отчета", help_text="Загрузите файл отчета")
    is_active = models.BooleanField(default=True, verbose_name='Активная категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания отчета")

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"

    def __str__(self) -> str:
        return self.name - self.created_at