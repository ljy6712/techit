# Generated by Django 4.2 on 2023-05-18 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='생성 일시')),
                ('category', models.CharField(choices=[('1', '일반'), ('2', '계정'), ('3', '기타')], max_length=2, verbose_name='카테고리')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('title', models.CharField(max_length=80, verbose_name='질문 제목')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='문자메시지')),
                ('is_email', models.BooleanField(default=False, verbose_name='이메일 수신 여부')),
                ('is_phone', models.BooleanField(default=False, verbose_name='문자메시지 수신 여부')),
                ('content', models.TextField(verbose_name='문의 내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='생성 일시')),
                ('title', models.CharField(max_length=80, verbose_name='질문 제목')),
                ('content', models.TextField(verbose_name='질문 내용')),
                ('category', models.CharField(choices=[('1', '일반'), ('2', '계정'), ('3', '기타')], max_length=2, verbose_name='카테고리')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='생성 일시')),
                ('content', models.TextField(verbose_name='답변 내용')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_created_by', to=settings.AUTH_USER_MODEL)),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]