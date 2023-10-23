from django.shortcuts import render
from my_app.models import Book
# Create your views here.

def index_view(request):
    my_obj = Book.objects.all()

    context = {
        
    'my_obj':my_obj

    }
    return render(request,'index.html',context)
