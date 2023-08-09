def simple_timetable_optimization(faculties, subjects, rooms, days, time_slots):
    timetable = {}

    # Iterate through each day and time slot
    for day in days:
        for time_slot in time_slots:
            for faculty in faculties:
                for subject in subjects:
                    if subject in faculty.subjects and subject not in timetable.values():
                        # Check if the faculty is available and the room is available
                        if faculty.is_available(day, time_slot) and rooms.is_available(day, time_slot):
                            timetable[(day, time_slot)] = subject
                            break  # Move to the next time slot

    return timetable
