from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.users.serializer import *

class UserViewSet(GenericViewSet):
   serializer_class = UserSerializer

   def get_queryset(self):
      return self.get_serializer().Meta.model.objects.all()
   
   def list(self, request):
      data = self.get_queryset()
      data = self.get_serializer(data, many=True)
      data = {
         'msg': 'OK',
         'data': data.data
      }
      return Response(data)

   def retrieve(self, reques, pk):
      pass

   @action(detail=True, methods=['post'])
   def set_password(self, request, pk=None):
      pass
   
   def create(self, request):
      user_serializer = self.serializer_class(data=request.data)
      if user_serializer.is_valid():
         user_serializer.save()
         data = {
            'status': 201,
            'message': 'Registro creado correctamente',
            'data': user_serializer.data
         }
         Response(data)
      data = {
         'status': 400,
         'message': 'Se produjo un error al crear el registro',
         'data': None
      }
      Response(data)

   def update(self, request, pk):
      if not self.get_object().exists():
         return Response({
            'status': 404,
             'message': 'No se encontro el elemento solicitado',
             'data': None
         })
      
      user_serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
      if user_serializer.is_valid():
         user_serializer.save()
         return Response({
            'status': 200,
            'message': 'Registro actualizado correctamente',
            'data': user_serializer.data
         })
      
      return Response({
         'status': 400,
         'message': 'Se produjo un error al actualizar los datos',
         'data': None
      })
   
   def partial_update(self, request, pk):
      pass
   
   def destroy(self, request, pk):
      pass