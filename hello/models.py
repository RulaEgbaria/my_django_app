from django.db import models

# Create your models here.
from django.db import models
import pycountry

from django.conf import settings
from users import forms
from django.core.validators import MinValueValidator,MaxValueValidator

class volunteer(models.Model):
    id= models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    OPTION_CHOICES = (
        ('user', 'user'),
        ('vistor', 'vistor'),
    )
    type = models.CharField(max_length=20, choices=OPTION_CHOICES, default='vistor')
    is_vervied = models.BooleanField()
    age = models.IntegerField()
    native_country = models.CharField(max_length=255, choices=[(c.name, c.name) for c in pycountry.countries.Country])
    current_country = models.CharField(max_length=255, choices=[(c.name, c.name) for c in pycountry.countries.Country])
    recent_year_of_knowldge = models.IntegerField()
    education_CHOICES = (
        ('M.A', 'M.A'),
        ('School', 'School'),
        ('B.A', 'B.A'),
        ('Other', 'Other'))
    education= models.CharField(max_length=20,choices=education_CHOICES)
    recent_year_of_EDUCATION = models.IntegerField()
    language = models.CharField(max_length=255, choices=[(l.name, l.name) for l in pycountry.languages])
    degree_name = models.TextField()


 class domain(models.Model) :
     doaimn1_lan = models.TextField()
     domain1_words = models.TextField()
     domain2_lan = models.TextField()
     domain2_words = models.TextField()
     domain3_lan= models.TextField()
     domain3_words = models.TextField()
     domain4_lan = models.TextField()
     domain4_words = models.TextField()
class to_do(forms.ModelForm):
    id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    what_to_do_CHOICES = (
        ('domain1', 'searching a word in  exsiting doaimn'),
        ('domain2', 'suggest a word with the result of searching '),
        ('domain3', 'transalte a domain')
    )
    what_to_do = models.CharField(max_length=20, choices=what_to_do_CHOICES)
    domain_CHOICES = (
        ('domain1', 'domain1'),
        ('domain2', 'domain2'),
        ('domain3', 'domain3'),
        ('domain4', 'domain4'),
    )
    dependent_choice_1 = models.CharField(max_length=255, choices=domain_CHOICES,blank=False)
    dependent_choice_1_1 = forms.ModelChoiceField(queryset=domain.domain1_words.objects.all())
    dependent_choice_1_2 = forms.ModelChoiceField(queryset=domain.domain2_words.objects.all())
    dependent_choice_1_3 = forms.ModelChoiceField(queryset=domain.domain3_words.objects.all())
    dependent_choice_1_4 = forms.ModelChoiceField(queryset=domain.domain4_words.objects.all())
    dependent_choice_2 = models.CharField(max_length=255, blank=False)
    dependent_choice_3 = models.CharField(max_length=255, choices=domain_CHOICES, blank=False)
class translated_words(forms.ModelForm):
    id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    dependent_choice_3= models.ForeignKey(to_do, on_delete=models.CASCADE)
    dependent_choice_translate = forms.ModelChoiceField(queryset=dependent_choice_3.objects.all())
    the_translation=models.TextField()
    is_vervied1 = models.BooleanField()

#class existing_domains(models.Model):
    #domain_1 = models.CharField(max_length=255)
    #domain_2 = models.CharField(max_length=255)
    #domain_3 = models.CharField(max_length=255)
    #domain_4 = models.CharField(max_length=255)

#class existing_phrases(models.Model):
        #domain_1 = models.CharField(max_length=255)
        #domain_2 = models.CharField(max_length=255)
        #domain_3 = models.CharField(max_length=255)
        #domain_4 = models.CharField(max_length=255)
