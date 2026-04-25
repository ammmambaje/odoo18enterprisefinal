# -*- coding: utf-8 -*-

from odoo import models, fields


class roomtypes(models.Model):
    _name = 'hotel.roomtypes'
    _inherit = ['hotel.company.mixin']
    _description = 'hotel roomtypes master list'
    _order = 'name'

    name = fields.Char('Room Type Name')
    description = fields.Char('Room Type Description')
    pax = fields.Char('PAX')
    imageroom = fields.Image('Room')
    imagebathroom = fields.Image('Bath Room')

    room_ids = fields.One2many('hotel.rooms', 'roomtype_id', string='Rooms')
    dailycharges_ids = fields.One2many('hotel.dailycharges', 'roomtype_id', string='Daily Charges')