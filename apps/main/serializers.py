from rest_framework.serializers import ModelSerializer
from apps.main.models import Alumn, Company, Job, Applications

class AlumnSerializer(ModelSerializer):
   class Meta:
      model = Alumn
      fields = '__all__'


class CompanySerializer(ModelSerializer):
   class Meta:
      model = Company
      fields = '__all__'


class JobSerializer(ModelSerializer):
   class Meta:
      model = Job
      fields = '__all__'

class JobUpdateSerializer(ModelSerializer):
   class Meta:
      model = Job
      fields = ['title', 'workplace', 'ubication', 'job_type', 'description', 'salary', 'status']


class ApplicationSerializer(ModelSerializer):
   class Meta:
      model = Applications
      fields = '__all__'


class ApplicationUpdateSerializer(ModelSerializer):
   class Meta:
      model = Applications
      fields = ['id_job', 'id_alumn', 'status', 'message', 'interview_date', ]