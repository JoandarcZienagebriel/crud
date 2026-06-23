from django.db import models
from django.urls import reverse

class Point(models.Model):
    author=models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    math=models.PositiveIntegerField(null=True, blank=True)
    physics=models.PositiveIntegerField(null=True, blank=True)
    chemistry=models.PositiveIntegerField(null=True, blank=True)
    biology=models.PositiveIntegerField(null=True, blank=True)
    name=models.CharField(max_length=60)

    def get_absolute_url(self):
        return reverse("detail_school", kwargs={"pk": self.pk})

# Create your models here.
class GradeTen(models.Model):
    author=models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    math=models.PositiveIntegerField(null=True, blank=True)
    physics=models.PositiveIntegerField(null=True, blank=True)
    chemistry=models.PositiveIntegerField(null=True, blank=True)
    biology=models.PositiveIntegerField(null=True, blank=True)
    name=models.CharField(max_length=60)

    def get_absolute_url(self):
        return reverse("detail_ten", kwargs={"pk": self.pk})

# Create your models here.
