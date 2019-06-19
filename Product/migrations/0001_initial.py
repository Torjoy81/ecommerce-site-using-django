# Generated by Django 2.0.7 on 2018-07-17 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=80)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('hight', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('image', models.ImageField(height_field='hight', upload_to=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Product.Category'), width_field='width')),
                ('store', models.PositiveIntegerField()),
                ('shirt_size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, null=True)),
                ('T_shirt_size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, null=True)),
                ('shoe_size', models.CharField(blank=True, choices=[('38', '38'), ('39', '39'), ('40', '40'), ('41', '42'), ('42', '42')], max_length=1, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Brand', to='Product.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Product.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]