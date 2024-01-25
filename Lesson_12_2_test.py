import pytest
import Lesson_12_2
import user_data

def test_registration_success():
    assert Lesson_12_2.registration() == user_data.email
