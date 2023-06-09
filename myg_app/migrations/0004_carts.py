# Generated by Django 4.0 on 2023-03-21 07:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myg_app', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('qty', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('status', models.CharField(choices=[('in cart', 'in cart'), ('order_placed', 'order_placed'), ('cancelled', 'cancelled')], default='in cart', max_length=12)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myg_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
