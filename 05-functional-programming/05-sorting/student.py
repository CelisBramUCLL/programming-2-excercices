def sort_by_age(people):
    return sorted(people, key=lambda people: people.age)


def sort_by_decreasing_age(people):
    return sorted(people, reverse=True, key=lambda people: people.age)


def sort_by_name(people):
    return sorted(people, key=lambda people: people.name)


def sort_by_name_then_age(people):
    return sorted(people, key=lambda people: (people.name, people.age))


def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda people: (people.name, -people.age))
