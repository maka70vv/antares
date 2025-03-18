from django.db import models

class DocumentFusitek(models.Model):
    FUSITEK = 'Fusitek'
    FUSIONPLAST = 'FusionPlast'

    DOC_TYPES = [
        (FUSITEK, 'Прайс Фузитек'),
        (FUSIONPLAST, 'Прайс Фузионпласт'),
    ]

    doc_type = models.CharField(max_length=13, choices=DOC_TYPES, unique=True, verbose_name="Тип документа")
    file = models.FileField(upload_to="documents/", verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return dict(self.DOC_TYPES).get(self.doc_type, "Неизвестный документ")