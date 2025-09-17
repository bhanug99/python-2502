def student_grade_tracker():
    stud_id = input("Enter Student ID : ")
    stud_name = input("Enter Student Name : ")
    attendance = float(input("Enter Attendance Percentage : "))
    scores = []
    while True:
        score = float(input("Enter your Score : "))
        scores.append(score)

        more = input("Do you want to add more marks (yes / no): ").strip().lower()
        if more != "yes":
            break
    total_score = sum(scores)
    avg_score = total_score / len(scores)
    nos_entries = len(scores)
    # Grade Calculator
    if avg_score >= 85:
        grade = "A"
    elif 70 <= avg_score < 85:
        grade = "B"
    elif 50 <= avg_score < 70:
        grade = "C"
    else:
        grade = "Fail"

     # Attendance criteria
    if attendance < 75:
        attendance_status = "WARNING: LOW ATTENDANCE"
    else:
        attendance_status = "OK: GOOD ATTENDANCE"
    # Award eligibility
    if attendance >= 75 and grade == "A":
        award = "Eligible for Award 🏆"
    else:
        award = "Not Eligible for Award"
    # Output
    print("\n--- STUDENT REPORT ---")
    print(f"Student ID       : {stud_id}")
    print(f"Student Name     : {stud_name}")
    print(f"Attendance       : {attendance}%")
    print(f"Total Score      : {total_score}")
    print(f"Average Score    : {avg_score:.2f}")
    print(f"Number of Scores : {nos_entries}")
    print(f"Student Grade    : {grade}")
    print(f"Attendance Status: {attendance_status}")
    print(f"Award Eligibility: {award}")
    # Run the tracker
student_grade_tracker()