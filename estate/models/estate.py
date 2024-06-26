from odoo import models, fields
from dateutil.relativedelta import relativedelta

class Estate(models.Model):
    _name= "estate"
    _description= "Estate"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    number_of_bedrooms=fields.Integer(default=2)


    date_availability = fields.Date(default=lambda self: fields.Datetime.today() + relativedelta(months=3), copy=False)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new','New'),
            ('ongoing','Ongoing'),
            ('done','Done'),
            ('cancel','Cancel'),
        ],
        string="Status", readonly=True, copy=False, tracking=3, default='new')