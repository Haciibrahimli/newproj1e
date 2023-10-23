from django.contrib import admin
from my_app.models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(Keywords)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(BookImage)