class sugessted_phrases(forms.ModelForm):
    id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    dependent_choice_3 = models.ForeignKey(to_do, on_delete=models.CASCADE)
    is_accepted = models.BooleanField()
    the_suggtion = models.TextField()
    site_type=models.TextField()
    the_content_producer=models.TextField()
    free_access = models.BooleanField()
    recent = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    recent_information = models.CharField(max_length=255, choices=recent, blank=False)
    auther_backgrounds= (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    auther_background= models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
    the_need_of_scientfic_background= models.BooleanField()
    options= (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
     )
    lay_people = models.CharField(max_length=255, choices=options, blank=False)
    depend_lay_people=models.BooleanField()
    major_err = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    major_error = models.CharField(max_length=255, choices=major_err, blank=False)
    scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#we have to wrhte a note about the scale
    accurate = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    accurate_content= models.CharField(max_length=255, choices=accurate, blank=False)
    scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sources = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('4', 'Opt'),
        ('5', 'Optio'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8 '),
        ('9', '9 3'),
    )
    multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
    refernce_evrey_Day=models.CharField(max_length=255, choices=options, blank=False)
    local_example=models.CharField(max_length=255, choices=options, blank=False)
    advantages=models.CharField(max_length=255, choices=options, blank=False)
    options1 = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    content_reject = models.CharField(max_length=255, choices=options1, blank=False)
    malicios_meaning = models.CharField(max_length=255, choices=options1, blank=False)
    claims_contradict = models.CharField(max_length=255, choices=options1, blank=False)
    specific_group = models.CharField(max_length=255, choices=options1, blank=False)
def create_new_tables():
    words = domain.objects.values_list('domain1_words', flat=True).distinct()
    for word in words:
        class NewTable(models.Model):
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            site_type = models.TextField()
            the_content_producer = models.TextField()
            free_access = models.BooleanField()
            recent = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('option1', 'Option 1'),
                ('option2', 'Option 2'),
                ('option3', 'Option 3'),
                ('4', 'Opt'),
                ('5', 'Optio'),
                ('6', '6'),
                ('7', '7'),
                ('8', '8 '),
                ('9', '9 3'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            malicios_meaning = models.CharField(max_length=255, choices=options1, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options1, blank=False)
            specific_group = models.CharField(max_length=255, choices=options1, blank=False)
def create_new_tables():
    words = domain.objects.values_list('domain2_words', flat=True).distinct()
    for word in words:
        class NewTable(models.Model):
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            site_type = models.TextField()
            the_content_producer = models.TextField()
            free_access = models.BooleanField()
            recent = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('option1', 'Option 1'),
                ('option2', 'Option 2'),
                ('option3', 'Option 3'),
                ('4', 'Opt'),
                ('5', 'Optio'),
                ('6', '6'),
                ('7', '7'),
                ('8', '8 '),
                ('9', '9 3'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            malicios_meaning = models.CharField(max_length=255, choices=options1, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options1, blank=False)
            specific_group = models.CharField(max_length=255, choices=options1, blank=False)
def create_new_tables():
    words = domain.objects.values_list('domain3_words', flat=True).distinct()
    for word in words:
        class NewTable(models.Model):
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            site_type = models.TextField()
            the_content_producer = models.TextField()
            free_access = models.BooleanField()
            recent = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('option1', 'Option 1'),
                ('option2', 'Option 2'),
                ('option3', 'Option 3'),
                ('4', 'Opt'),
                ('5', 'Optio'),
                ('6', '6'),
                ('7', '7'),
                ('8', '8 '),
                ('9', '9 3'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            malicios_meaning = models.CharField(max_length=255, choices=options1, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options1, blank=False)
            specific_group = models.CharField(max_length=255, choices=options1, blank=False)

    def create_new_tables():
        words = domain.objects.values_list('domain4_words', flat=True).distinct()
        for word in words:
            class NewTable(models.Model):
                original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
                site_type = models.TextField()
                the_content_producer = models.TextField()
                free_access = models.BooleanField()
                recent = (
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                )
                recent_information = models.CharField(max_length=255, choices=recent, blank=False)
                auther_backgrounds = (
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                )
                auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
                the_need_of_scientfic_background = models.BooleanField()
                options = (
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                )
                lay_people = models.CharField(max_length=255, choices=options, blank=False)
                depend_lay_people = models.BooleanField()
                major_err = (
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                )
                major_error = models.CharField(max_length=255, choices=major_err, blank=False)
                scale_variable_major_error = models.IntegerField(
                    validators=[MinValueValidator(1), MaxValueValidator(5)])
                # we have to wrhte a note about the scale
                accurate = (
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                )
                accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
                scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
                sources = (
                    ('option1', 'Option 1'),
                    ('option2', 'Option 2'),
                    ('option3', 'Option 3'),
                    ('4', 'Opt'),
                    ('5', 'Optio'),
                    ('6', '6'),
                    ('7', '7'),
                    ('8', '8 '),
                    ('9', '9 3'),
                )
                multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
                refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
                local_example = models.CharField(max_length=255, choices=options, blank=False)
                advantages = models.CharField(max_length=255, choices=options, blank=False)
                options1 = (
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                )
                content_reject = models.CharField(max_length=255, choices=options1, blank=False)
                malicios_meaning = models.CharField(max_length=255, choices=options1, blank=False)
                claims_contradict = models.CharField(max_length=255, choices=options1, blank=False)
                specific_group = models.CharField(max_length=255, choices=options1, blank=False)