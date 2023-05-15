from django import forms

from .models import Product

INPUT_CLASSES = 'w-1/2  py-4 px-6  border'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name','slug', 'description', 'price', 'image','thumbnail',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'slug': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'thumbnail': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','slug', 'description', 'price', 'image', 'thumbnail')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'slug': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'thumbnail': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }