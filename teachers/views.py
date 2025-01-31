from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from subjects.models import Subject

def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)

def teacher_create(request):
    if request.method == 'POST':
        name = request.POST.get('firstName')
        familiya = request.POST.get('lastName')
        fan_id = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        if name and familiya and fan_id and phone and email and experience and image:
            subject = get_object_or_404(Subject, pk=fan_id)
            Teacher.objects.create(
                first_name=name,
                last_name=familiya,
                subject=subject,
                phone_number=phone,
                email=email,
                experience=experience,
                image=image
            )
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    return render(request, 'teachers/form.html', {'subjects': subjects})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/teacher-detail.html', {'teacher': teacher})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    name = request.POST.get('firstName')
    familiya = request.POST.get('lastName')
    fan_id = request.POST.get('subject')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    experience = request.POST.get('experience')
    image = request.FILES.get('image')
    if name and familiya and fan_id and phone and email and experience and image:
        subject = get_object_or_404(Subject, pk=fan_id)
        teacher.first_name = name
        teacher.last_name = familiya
        teacher.subject = subject
        teacher.phone_number = phone
        teacher.email = email
        teacher.experience = experience
        teacher.image = image
        teacher.save()
        return redirect(teacher.get_detail_url())
    subjects = Subject.objects.all()
    return render(request, 'teachers/form.html', {'teacher': teacher, 'subjects': subjects})

def teacher_del_conf(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers:list')
    return render(request, 'teachers/del_conf.html', {'teacher': teacher})
