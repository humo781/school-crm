from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from ..students.models import Student
from ..teachers.models import Teacher

def students_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)


def student_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if full_name and date_of_birth and phone_number and address and image:
            Student.objects.create(
                full_name=full_name,
                date_of_birth=date_of_birth,
                phone_number=phone_number,
                address=address,
                image=image
            )
            return redirect('students:list')
    return render(request, 'students/form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if full_name and date_of_birth and phone_number and address and image:
            student.full_name = full_name
            student.date_of_birth = date_of_birth
            student.phone_number = phone_number
            student.address = address
            student.image = image
            student.save()
            return redirect('groups:list')
    ctx = {'student': student}
    return render(request, 'groups/form.html', ctx)

def student_del_confirm(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('groups:list')
    ctx = {'student': student}
    return render(request, 'students/del-confirm.html', ctx)
