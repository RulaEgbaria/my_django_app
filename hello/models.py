from django.db import models

# Create your models here.
from django.db import models
import pycountry
from django import forms

from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
import csv
from django.db import connection
class Data(models.Model):
    term_id=models.IntegerField(('term_id'))
    language=models.CharField(('langs'),max_length=255)
    country=models.CharField(('country'),max_length=255)
    term=models.CharField(('term'),max_length=255)
    domain=models.CharField(('type'),max_length=255)
    code_lang=models.CharField(('code_lang'),max_length=10)
class QuestionaireTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_spent = models.DurationField()
class volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    OPTION_CHOICES = (
        ('user', 'user'),
        ('vistor', 'vistor'))
    type = models.CharField(max_length=20, choices=OPTION_CHOICES, default='vistor')
    is_vervied = models.BooleanField()
    age = models.IntegerField()
    native_country = models.CharField(max_length=255, choices=[(c.name, c.name) for c in pycountry.countries])
    current_country = models.CharField(max_length=255, choices=[(c.name, c.name) for c in pycountry.countries])
    recent_year_of_knowldge = models.IntegerField()
    education_CHOICES = (
        ('M.A', 'M.A'),
        ('School', 'School'),
        ('B.A', 'B.A'),
        ('Other', 'Other'))
    education= models.CharField(max_length=20,choices=education_CHOICES)
    recent_year_of_EDUCATION = models.IntegerField()
    language = models.CharField(max_length=255, choices=[(l.name, l.name) for l in pycountry.languages])


class domain(models.Model):
     doaimn1_lan = models.TextField()
     domain1_words = models.TextField()
     domain2_lan = models.TextField()
     domain2_words = models.TextField()
     domain3_lan= models.TextField()
     domain3_words = models.TextField()
     domain4_lan = models.TextField()
     domain4_words = models.TextField()


