from django import forms
from django.forms import DateTimeInput

from announcement.models import Announcement


class AnnouncementForm(forms.ModelForm):
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

        # for field in self.Meta.fields:
        #     self.fields[field].widget.attrs.update({
        #         'class': 'uk-input'
        #     })

    class Meta:
        model = Announcement
        fields = {'start_date', 'end_date', 'title', 'description', 'tags'}
