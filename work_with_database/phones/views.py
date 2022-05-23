from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones_objects = Phone.objects.all().order_by('name')
    if sort == 'min_price':
        phones_objects = Phone.objects.all().order_by('price')
    if sort == 'max_price':
        phones_objects = Phone.objects.all().order_by('-price')

    template = 'catalog.html'
    context = {'phones': phones_objects, }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)

    context = {'phone': phone[0],}
    return render(request, template, context)
