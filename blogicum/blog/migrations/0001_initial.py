from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Initial migration."""

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa: E501
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')), # noqa: E501
                ('description', models.TextField(verbose_name='Описание')), # noqa: E501
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')), # noqa: E501
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')), # noqa: E501
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')), # noqa: E501
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa: E501
                ('name', models.CharField(max_length=256, verbose_name='Название места')), # noqa: E501
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')), # noqa: E501
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')), # noqa: E501
            ],
            options={
                'verbose_name': 'местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa: E501
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')), # noqa: E501
                ('text', models.TextField(verbose_name='Текст')), # noqa: E501
                ('pub_date', models.DateTimeField(help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации')), # noqa: E501
                ('is_published', models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано')), # noqa: E501
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')), # noqa: E501
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации')), # noqa: E501
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='Категория')), # noqa: E501
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.location', verbose_name='Местоположение')), # noqa: E501
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
