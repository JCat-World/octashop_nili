from django.shortcuts import render
from apps.catalogs.models import Category,Product
from apps.home.models import TopSliderModel




def sub_category_list():
    return Category.objects.filter(depth=1, is_public=True).order_by("title")


def home(request):
    context = {}
    context["sub_categories"] = sub_category_list()
    context["hero_sliders"] = TopSliderModel.objects.all().order_by("-id")[0:10]
    context['title_header'] = "نیلی طب"
    context["more_offer"] = Product.objects.filter(stockrecords__in_offer=True).order_by("-id")[0:10]
    return render(request, 'home/home.html', context)


def category_view(request, pk):
    context = {}
    context["sub_categories"] = sub_category_list()
    # context["category"] = ProductCategory.objects.get(id=pk).category
    context['title_header'] = "نیلی طب"
    context["products"] = Product.objects.filter(category=pk)

    return render(request, 'shops/product-category.html', context)

def product_view(request,pk):
    context = {}
    context["sub_categories"] = sub_category_list()
    context["product"] = Product.objects.get(id = pk)
    return render(request, "products/product.html", context)

def about_us(request):
    context = {}
    context["sub_categories"] = sub_category_list()
    return render(request, "shops/about-us.html", context)

def category_summary_view(request):
    context = {}
    return render(request,"shops/category-summary.html",context)


class FetchDataAPI():
    pass


def last_offer(request):
    context = {}
    context["sub_categories"] = sub_category_list()
    context["products"] = Product.objects.filter(is_public = True, stockrecords__in_offer = True)
    return render(request,"shops/last-offer.html",context)