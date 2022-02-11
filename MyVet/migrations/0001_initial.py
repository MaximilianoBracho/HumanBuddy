# Generated by Django 4.0 on 2022-02-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('person_id', models.CharField(default='', max_length=8, verbose_name='DNI')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('surname', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('birthdate', models.DateField(null=True, verbose_name='Fecha de Nacimiento')),
                ('address', models.CharField(default='', max_length=100, verbose_name='Domicilio')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Teléfono')),
                ('cellphone', models.CharField(default='', max_length=20, verbose_name='Celular')),
                ('mail', models.EmailField(default='info@mail.com', max_length=254)),
                ('fiscal_id', models.CharField(default='', max_length=11, verbose_name='CUIL')),
                ('cargo', models.CharField(default='', max_length=50, verbose_name='Cargo')),
                ('user_id', models.IntegerField(null=True)),
                ('vet_id', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('fiscal_id', models.CharField(default='', max_length=11, verbose_name='CUIT')),
                ('fiscal_name', models.CharField(default='', max_length=100, verbose_name='Razón Social')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nombre de Veterinaria')),
                ('start_date', models.DateField(null=True, verbose_name='Fecha de Inscripción')),
                ('fiscal_address', models.CharField(default='', max_length=100, verbose_name='Dirección Fiscal')),
                ('real_address', models.CharField(default='', max_length=100, verbose_name='Dirección Real')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Teléfono')),
                ('mail', models.EmailField(default='info@mail.com', max_length=254)),
                ('user_id', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('person_id', models.CharField(default='', max_length=8, verbose_name='DNI')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('surname', models.CharField(default='', max_length=50, verbose_name='Apellido')),
                ('birthdate', models.DateField(null=True, verbose_name='Fecha de Nacimiento')),
                ('address', models.CharField(default='', max_length=100, verbose_name='Domicilio')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Teléfono')),
                ('cellphone', models.CharField(default='', max_length=20, verbose_name='Celular')),
                ('mail', models.EmailField(default='info@mail.com', max_length=254)),
                ('fiscal_id', models.CharField(default='', max_length=11, verbose_name='CUIL')),
                ('cargo', models.CharField(default='', max_length=50, verbose_name='Cargo')),
                ('license', models.CharField(default='', max_length=11, verbose_name='Licencia')),
                ('user_id', models.IntegerField(null=True)),
                ('vet_id', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
