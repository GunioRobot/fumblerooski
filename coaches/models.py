from django.db import models

class Coach(models.Model):
    ncaa_name = models.CharField(max_length=90)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    alma_mater = models.CharField(max_length=75)
    birth_date = models.DateField(null=True, blank=True)
    years = models.IntegerField(default=0, blank=True)
    wins = models.IntegerField(default=0, blank=True)
    losses = models.IntegerField(default=0, blank=True)
    ties = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return '/college/coaches/%s/' % self.slug
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ['last_name']
        verbose_name_plural = 'Coaches'
        db_table = 'college_coach'

class CoachingJob(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'college_coachingjob'