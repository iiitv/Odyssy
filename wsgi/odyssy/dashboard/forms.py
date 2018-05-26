from django import forms
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from announcement.models import Announcement
from events.models import Event
from news.models import News


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Re-type the password'
        self.fields['username'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'uk-input',
            'type': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'uk-input',
            'type': 'password'
        })

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                msg = u"Password must be same"
                self._errors['password2'] = self.error_class([msg])

        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


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

    def clean(self):
        cleaned_data = super(AnnouncementForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                msg = u"Start date must be before the end date"
                self._errors['start_date'] = self.error_class([msg])

        return self.cleaned_data

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
        self.fields['title'].label = 'Title'
        self.fields['place'].label = 'Place'
        self.fields['description'].label = 'Description'
        self.fields['title'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['place'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'uk-input'
        })

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                msg = u"Start date must be before the end date"
                self._errors['start_date'] = self.error_class([msg])

        return self.cleaned_data

    class Meta:
        model = Event
        fields = {'title', 'description', 'place'}


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

    def clean(self):
        cleaned_data = super(NewsForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                msg = u"Start date must be before the end date"
                self._errors['start_date'] = self.error_class([msg])

        return self.cleaned_data

    class Meta:
        model = News
        fields = {'title', 'description'}