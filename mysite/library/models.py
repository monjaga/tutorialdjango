from django.db import models
from django.urls import reverse


class Book(models.Model):   
    title = models.CharField(max_length=200)
    author = models.ManyToManyField("Author", verbose_name=("Author"))
    description = models.TextField(("Description"))
    added_date = models.DateTimeField(("Date Add"), auto_now=False, auto_now_add=False)
    image = models.ImageField(("Image"), upload_to=None, height_field=None, width_field=None, max_length=None)

    def display_author(self):
        
        return ', '.join([ author.first_name + ' ' + author.last_name for author in self.author.all()[:3] ])
    display_author.short_description = 'Author'
    
    def __str__(self):
       
        return self.title


    def get_absolute_url(self):
        
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    books = models.CharField(max_length=200)


    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)