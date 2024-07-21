from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    main_muscle_group = models.CharField(max_length=255)
    bodyweight = models.BooleanField
    image_url = models.CharField(max_length=1023)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    full_name = models.CharField(max_length=255)
    encrypted_pw  = models.CharField(max_length=255)
    age  = models.IntegerField
    description  = models.TextField(default="")
    preferred_category  = models.CharField(max_length=255)
    weight  = models.IntegerField
    level  = models.CharField(max_length=255)
    profile_picture_url  = models.CharField(max_length=1023)

    def __str__(self):
        return self.full_name

class Session(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Set(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    weight = models.FloatField
    reps = models.IntegerField
    rest_time_seconds = models.IntegerField

    def __str__(self):
        return self.exercise.name + " - " + self.reps + " x " + self.weight + "kg"