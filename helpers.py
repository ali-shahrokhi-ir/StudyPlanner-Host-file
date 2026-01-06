# helpers.py

def parse_time_input(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def round_to_quarter(minutes):
    return round(minutes / 15) * 15


def format_time(minutes):
    hours = minutes // 60
    mins = minutes % 60

    if hours > 0 and mins > 0:
        return f"{hours} hour(s) and {mins} minute(s)"
    elif hours > 0:
        return f"{hours} hour(s)"
    else:
        return f"{mins} minute(s)"


def calculate_importance(score, total_score):
    percentage = (score / total_score) * 100

    if percentage < 50:
        return 5
    elif percentage < 65:
        return 4
    elif percentage < 80:
        return 3
    elif percentage < 90:
        return 2
    else:
        return 1


def generate_plan(lessons, free_time_str):
    total_minutes = parse_time_input(free_time_str)
    total_priority = 0

    # Step 1: calculate priority for each lesson
    for lesson in lessons:
        importance = calculate_importance(
            lesson["score"], lesson["total_score"]
        )
        weakness = lesson["total_score"] - (lesson["score"] - 1)

        lesson["importance"] = importance
        lesson["priority"] = weakness * importance
        total_priority += lesson["priority"]

    # Step 2: initial time allocation
    for lesson in lessons:
        raw_minutes = (lesson["priority"] / total_priority) * total_minutes
        rounded_minutes = round_to_quarter(raw_minutes)

        # Ensure no lesson gets removed
        if rounded_minutes < 15:
            rounded_minutes = 15

        lesson["minutes"] = rounded_minutes

    # Step 3: adjust total time to match available time
    current_total = sum(l["minutes"] for l in lessons)
    diff = current_total - total_minutes

    lessons.sort(key=lambda x: x["minutes"], reverse=True)

    i = 0
    while diff != 0:
        if diff > 0 and lessons[i]["minutes"] > 15:
            lessons[i]["minutes"] -= 15
            diff -= 15
        elif diff < 0:
            lessons[i]["minutes"] += 15
            diff += 15
        i = (i + 1) % len(lessons)

    # Step 4: final formatting
    for lesson in lessons:
        lesson["study_time"] = format_time(lesson["minutes"])

    return lessons
