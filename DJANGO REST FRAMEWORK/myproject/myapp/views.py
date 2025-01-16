from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .studentserializers import StudentSerializer

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)  # Deserialize incoming data
    
    if serializer.is_valid():  # Check if the data is valid
        serializer.save()  # Save the new student to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # HTTP 201 Created
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # HTTP 400 Bad Request

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()  # Retrieve all student records
    serializer = StudentSerializer(students, many=True)  # Serialize multiple records
    return Response(serializer.data)

@api_view(['GET'])
def get_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)  # Retrieve student by ID
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['PUT'])
def update_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)  # Retrieve student by ID
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data)  # Deserialize incoming data
    if serializer.is_valid():
        serializer.save()  # Save updated student information to the database
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)  # Retrieve student by ID
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    student.delete()  # Delete the student record
    return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
