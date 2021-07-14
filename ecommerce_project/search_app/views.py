from django.shortcuts import render
from ecommerce_app.models import Product
from django.db.models import Q

# Create your views here.
def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        print(query)
        products=Product.objects.all().filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,"search.html",{'query':query,'products':products})