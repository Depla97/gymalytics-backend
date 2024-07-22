from rest_framework import serializers

from .models import Athlete

MUSCLE_CHOICES = [
    ("Chest"),
    ("Back"),
    ("Biceps"),
    ("Triceps"),
    ("Delts"),
    ("Quads"),
    ("Hamstrings"),
    ("Legs"),
    ("Abs"),
]

CATEGORIES_CHOICES = [
    ("Bodybuilding"),
    ("Calisthenics"),
    ("Powerlifting"),
    ("Hybrid"),
]

class AthleteSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    age  = serializers.IntegerField()
    description  = serializers.CharField(max_length=255)
    preferred_category  = serializers.ChoiceField(choices=CATEGORIES_CHOICES)
    weight  = serializers.IntegerField()
    level  = serializers.CharField(max_length=255)
    profile_picture_url  = serializers.CharField(max_length=1023)

    def create(self, validated_data):
        return Athlete.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.age = validated_data.get('age', instance.age)
        instance.description = validated_data.get('description', instance.description)
        instance.preferred_category = validated_data.get('preferred_category', instance.preferred_category)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.level = validated_data.get('level', instance.level)
        instance.profile_picture_url = validated_data.get('profile_picture_url', instance.profile_picture_url)
        instance.save()
        return instance