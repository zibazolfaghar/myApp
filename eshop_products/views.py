import itertools

from django.shortcuts import render
from django.views.generic import ListView

from eshop_order.forms import UserNewOrderForm
from eshop_product_category.models import productcategory
from .models import products,productsgallery
from django.http import Http404

from eshop_tag.models import Tag

# Create your views here.

class productlist(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6
    def get_queryset(self):
        return products.objects.get_active_product()

class productlistbycategory(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6
    def get_queryset(self):
        # print(self.kwargs)
        category_name=self.kwargs['category_name']
        category=productcategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return products.objects.get_product_by_category(category_name)

def my_grouper(n, iterable):
   args = [iter(iterable)] * n
   return ([e for e in t if e is not  None] for t in itertools.zip_longest(*args))


def product_detail(request,*args,**kwargs):

    selected_product_id=kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None,initial={'product_id':selected_product_id})
    product_name=kwargs['product_name']
    product = products.objects.get_by_id(selected_product_id)
    if product is None or not product.active:
        raise Http404("محصول مورد نظر یافت نشد")
    related_products=products.objects.get_queryset().filter(categoris__products=product).distinct()
    grouped_related_products=list(my_grouper(3,related_products))
    galleries = productsgallery.objects.filter(product_id=selected_product_id)
    grouped_galleries=list(my_grouper(3,galleries))
    context = {
        'product': product,
        'galleries' : grouped_galleries,
        'related_products':grouped_related_products,
        'new_order_form':new_order_form
    }
    # tag=Tag.objects.first()
    # print(tag.products.all())
    # print(product.tag_set)
    return render(request, "products/products_detail.html", context)



class SearchProductsView(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6
    def get_queryset(self):
        request=self.request
        # print(request.GET)
        query=request.GET.get('q')
        if query is not None:
                return products.objects.search(query)
        return products.objects.get_active_product()

def products_categories_partial(request):
    categories=productcategory.objects.all()
    context={
        'categories':categories
    }
    return  render(request,'products/product_categories_partial.html',context)




