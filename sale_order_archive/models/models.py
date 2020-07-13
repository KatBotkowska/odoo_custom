# -*- coding: utf-8 -*-
import datetime


from odoo import models, fields, api


class sale_order_archive(models.Model):
    _name = 'sale_order_archive.sale_order_archive'
    _description = 'Sale order archive modul'
    _inherit = 'sale.order'
    _order = 'order_create_date, customer, sale_person'

    name = fields.Char(string='Name', required=True)
    order_create_date = fields.Date(string='Order create date', required=True)
    customer = fields.Many2one('res.partner', string='Customer', required=True)
    sale_person = fields.Many2one('res.users', string='Sale person', required=True)
    order_total_amount = fields.Monetary(currency_field='order_currency', string='Order total amount', required=True)
    order_currency = fields.Many2one('res.currency', string='Currency', required=True)
    count_order_lines = fields.Integer(string='Count of order lines', required=True)

    def _archive_sale_orders(self):
        # today = datetime.date.today()
        # date_condition = today-datetime.timedelta(days=7)
        # old_orders = self.env['sale.order'].search()
        older = self.env.cr.execute('SELECT '
                                    'name, order_create_date, customer, sale_person, order_total_amount,'
                                    'order_currency, count_order_lines FROM sale.order '
                                    'WHERE order_create_date<datetime.date.today()-datetime.timedelta(days=7)')
        if older:
            # self.env.cr.execute('CREATE name, order_create_date, customer, sale_person, order_total_amount, '
            #                     'order_currency, count_order_lines FROM sale.order')
            for row in older:
                self.env['sale_order_archive.sale_order_archive'].create({
                    'name': row['name'],
                    'order_create_date': row['order_create_date'],
                    'customer':row['customer'],
                    'sale_person':row['sale_person'],
                    'order_total_amount':row['order_total_amount'],
                    'order_currency':row['order_currency'],
                    'count_order_lines':row['count_order_lines']
            })
            self.env.cr.execute('DELETE * FROM sale.order WHERE '
                                'order_create_date<datetime.date.today()-datetime.timedelta(days=7)')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
