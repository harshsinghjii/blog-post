from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_src',
            field=models.URLField(default='/staticfiles/images/Formal blue Awesome.jpeg', max_length=250),
            preserve_default=False,
        ),
    ]
