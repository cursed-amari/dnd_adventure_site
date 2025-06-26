from django.db import models


class HomePagePost(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "пост"
        verbose_name_plural = "Посты"
