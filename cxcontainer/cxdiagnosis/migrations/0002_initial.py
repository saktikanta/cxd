from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.auth.hashers import make_password

def create_user(apps, schema_editor):
    User = apps.get_model('cxdiagnosis', 'User')
    User.objects.create(first_name='Cxadmin',
                                last_name='Cxadmin',
                                username='cxadmin',
                                email='cxadmin@mail.net',
                                password=make_password('cxadminpass'),
                                is_cxsuperuser='1',
                                change_pass='1')

def create_domains(apps, schema_editor):
    Domain = apps.get_model('cxdiagnosis', 'Domain')
    Domain.objects.create(name='H & PS')
    Domain.objects.create(name='Insurance')
    Domain.objects.create(name='Travel')
    Domain.objects.create(name='Banking')
    Domain.objects.create(name='Energy')
    Domain.objects.create(name='Finance')
    Domain.objects.create(name='Retail')

def create_organisations(apps, schema_editor):
    Organisation = apps.get_model('cxdiagnosis', 'Organisation')
    Organisation.objects.create(name='abc pvt ltd')
    Organisation.objects.create(name='xyz pft ltd')
    Organisation.objects.create(name='pqr ltd')
    Organisation.objects.create(name='demo ltd')

def create_maturitylevel(apps, schema_editor):
    MaturityLevel = apps.get_model('cxdiagnosis', 'MaturityLevel')
    MaturityLevel.objects.create(name='Not Started', score='0')
    MaturityLevel.objects.create(name='Basic', score='5')
    MaturityLevel.objects.create(name='Medium', score='10')
    MaturityLevel.objects.create(name='Pro', score='15')

class Migration(migrations.Migration):

    dependencies = [
        ('cxdiagnosis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_domains),
        migrations.RunPython(create_organisations),
        migrations.RunPython(create_user),
        migrations.RunPython(create_maturitylevel),
    ]
