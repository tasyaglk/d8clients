from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
        Пользовательский менеджер, через который
        создаются запросы к модели user
    """

    # создание обычного пользователя
    def create_user(self, email, name, surname, password, **extra_fields):

        if not email:
            raise ValueError('Укажите e-mail')
        if not name:
            raise ValueError('Укажите свое имя')
        if not surname:
            raise ValueError('Укажите свою фамилию')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # создание пользователя с правами администратора (самого веб-приложения)
    def create_superuser(self, email, name, surname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Атрибут is_staff должен быть равен True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Атрибут is_superuser должен быть равен True')
        return self.create_user(email, name=name, surname=surname, password=password, **extra_fields)
