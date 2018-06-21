import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

import random
from first_app.models import User, AccessRecord
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.free_email()
        fake_date = fakegen.date()

        new_user = User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]
        acc_rec = AccessRecord.objects.get_or_create(user=new_user,date=fake_date)[0]

if __name__ == '__main__':
    print('starting to populate')
    populate(20)
    print('done!')
