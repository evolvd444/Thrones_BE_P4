from rest_framework import serializers
from thrones_be.models import Bathroom, Tag, Review
from users.models import Profile





class BathroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bathroom
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Review
        fields = '__all__'

class BathroomSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Bathroom
        fields = '__all__'
    
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many = True)
        return serializer.data