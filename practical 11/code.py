
# Logical Reasoning using Propositional Logic

# Propositions
assignments_completed = True
attendance_75 = True

# Knowledge Base
# If assignments are completed AND attendance is >= 75%,
# then the student is eligible.

def logical_inference(assignments, attendance):
    eligible = assignments and attendance

    print("Knowledge Base:")
    print("1. Assignments must be completed.")
    print("2. Attendance must be at least 75%.")
    print("3. If both conditions are true, student is eligible.")

    print("\nFacts:")
    print("Assignments Completed:", assignments)
    print("Attendance >= 75%:", attendance)

    print("\nLogical Inference:")

    if eligible:
        print("Conclusion: Student is ELIGIBLE for examination.")
    else:
        print("Conclusion: Student is NOT ELIGIBLE for examination.")

    return eligible


logical_inference(assignments_completed, attendance_75)
