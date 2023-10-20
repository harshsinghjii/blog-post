from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_src',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
