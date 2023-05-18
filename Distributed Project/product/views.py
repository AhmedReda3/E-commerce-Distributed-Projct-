from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import NewProductForm, EditProductForm

from .models import Product, Review

from rest_framework import generics
from .models import Product, Category
from .models import Product, Review
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product', slug=slug)

    return render(request, 'product/product.html', {'product': product})


@login_required
def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            #missing
            return redirect('/')
    else:
        form = NewProductForm()

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New product',
    })


@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    product.delete()

    return redirect('/')


def edit(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = EditProductForm(instance=product)

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'Edit product',
    })
