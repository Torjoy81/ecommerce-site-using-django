# Generated by Django 2.0.7 on 2018-07-30 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0005_auto_20180718_0437'),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Createcart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='Product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.Customer_Account')),
            ],
        ),
    ]
