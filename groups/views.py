from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from subjects.models import Subject
from teachers.models import Teacher
from .models import Group

def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    subjects = Subject.objects.all()
    ctx = {
        'students': students,
        'teachers': teachers,
        'groups': groups,
        'subjects': subjects
           }
    return render(request, 'index.html', ctx)

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        student_ids = request.POST.getlist('student')
        if name and teacher_id and student_ids:
            teacher = get_object_or_404(Teacher, pk=teacher_id)
            group = Group.objects.create(
                name=name,
                teacher=teacher,
            )
            for student_id in student_ids:
                student = get_object_or_404(Student, pk=student_id)
                student.group = group
                student.save()
            return redirect('groups:list')
    ctx = {'teachers': teachers, 'students': students}
    return render(request, 'groups/form.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    teachers = Teacher.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        student_ids = request.POST.getlist('student')

        if name and teacher_id and student_ids:
            teacher = get_object_or_404(Teacher, pk=teacher_id)

            group.name = name
            group.teacher = teacher
            group.save()

            for student_id in student_ids:
                student = get_object_or_404(Student, pk=student_id)
                student.group = group
                student.save()
            return redirect(group.get_detail_url())
    ctx = {
        'group': group,
        'teachers': teachers,
        'students': students

    }
    return render(request, 'groups/form.html', ctx)

def group_del_conf(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:list')
    return render(request, 'groups/del_conf.html', {'group': group})
