from django.db import models


class AddClient(models.Model):
    client_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=13)
    alternate_number = models.CharField(max_length=13, null=True, blank=True)
    email_id = models.EmailField()
    reference = models.CharField(choices=(("1", "google"),("2", "Facebook"), ("3", "Website"),
                                          ("4", "Previous Client"), ("5", "Other")),
                                 max_length=10)

    def __str__(self):
        return self.client_name
