import pytest
from search import *
from student import Student


@pytest.mark.parametrize(
    "students",
    [
        [],
        [Student(id) for id in range(0, 100)],
        [Student(id) for id in [4, 5, 6, 11, 15, 16, 17, 18, 25, 27, 55, 56, 59, 70]],
    ],
)
@pytest.mark.parametrize("target_id", range(0, 100))
def test_find_student_with_id(students, target_id):
    assert linear_search(students, target_id) == binary_search(students, target_id)
