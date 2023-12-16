import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_gender: str
    user_phone_number: str
    month: str
    year: str
    day: str
    user_subject: str
    user_hobby: str
    user_picture: str
    user_current_address: str
    user_state: str
    user_city: str


alex = User(
    first_name='Alex',
    last_name='Davydov',
    user_email='Alex@gmail.com',
    user_gender='Male',
    user_phone_number='8005553535',
    month='June',
    year='1992',
    day='20',
    user_subject='English',
    user_hobby='Reading',
    user_picture='selfies.jpeg',
    user_current_address='South Street',
    user_state='Haryana',
    user_city='Karnal',
)
