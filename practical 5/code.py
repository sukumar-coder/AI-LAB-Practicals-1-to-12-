
# Rule-Based Expert System
# Student Performance Advisory System

def student_expert_system():

    print("===================================")
    print(" STUDENT PERFORMANCE EXPERT SYSTEM")
    print("===================================")

    attendance = int(input("Enter attendance percentage: "))
    study_hours = float(input("Enter daily study hours: "))
    assignments = input("Are assignments completed? (yes/no): ").lower()
    test_score = int(input("Enter test score (0-100): "))

    print("\n--- EXPERT SYSTEM ANALYSIS ---")

    # Rule 1
    if attendance < 75:
        print("Advice: Improve attendance.")
        print("Reason: Attendance is below 75%.")

    # Rule 2
    if study_hours < 2:
        print("Advice: Increase daily study hours.")
        print("Reason: Study time is insufficient.")

    # Rule 3
    if assignments == "no":
        print("Advice: Complete pending assignments.")
        print("Reason: Assignments are incomplete.")

    # Rule 4
    if test_score < 40:
        print("Performance: Poor")
        print("Advice: Seek additional academic support.")

    # Rule 5
    elif test_score < 60:
        print("Performance: Average")
        print("Advice: Practice more questions.")

    # Rule 6
    elif test_score < 80:
        print("Performance: Good")
        print("Advice: Continue regular preparation.")

    # Rule 7
    else:
        print("Performance: Excellent")
        print("Advice: Maintain your performance.")

    # Overall Result
    if (attendance >= 75 and study_hours >= 2
            and assignments == "yes" and test_score >= 60):
        print("\nOverall Result: Good Academic Performance")
    else:
        print("\nOverall Result: Improvement Required")


# Run Expert System
student_expert_system()
