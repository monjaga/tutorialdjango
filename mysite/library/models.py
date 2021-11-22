from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ManyToManyField("Author", verbose_name=("Author"))
    description = models.TextField(("Description"))
    added_date = models.DateTimeField(auto_now_add=True)
    image  = models.ImageField(
        ("Image"), upload_to='library\static\images', max_length=None)

    def display_author(self):
        return ' , '.join([author.first_name + '  ' + author.last_name for author in self.author.all()[:3]])
    display_author.short_description = 'Author'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


    def save(self, *args, **kwargs):
        try:
            this = Book.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass
        super(Book, self).save(*args, **kwargs)


    def image_tag(self):
            return mark_safe('<img src="\%s" width="100" height="120" >' % (self.image))

    image_tag.short_description = 'Image pictures'

class Meta:
        ordering = ['title', 'display_author']

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    books = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    class Meta:
        ordering = ['last_name', 'first_name']


    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return '{0}  {1}'.format(self.last_name, self.first_name)
