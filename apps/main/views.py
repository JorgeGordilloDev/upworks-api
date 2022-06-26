from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from apps.main.serializers import *

class AlumnViewSet(GenericViewSet):
   serializer_class = AlumnSerializer

   def get_queryset(self):
      return self.get_serializer().Meta.model.objects.all()
   
   def get_object(self):
      return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
   
   def list(self, request):
      data = self.get_queryset()
      data = self.get_serializer(data, many=True)
      data = {
         'msg': 'OK',
         'data': data.data
      }
      return Response(data)
   
   def retrieve(self, reques, pk=None):
      if self.get_object().exists():
         data = self.get_object().get()
         data = self.get_serializer(data)
         return Response(data.data)
      return Response({'message':'', 'error':'Unidad de Medida no encontrada!'}, status=HTTP_400_BAD_REQUEST)
   
   def create(self, request):
      alumn_serializer = self.serializer_class(data=request.data)
      if alumn_serializer.is_valid():
         alumn_serializer.save()
         data = {
            'status': 201,
            'message': 'Registro creado correctamente',
            'data': alumn_serializer.data
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
      
      alumn_serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
      if alumn_serializer.is_valid():
         alumn_serializer.save()
         return Response({
            'status': 200,
            'message': 'Registro actualizado correctamente',
            'data': alumn_serializer.data
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

class CompanyViewSet(GenericViewSet):
   serializer_class = CompanySerializer

   def get_queryset(self):
      return self.get_serializer().Meta.model.objects.all()
   
   def get_object(self):
      return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
   
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

   def create(self, request):
      company_serializer = self.serializer_class(data=request.data)
      if company_serializer.is_valid():
         company_serializer.save()
         data = {
            'status': 201,
            'message': 'Registro creado correctamente',
            'data': company_serializer.data
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
      
      company_serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
      if company_serializer.is_valid():
         company_serializer.save()
         return Response({
            'status': 200,
            'message': 'Registro actualizado correctamente',
            'data': company_serializer.data
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


class JobViewSet(GenericViewSet):
   serializer_class = JobSerializer

   def get_queryset(self):
      return self.get_serializer().Meta.model.objects.all()
   
   def get_object(self):
      return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
   
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
   
   def create(self, request):
      job_serializer = self.serializer_class(data=request.data)
      if job_serializer.is_valid():
         job_serializer.save()
         data = {
            'status': 201,
            'message': 'Registro creado correctamente',
            'data': job_serializer.data
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
      
      job_serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
      if job_serializer.is_valid():
         job_serializer.save()
         return Response({
            'status': 200,
            'message': 'Registro actualizado correctamente',
            'data': job_serializer.data
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

class ApplicationViewSet(GenericViewSet):
   serializer_class = ApplicationSerializer

   def get_queryset(self):
      return self.get_serializer().Meta.model.objects.all()
   
   def get_object(self):
      return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
   
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
   
   def create(self, request):
      application_serializer = self.serializer_class(data=request.data)
      if application_serializer.is_valid():
         application_serializer.save()
         data = {
            'status': 201,
            'message': 'Registro creado correctamente',
            'data': application_serializer.data
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
      
      application_serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
      if application_serializer.is_valid():
         application_serializer.save()
         return Response({
            'status': 200,
            'message': 'Registro actualizado correctamente',
            'data': application_serializer.data
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