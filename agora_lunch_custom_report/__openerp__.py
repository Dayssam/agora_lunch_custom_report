# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2005-2016 Agora Developpement (<http://agoradeveloppement.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
 
# noinspection PyStatementEffect
{
    "name" : "Agora Lunch Custom report",
    
    "author" : "Red  ROUICHI",
    
    
    "licence" : "AGPL-3",
    "description": """
Lunch Custom
====================================
custom lunch report / group by product
& show the quantity of each product
                    """,
    "depends" : ['lunch'],
    "data" : [
        'lunch_order_views_custom_report.xml',
        'lunch_order_templates_custom_report.xml',

        ],
    "demo" : [],
    "installable": True,
    "auto_install": False,
    "application": True,
    'price': 0.0,
    'currency': 'EUR',
}
