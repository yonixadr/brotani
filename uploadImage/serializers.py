from rest_framework import serializers
from .models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False))

    class Meta:
        model = FileUpload
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data['name']
        file = validated_data.pop('file')
        image_list = []
        for img in file:
            photo = FileUpload.objects.create(file=img, name=name)
            imageurl = f'{photo.file.url}'
            image_list.append(imageurl)
        return image_list


class FileUploadDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'
