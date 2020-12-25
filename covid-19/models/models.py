# -*- coding: utf-8 -*-

from odoo import models, fields, api

class covid_19(models.Model):
    _name = 'covid.covid_19'
    _order = 'id desc'

    source = fields.Char(string='Source',required=True)
    date = fields.Datetime(string='Date Time',required=True,default=fields.Datetime.now())
    country_id = fields.Many2one('res.country',required=True)
    infected = fields.Integer(string='Infected',required=True,default=0)
    recovered = fields.Integer(string='Recovered',required=True,default=0)
    deseaced = fields.Integer(string='Deseaced',required=True,default=0)
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
    
    def set_percentage_infected(self):
        total=0
        if self.infected:
            total=(self.infected*100)/self.total_infected
        return total
        
    def set_percentage_recovered(self):
        total=0
        if self.recovered:
            total=(self.recovered*100)/self.total_recovered
        return total 
        
    def set_percentage_deseaced(self):
        total=0
        if self.deseaced:
            total=(self.deseaced*100)/self.total_deceased
        return total
        
        
