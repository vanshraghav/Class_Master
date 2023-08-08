from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .genetic_algorithm import initialize_population, fitness_function, selection, crossover, mutation, genetic_algorithm
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
def tt_1(request):
    if request.method == "POST":
        number_of_faculty=int(request.POST['number_of_faculty'])
    return render(request,'tt_1.html')

def tt_2(request):
    if request.method == "POST":
        # Get the data from the submitted form
        number_of_faculty = int(request.POST['number_of_faculty'])
        faculty_names = request.POST.getlist('faculty_name')
        class_names = request.POST.getlist('class_name[]')
        subject_names = request.POST.getlist('subject_name[]')
        subject_durations = request.POST.getlist('subject_duration[]')
        practical_lectures = request.POST.getlist('practical_lectures[]')
        practical_batches = request.POST.getlist('practical_batches[]')

        # Create Faculty, Subject instances based on form data
        faculties = []
        for i in range(number_of_faculty):
            subjects = []
            if practical_lectures[i] == 'yes':
                subjects.append(Subject(name='Practical', is_practical=True))
            for j in range(len(subject_names[i])):
                subjects.append(Subject(name=subject_names[i][j], is_practical=False))
            faculties.append(Faculty(name=faculty_names[i], subjects=subjects, year=class_names[i]))

        # Prepare data for Genetic Algorithm
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']  # List of available days
        slot_availability = {
            '08:00 AM': 1,
            '09:00 AM': 1,
            '10:00 AM': 1,
            # ... define other time slots and their initial availability
        }

        # Call the Genetic Algorithm to generate the timetable
        best_timetable = genetic_algorithm(faculties, days, slot_availability)

        # Prepare data for rendering
        timetable_data = []
        for faculty_name, faculty_slots in best_timetable.items():
            faculty = Faculty.objects.get(name=faculty_name)  # Assuming you have a Faculty model
            slots_assigned = []
            for subject, slot in faculty_slots:
                slots_assigned.append({
                    'subject': subject,
                    'slot': slot,
                })
                # Adjust slot availability for practicals
                if subject.is_practical:
                    slot_duration = 2
                else:
                    slot_duration = 1
                for i in range(slot_duration):
                    slot_availability[slot + i] -= slot_duration

            timetable_data.append({
                'faculty': faculty,
                'slots_assigned': slots_assigned,
            })

        context = {
            'timetable_data': timetable_data,
        }

        return render(request, 'timetable_result.html', context)

    return render(request, 'tt-2.html')  # Render the initial form if it's not a POST request
