from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model) :
	user = models.OneToOneField(User, primary_key=True)
	job_title = models.CharField(max_length=40)
	admission_date = models.DateField()
	#tel = IntegerField(max_length = 12)
	ADMINISTRATOR = 'Admin'
	MANAGER = 'MAG'
	USER = 'Benutzer'
	USING_LEVEL_CHOICES = ( (ADMINISTRATOR,'administrator'),
				(MANAGER, 'manager'),
				(USER, 'benutzer'),
	)
	user_level = models.CharField(max_length=20,choices=USING_LEVEL_CHOICES, default=USER)
	def __unicode__(self):
		return self.user.username
