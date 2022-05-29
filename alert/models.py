
from django.db import models

from twilio.rest import Client


import redis

from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.urls import reverse
from six import python_2_unicode_compatible
from timezone_field import TimeZoneField
#from __future__ import unicode_literals

import arrow
# Create your models here.
import datetime



#@python_2_unicode_compatible
class Birthday(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    msg = models.CharField(max_length=300)
    #time_zone = TimeZoneField(default='UTC')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        



# create a Twilio client
        account_sid = 'ACc51c5e112e597f8d2c59cd7d6110a3c0'
        auth_token = 'c1c7655e5384b945653a82c4f279208a'
        client = Client(account_sid, auth_token)

        # schedule message to be sent 61 minutes after current time
        #send_when = datetime.gmtnow() + timedelta(minutes=5)
        send_when = self.time
        # send the SMS
        messaging_service_sid = 'MGf9ff7ef736d26cd5756bef677b9b9f53'
        message = client.messages.create(
            from_=messaging_service_sid,
            to='+233551911595',  # ← your phone number here
            body=f'{self.msg}',
            schedule_type='fixed',
            send_at=send_when,
        )

        return super().save(*args, **kwargs)



class MothersDay(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    msg = models.CharField(max_length=300)
    #time_zone = TimeZoneField(default='UTC')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        



# create a Twilio client
        account_sid = 'ACc51c5e112e597f8d2c59cd7d6110a3c0'
        auth_token = 'c1c7655e5384b945653a82c4f279208a'
        client = Client(account_sid, auth_token)

        # schedule message to be sent 61 minutes after current time
        #send_when = datetime.gmtnow() + timedelta(minutes=5)
        send_when = self.time
        # send the SMS
        messaging_service_sid = 'MGf9ff7ef736d26cd5756bef677b9b9f53'
        message = client.messages.create(
            from_=messaging_service_sid,
            to='+233551911595',  # ← your phone number here
            body=f'{self.msg}',
            schedule_type='fixed',
            send_at=send_when,
        )

        return super().save(*args, **kwargs)



class MarriageAnniversary(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    msg = models.CharField(max_length=300)
    #time_zone = TimeZoneField(default='UTC')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        



# create a Twilio client
        account_sid = 'ACc51c5e112e597f8d2c59cd7d6110a3c0'
        auth_token = 'c1c7655e5384b945653a82c4f279208a'
        client = Client(account_sid, auth_token)

        # schedule message to be sent 61 minutes after current time
        #send_when = datetime.gmtnow() + timedelta(minutes=5)
        send_when = self.time
        # send the SMS
        messaging_service_sid = 'MGf9ff7ef736d26cd5756bef677b9b9f53'
        message = client.messages.create(
            from_=messaging_service_sid,
            to='+233551911595',  # ← your phone number here
            body=f'{self.msg}',
            schedule_type='fixed',
            send_at=send_when,
        )

        return super().save(*args, **kwargs) 



class RelationshipAnniversary(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    msg = models.CharField(max_length=300)
    #time_zone = TimeZoneField(default='UTC')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        



# create a Twilio client
        account_sid = 'ACc51c5e112e597f8d2c59cd7d6110a3c0'
        auth_token = 'c1c7655e5384b945653a82c4f279208a'
        client = Client(account_sid, auth_token)

        # schedule message to be sent 61 minutes after current time
        #send_when = datetime.gmtnow() + timedelta(minutes=5)
        send_when = self.time
        # send the SMS
        messaging_service_sid = 'MGf9ff7ef736d26cd5756bef677b9b9f53'
        message = client.messages.create(
            from_=messaging_service_sid,
            to='+233551911595',  # ← your phone number here
            body=f'{self.msg}',
            schedule_type='fixed',
            send_at=send_when,
        )

        return super().save(*args, **kwargs)   





class Score(models.Model):
    result = models.PositiveIntegerField()


    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):

        if self.result < 70:

            account_sid = 'ACc51c5e112e597f8d2c59cd7d6110a3c0'
            auth_token = 'c1c7655e5384b945653a82c4f279208a'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                          body=f'The current result is bad motherfucker! - {self.result}',
                                          from_='+18575973293',
                                          to='+233275278775'
                                      )

            print(message.sid)

        return super().save(*args, **kwargs)

