from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, null=False)
    score = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],
        null=False
    )
    reviewer = models.ForeignKey(
        'users.User',
        related_name='reviews_written',
        on_delete=models.SET('NO AUTHOR')
    )