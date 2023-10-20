from django.db import migrations
class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191217_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
