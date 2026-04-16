from rest_framework.serializers import ModelSerializer

from apps.users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'birth_date', 'gender']
        read_only_fields = ['id']

