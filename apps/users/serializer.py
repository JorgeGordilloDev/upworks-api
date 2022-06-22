from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelField):
   class Meta:
      model = User
      fields = '__all__'