from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191217_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_src',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
