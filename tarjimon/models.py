from django.db import models

# Create your models here.
class Lugat(models.Model):
    ingilizcha = models.CharField('Ingilizcha',max_length=100) 
    uzbekcha = models.CharField('Uzbekcha', max_length=100)

    def __repr__(self) -> str:
        return f"Lugat(ingilizcha={self.ingilizcha}, uzbekcha={self.uzbekcha})"
