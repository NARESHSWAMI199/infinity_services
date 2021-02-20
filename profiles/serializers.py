from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Profile
from core.models import Service,UserDetail




class Profile_Serializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'ref_code',
            'image',
        ]


    def get_username(self,obj):
        return obj.user.username
    def get_first_name(self,obj):
        return obj.user.first_name
    def get_last_name(self,obj):
        return obj.user.last_name

