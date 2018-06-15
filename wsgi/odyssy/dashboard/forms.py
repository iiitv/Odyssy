import itertools

from django import forms
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify

from announcement.models import Announcement
from events.models import Event
from news.models import News
from people.models import People
from academic.models import Programme, Course


class ProgrammeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgrammeForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Programme Short Name'
        self.fields['full_name'].label = 'Programme Full Name'
        self.fields['branch_name'].label = 'Branch Full Name'
        self.fields['branch_code'].label = 'Branch Code'
        self.fields['info'].label = 'Details'
        self.fields['name'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['full_name'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['branch_code'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['branch_code'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['info'].widget.attrs.update({
            'class': 'uk-input'
        })

    class Meta:
        model = Programme
        fields = {'name', 'full_name', 'branch_code', 'branch_name', 'info'}


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['programme'].label = 'Programme'
        self.fields['semester'].label = 'Semester'
        self.fields['name'].label = 'Course Full Name'
        self.fields['code'].label = 'Course Code'
        self.fields['is_elective'].label = 'Elective'
        self.fields['lecture'].label = 'Lecture Credits'
        self.fields['tutorial'].label = 'Tutorial Credits'
        self.fields['practical'].label = 'Practical Credits'
        self.fields['credits'].label = 'Total Credits'
        self.fields['content'].label = 'Course Content'
        self.fields['text_book'].label = 'Text Books'
        self.fields['ref_book'].label = 'Ref. Books'
        self.fields['programme'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['semester'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['code'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['is_elective'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['lecture'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['tutorial'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['practical'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['credits'].widget.attrs.update({
            'class': 'uk-input'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'uk-input'
        })

        self.fields['text_book'].widget.attrs.update({
            'class': 'uk-input'
        })

        self.fields['ref_book'].widget.attrs.update({
            'class': 'uk-input'
        })

    class Meta:
        model = Course
        fields = {'programme', 'semester', 'name', 'code', 'is_elective', 'lecture', 'tutorial', 'practical', 'credits',
                  'content', 'text_book', 'ref_book'}


class PeopleProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeopleProfileForm, self).__init__(*args, **kwargs)
        self.fields['photo'].label = 'Photo'
        self.fields['link_gh'].label = 'Github profile'
        self.fields['link_ln'].label = 'LinkedIn profile'
        self.fields['link_gs'].label = 'Google Scholars profile'
        self.fields['link_tw'].label = 'Twitter profile'
        self.fields['link_fb'].label = 'Facebook profile'
        self.fields['name'].label = 'Full Name'
        self.fields['post'].label = 'Current Post'
        self.fields['email'].label = 'E-mail'
        self.fields['office'].label = 'Office'
        self.fields['academic_highlights'].label = 'Academic Highlights'
        self.fields['area_of_interest'].label = 'Area of interest'
        self.fields['academic_qualifications'].label = 'Academic Qualifications'
        self.fields['status'].label = 'Category'
        self.fields['publications'].label = 'Publications'
        self.fields['teaching'].label = 'Teaching'
        self.fields['other'].label = 'Other'
        self.fields['administrative_experience'].label = 'Administrative Experience'
        self.fields['work_experience'].label = 'Work Experience'
        self.fields['professional_memberships'].label = 'Professional Memberships'

    def save(self):
        instance = super(PeopleProfileForm, self).save(commit=False)
        if not instance.slug:
            instance.slug = orig = slugify(instance.name)
            for x in itertools.count(1):
                if not People.objects.filter(slug=instance.slug).exists():
                    break
                instance.slug = '%s-%d' % (orig, x)

        instance.save()
        return instance

    class Meta:
        model = People
        fields = {'photo', 'name', 'post', 'email', 'office', 'academic_highlights', 'area_of_interest',
                  'academic_qualifications', 'status', 'professional_memberships', 'work_experience',
                  'administrative_experience', 'publications', 'teaching', 'other', 'link_fb', 'link_tw', 'link_gs',
                  'link_ln', 'link_gh'}


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

    def save(self):
        instance = super(AnnouncementForm, self).save(commit=False)
        if not instance.slug:
            instance.slug = orig = slugify(instance.title)
            for x in itertools.count(1):
                if not Announcement.objects.filter(slug=instance.slug).exists():
                    break
                instance.slug = '%s-%d' % (orig, x)

        instance.save()
        return instance

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

    def save(self):
        instance = super(EventForm, self).save(commit=False)
        if not instance.slug:
            instance.slug = orig = slugify(instance.title)
            for x in itertools.count(1):
                if not Event.objects.filter(slug=instance.slug).exists():
                    break
                instance.slug = '%s-%d' % (orig, x)

        instance.save()
        return instance

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

    def save(self):
        instance = super(NewsForm, self).save(commit=False)
        if not instance.slug:
            instance.slug = orig = slugify(instance.title)
            for x in itertools.count(1):
                if not News.objects.filter(slug=instance.slug).exists():
                    break
                instance.slug = '%s-%d' % (orig, x)

        instance.save()
        return instance

    class Meta:
        model = News
        fields = {'title', 'description'}
