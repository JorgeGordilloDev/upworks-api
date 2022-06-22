from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from apps.users.models import User
from apps.users.serializer import UserSerializer

class UserViewSet(GenericViewSet):
   serializer_class = UserSerializer

   def get_queryset(self):
      return self.get_serializer().Meta.model.objects.all()
   
   def list(self, request):
      users = self.get_queryset()
      users = self.get_serializer(users, many=True)
      data = {
         'msg': 'OK',
         'data': users
      }
      return Response(data)
