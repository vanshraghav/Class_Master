import random
teachers = ["Teacher A", "Teacher B", "Teacher C"]
subjects = ["Math", "Science", "History"]
classes = ["Class X", "Class Y", "Class Z"]
time_slots = ["8:00 AM - 9:00 AM", "9:15 AM - 10:15 AM", "10:30 AM - 11:30 AM", "11:45 AM - 12:45 PM"]

import random

def has_clashes(schedule, day, slot, teacher, _class, subject):
    for existing_teacher, existing_schedule in schedule.items():
        for entry in existing_schedule:
            existing_day, existing_slot, existing_class, existing_subject = entry
            if existing_day == day and existing_slot == slot:
                if (existing_teacher == teacher and existing_class != _class) or \
                   (existing_teacher == teacher and existing_subject != subject) or \
                   (existing_class == _class and existing_teacher != teacher) or \
                   (existing_subject == subject and existing_teacher != teacher):
                    return True
    return False

# Predefined subject-to-teacher mappings
subject_teacher_mapping = {
    "Math": "Teacher A",
    "Science": "Teacher B",
    "History": "Teacher C",
    "M-2": "Teacher D",
    "Spos": "Teacher E"
}

teachers = ["Teacher A", "Teacher B", "Teacher C","Teacher D","Teacher E"]
subjects = list(subject_teacher_mapping.keys())  # Use the keys from the mapping
classes = ["Class X", "Class Y", "Class Z"]
time_slots = ["8:00 AM - 9:00 AM", "9:15 AM - 10:15 AM", "10:30 AM - 11:30 AM", "11:45 AM - 12:45 PM"]
import random
time_slots = [
    "8:00 AM - 9:00 AM",
    "9:15 AM - 10:15 AM",
    "10:30 AM - 11:30 AM",
    "11:45 AM - 12:45 PM",
]

# Create copies of teachers and subjects to avoid modifying the original lists
available_teachers = teachers.copy()
available_subjects = subjects.copy()

# Create an empty timetable dictionary
timetable = {}

# Generate timetable using a basic scheduling algorithm for a week (5 days)
for day in range(5):  # Assuming a 5-day work week
    for slot in time_slots:
        for _class in classes:
            if available_teachers and available_subjects:
                subject = random.choice(available_subjects)
                teacher = subject_teacher_mapping[subject]  # Retrieve teacher from mapping
                if teacher not in timetable:
                    timetable[teacher] = []
                timetable[teacher].append((day, slot, _class, subject))
                # Remove the teacher and subject from available options to prevent double allocation
                available_teachers.remove(teacher)
                available_subjects.remove(subject)

# Print the generated timetable for the week
for teacher, schedule in timetable.items():
    print(f"Teacher: {teacher}")
    for entry in schedule:
        day, slot, _class, subject = entry
        print(
            f"Day {day+1}, Slot: {slot}, Class: {_class}, Subject: {subject}"
        )
print(timetable)