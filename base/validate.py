from django import forms
from re import search, sub


# функция проверяет корректность введенного пользователем пароля
def validate_password(cleaned_data):
    valid_err = []
    if ('password' or 'password2') not in cleaned_data:
        valid_err.append(forms.ValidationError(
            'Пароль не должен быть пустым, содержать пробелы или символы табуляции'))
    else:
        password = cleaned_data['password']
        password2 = cleaned_data['password2']

        # проверка, что пользователь верно ввел пароль 2 раза
        if password != password2:
            valid_err.append(forms.ValidationError('Пароли не совпадают'))

        # проверка, что пароль не слишком короткий
        if len(password) < 8:
            valid_err.append(forms.ValidationError(
                'Пароль должен содержать не менее 8 символов'))

        # проверка, что пароль не слишком длинный
        if len(password) > 128:
            valid_err.append(forms.ValidationError(
                'Пароль должен содержать не более 128 символов'))

        # проверка, что пароль состоит только из латинских букв, арабских цифр и специальных символов
        if search("[^a-zA-Z0-9`\\-~!@#$%^&*()_+={}\[\]|:;'<>,.?\\\/]", password):
            valid_err.append(forms.ValidationError(
                'Пароль содержит недопустимые символы'))

    return valid_err


# функция проверяет корректность введенного имени/фамилии, str_name='name'/'surname' соответственно
def validate_name(cleaned_data, str_name='name'):
    valid_err = []

    if str_name not in cleaned_data:
        valid_err.append(forms.ValidationError(
            'Имя и фамилия не должны быть пустыми или содержать пробелы'))
    else:
        name = cleaned_data[str_name]
        if len(name) > 64:
            valid_err.append(forms.ValidationError(
                'Длина имени/фамилии не должна превышать 64 символа'))
        if not sub('[-]', '', name).isalpha():
            valid_err.append(forms.ValidationError(
                'Имя и фамилия должны состоять только из букв или тире'))
    return valid_err
