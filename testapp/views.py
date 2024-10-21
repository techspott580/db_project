from django.shortcuts import render

# Create your views here.
from testapp.models import Student
def student_view(request):
    #student_list = Student.objects.all()
    #student_list = Student.objects.filter(marks__lt=35)
    #student_list = Student.objects.filter(name__startswith='A')
    student_list = Student.objects.all().order_by('-marks')
    my_dict = {'student_list':student_list}
    return render(request,'std.html',my_dict)