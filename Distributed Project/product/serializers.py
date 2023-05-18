from rest_framework import serializers
from .models import Product, Review,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ('id', 'product', 'rating', 'content', 'created_by', 'created_at')

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'description', 'price', 'created_at', 'created_by', 'image', 'thumbnail', 'reviews')

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews', None)
        product = Product.objects.create(**validated_data)
        if reviews_data:
            for review_data in reviews_data:
                Review.objects.create(product=product, **review_data)
        return product

    def update(self, instance, validated_data):
        reviews_data = validated_data.pop('reviews', None)
        reviews = (instance.reviews).all()
        reviews = list(reviews)
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.save()

        if reviews_data:
            for review_data in reviews_data:
                review = reviews.pop(0)
                review.rating = review_data.get('rating', review.rating)
                review.content = review_data.get('content', review.content)
                review.save()

        for review in reviews:
            review.delete()

        return instance