from rest_framework_json_api import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    contact = serializers.CharField(required=False, allow_blank=True, max_length=100) 
    about = serializers.CharField(required=False, allow_blank=True, max_length=100)
    education = serializers.CharField(required=False, allow_blank=True, max_length=100)
    skills = serializers.CharField(required=False, allow_blank=True, max_length=100)
    work = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.about = validated_data.get('about', instance.about)
        instance.education = validated_data.get('education', instance.education)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.work = validated_data.get('work', instance.work)
        
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('name','contact', 'about', 'education', 'skills', 'work')

    
