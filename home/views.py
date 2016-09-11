from django.db.models import Q
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

# Create your views here.
from home.models import Car, Brand


class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        categories = []
        for car in cars:
            if car.category not in categories:
                categories.append(car.category)
        barnds = Brand.objects.all()
        return TemplateResponse(request, 'index.html', {'cars': cars, 'barnds': barnds, 'categories': categories})

    def post(self, request, *args, **kwargs):
        print "POST...."
        colors = request.POST.getlist('colors')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        start_milage = int(request.POST.get('start_milage'))
        end_milage = int(request.POST.get('end_milage'))
        start_price = int(request.POST.get('start_price'))
        end_price = int(request.POST.get('end_price'))
        cars = Car.objects.all()
        if colors:
            cars = Car.objects.filter(color__in=colors)
        else:
            cars =cars.filter(category=category).filter(brand__name=brand).filter(milage__gte=start_milage).filter(milage__lte=end_milage).filter(price__gte=start_price).filter(price__lte=end_price)
        categories = []
        for car in Car.objects.all():
            if car.category not in categories:
                categories.append(car.category)
        barnds = Brand.objects.all()
        return TemplateResponse(request, 'index.html', {'cars': cars, 'barnds': barnds, 'categories': categories})
