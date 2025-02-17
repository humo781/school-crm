from django.shortcuts import render, redirect, get_object_or_404

from groups.models import Group
from .models import Student

def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)

def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_id = request.POST.get('group')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        group = get_object_or_404(Group, pk=group_id)
        if first_name and last_name and group_id and dob and photo and phone and address:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                group=group,
                birth_of_date=dob,
                phone_number=phone,
                address=address,
                image=photo
            )
            return redirect('students:list')
    groups = Group.objects.all()
    return render(request, 'students/form.html', {'groups': groups})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_id = request.POST.get('group')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        group = get_object_or_404(Group, pk=group_id)
        if first_name and last_name and group and dob and photo and phone and address:
            student.first_name = first_name
            student.last_name = last_name
            student.group = group
            student.birth_of_date = dob
            student.phone_number = phone
            student.address = address
            student.image = photo
            student.save()
            return redirect(student.get_detail_url())
    groups = Group.objects.all()
    ctx = {'student': student, 'groups': groups}
    return render(request, 'students/form.html', ctx)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)

def student_del_conf(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    return render(request, 'students/del_conf.html', {'student': student})
