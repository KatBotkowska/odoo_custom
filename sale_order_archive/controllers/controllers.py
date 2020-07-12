# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderArchive(http.Controller):
#     @http.route('/sale_order_archive/sale_order_archive/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_archive/sale_order_archive/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_archive.listing', {
#             'root': '/sale_order_archive/sale_order_archive',
#             'objects': http.request.env['sale_order_archive.sale_order_archive'].search([]),
#         })

#     @http.route('/sale_order_archive/sale_order_archive/objects/<model("sale_order_archive.sale_order_archive"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_archive.object', {
#             'object': obj
#         })
