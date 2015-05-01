from rest_framework import serializers
from models import Project, Command


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('owner', )
        #fields = ('name', 'id')


class CommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Command


