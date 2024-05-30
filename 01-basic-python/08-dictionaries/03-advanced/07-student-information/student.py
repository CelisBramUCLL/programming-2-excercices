# Write your code here


def process_data(string_data):
    dict = {}
    for i in range(0, len(string_data)):
        strings = string_data[i].split(",")
        dict[strings[0]] = {"age": int(strings[1]), "courses": strings[2:]}
    return dict


def average_age(data):
    sum_age = 0
    for key in data:
        sum_age += data[key]["age"]

    return sum_age / len(data)


def courses(data):
    courses = set()
    for i in data:
        for course in data[i]["courses"]:
            courses.add(course)

    return courses


def most_common_courses(data):
    course_dict = {}
    for key in data:
        for course in data[key]["courses"]:
            if course in course_dict.keys():
                course_dict[course] += 1
            else:
                course_dict[course] = 1

    highest = 0
    most_common_courses = []
    for k, v in course_dict.items():
        if v > highest:
            highest = v
            most_common_courses.clear()
            most_common_courses.append(k)
        elif v == highest:
            most_common_courses.append(k)

    return set(most_common_courses)
