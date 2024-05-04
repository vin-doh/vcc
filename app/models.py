from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models. CharField(max_length=255, default="Company")
    location = models. CharField(max_length=255)
    email = models. EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models. CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
# To customise database table name as in the default app_generalinfo to db_table. add  these codes below

# class Meta:
#   db_table = "custom_table_name"

class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    user_image = models.CharField(max_length=225, blank=True, null=True)

    stars_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField(choices=stars_count)
    username = models.CharField(max_length=50)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.user_job_title}"
    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question