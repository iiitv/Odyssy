from django.db import models


class Event(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    event_date = models.DateField()
    description = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

    int_to_month = {'1': 'JAN',
                    '2': 'FEB',
                    '3': 'MAR',
                    '4': 'APR',
                    '5': 'MAY',
                    '6': 'JUN',
                    '7': 'JUL',
                    '8': 'AUG',
                    '9': 'SEP',
                    '10': 'OCT',
                    '11': 'NOV',
                    '12': 'DEC'
                    }

    def __str__(self):
        return self.description + " at " + self.place + " on " + \
               str(self.event_date.day) + " - " + self.int_to_month[str(self.event_date.month)] + \
               " - " + str(self.event_date.year)
