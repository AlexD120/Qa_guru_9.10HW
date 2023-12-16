from qa_guru_9_10HW.page.registration_page import RegistrationPage
from qa_guru_9_10HW.data.user import User, alex


def test_practice_form():
    registration_page = RegistrationPage()
    registration_page.register(alex)
    registration_page.should_registered_user_with(alex)
