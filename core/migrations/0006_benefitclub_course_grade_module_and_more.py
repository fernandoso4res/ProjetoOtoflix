# Generated by Django 4.1.3 on 2022-11-17 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_flashcard_deck"),
    ]

    operations = [
        migrations.CreateModel(
            name="BenefitClub",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("benefit_name", models.CharField(max_length=255)),
                ("benefit_description", models.TextField()),
                ("benefit_end_date", models.DateTimeField(auto_now=True)),
                ("benefit_percentage", models.FloatField()),
                ("saved_amount", models.FloatField()),
                ("benefit_link", models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("course_image", models.ImageField(upload_to="core/pictures/%Y/%m/%d")),
                ("teacher_name", models.TextField()),
                ("duration", models.TimeField()),
                ("course_classification", models.FloatField()),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("course_expiration", models.DateTimeField()),
                (
                    "teacher_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.teacher"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("duration", models.TimeField()),
                ("comments", models.TextField()),
                ("video", models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionsMultipeChoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("image", models.URLField(max_length=255)),
                ("video", models.URLField(max_length=255)),
                ("type_question", models.CharField(max_length=255)),
                ("right_answer", models.TextField()),
                ("explication", models.TextField()),
                ("alternatives", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionsText",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("image", models.URLField(max_length=255)),
                ("video", models.URLField(max_length=255)),
                ("type_question", models.CharField(max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Simulated",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creator", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("limit_time", models.TimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.category"
                    ),
                ),
                (
                    "teacher_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.teacher"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscriptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subscription_name", models.CharField(max_length=255)),
                ("subscription_description", models.TextField()),
                ("subscription_price", models.FloatField()),
                ("subscription_duration_unit", models.CharField(max_length=50)),
                ("subscription_duration_value", models.IntegerField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.student"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Courses",),
        migrations.AlterField(
            model_name="flashcard",
            name="deck",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flashcards",
                to="core.deck",
            ),
        ),
        migrations.AddField(
            model_name="grade",
            name="module_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.module"
            ),
        ),
    ]
