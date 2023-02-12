from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Создает случайных пользователей'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Указывает сколько пользователей необходимо создать')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            CustomUser.objects.create_user(username=get_random_string(7), email='', password='1234567890')