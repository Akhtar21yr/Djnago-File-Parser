from rest_framework import serializers
from .models  import StuAditionalInfo,Student

class StudentSerializer(serializers.Serializer):
    class Mete :
        model = Student
        fields = '__all__'
class StudentInfoSerializer(serializers.Serializer):
    class Mete :
        model = StuAditionalInfo
        fields = '__all__'