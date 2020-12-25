# -*- coding: utf-8 -*-

from odoo import models, fields, api

class covid19(models.Model):
    
    _name = 'covid.covid19'
    source = fields.Char(string='Source', required=True,  default=fields.Datetime.now())
    date = fields.Date(string='Date Time',required=True)
    country_id =  fields.Many2one('res.country',required=True, default=0)
    infected = fields.Integer(string='Infected',required=True, default=0)
    recovered = fields.Integer(string='Recovered',required=True, default=0)
    deseaced = fields.Integer(string='Deseaced',required=True, default=0)
    total_infected = fields.Integer(string='Total Infected',compute='set_total_infected',required=True,default=0)
    total_recovered = fields.Integer(string='Total Recovered',compute='set_total_recovered',required=True,default=0)
    total_deceased = fields.Integer(string='Total Deceased',compute='set_total_deceased',required=True,default=0)

    def set_total_infected(self):
        for data in self:
            domain=[
                    ('country_id','=',data.country_id.id),
                    ('date','<',data.date),
                    ]
            records=self.search(domain)
            Infecteds=records.mapped('infected')
            data.total_infected=sum(Infecteds)+data.infected
    def set_total_recovered(self):
        for data in self:
            domain=[
                    ('country_id','=',data.country_id.id),
                    ('date','<',data.date),
                    ]
            records=self.search(domain)
            Recovereds=records.mapped('recovered')
            data.total_recovered=sum(Recovereds)+data.recovered
            
    def set_total_deceased(self):
        for data in self:
            domain=[
                    ('country_id','=',data.country_id.id),
                    ('date','<',data.date),
                    ]
            records=self.search(domain)
            Deceaseds=records.mapped('deseaced')
            data.total_deceased=sum(Deceaseds)+data.deseaced
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100