class phrase(models.Model):
    id = models.ForeignKey(volunteer, primary_key=True, on_delete=models.CASCADE)
    original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
    result_number = models.IntegerField()
    link = models.TextField()
    site_name = models.TextField()
    site_types = (
        ('Text', 'Text'),
        ('Information Search Database', '	Information Search Database'),
        ('	Video', 'Video'),
        ('	Simulation', '	Simulation'),
        ('	Other', 'Other')
    )
    site_type = models.CharField(max_length=255, choices=site_types, blank=False)
    the_content_producer_options = (
        ('	Government body (e.g. ministry of health, CDC, FDA, NASA)',
         '	Government body (e.g. ministry of health, CDC, FDA, NASA)'),
        ('	NGO (Non Governmental Organizations)', 'NGO (Non Governmental Organizations)'),
        ('	Research organizations (e.g. CERN)', 'Research organizations (e.g. CERN)'),
        ('	International organizations (e.g. WHO, UN, UNESCO)',
         '	-	International organizations (e.g. WHO, UN, UNESCO)'),
        ('Higher education\Academic institution (e.g. university \college)',
         '	Higher education\Academic institution (e.g. university \college)'),
        ('	Internet site for formal schooling\ K-12 education system',
         '	Internet site for formal schooling\ K-12 education system'),
        ('	Informal science education and popular science (e.g.  science museum, Scientific American)',
         '	Informal science education and popular science (e.g.  science museum, Scientific American)'),
        ('	Scientific Journals (e.g. Science, Nature) or Google  Scholar',
         '	Scientific Journals (e.g. Science, Nature) or Google  Scholar'),
        ('Medical site (e.g. health insurance provider, hospital)',
         'Medical site (e.g. health insurance provider, hospital)'),
        ('	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)',
         '	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)'),
        ('	Media and communication (e.g. news sites)', '	Media and communication (e.g. news sites)'),
        ('Commercial / Economic (e.g. pharmaceutical     companies)',
         'Commercial / Economic (e.g. pharmaceutical     companies)'),
        ('Satire site', 'Satire site'),
        ('Social media site (e.g. Twitter, Facebook, LinkedIn etc.)',
         'Social media site (e.g. Twitter, Facebook, LinkedIn etc.)'),
        ('Fact checkers site', 'Fact checkers site'),
        ('others', 'others')

    )
    the_content_producer = models.CharField(max_length=255, choices=the_content_producer_options, blank=False)

    free_access = models.BooleanField()
    recent = (
        ('Not mentioned', 'Not mentioned'),
        ('IOver 10 years', 'Over 10 years'),
        ('	5 to 10 yea', '5 to 10 yea'),
        ('	 Rather new (1 to 5 years)', '	 Rather new (1 to 5 years)'),
        ('	Other', 'Other')
    )
    recent_information = models.CharField(max_length=255, choices=recent, blank=False)
    auther_backgrounds = (
        ('The Author is not mention', 'The Author is not mention'),
        (
        'The author is mentioned but there is no information about their background, or their background is not relevant',
        'The author is mentioned but there is no information about their background, or their background is not relevant'),
        (' The author has relevant expertise to the content', ' The author has relevant expertise to the content')
    )
    auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
    the_need_of_scientfic_background = models.BooleanField()
    options = (
        ('NO', 'NO'),
        ('YES', 'YES'),
        ('Irrelevant', 'Irrelevant'),
    )
    lay_people = models.CharField(max_length=255, choices=options, blank=False)
    depend_lay_people = models.BooleanField()
    major_err = (
        ('There are no major scientific errors in the content', 'There are no major scientific errors in the content'),
        ('There are major scientific errors in the content (if so give an example)',
         'There are major scientific errors in the content (if so give an example)'),
        ('Irrelevant', 'Irrelevant'),
    )
    major_error = models.CharField(max_length=255, choices=major_err, blank=False)
    scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # we have to wrhte a note about the scale
    accurate = (
        ('Accurate', 'Accurate'),
        ('Neiter', 'Neiter'),
        ('Inaccurate', 'Inaccurate'),
        ('Irrelevant', 'Irrelevant'),
    )
    accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
    scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sources = (
        ('None of the below', 'ONone of the below'),
        ('Others', 'Others'),
        ('Place to leave comments\ ask questions', 'Place to leave comments\ ask questions'),
        ('Graphs', 'Graphs'),
        (' Relevant multimedia (e.g. pictures, video, animation etc.)',
         ' Relevant multimedia (e.g. pictures, video, animation etc.)'),
        ('Hyper-links', 'Hyper-links'),
        ('Numerical data', 'Numerical data'),
        (' List of sources', ' List of sources '),
        (' Citation or references to relevant literature', ' Citation or references to relevant literature'),
    )
    multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
    refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
    local_example = models.CharField(max_length=255, choices=options, blank=False)
    advantages = models.CharField(max_length=255, choices=options, blank=False)
    options1 = (
        ('The content rejects the conspiracy', 'The content rejects the conspiracy'),
        (' Not sure', ' Not sure'),
        (' The content reinforce the conspiracy', ' The content reinforce the conspiracy'),
        ('Irrelevant', 'Irrelevant'),
    )
    content_reject = models.CharField(max_length=255, choices=options1, blank=False)
    options2 = (
        ('NO', 'NO'),
        ('Not sure', 'Not sure'),
        ('YES', 'YES'),
        ('Irrelevant', 'Irrelevant'),
    )
    malicios_meaning = models.CharField(max_length=255, choices=options2, blank=False)
    claims_contradict = models.CharField(max_length=255, choices=options2, blank=False)
    specific_group = models.CharField(max_length=255, choices=options2, blank=False)


