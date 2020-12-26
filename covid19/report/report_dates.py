# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api

class ReportCovid19WithDates(models.AbstractModel):
    _name = 'report.covid19.report_covid_19_dates'
    _description = 'COVID-19 report with dates'

    @api.model
    def _get_report_values(self, docids, data=None):
        print ('fskfjskjdfs')
        print ('fskfjskjdfs')
        print ('fskfjskjdfs')
        print ('fskfjskjdfs')
        return {
            'doc_ids': docids,
            'doc_model': 'covid19.date.report.wizard',
            'docs': self.env['covid19.date.report.wizard'].browse(docids),
            'report_type': data.get('report_type') if data else '',
        }
