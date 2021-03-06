#-*- coding: UTF-8 -*-
import os
import settings
from prototipo.utils.functions import get_file_extension, upload_file, get_gdoc_key, store_file
from django.db import models
from course_instance import CourseInstance
from prototipo.models import Group
from report import Report

class ReportDescription(models.Model):
    '''
    Esquema de una entrega, define fechas y el
    template a ocupar para su feedback
    '''
    name = models.CharField(max_length = 255)
    course_instance = models.ForeignKey(CourseInstance)
    delivery_start_date = models.DateTimeField()
    delivery_end_date = models.DateTimeField()
    feedback_return_date = models.DateTimeField()
    feedback_template_key = models.CharField(max_length = 255)

    @staticmethod
    def generate_report(form, course_instance):
        report = ReportDescription()
        report.name = form.cleaned_data['name']
        report.delivery_start_date = form.cleaned_data['delivery_start_date']
        report.delivery_end_date = form.cleaned_data['delivery_end_date']
        report.feedback_return_date = form.cleaned_data['feedback_return_date']
        report.course_instance = course_instance
        report.feedback_template_key = ''
        report.save()

        report.store_file(form.cleaned_data['feedback_template'])
        document_url = upload_file(report, str(report.course_instance) + ' - ' + report.name + ' - Feedback Template')
        report.feedback_template_key = get_gdoc_key(document_url)

        report.save()

        groups = Group.objects.filter(leader__course_instance = course_instance)
        for group in groups:
            Report.generate_report(report, group)

    def store_file(self, uploaded_file):
        store_file(uploaded_file, 'uploaded_templates', self.id, ['.xls'])

    def __unicode__(self):
        return unicode(self.course_instance) + ' - ' + self.name

    class Meta:
        app_label = 'prototipo'
