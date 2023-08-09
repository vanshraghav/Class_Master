from django.shortcuts import render,redirect
from django.http import HttpResponse
#from genetic import initialize_population, fitness_function, selection, crossover, mutation, genetic_algorithm
from .models import Faculty, Subject  # Import your models

# Create your views here.
def index(request):
    return render(request,'index.html')
def seating(request):
    res={}
    if request.method == "POST":
        exam=request.POST['exam']
        no_of_class=int(request.POST['no_of_class'])
        capacity=int(request.POST['capacity'])
        startin_roll=int(request.POST['start_roll'])
        ending_roll=int(request.POST['ending_roll'])
        classes = [[] for _ in range(no_of_class)]

        current_roll = startin_roll
        for i in range(no_of_class):
            for _ in range(capacity):
                if current_roll <= ending_roll:
                 classes[i].append(current_roll)
                current_roll += 1
        
        res={
            'exam':exam,
            'classes': enumerate(classes, 1),
            'noofclass':no_of_class
        }
    return render(request,'seating.html',res)
# def tt_1(request):
#     if request.method == "POST":
#         number_of_faculty=int(request.POST['number_of_faculty'])
#     return render(request,'tt_1.html')
# from django.shortcuts import render
# from .models import Faculty, Subject, Room  # Import your models

# def simple_timetable_optimization(faculties, subjects, rooms, days, time_slots):
#     timetable = {}

#     # Iterate through each day and time slot
#     for day in days:
#         for time_slot in time_slots:
#             for faculty in faculties:
#                 for subject in subjects:
#                     if subject in faculty.subjects and subject not in timetable.values():
#                         # Check if the faculty is available and the room is available
#                         if faculty.is_available(day, time_slot) and rooms.is_available(day, time_slot):
#                             timetable[(day, time_slot)] = subject
#                             break  # Move to the next time slot

#     return timetable

# def tt_2(request):
#     faculties = Faculty.objects.all()
#     subjects = Subject.objects.all()
#     rooms = Room.objects.all()  # Replace with your Room model
    
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#     time_slots = ['09:00 AM - 10:00 AM', '10:00 AM - 11:00 AM', ...]  # Define your time slots
    
#     timetable = simple_timetable_optimization(faculties, subjects, rooms, days, time_slots)
    
#     context = {
#         'timetable': timetable,
#     }
    
#     return render(request, 'timetable.html', context)

# views.py

# views.py

from django.shortcuts import render, redirect
from .form import SubjectForm
from .models import Subject, Timetable

def create_timetable(request):
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)  # Create an object but don't save yet
            # Check your conditions here using if statements
            if subject.duration > 0 and subject.practical_lectures:
                # Conditions met, save the subject to the timetable
                subject.save()
                # You might also want to associate the subject with a faculty and class
                timetable_entry = Timetable(subject=subject, faculty=request.user.faculty, classes=request.user.classes)
                timetable_entry.save()
                return redirect('view_timetable')  # Redirect to view timetable
            else:
                # Conditions not met, display an error message or handle appropriately
                error_message = "Conditions for adding subject not met."
                return render(request, 'create_timetable.html', {'subject_form': subject_form, 'error_message': error_message})
    else:
        subject_form = SubjectForm()
    return render(request, 'create_timetable.html', {'subject_form': subject_form})


def view_timetable(request):
    # Fetch timetable data and pass it to the template
    timetable_data = Timetable.objects.all()
    context = {
        'timetable_data': timetable_data,
    }
    return render(request, 'view_timetable.html', context)
