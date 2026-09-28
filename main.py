from datetime import datetime

entries = []


def line():
    print("=" * 55) 


def pause():
    input("\nPress Enter to continue...")


def get_number(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print("Enter a value between", minimum, "and", maximum)

        except ValueError:
            print("Please enter a valid number.")


def get_integer(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print("Enter a whole number between", minimum, "and", maximum)

        except ValueError:
            print("Please enter a valid whole number.")


def add_entry():
    line()
    print("ADD DAILY ENTRY")
    line()

    name = input("Student name: ").strip()

    if name == "":
        print("Please enter your name.")
        pause()
        return

    subject = input("Subject studied: ").strip()

    if subject == "":
        print("Please enter the subject you studied.")
        pause()
        return

    study_hours = get_number(
        "How many hours did you study today? (0-24): ",
        0,
        24
    )

    assignments = get_integer(
        "How many assignments do you have? ",
        0,
        50
    )

    workload = get_number(
        "How would you rate your workload? (1-10): ",
        1,
        10
    )

    confidence = get_number(
        "How confident do you feel about your exams? (1-10): ",
        1,
        10
    )

    sleep_hours = get_number(
        "How many hours did you sleep last night? (0-24): ",
        0,
        24
    )

    new_entry = {
        "date": datetime.now().strftime("%d-%m-%Y"),
        "name": name,
        "subject": subject,
        "study_hours": study_hours,
        "assignments": assignments,
        "workload": workload,
        "confidence": confidence,
        "sleep_hours": sleep_hours
    }

    entries.append(new_entry)

    print("\nYour entry has been added.")
    print("Student:", name)
    print("Subject:", subject)

    pause()

def average(key):
    if len(entries) == 0:
        return 0

    total = 0

    for entry in entries:
        total += entry[key]

    return total / len(entries)


def most_studied_subject():
    if len(entries) == 0:
        return "No data"

    subject_hours = {}

    for entry in entries:
        subject = entry["subject"]
        hours = entry["study_hours"]

        if subject in subject_hours:
            subject_hours[subject] += hours
        else:
            subject_hours[subject] = hours

    highest_subject = ""
    highest_hours = -1

    for subject in subject_hours:
        if subject_hours[subject] > highest_hours:
            highest_hours = subject_hours[subject]
            highest_subject = subject

    return highest_subject


def get_pulse_status():
    if len(entries) == 0:
        return "No data available"

    study = average("study_hours")
    workload = average("workload")
    confidence = average("confidence")

    score = 0

    if study >= 5:
        score += 3
    elif study >= 3:
        score += 2
    else:
        score += 1

    if workload <= 4:
        score += 3
    elif workload <= 7:
        score += 2
    else:
        score += 1

    if confidence >= 7:
        score += 3
    elif confidence >= 4:
        score += 2
    else:
        score += 1

    if score >= 8:
        return "GOOD"
    elif score >= 6:
        return "MODERATE"
    else:
        return "NEEDS ATTENTION"


def dashboard():
    line()
    print("CAMPUS PULSE - DASHBOARD")
    line()

    if len(entries) == 0:
        print("No entries available.")
        print("Add a daily entry first.")
        pause()
        return

    study = average("study_hours")
    assignments = average("assignments")
    workload = average("workload")
    confidence = average("confidence")
    sleep = average("sleep_hours")

    print("Total entries      :", len(entries))
    print("Average study time :", format(study, ".2f"), "hours")
    print("Average assignments:", format(assignments, ".2f"))
    print("Average workload   :", format(workload, ".2f"), "/10")
    print("Average confidence :", format(confidence, ".2f"), "/10")
    print("Average sleep      :", format(sleep, ".2f"), "hours")
    print("Most studied       :", most_studied_subject())
    print("Campus Pulse       :", get_pulse_status())

    print("\nStudy Level")

    if study >= 5:
        print("[##########] Excellent")
    elif study >= 3:
        print("[######----] Good")
    else:
        print("[###-------] Low")

    print("\nConfidence Level")

    if confidence >= 7:
        print("[##########] High")
    elif confidence >= 4:
        print("[######----] Average")
    else:
        print("[###-------] Low")

    print("\nWorkload Level")

    if workload <= 4:
        print("[###-------] Low")
    elif workload <= 7:
        print("[######----] Moderate")
    else:
        print("[##########] High")

    pause()


def view_history():
    line()
    print("STUDY HISTORY")
    line()

    if len(entries) == 0:
        print("No study history available.")
        pause()
        return

    for i, entry in enumerate(entries, start=1):
        print("\nEntry", i)
        print("-" * 40)
        print("Date        :", entry["date"])
        print("Student     :", entry["name"])
        print("Subject     :", entry["subject"])
        print("Study hours :", entry["study_hours"])
        print("Assignments :", entry["assignments"])
        print("Workload    :", entry["workload"], "/10")
        print("Confidence  :", entry["confidence"], "/10")
        print("Sleep       :", entry["sleep_hours"], "hours")

    pause()


def todays_priority():
    line()
    print("TODAY'S PRIORITY")
    line()

    if len(entries) == 0:
        print("No data available.")
        print("Add a daily entry first.")
        pause()
        return

    study = average("study_hours")
    workload = average("workload")
    confidence = average("confidence")
    sleep = average("sleep_hours")

    priorities = []

    if confidence < 5:
        priorities.append("Spend some time preparing for exams and revising difficult topics.")

    if study < 3:
        priorities.append("Try to increase your focused study time.")

    if workload >= 8:
        priorities.append("Finish the most important assignments first.")

    if sleep < 6:
        priorities.append("Try to follow a better sleep schedule.")

    if len(priorities) == 0:
        priorities.append("Keep following your current routine and revise regularly.")

    for i, priority in enumerate(priorities, start=1):
        print(str(i) + ".", priority)

    print("\nRecommended focus:")

    if confidence < 5:
        print("-> Exam preparation")
    elif workload >= 8:
        print("-> Assignments")
    elif study < 3:
        print("-> Regular study")
    else:
        print("-> Revision and practice")

    pause()


def subject_analysis():
    line()
    print("SUBJECT ANALYSIS")
    line()

    if len(entries) == 0:
        print("No data available.")
        pause()
        return

    subjects = {}

    for entry in entries:
        subject = entry["subject"]

        if subject not in subjects:
            subjects[subject] = {
                "hours": 0,
                "count": 0
            }

        subjects[subject]["hours"] += entry["study_hours"]
        subjects[subject]["count"] += 1

    for subject in subjects:
        hours = subjects[subject]["hours"]
        count = subjects[subject]["count"]

        print("\nSubject:", subject)
        print("Total study hours:", format(hours, ".2f"))
        print("Number of entries:", count)

    pause()


def delete_last_entry():
    line()
    print("DELETE LAST ENTRY")
    line()

    if len(entries) == 0:
        print("There is nothing to delete yet.")
        pause()
        return

    last = entries[-1]

    print("Student :", last["name"])
    print("Subject :", last["subject"])
    print("Date    :", last["date"])

    choice = input("\nDelete this entry? (y/n): ").lower()

    if choice == "y":
        entries.pop()
        print("The last entry was deleted.")
    else:
        print("Okay, the entry was kept.")

    pause()


def about_project():
    line()
    print("ABOUT CAMPUS PULSE")
    line()

    print("""
Campus Pulse is a simple Python program for keeping track
of daily student activities and study habits.

It records:
- Study hours
- Assignments
- Workload
- Exam confidence
- Sleep hours
- Subjects studied

The program uses this information to show a basic summary
and suggest what the student can focus on.

Python concepts used:
- Lists
- Dictionaries
- Functions
- Loops
- If-else statements
- Basic calculations
- Date and time
""")

    pause()


def main():
    while True:
        line()
        print("CAMPUS PULSE")
        print("Student Activity Analyzer")
        line()

        print("1. Add Daily Entry")
        print("2. View Dashboard")
        print("3. View Study History")
        print("4. Today's Priority")
        print("5. Subject Analysis")
        print("6. Delete Last Entry")
        print("7. About Project")
        print("8. Exit")

        line()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            dashboard()
        elif choice == "3":
            view_history()
        elif choice == "4":
            todays_priority()
        elif choice == "5":
            subject_analysis()
        elif choice == "6":
            delete_last_entry()
        elif choice == "7":
            about_project()
        elif choice == "8":
            print("\nThank you for using Campus Pulse!")
            print("Have a productive day!")
            break
        else:
            print("\nInvalid choice. Please select 1-8.")
            pause()


if __name__ == "__main__":
    main()
