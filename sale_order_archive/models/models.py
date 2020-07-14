# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


class sale_order_archive(models.Model):
    _name = 'sale_order_archive.sale_order_archive'
    _description = 'Sale order archive modul'
    # _inherits = 'sale.order'
    _order = 'create_date, partner_id, user_id'

    name = fields.Char(string='Name', required=True)
    create_date = fields.Date(string='Order create date', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    user_id = fields.Many2one('res.users', string='Sale person', required=True)
    amount_total = fields.Monetary(currency_field='currency_id', string='Order total amount', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    order_line = fields.Integer(string='Count of order lines', required=True)

    # @api.one
    def _archive_sale_orders(self):
        query = 'SELECT name, create_date, partner_id, user_id, amount_total, currency_id, order_line ' \
                'FROM sale.order WHERE create_date > %s'
        query_params = datetime.date.today() - datetime.timedelta(days=7)
        old_orders = self.env.cr.execute(query, query_params)
        orders_to_archive=self.env['sale_order_archive.sale_order_archive'].search([('create_date', '>', query_params)])
        if orders_to_archive:
            for set in orders_to_archive:
                self.env['sale_order_archive.sale_order_archive'].create({
                    'name': set['name'],
                    'create_date': set['create_date'],
                    'partner_id': set['partner_id'],
                    'user_id': set['user_id'],
                    'amount_total': set['amount_total'],
                    'currency_id': set['currency_id'],
                    'order_line': set['order_line']
                })
            orders_to_archive.unlink()

        if old_orders:
            for set in old_orders.fetchall():
                self.env['sale_order_archive.sale_order_archive'].create({
                    'name': set['name'],
                    'create_date': set['create_date'],
                    'partner_id': set['partner_id'],
                    'user_id': set['user_id'],
                    'amount_total': set['amount_total'],
                    'currency_id': set['currency_id'],
                    'order_line': set['order_line']
                })
            self.env["sale.order"].search([('create_date', '>', query_params)]).unlink()

