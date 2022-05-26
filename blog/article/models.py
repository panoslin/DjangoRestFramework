from django.db import models
from django.utils import timezone
from login.models import User


class Article(models.Model):
    objects: models.QuerySet
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    title = models.CharField(max_length=100)
    
    status_choices = [
        (0, 'Draft'),
        (1, 'Public'),
        (2, 'Private'),
    ]
    status = models.IntegerField(default=0, choices=status_choices)
    
    desc = models.CharField(max_length=200)
    
    content = models.TextField(null=True, blank=True)
    
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
        ]
        
    def __str__(self):
        return f"`{self.title}` - {self.author.username}"