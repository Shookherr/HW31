import datetime

from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    age = (datetime.date.today() - birth_date).days // 365  # 18-00

    if age < 9:
        raise ValidationError(f'Пользователь слишком молод ({age} лет) для регистрации.')


def check_email(email):
    if 'rambler.ru' in email:
        raise ValidationError('It is not allowed to register addresses of the RAMBLER domain.')
