from odoo import models, fields

from .common import company_id_field

class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'hotel rooms master list'
    _order = 'name'

    name = fields.Char('Room No')
    description = fields.Char('Room Description')

    roomtype_id = fields.Many2one('hotel.roomtypes', string='Room Type')

    roomtypename = fields.Char('Room Type Name', related='roomtype_id.name')

    company_id = company_id_field()