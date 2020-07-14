# -*- coding: utf-8 -*-
import datetime
import logging

from odoo import models, fields


class sale_order_archive(models.Model):
    _name = 'sale_order_archive.sale_order_archive'
    _description = 'Sale order archive modul'
    _order = 'create_date, partner_id, user_id'

    name = fields.Char(string='Name', required=True)
    create_date = fields.Date(string='Order create date', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    user_id = fields.Many2one('res.users', string='Sale person', required=True)
    amount_total = fields.Monetary(currency_field='currency_id', string='Order total amount', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    order_line = fields.Integer(string='Count of order lines', required=True)

    def _archive_sale_orders(self):
        border_date = datetime.datetime.now() - datetime.timedelta(days=7)
        date = border_date.strftime("%Y-%m-%d")
        orders_to_archive = self.env['sale.order'].search([('create_date', '>', date)])
        if orders_to_archive:
            for set in orders_to_archive:
                lines = len(self.env['sale.order.line'].search([('order_id', '=', set['id'])])._ids)
                self.env['sale_order_archive.sale_order_archive'].create({
                    'name': set['name'],
                    'create_date': set['create_date'],
                    'partner_id': set['partner_id'],
                    'user_id': set['user_id'],
                    'amount_total': set['amount_total'],
                    'currency_id': set['currency_id'],
                    'order_line': lines
                })
            orders_to_archive.unlink()
            logging.info('Archive done')
        else:
            logging.info('No rows to archive')
