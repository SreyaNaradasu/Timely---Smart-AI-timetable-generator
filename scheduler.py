import csv
import random
from colorama import Fore, Style

# Define time slots and weekdays
time_slots = [
    "08:50–09:40", "09:40–10:30", "Break", "10:45–11:35", "11:35–12:25",
    "12:25–01:15", "Lunch Break", "02:05–02:55", "02:55–03:45", "03:45–04:35"
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Load faculty-subject mappings from CSV
def load_faculty_mapping(filename="faculty_course_allocation.csv"):
    mapping = {}

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("Semester") or not row.get("Section"):
                continue  # Skip malformed or blank rows

            semester = row["Semester"].strip()
            section = row["Section"].strip()
            subject = row.get("Subject", "").strip()
            faculty = row.get("Faculty", "").strip()
            course_code = row.get("Course Code", "").strip()
            venue = row.get("Venue", "").strip()

            if not subject:
                continue

            key = f"{semester}-{section}"
            if key not in mapping:
                mapping[key] = []

            mapping[key].append({
                "subject": subject,
                "faculty": faculty,
                "code": course_code,
                "venue": venue
            })

    return mapping

# Generate timetable based on semester and section
def generate_timetable(semester, section):
    mapping = load_faculty_mapping()
    key = f"{semester}-{section}"
    courses = mapping.get(key, [])

    if not courses:
        return {}  # No mapping found for this semester-section

    timetable = {}

    for day in days:
        timetable[day] = {}
        for slot in time_slots:
            if slot in ["Break", "Lunch Break"]:
                timetable[day][slot] = ""  # Always leave break slots empty
            elif random.random() < 0.25:
                timetable[day][slot] = ""  # 25% chance of being a free slot
            else:
                course = random.choice(courses)
                formatted = f"{course['code']}<br>{course['subject']}<br><i>{course['faculty']}</i>"
                timetable[day][slot] = formatted

    return timetable

# Debug output (optional)
if __name__ == "__main__":
    semester = "5"
    section = "B"
    timetable = generate_timetable(semester, section)

    print(Fore.CYAN + f"\n📅 Timetable for Semester {semester}, Section {section}\n" + Style.RESET_ALL)
    print("Day\t\t" + "\t".join(time_slots))
    for day in days:
        print(f"{day:10}", end="\t")
        for slot in time_slots:
            cell = timetable[day][slot]
            print("FREE" if cell == "" else "X", end="\t")
        print()

