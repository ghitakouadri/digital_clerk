from django.db import models

class OfficeHours(models.Model):
	custom_profile_fk = models.IntegerField()
	module_code = models.CharField(max_length=50)
	start_time = models.CharField(max_length=50)
	end_time = models.CharField(max_length=50)
	start_date = models.DateField()
	location = models.CharField(max_length=100)
	title = models.CharField(max_length=50)

class Request(models.Model):
	REQUEST_STATUS = (
		(2, 'Pending'),
	    (1, 'Open'),
	    (0, 'Closed'),
	)
	office_hour = models.ForeignKey(OfficeHours, on_delete=models.CASCADE)
	request_user = models.IntegerField()
	lecturer = models.IntegerField()
	request_title = models.CharField(max_length=150)
	time_raised = models.DateTimeField()
	request_description = models.CharField(max_length=300)
	status = models.IntegerField(choices=REQUEST_STATUS, default=1)
	tried_solutions = models.CharField(max_length=300)

class Interaction(models.Model):
	INTERACTION_STATUS = (
		(2, 'Abandon'),
	    (1, 'Resolved'),
	    (0, 'Pending'),
	)
	office_hour = models.ForeignKey(OfficeHours, on_delete=models.CASCADE)
	request = models.ForeignKey(Request, on_delete=models.CASCADE)
	lecturer = models.IntegerField()
	time_opened = models.DateTimeField()
	time_closed = models.DateTimeField(null=True, blank=True)
	duration_seconds = models.IntegerField(default=0)
	status = models.IntegerField(choices=INTERACTION_STATUS, default=0)

class Feedback(models.Model):
	request = models.ForeignKey(Request, on_delete=models.CASCADE)
	lecturer = models.IntegerField()
	next_steps = models.CharField(max_length=300, null=True, blank=True)
	foot_note = models.CharField(max_length=300, null=True, blank=True)
