from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from dingoapp.forms import BookingForm
from dingoapp.models import FoodModel, Category, Chefs


def index(request):
    exfoods = FoodModel.objects.filter(exclusive=True)[:3]
    category = Category.objects.all()
    cat = request.GET.get('cat')
    chefs = Chefs.objects.filter(level__ch_level='Chef Master')[:3]

    if cat is None:
        cat = 'Special'
    foods = FoodModel.objects.filter(category__category_name=cat)[:6]
    tags = FoodModel.objects.filter(tags__tag='Food news')[:3]
    booking_form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'home_menu': 'home_menu',
               'foods3': foods[:3],
               'foods6': foods[3:6],
               'tags': tags,
               'exfoods': exfoods,
               'categories': category,
               'cat': cat,
               'chefs': chefs,
               'form': booking_form
               }
    return render(request, 'index.html', context)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        my_context = super().get_context_data(**kwargs)
        my_context['chefs'] = Chefs.objects.all()

        return my_context


class MenuView(TemplateView):
    template_name = 'food_menu.html'

    def get_context_data(self, **kwargs):
        cat = self.request.GET.get('cat')
        if cat is None:
            cat = 'Special'

        foods = FoodModel.objects.filter(category__category_name=cat)[:6]
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['foods3'] = foods[3]
        context['foods6'] = foods[3:6]

        return context


class ChefsView(TemplateView):
    template_name = 'chefs.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
