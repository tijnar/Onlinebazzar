from django.shortcuts import render

# Create your views here.
from django.views import View

from cms.models import Menu, Banner
from shop.models import Category, Product


class BaseView(View):
    template_context = {
        'menus': Menu.objects.all(),
        'categories': Category.objects.all(),
    }


class HomeView(BaseView):

    def get(self, request):  # get is the convention

        context = {
            'banners': Banner.objects.all(),
            'deal_of_the_day': Product.objects.filter(deals_of_the_day=True),
            'latest_products': Product.objects.order_by('-pubdate')[:8],
            'pick_for_you': Product.objects.order_by('?')[:4],

        }
        context.update(self.template_context)

        return render(request, 'index.html', context )


class ProductView(BaseView):
    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)

        context = {
            'product': product,
            'pick_for_you': Product.objects.order_by('?')[:4],

        }
        context.update(self.template_context)
        return render(request, 'product.html', context )
