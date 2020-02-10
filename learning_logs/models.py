from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Topic(models.Model):
    """Тема которую изучаем."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('topic', kwargs={'id':self.id})

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
		
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."