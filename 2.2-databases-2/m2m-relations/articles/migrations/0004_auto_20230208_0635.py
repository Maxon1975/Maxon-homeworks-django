
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20230208_0624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationship',
            options={'ordering': ['-is_main', 'tag'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
    ]
