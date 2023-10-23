from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name='cateqoriya adi')

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',)
       verbose_name = 'cateqoriya adi'
       verbose_name_plural = 'cateqoriya adlari'

class Author(models.Model):
   name = models.CharField(max_length=255,verbose_name='author adi')

   def __str__(self):

     return self.name
    
   class Meta:
       ordering = ('name',)
       verbose_name = 'author adi'
       verbose_name_plural = 'author adlari'

class Keywords(models.Model):
    name = models.CharField(max_length=255,verbose_name='tag adi')

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',)
       verbose_name = 'tag adi'
       verbose_name_plural = 'tag adlari'

class Book(models.Model):
    name = models.CharField(max_length=255,verbose_name='adi')
    seria_number = models.CharField(max_length=255,verbose_name='seria nomresi')
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,blank=True)
    tags = models.ManyToManyField(Keywords)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',) 
       verbose_name = 'kitab'
       verbose_name_plural = 'kitablar'

class BookImage(models.Model):
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='media/')


    def __str__(self):

     return self.book.name
    



   


   




