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
            print("Please enter a whole number.")


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
        print("Please enter the subject.")
        pause()
        return

    study_hours = get_number(
        "How many hours did you study today? (0-24): ", 0, 24
    )

    assignments = get_integer(
        "How many assignments do you have? (0-50): ", 0, 50
    )

    workload = get_number(
        "How would you rate your workload? (1-10): ", 1, 10
    )

    confidence = get_number(
        "How confident do you feel about your exams? (1-10): ", 1, 10
    )

    sleep_hours = get_number(
        "How many hours did you sleep last night? (0-24): ", 0, 24
    )

    entry = {
        "date": datetime.now().strftime("%d-%m-%Y"),
        "name": name,
        "subject": subject,
        "study_hours": study_hours,
        "assignments": assignments,
        "workload": workload,
        "confidence": confidence,
        "sleep_hours": sleep_hours
    }

    entries.append(entry)

    print("\nEntry saved.")
    print("Student :", name)
    print("Subject :", subject)
    print("Keep going. Small progress adds up.")

    pause()


def average(key):
    if not entries:
        return 0

    total = 0
    for entry in entries:
        total += entry[key]

    return total / len(entries)


def most_studied_subject():
    if not entries:
        return "No data"

    subject_hours = {}

    for entry in entries:
        subject = entry["subject"]
        subject_hours[subject] = subject_hours.get(subject, 0)
        subject_hours[subject] += entry["study_hours"]

    highest_subject = ""
    highest_hours = -1

    for subject in subject_hours:
        if subject_hours[subject] > highest_hours:
            highest_hours = subject_hours[subject]
            highest_subject = subject

    return highest_subject


def get_pulse_status():
    if not entries:
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
    return "NEEDS ATTENTION"


def dashboard():
    line()
    print("CAMPUS PULSE - DASHBOARD")
    line()

    if not entries:
        print("No entries yet. Add a daily entry first.")
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

    if not entries:
        print("No study history available.")
        pause()
        return

    for number, entry in enumerate(entries, start=1):
        print("\nEntry", number)
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

    if not entries:
        print("No data available. Add a daily entry first.")
        pause()
        return

    study = average("study_hours")
    workload = average("workload")
    confidence = average("confidence")
    sleep = average("sleep_hours")

    priorities = []

    if confidence < 5:
        priorities.append("Spend some time revising your difficult topics.")

    if study < 3:
        priorities.append("Try to get a little more focused study time today.")

    if workload >= 8:
        priorities.append("Start with the most important assignment first.")

    if sleep < 6:
        priorities.append("Try to get some proper rest before the next study session.")

    if not priorities:
        priorities.append("Your routine looks balanced. Keep the same consistency.")

    for number, priority in enumerate(priorities, start=1):
        print(str(number) + ".", priority)

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

    if not entries:
        print("No data available.")
        pause()
        return

    subjects = {}

    for entry in entries:
        subject = entry["subject"]

        if subject not in subjects:
            subjects[subject] = {"hours": 0, "count": 0}

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

    if not entries:
        print("There is nothing to delete yet.")
        pause()
        return

    last = entries[-1]

    print("Student :", last["name"])
    print("Subject :", last["subject"])
    print("Date    :", last["date"])

    choice = input("\nDelete this entry? (y/n): ").strip().lower()

    if choice == "y":
        entries.pop()
        print("The last entry was deleted.")
    else:
        print("Okay, the entry was kept.")

    pause()


def quick_study_checkin():
    line()
    print("QUICK STUDY CHECK-IN")
    line()

    if not entries:
        print("Add at least one daily entry before using this option.")
        pause()
        return

    study = average("study_hours")
    workload = average("workload")
    confidence = average("confidence")
    sleep = average("sleep_hours")

    print("Here is a quick look at how things are going.\n")

    if study >= 5:
        print("Study: You are putting in a solid amount of time.")
    elif study >= 3:
        print("Study: You are getting some work done. A little more consistency could help.")
    else:
        print("Study: Your study time is quite low. Even one focused session can help.")

    if confidence >= 7:
        print("Confidence: You seem comfortable with your preparation.")
    elif confidence >= 4:
        print("Confidence: You are in the middle. More practice may make you feel more ready.")
    else:
        print("Confidence: You may need some extra revision before the exams.")

    if workload >= 8:
        print("Workload: You have a lot on your plate. Take one task at a time.")
    elif workload >= 5:
        print("Workload: Your workload is manageable, but keep an eye on deadlines.")
    else:
        print("Workload: Things look fairly comfortable right now.")

    if sleep < 6:
        print("Sleep: Try not to ignore rest. It can make studying harder when you are tired.")
    else:
        print("Sleep: Your average sleep is looking okay.")

    print("\nOne simple suggestion:")
    if confidence < 5:
        print("Pick one weak topic and revise it today.")
    elif workload >= 8:
        print("Finish your most urgent task before starting something new.")
    elif study < 3:
        print("Set aside one distraction-free study session today.")
    else:
        print("Keep the routine steady and focus on regular revision.")

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
        print("7. Quick Study Check-in")
        print("8. Exit")

        line()

        choice = input("Enter your choice: ").strip()

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
            quick_study_checkin()
        elif choice == "8":
            print("\nThanks for using Campus Pulse!")
            print("Keep studying at your own pace. Good luck!")
            break
        else:
            print("\nPlease enter a number from 1 to 8.")
            pause()


if __name__ == "__main__":
    main()
