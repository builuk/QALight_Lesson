import pytest
import Lesson13
from helper.user import data as user_data
from helper.compare_info import base_failure

def test_registration_success():
    assert Lesson13.registration(True,user_data.email,user_data.nick,user_data.password) == user_data.nick

def test_registration_failed():
    Lesson13.registration(True, user_data.email, user_data.nick, user_data.password)
    assert base_failure.user_email_register in Lesson13.registration(False,user_data.email,user_data.nick,user_data.password)