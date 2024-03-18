from django.db import models

from users.models import User


class Specialization(models.Model):
    name = models.TextField('Название профессии', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Профессия'
    #     verbose_name_plural = 'Профессии'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Towns(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Город'
    #     verbose_name_plural = 'Города'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Опыт работы'
    #     verbose_name_plural = 'Варианты опыта работы'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Образование'
    #     verbose_name_plural = 'Варианты образования'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Знание языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class LanguageLevel(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Уровень языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Уровень языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Уровень языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.TextField('Название профессии', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Профессия'
    #     verbose_name_plural = 'Профессии'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.TextField('График работы', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'График работы'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Expectations(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'непонятно'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Payments(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'непонятно'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Application(models.Model):
    # поля модели скомпанованы по типу:

    # данные проставляются автоматически
    employer_id = models.ForeignKey( ###
        User,
        on_delete=models.CASCADE,
        )
    date = models.DateField( ###
        auto_now_add=True
        )

    # юзер ставит галочку или нет
    mission = models.BooleanField() ### или поменять на выбор из нескольких?
    bonus = models.BooleanField() ###

    # юзер вводит значения вручную
    # name = models.TextField(
    #     default='Новая заявка', # на 2ом шаге данные подтягиваются из поле “специальность
    #     verbose_name='Название вакансии/заявки'
    # )
    salary = models.PositiveIntegerField() ###
    responsibilities = models.TextField(
        verbose_name='Обязанности'
    )
    # other_requirements = models.TextField(
    #     verbose_name='Прочие требования'
    # )
    countCandidates = models.PositiveIntegerField() ###
    countRecruiter = models.PositiveIntegerField() ###
    award = models.PositiveIntegerField() ###

    # юзер выбирает одно из списка. или добавляет свое
    specialization = models.ForeignKey( ###
        Specialization,
        on_delete=models.SET_NULL  # добавить: при вводе букв - подсказки
    )
    towns = models.ForeignKey( ###
        Towns,
        on_delete=models.SET_NULL  # добавить: при вводе букв - подсказки
    )
    experience = models.ForeignKey( ###
        Experience,
        on_delete=models.SET_NULL  # добавить: при вводе букв - подсказки
    )
    education = models.ForeignKey( ###
        Education,
        on_delete=models.SET_NULL  # добавить: при вводе букв - подсказки
    )
    payments = models.ForeignKey( ###
        Payments,
        on_delete=models.SET_NULL  # добавить: при вводе букв появляются подсказки
    )


    # юзер выбирает несколько из списка
    skills = models.ManyToManyField(  ###
        Skill,
        through='SkillApplication',
    )
    languages = models.ManyToManyField(  #### уточнить и переделать в несколько языков
        Language,
        through='LanguageApplication',
    )
    registration = models.ManyToManyField( ### чекчек
        Registration,
        through='RegistrationApplication',
    )
    occupation = models.ManyToManyField( ###
        Occupation,
        through='OccupationApplication',
    )
    timetable = models.ManyToManyField(  ###
        Schedule,
        through='ScheduleApplication',
    )
    expectations = models.ManyToManyField(  ###
        Expectations,
        through='ExpectationsApplication',
    )

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.specialization


class SkillApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    skill_id = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )


class LanguageApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    language_id = models.ForeignKey(
        Language,
        on_delete=models.CASCADE
    )
    language_level = models.ForeignKey(
        LanguageLevel,
        on_delete=models.SET_NULL  # добавить: при вводе букв появляются подсказки
    )


class ScheduleApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    Schedule_id = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE
    )


class OccupationApplication(models.Model):
    occupation_id = models.ForeignKey(
        Occupation,
        on_delete=models.CASCADE
    )
    registration_id = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE
    )


class RegistrationApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    registration_id = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE
    )


class ExpectationsApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    expectations_id = models.ForeignKey(
        Expectations,
        on_delete=models.CASCADE
    )