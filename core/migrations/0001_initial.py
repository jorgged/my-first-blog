# Generated by Django 2.0.2 on 2018-03-09 21:31

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('adress', models.CharField(max_length=100)),
                ('cellphone', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('dni', models.CharField(max_length=100)),
                ('type_user', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('seccion', models.CharField(max_length=30)),
                ('period', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=30)),
                ('teacher_last_name', models.CharField(max_length=30)),
                ('seats', models.IntegerField()),
                ('teacher_exp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('password', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('cellphone', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('dni', models.CharField(max_length=100)),
                ('career', models.CharField(max_length=500)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='student_inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_exp', models.CharField(max_length=30)),
                ('student_name', models.CharField(max_length=30)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('password', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('cellphone', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('dni', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]