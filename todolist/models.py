from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(
        "auth.User", related_name="tasks", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title
