from django.db import models

# Create your models here.
from django.db import models
import pycountry

from django.conf import settings


class user(models.Model):
    ID= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    mail=models.EmailField(primary_key=True)
    is_vervied = models.BooleanField()
    age = models.IntegerField()
    native_country = models.CharField(max_length=255,null=False,default='unknown',choices=[(c.name, c.name) for c in pycountry.countries])
    current_country = models.CharField(max_length=255,null=False,default='unknown', choices=[(c.name, c.name) for c in pycountry.countries])
    recent_year_of_knowldge = models.IntegerField()
    language = models.CharField(max_length=255, choices=[(l.name, l.name) for l in pycountry.languages])


# class choise(models.Model):
#     ID = models.ForeignKey(user,null=True,on_delete=models.CASCADE)
#     domain_CHOICES = (
#        ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#      )
#     chosen_doaimn = models.CharField(max_length=20, choices=domain_CHOICES, null=False, default='unknown')
#     what_to_do_CHOICES = (
#         ('domain1', 'searching a word in  exsiting doaimn'),
#         ('domain2', 'suggest a word with the result of searching '),
#         ('domain3', 'transalte a domain'),
#
#     )
#     what_to_do = models.CharField(max_length=20, choices=what_to_do_CHOICES)
#     domain_CHOICES = (
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#     )
#     the_words_of_domain1=(
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#
#     )
#     the_words_of_domain2 = (
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#     )
#     the_words_of_domain3 = (
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#     )
#     the_words_of_domain4 = (
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#         ('domain1', 'domain1'),
#         ('domain2', 'domain2'),
#         ('domain3', 'domain3'),
#         ('domain4', 'domain4'),
#     )
#     dependent_choice_1 = models.CharField(max_length=255, choices=domain_CHOICES,blank=False)
#     dependent_choice_1_1 = models.CharField(max_length=255, choices=the_words_of_domain1, blank=False)
#     dependent_choice_1_2 = models.CharField(max_length=255, choices=the_words_of_domain2, blank=False)
#     dependent_choice_1_3 = models.CharField(max_length=255, choices=the_words_of_domain3, blank=False)
#     dependent_choice_1_4 = models.CharField(max_length=255, choices=the_words_of_domain4, blank=False)
#     dependent_choice_2 = models.CharField(max_length=255, blank=False)
#     dependent_choice_3 = models.CharField(max_length=255, choices=domain_CHOICES,blank=False)

class existing_language_domains(models.Model):
    domain_1 = models.CharField(max_length=255)
    domain_2 = models.CharField(max_length=255)
    domain_3 = models.CharField(max_length=255)
    domain_4 = models.CharField(max_length=255)

class existing_phrases_domains(models.Model):
        domain_1 = models.CharField(max_length=255)
        domain_2 = models.CharField(max_length=255)
        domain_3 = models.CharField(max_length=255)
        domain_4 = models.CharField(max_length=255)

class PhraseTable(models.Model):
    phrase = models.ForeignKey(existing_phrases_domains, on_delete=models.CASCADE)
    # adding any other fields you need for this table
    answers=models.CharField(max_length=255)

def create_phrase_tables():
    phrases = existing_phrases_domains.objects.all()
    for phrase in existing_phrases_domains:
        PhraseTable.objects.create(phrase=phrase)
class sugessted_phrases(models.Model):
    domain_name = models.CharField(max_length=255)
    phrase=models.CharField(max_length=255)
# class results_exsit_domain1(models.Model):





