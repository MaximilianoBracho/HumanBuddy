# Generated by Django 4.0 on 2022-02-01 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=20, verbose_name='Tipo de Transacción')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SiteAdmin.entity')),
                ('species', models.CharField(max_length=50, verbose_name='Especie')),
                ('family', models.CharField(max_length=50, verbose_name='Familia')),
                ('race', models.CharField(max_length=50, verbose_name='Raza')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
            ],
            bases=('SiteAdmin.entity',),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SiteAdmin.entity')),
                ('fiscal_id', models.CharField(max_length=11, verbose_name='CUIT')),
                ('fiscal_name', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de Veterinaria')),
                ('start_date', models.DateField(verbose_name='1990-01-01')),
                ('fiscal_address', models.CharField(max_length=100, verbose_name='Direccion Fiscal')),
                ('real_address', models.CharField(max_length=100, verbose_name='Direccion Real')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('mail', models.EmailField(max_length=254)),
            ],
            bases=('SiteAdmin.entity',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SiteAdmin.entity')),
                ('person_id', models.CharField(max_length=8, verbose_name='DNI')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('birthdate', models.DateField(verbose_name='01/01/1990')),
                ('address', models.CharField(max_length=100, verbose_name='Domicilio')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('cellphone', models.CharField(max_length=20, verbose_name='Celular')),
                ('mail', models.EmailField(max_length=254)),
            ],
            bases=('SiteAdmin.entity',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SiteAdmin.person')),
                ('fiscal_id', models.CharField(max_length=11, verbose_name='CUIL')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('company_id', models.IntegerField()),
            ],
            bases=('SiteAdmin.person',),
        ),
    ]