# Timely – Smart AI Timetable Generator

Welcome to **Timely**, a smart and modern web-based timetable generator built for academic institutions. It automatically creates optimized weekly class schedules based on semester and section selections, intelligently assigning faculty, courses, and venues using a CSV file.

---

## Features

AI-driven dynamic timetable generation  
Faculty, course, and room mapping from CSV  
Smart handling of breaks, lunch, and free periods  
Beautiful, responsive UI with animations  
Randomized empty slots to reduce over-scheduling  
Easy to customize and scale



## Tech Stack

| Layer         | Tech Used                          |
|---------------|-------------------------------------|
| Frontend      | HTML, CSS, JavaScript, Jinja2       |
| Backend       | Python, Flask                       |
| Data Source   | CSV (`faculty_course_allocation.csv`) |
| Deployment    | GitHub + Local Flask Server         |


Smart AI Timetable Generator (CSP-based)
AI-driven scheduler built using Constraint Satisfaction Problem (CSP) techniques.

Automatically generates conflict-free timetables for classes, teachers, and rooms.

Handles hard constraints like:

No teacher or student group in two places at once

Room availability and capacity

Subject-teacher mapping

Supports soft constraints like:

Preferred time slots

Balanced workload across days

Uses backtracking, forward checking, and MRV heuristics for efficient solving.

Customizable for schools, colleges, and training institutions.

Built using Python (or your language of choice) and supports JSON/CSV input for data


