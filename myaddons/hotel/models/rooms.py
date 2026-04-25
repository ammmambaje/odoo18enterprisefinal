from odoo import models, fields

class rooms(models.Model):
    _name = 'hotel.rooms'
    _inherit = ['hotel.company.mixin']
    _description = 'hotel rooms master list'
    _order = 'name'

    name = fields.Char('Room No')
    description = fields.Char('Room Description')

    roomtype_id = fields.Many2one('hotel.roomtypes', string='Room Type')

    roomtypename = fields.Char('Room Type Name', related='roomtype_id.name')