from rest_framework import serializers
from thrones_be.models import Bathroom, Tag
# from users.models import Profile

class BathroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bathroom
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BathroomSerializer(serializers.ModelSerializer):
    # owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)


    class Meta:
        model = Bathroom
        fields = '__all__'