# class to_do(forms.ModelForm):
#     id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
#     what_to_do_CHOICES = (
#         ('domain1', 'searching a word in  exsiting doaimn'),
#         ('domain2', 'suggest a word with the result of searching '),
#         ('domain3', 'transalte a domain')
#     )
#     what_to_do = models.CharField(max_length=20, choices=what_to_do_CHOICES)
#     domain_CHOICES = (
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4')
#     )
#     dependent_choice_1 = models.CharField(max_length=255, choices=domain_CHOICES,blank=False)
#     dependent_choice_1_1 = forms.ModelChoiceField(queryset=domain.domain1_words.objects.all())
#     dependent_choice_1_2 = forms.ModelChoiceField(queryset=domain.domain2_words.objects.all())
#     dependent_choice_1_3 = forms.ModelChoiceField(queryset=domain.domain3_words.objects.all())
#     dependent_choice_1_4 = forms.ModelChoiceField(queryset=domain.domain4_words.objects.all())
#     dependent_choice_2 = models.CharField(max_length=255, blank=False)
#     dependent_choice_3 = models.CharField(max_length=255, choices=domain_CHOICES, blank=False)
class translated_words(models.Model):
    id = models.ForeignKey(volunteer, primary_key=True,on_delete=models.CASCADE)
    domain_CHOICES = (
        ('domain1', 'domain1'),
        ('domain2', 'domain2'),
        ('domain3', 'domain3'),
        ('domain4', 'domain4')
    )
    dependent_choice_1 = models.CharField(max_length=255, choices=domain_CHOICES, blank=False)
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
class sugessted_phrases(models.Model):
    id = models.ForeignKey(volunteer,primary_key=True, on_delete=models.CASCADE)
    domain_CHOICES = (
        ('domain1', 'domain1'),
        ('domain2', 'domain2'),
        ('domain3', 'domain3'),
        ('domain4', 'domain4')
    )
    dependent_choice_1 = models.CharField(max_length=255, choices=domain_CHOICES, blank=False)
    is_accepted = models.BooleanField()
    the_suggtion = models.TextField()
    site_name=models.TextField()
    result_number=models.IntegerField()
    link=models.TextField()
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
            id = models.ForeignKey(volunteer,primary_key=True, on_delete=models.CASCADE)
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            result_number = models.IntegerField()
            link = models.TextField()
            site_name = models.TextField()
            site_types=(
                ('Text', 'Text'),
                ('Information Search Database', '	Information Search Database'),
                ('	Video', 'Video'),
                ('	Simulation', '	Simulation'),
                ('	Other', 'Other')
            )
            site_type=models.CharField(max_length=255, choices=site_types, blank=False)
            the_content_producer_options = (
                ('	Government body (e.g. ministry of health, CDC, FDA, NASA)', '	Government body (e.g. ministry of health, CDC, FDA, NASA)'),
                ('	NGO (Non Governmental Organizations)', 'NGO (Non Governmental Organizations)'),
                ('	Research organizations (e.g. CERN)', 'Research organizations (e.g. CERN)'),
                ('	International organizations (e.g. WHO, UN, UNESCO)', '	-	International organizations (e.g. WHO, UN, UNESCO)'),
                ('Higher education\Academic institution (e.g. university \college)', '	Higher education\Academic institution (e.g. university \college)'),
                ('	Internet site for formal schooling\ K-12 education system','	Internet site for formal schooling\ K-12 education system'),
                ('	Informal science education and popular science (e.g.  science museum, Scientific American)', '	Informal science education and popular science (e.g.  science museum, Scientific American)'),
                ('	Scientific Journals (e.g. Science, Nature) or Google  Scholar', '	Scientific Journals (e.g. Science, Nature) or Google  Scholar'),
                ('Medical site (e.g. health insurance provider, hospital)', 'Medical site (e.g. health insurance provider, hospital)'),
                ('	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)','	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)'),
                ('	Media and communication (e.g. news sites)', '	Media and communication (e.g. news sites)'),
                ('Commercial / Economic (e.g. pharmaceutical     companies)', 'Commercial / Economic (e.g. pharmaceutical     companies)'),
                ('Satire site', 'Satire site'),
                ('Social media site (e.g. Twitter, Facebook, LinkedIn etc.)', 'Social media site (e.g. Twitter, Facebook, LinkedIn etc.)'),
                ('Fact checkers site', 'Fact checkers site'),
                ('others','others')

            )
            the_content_producer= models.CharField(max_length=255, choices=the_content_producer_options, blank=False)

            free_access = models.BooleanField()
            recent = (
                ('Not mentioned', 'Not mentioned'),
                ('IOver 10 years', 'Over 10 years'),
                ('	5 to 10 yea', '5 to 10 yea'),
                ('	 Rather new (1 to 5 years)', '	 Rather new (1 to 5 years)'),
                ('	Other',	'Other')
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('The Author is not mention', 'The Author is not mention'),
                ('The author is mentioned but there is no information about their background, or their background is not relevant', 'The author is mentioned but there is no information about their background, or their background is not relevant'),
                (' The author has relevant expertise to the content', ' The author has relevant expertise to the content')
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('NO', 'NO'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('There are no major scientific errors in the content', 'There are no major scientific errors in the content'),
                ('There are major scientific errors in the content (if so give an example)', 'There are major scientific errors in the content (if so give an example)'),
                ('Irrelevant', 'Irrelevant'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('Accurate', 'Accurate'),
                ('Neiter', 'Neiter'),
                ('Inaccurate', 'Inaccurate'),
                ('Irrelevant', 'Irrelevant'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('None of the below', 'ONone of the below'),
                ('Others', 'Others'),
                ('Place to leave comments\ ask questions', 'Place to leave comments\ ask questions'),
                ('Graphs', 'Graphs'),
                (' Relevant multimedia (e.g. pictures, video, animation etc.)', ' Relevant multimedia (e.g. pictures, video, animation etc.)'),
                ('Hyper-links', 'Hyper-links'),
                ('Numerical data', 'Numerical data'),
                (' List of sources', ' List of sources '),
                (' Citation or references to relevant literature', ' Citation or references to relevant literature'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('The content rejects the conspiracy', 'The content rejects the conspiracy'),
                (' Not sure', ' Not sure'),
                (' The content reinforce the conspiracy', ' The content reinforce the conspiracy'),
                ('Irrelevant', 'Irrelevant'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            options2= (
                ('NO', 'NO'),
                ('Not sure','Not sure'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            malicios_meaning = models.CharField(max_length=255, choices=options2, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options2, blank=False)
            specific_group = models.CharField(max_length=255, choices=options2, blank=False)

def create_new_tables():
    words = domain.objects.values_list('domain2_words', flat=True).distinct()
    for word in words:
        class NewTable(models.Model):
            id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            result_number = models.IntegerField()
            link = models.TextField()
            site_name = models.TextField()
            site_types = (
                ('Text', 'Text'),
                ('Information Search Database', '	Information Search Database'),
                ('	Video', 'Video'),
                ('	Simulation', '	Simulation'),
                ('	Other', 'Other')
            )
            site_type = models.CharField(max_length=255, choices=site_types, blank=False)
            the_content_producer_options = (
                ('	Government body (e.g. ministry of health, CDC, FDA, NASA)',
                 '	Government body (e.g. ministry of health, CDC, FDA, NASA)'),
                ('	NGO (Non Governmental Organizations)', 'NGO (Non Governmental Organizations)'),
                ('	Research organizations (e.g. CERN)', 'Research organizations (e.g. CERN)'),
                ('	International organizations (e.g. WHO, UN, UNESCO)',
                 '	-	International organizations (e.g. WHO, UN, UNESCO)'),
                ('Higher education\Academic institution (e.g. university \college)',
                 '	Higher education\Academic institution (e.g. university \college)'),
                ('	Internet site for formal schooling\ K-12 education system',
                 '	Internet site for formal schooling\ K-12 education system'),
                ('	Informal science education and popular science (e.g.  science museum, Scientific American)',
                 '	Informal science education and popular science (e.g.  science museum, Scientific American)'),
                ('	Scientific Journals (e.g. Science, Nature) or Google  Scholar',
                 '	Scientific Journals (e.g. Science, Nature) or Google  Scholar'),
                ('Medical site (e.g. health insurance provider, hospital)',
                 'Medical site (e.g. health insurance provider, hospital)'),
                ('	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)',
                 '	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)'),
                ('	Media and communication (e.g. news sites)', '	Media and communication (e.g. news sites)'),
                ('Commercial / Economic (e.g. pharmaceutical     companies)',
                 'Commercial / Economic (e.g. pharmaceutical     companies)'),
                ('Satire site', 'Satire site'),
                ('Social media site (e.g. Twitter, Facebook, LinkedIn etc.)',
                 'Social media site (e.g. Twitter, Facebook, LinkedIn etc.)'),
                ('Fact checkers site', 'Fact checkers site'),
                ('others', 'others')

            )
            the_content_producer = models.CharField(max_length=255, choices=the_content_producer_options, blank=False)

            free_access = models.BooleanField()
            recent = (
                ('Not mentioned', 'Not mentioned'),
                ('IOver 10 years', 'Over 10 years'),
                ('	5 to 10 yea', '5 to 10 yea'),
                ('	 Rather new (1 to 5 years)', '	 Rather new (1 to 5 years)'),
                ('	Other', 'Other')
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('The Author is not mention', 'The Author is not mention'),
                (
                'The author is mentioned but there is no information about their background, or their background is not relevant',
                'The author is mentioned but there is no information about their background, or their background is not relevant'),
                (' The author has relevant expertise to the content',
                 ' The author has relevant expertise to the content')
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('NO', 'NO'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('There are no major scientific errors in the content',
                 'There are no major scientific errors in the content'),
                ('There are major scientific errors in the content (if so give an example)',
                 'There are major scientific errors in the content (if so give an example)'),
                ('Irrelevant', 'Irrelevant'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('Accurate', 'Accurate'),
                ('Neiter', 'Neiter'),
                ('Inaccurate', 'Inaccurate'),
                ('Irrelevant', 'Irrelevant'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('None of the below', 'ONone of the below'),
                ('Others', 'Others'),
                ('Place to leave comments\ ask questions', 'Place to leave comments\ ask questions'),
                ('Graphs', 'Graphs'),
                (' Relevant multimedia (e.g. pictures, video, animation etc.)',
                 ' Relevant multimedia (e.g. pictures, video, animation etc.)'),
                ('Hyper-links', 'Hyper-links'),
                ('Numerical data', 'Numerical data'),
                (' List of sources', ' List of sources '),
                (' Citation or references to relevant literature', ' Citation or references to relevant literature'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('The content rejects the conspiracy', 'The content rejects the conspiracy'),
                (' Not sure', ' Not sure'),
                (' The content reinforce the conspiracy', ' The content reinforce the conspiracy'),
                ('Irrelevant', 'Irrelevant'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            options2 = (
                ('NO', 'NO'),
                ('Not sure', 'Not sure'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            malicios_meaning = models.CharField(max_length=255, choices=options2, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options2, blank=False)
            specific_group = models.CharField(max_length=255, choices=options2, blank=False)
def create_new_tables():
    words = domain.objects.values_list('domain3_words', flat=True).distinct()
    for word in words:
        class NewTable(models.Model):
            id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            result_number = models.IntegerField()
            link = models.TextField()
            site_name = models.TextField()
            site_types = (
                ('Text', 'Text'),
                ('Information Search Database', '	Information Search Database'),
                ('	Video', 'Video'),
                ('	Simulation', '	Simulation'),
                ('	Other', 'Other')
            )
            site_type = models.CharField(max_length=255, choices=site_types, blank=False)
            the_content_producer_options = (
                ('	Government body (e.g. ministry of health, CDC, FDA, NASA)',
                 '	Government body (e.g. ministry of health, CDC, FDA, NASA)'),
                ('	NGO (Non Governmental Organizations)', 'NGO (Non Governmental Organizations)'),
                ('	Research organizations (e.g. CERN)', 'Research organizations (e.g. CERN)'),
                ('	International organizations (e.g. WHO, UN, UNESCO)',
                 '	-	International organizations (e.g. WHO, UN, UNESCO)'),
                ('Higher education\Academic institution (e.g. university \college)',
                 '	Higher education\Academic institution (e.g. university \college)'),
                ('	Internet site for formal schooling\ K-12 education system',
                 '	Internet site for formal schooling\ K-12 education system'),
                ('	Informal science education and popular science (e.g.  science museum, Scientific American)',
                 '	Informal science education and popular science (e.g.  science museum, Scientific American)'),
                ('	Scientific Journals (e.g. Science, Nature) or Google  Scholar',
                 '	Scientific Journals (e.g. Science, Nature) or Google  Scholar'),
                ('Medical site (e.g. health insurance provider, hospital)',
                 'Medical site (e.g. health insurance provider, hospital)'),
                ('	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)',
                 '	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)'),
                ('	Media and communication (e.g. news sites)', '	Media and communication (e.g. news sites)'),
                ('Commercial / Economic (e.g. pharmaceutical     companies)',
                 'Commercial / Economic (e.g. pharmaceutical     companies)'),
                ('Satire site', 'Satire site'),
                ('Social media site (e.g. Twitter, Facebook, LinkedIn etc.)',
                 'Social media site (e.g. Twitter, Facebook, LinkedIn etc.)'),
                ('Fact checkers site', 'Fact checkers site'),
                ('others', 'others')

            )
            the_content_producer = models.CharField(max_length=255, choices=the_content_producer_options, blank=False)

            free_access = models.BooleanField()
            recent = (
                ('Not mentioned', 'Not mentioned'),
                ('IOver 10 years', 'Over 10 years'),
                ('	5 to 10 yea', '5 to 10 yea'),
                ('	 Rather new (1 to 5 years)', '	 Rather new (1 to 5 years)'),
                ('	Other', 'Other')
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('The Author is not mention', 'The Author is not mention'),
                (
                'The author is mentioned but there is no information about their background, or their background is not relevant',
                'The author is mentioned but there is no information about their background, or their background is not relevant'),
                (' The author has relevant expertise to the content',
                 ' The author has relevant expertise to the content')
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('NO', 'NO'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('There are no major scientific errors in the content',
                 'There are no major scientific errors in the content'),
                ('There are major scientific errors in the content (if so give an example)',
                 'There are major scientific errors in the content (if so give an example)'),
                ('Irrelevant', 'Irrelevant'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('Accurate', 'Accurate'),
                ('Neiter', 'Neiter'),
                ('Inaccurate', 'Inaccurate'),
                ('Irrelevant', 'Irrelevant'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('None of the below', 'ONone of the below'),
                ('Others', 'Others'),
                ('Place to leave comments\ ask questions', 'Place to leave comments\ ask questions'),
                ('Graphs', 'Graphs'),
                (' Relevant multimedia (e.g. pictures, video, animation etc.)',
                 ' Relevant multimedia (e.g. pictures, video, animation etc.)'),
                ('Hyper-links', 'Hyper-links'),
                ('Numerical data', 'Numerical data'),
                (' List of sources', ' List of sources '),
                (' Citation or references to relevant literature', ' Citation or references to relevant literature'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('The content rejects the conspiracy', 'The content rejects the conspiracy'),
                (' Not sure', ' Not sure'),
                (' The content reinforce the conspiracy', ' The content reinforce the conspiracy'),
                ('Irrelevant', 'Irrelevant'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            options2 = (
                ('NO', 'NO'),
                ('Not sure', 'Not sure'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            malicios_meaning = models.CharField(max_length=255, choices=options2, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options2, blank=False)
            specific_group = models.CharField(max_length=255, choices=options2, blank=False)

def create_new_tables():
    words = domain.objects.values_list('domain4_words', flat=True).distinct()
    for word in words:
        class NewTable(models.Model):
            id = models.ForeignKey(volunteer, on_delete=models.CASCADE)
            original_word = models.ForeignKey(domain, on_delete=models.CASCADE)
            result_number = models.IntegerField()
            link = models.TextField()
            site_name = models.TextField()
            site_types = (
                ('Text', 'Text'),
                ('Information Search Database', '	Information Search Database'),
                ('	Video', 'Video'),
                ('	Simulation', '	Simulation'),
                ('	Other', 'Other')
            )
            site_type = models.CharField(max_length=255, choices=site_types, blank=False)
            the_content_producer_options = (
                ('	Government body (e.g. ministry of health, CDC, FDA, NASA)',
                 '	Government body (e.g. ministry of health, CDC, FDA, NASA)'),
                ('	NGO (Non Governmental Organizations)', 'NGO (Non Governmental Organizations)'),
                ('	Research organizations (e.g. CERN)', 'Research organizations (e.g. CERN)'),
                ('	International organizations (e.g. WHO, UN, UNESCO)',
                 '	-	International organizations (e.g. WHO, UN, UNESCO)'),
                ('Higher education\Academic institution (e.g. university \college)',
                 '	Higher education\Academic institution (e.g. university \college)'),
                ('	Internet site for formal schooling\ K-12 education system',
                 '	Internet site for formal schooling\ K-12 education system'),
                ('	Informal science education and popular science (e.g.  science museum, Scientific American)',
                 '	Informal science education and popular science (e.g.  science museum, Scientific American)'),
                ('	Scientific Journals (e.g. Science, Nature) or Google  Scholar',
                 '	Scientific Journals (e.g. Science, Nature) or Google  Scholar'),
                ('Medical site (e.g. health insurance provider, hospital)',
                 'Medical site (e.g. health insurance provider, hospital)'),
                ('	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)',
                 '	Encyclopedia or dictionary (e.g. Wikipedia, Oxford   dictionary)'),
                ('	Media and communication (e.g. news sites)', '	Media and communication (e.g. news sites)'),
                ('Commercial / Economic (e.g. pharmaceutical     companies)',
                 'Commercial / Economic (e.g. pharmaceutical     companies)'),
                ('Satire site', 'Satire site'),
                ('Social media site (e.g. Twitter, Facebook, LinkedIn etc.)',
                 'Social media site (e.g. Twitter, Facebook, LinkedIn etc.)'),
                ('Fact checkers site', 'Fact checkers site'),
                ('others', 'others')

            )
            the_content_producer = models.CharField(max_length=255, choices=the_content_producer_options, blank=False)

            free_access = models.BooleanField()
            recent = (
                ('Not mentioned', 'Not mentioned'),
                ('IOver 10 years', 'Over 10 years'),
                ('	5 to 10 yea', '5 to 10 yea'),
                ('	 Rather new (1 to 5 years)', '	 Rather new (1 to 5 years)'),
                ('	Other', 'Other')
            )
            recent_information = models.CharField(max_length=255, choices=recent, blank=False)
            auther_backgrounds = (
                ('The Author is not mention', 'The Author is not mention'),
                (
                'The author is mentioned but there is no information about their background, or their background is not relevant',
                'The author is mentioned but there is no information about their background, or their background is not relevant'),
                (' The author has relevant expertise to the content',
                 ' The author has relevant expertise to the content')
            )
            auther_background = models.CharField(max_length=255, choices=auther_backgrounds, blank=False)
            the_need_of_scientfic_background = models.BooleanField()
            options = (
                ('NO', 'NO'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            lay_people = models.CharField(max_length=255, choices=options, blank=False)
            depend_lay_people = models.BooleanField()
            major_err = (
                ('There are no major scientific errors in the content',
                 'There are no major scientific errors in the content'),
                ('There are major scientific errors in the content (if so give an example)',
                 'There are major scientific errors in the content (if so give an example)'),
                ('Irrelevant', 'Irrelevant'),
            )
            major_error = models.CharField(max_length=255, choices=major_err, blank=False)
            scale_variable_major_error = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            # we have to wrhte a note about the scale
            accurate = (
                ('Accurate', 'Accurate'),
                ('Neiter', 'Neiter'),
                ('Inaccurate', 'Inaccurate'),
                ('Irrelevant', 'Irrelevant'),
            )
            accurate_content = models.CharField(max_length=255, choices=accurate, blank=False)
            scale_variable_acccurate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
            sources = (
                ('None of the below', 'ONone of the below'),
                ('Others', 'Others'),
                ('Place to leave comments\ ask questions', 'Place to leave comments\ ask questions'),
                ('Graphs', 'Graphs'),
                (' Relevant multimedia (e.g. pictures, video, animation etc.)',
                 ' Relevant multimedia (e.g. pictures, video, animation etc.)'),
                ('Hyper-links', 'Hyper-links'),
                ('Numerical data', 'Numerical data'),
                (' List of sources', ' List of sources '),
                (' Citation or references to relevant literature', ' Citation or references to relevant literature'),
            )
            multi_option = forms.MultipleChoiceField(choices=sources, widget=forms.CheckboxSelectMultiple)
            refernce_evrey_Day = models.CharField(max_length=255, choices=options, blank=False)
            local_example = models.CharField(max_length=255, choices=options, blank=False)
            advantages = models.CharField(max_length=255, choices=options, blank=False)
            options1 = (
                ('The content rejects the conspiracy', 'The content rejects the conspiracy'),
                (' Not sure', ' Not sure'),
                (' The content reinforce the conspiracy', ' The content reinforce the conspiracy'),
                ('Irrelevant', 'Irrelevant'),
            )
            content_reject = models.CharField(max_length=255, choices=options1, blank=False)
            options2 = (
                ('NO', 'NO'),
                ('Not sure', 'Not sure'),
                ('YES', 'YES'),
                ('Irrelevant', 'Irrelevant'),
            )
            malicios_meaning = models.CharField(max_length=255, choices=options2, blank=False)
            claims_contradict = models.CharField(max_length=255, choices=options2, blank=False)
            specific_group = models.CharField(max_length=255, choices=options2, blank=False)
def create_new_table_lan():
    for l in pycountry.languages:
        class NewTable(models.Model):
            domain_1=models.CharField(max_length=255, blank=False)
            domain_2 = models.CharField(max_length=255, blank=False)
            domain_3 = models.CharField(max_length=255, blank=False)
            domain_4 = models.CharField(max_length=255, blank=False)


