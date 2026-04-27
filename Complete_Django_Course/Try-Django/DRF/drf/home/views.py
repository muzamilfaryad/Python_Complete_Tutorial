from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# /api/index
@api_view(['GET', 'POST', 'PUT', 'PATCH'])


def index(request):
    courses = {
        "course_name": "python",
        "learn": ["flask", "Django", "Fast Api"],
        "Course_Provider": "Muzamil"
    }
    if request.method == 'GET':
        # /api/index/?search=muzamil
        # /api/index/?search=ali
      print(request.GET.get('search'))
      print('GET Method')
      return Response(courses)

    elif request.method == 'POST':
        print('********************')
        data = request.data
        #print(data['name'])
        print(data)
        print('********************')

        print('Post Method')
        return Response(courses)

    elif request.method == 'PUT':
      print('PUT Method')
      return Response(courses)




from home.serializers import PersonSerializer, loginSerializer, RegisterSerializer
from .models import Person

# @api_view(['GET', 'POST'])
# def person(request):
#     if request.method == 'GET':
#         objs = Person.objects.all()
#         serializer = PersonSerializer(objs, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = request.data
#         serializer = PersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PUT':
#PUT method is used to update the entire record. 
# For example, if we want to update the name and 
# age of a person, we can use the PUT method and 
# send the following data:
# {
#     "id": 1,
#     "name": "Ali",
#     "age": 30
# }
        data = request.data
        person_id = data.get('id')
        if person_id is None:
            return Response({'error': 'id is required for PUT'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PATCH':
# PATCH method is used to update a specific field 
# of the record. For example, if we want to update 
# only the age of a person, we can use the PATCH 
# method and send the following data:
#   {
#     "id": 1,
#     "age": 25
#   }
        data = request.data
        person_id = data.get('id')
        if person_id is None:
            return Response({'error': 'id is required for PATCH'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        person_id = data.get('id')
        if person_id is None:
            return Response({'error': 'id is required for DELETE'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response('Deleted', status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    data = request.data
    print(data)
    serializer = loginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'Login successful'})

    return Response(serializer.errors)




#APIView is a class-based view that provides a way 
# to handle HTTP requests in a more structured way. 
# It allows you to define methods for each HTTP 
# method (GET, POST, PUT, PATCH, DELETE) and 
# provides a way to handle authentication, 
# permissions, and throttling. It also provides a 
# way to handle serialization and deserialization 
# of data.
from rest_framework.views import APIView
from django.core.paginator import Paginator
class PersonAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        objs = Person.objects.all()
        page = request.GET.get('page', 1)
        page_size = 3
        try:
            page = int(page)  # Convert string to integer
            paginator = Paginator(objs, page_size)
            page_obj = paginator.page(page)
        except Exception as e:
            return Response({'error': 'Invalid page number'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(page_obj.object_list, many=True)
        return Response({
            'data': serializer.data,
            'page': page,
            'total_pages': paginator.num_pages,
            'total_count': paginator.count
        })

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request):
        data = request.data
        person_id = data.get('id')
        if person_id is None:
            return Response({'error': 'id is required for PUT'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def patch(self, request):
        data = request.data
        person_id = data.get('id')
        if person_id is None:
            return Response({'error': 'id is required for PATCH'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request):
        data = request.data
        person_id = data.get('id')
        if person_id is None:
            return Response({'error': 'id is required for DELETE'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response('Deleted', status=status.HTTP_200_OK)


from rest_framework import viewsets

from rest_framework.decorators import action

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        print('List Method')
        search = request.GET.get('search')
        queryset = self.get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)
        serializer = PersonSerializer(queryset, many=True)
        
        return Response({'status': 200 , 'data': serializer.data})

    @action(detail=False, methods=['post'])
    def send_mail_to_person(self, request):
        return Response({'message': 'Mail sent to person'})




class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    'status':False, 
                    'message': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return  Response(
            {
                'status': True,
                'message': 'User registered successfully'
            }, status=status.HTTP_201_CREATED
        )


from django.contrib.auth import authenticate
class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = loginSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {'status': False, 'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is None:
            return Response(
                {'status': False, 'message': 'Invalid credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'status': True,
                'message': 'Login successful',
                'token': str(token)
            },
            status=status.HTTP_200_OK
        )







