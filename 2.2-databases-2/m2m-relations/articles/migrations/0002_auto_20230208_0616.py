
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationship',
            options={'ordering': ['tag', 'is_main'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterField(
            model_name='relationship',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Тэг'),
        ),
    ]
