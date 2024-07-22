from django.db import models

class Muscles(models.TextChoices):
    CHEST = "Chest"
    BACK = "Back"
    BICEPS = "Biceps"
    TRICEPS = "Triceps"
    DELTOIDS = "Delts"
    QUADS = "Quads"
    HAMSTRINGS = "Hamstrings"
    LEGS = "Legs"
    ABS = "Abs"

class Categories(models.TextChoices):
    BODYBUILDING = 'Bodybuilding'
    CALISTHENICS = 'Calisthenics'
    POWERLIFTING = 'Power Lifting'
    HYBRID = 'Hybrid'

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    main_muscle_group = models.CharField(max_length=50, choices=Muscles.choices)
    bodyweight = models.BooleanField
    image_url = models.CharField(max_length=1023,blank=True)
    category = models.CharField(max_length=50, choices=Categories.choices)

    def __str__(self):
        return self.name

class Athlete(models.Model):
    full_name = models.CharField(max_length=255)
    age  = models.IntegerField()
    description  = models.TextField(blank=True)
    preferred_category  = models.CharField(blank=True,max_length=255, choices=Categories.choices)
    weight  = models.IntegerField(blank=True)
    level  = models.CharField(blank=True,max_length=255)
    profile_picture_url  = models.CharField(blank=True,max_length=1023)

    def __str__(self):
        return self.full_name
    
    def serialize(self):
        return {
            'full_name': self.full_name,
            'age': self.age,
            'description': self.description,
            'preferred_category': self.preferred_category,
            'weight': self.weight,
            'level': self.level,
            'profile_picture_url': self.profile_picture_url,
        }

class Session(models.Model):
    date = models.DateTimeField()
    athlete = models.ForeignKey(Athlete,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return '{0}\'s session of {1}'.format(self.athlete.full_name, self.date)

class Set(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete,on_delete=models.CASCADE,default=None)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    reps = models.IntegerField(default=0)
    rest_time_seconds = models.IntegerField(default=0)

    def __str__(self):
        return '{0} - {1} x {2}kg'.format(self.exercise.name,self.reps,self.weight) 