from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from cms.models import Menu, Banner
from shop.forms import ReviewForm
from shop.models import Category, Product
from shop.serializers import CategorySerializer


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

        return render(request, 'index.html', context)


class ProductView(BaseView):
    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)

        context = {
            'form': ReviewForm(),
            'product': product,
            'pick_for_you': Product.objects.order_by('?')[:4],

        }
        context.update(self.template_context)
        return render(request, 'product.html', context)

    def post(self, request, product_slug):
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = Product.objects.get(slug=product_slug)
            review.save()
            return redirect('product_page', product_slug)
        else:
            product = Product.objects.get(slug=product_slug)

            context = {
                'form': form,
                'product': product,
                'pick_for_you': Product.objects.order_by('?')[:4],

            }
            context.update(self.template_context)
            return render(request, 'product.html', context)


class SignUpView(BaseView):
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        context.update(self.template_context)
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {
                'form': form
            }
            context.update(self.template_context)
            return render(request, 'registration/register.html', context)


class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

#views.py file has been chanaged.
#utprekshya
