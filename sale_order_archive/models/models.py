# -*- coding: utf-8 -*-
from odoo import models, fields, api


class sale_order_archive(models.Model):
    _name = 'sale_order_archive.sale_order_archive'
    _description = 'Sale order archive modul'
    _order = 'order_create_date, customer, sale_person'

    name = fields.Char(string='Name', required=True)
    order_create_date = fields.Date(string='Order create date', required=True)
    customer = fields.Many2one('res.partner', string='Customer', required=True)
    sale_person = fields.Many2one('res.user', string='Sale person', required=True)
    order_total_amount = fields.Monetary(currency_field='order_currency', string='Order total amount', required=True)
    order_currency = fields.Many2one('res.currency', string='Currency', required=True)
    count_order_lines = fields.Integer(string='Count of order lines', required=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
