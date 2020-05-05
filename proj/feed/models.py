from django.db import models

class feedback(models.Model):
    name = models.CharField('Название модели', max_length=120)
    email = models.EmailField('Email', max_length=120, blank=True, null=True)
    phone = models.CharField('Telephone', max_length=20)
    description = models.CharField('Opisanie', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name
        
class Meta:
    verbose_name = 'Forma obratnoy svyazi'
    verbose_name_plural = 'Formi obratnoy svyazi'
