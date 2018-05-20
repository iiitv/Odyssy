from django import forms
from django.forms.fields import DateField

from announcement.models import Announcement
from events.models import Event
from news.models import News


class AnnouncementForm(forms.ModelForm):
    start_date = DateField()
    end_date = DateField()

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = 'Start Date'
        self.fields['end_date'].label = 'End Date'
        self.fields['title'].label = 'Title'
        self.fields['description'].label = 'Description'
        self.fields['title'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'uk-input'
        })

    class Meta:
        model = Announcement
        fields = {'title', 'description'}


class EventForm(forms.ModelForm):
    start_date = DateField()
    end_date = DateField()

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = 'Start Date'
        self.fields['end_date'].label = 'End Date'
        self.fields['name'].label = 'Title'
        self.fields['description'].label = 'Description'
        self.fields['name'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'uk-input'
        })

    class Meta:
        model = Event
        fields = {'name', 'description'}


class NewsForm(forms.ModelForm):
    start_date = DateField()
    end_date = DateField()

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = 'Start Date'
        self.fields['end_date'].label = 'End Date'
        self.fields['title'].label = 'Title'
        self.fields['description'].label = 'Description'
        self.fields['title'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'uk-input'
        })

    class Meta:
        model = News
        fields = {'title', 'description'}
