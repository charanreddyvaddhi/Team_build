from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Technology(models.Model):
    """Model representing resource technology"""
    tech = models.CharField(max_length=200,
                            help_text='Enter technologies you are experienced on(if freshers mention "Fresher")')

    def __str__(self):
        """String for representing the Model object."""
        return self.tech


class Skill(models.Model):
    """model representing resource skills"""
    skills = models.CharField(max_length=200, help_text="Enter your skills(Technical or personal ...etc)")

    def __str__(self):
        """String for representing the Model object."""
        return self.skills


class People(models.Model):
    """model representing resource details"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    About = models.TextField(help_text='Resume of candidate')

    education = models.ForeignKey("Edu_Qualification", on_delete=models.SET_NULL, null=True)
    technologies = models.ManyToManyField(Technology, help_text="enter technology you are experience on(if freshers "
                                                                "mention Fresher)")
    experience = models.ForeignKey("Experience", on_delete=models.SET_NULL, null=True)
    ratings = models.ForeignKey("Rating", on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill, help_text="enter your skills(Technical or personal ...etc)")

    class Meta:
        ordering = ['first_name']

    def get_absolute_url(self):
        # Returns the url to access a particular resource instance.
        return reverse('Resource-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Experience(models.Model):
    """model representing resource experience"""
    year = models.CharField(max_length=50, help_text="Enter Years of experience")

    """def get_absolute_url(self):
        # Returns the url to access a particular author instance.
        return reverse('Resource-detail', args=[str(self.id)])"""

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.year


class Rating(models.Model):
    """model representing resource ratings"""
    rate = models.CharField(max_length=100, help_text="Enter your rating by HR")

    """def get_absolute_url(self):
        # Returns the url to access a particular author instance.
        return reverse('Resource-detail', args=[str(self.id)])"""

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.rate


class Edu_Qualification(models.Model):
    """model representing resource edu_qualifications"""
    Education = models.CharField(max_length=100, help_text="Enter the Educational qualifications")

    """def get_absolute_url(self):
        # Returns the url to access a particular author instance.
        return reverse('Resource-detail', args=[str(self.id)])"""

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Education


class Resume(models.Model):
    """model representing resource resume"""
    resume = models.TextField(help_text="Enter your resume")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.resume
