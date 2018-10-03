from django.db import models

class University(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty"

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(
        'university',
        on_delete=models.CASCADE,
        blank=True,
    )
    faculty = models.ForeignKey(
        'faculty',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
    )


    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)