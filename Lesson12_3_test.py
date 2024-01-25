import pytest
import Lesson12_3
import user_data

def test_registration_success():
    assert Lesson12_3.registration(user_data.email,user_data.nick,user_data.password) == user_data.nick
