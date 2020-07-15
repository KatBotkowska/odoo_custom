# Sale Order Archive - Odoo custom module
New Odoo custom module: Sale Order Archive.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)



## General info:
New Odoo custom module: Sale Order Archive -  based on Odoo Sale module.
View: Tree, Form for „sale.order.archive” model. User can access to tree view from module  Sales/Orders/Archvied Orders.
Cron (running every 24 hours). Cron create new „sale.order.archive” object for all orders (sale.order) older than 7 days and delete archived „sale.order” objects.

## Technologies

* Odoo v.13 



