from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def create(self, vals):
        res = super(SaleOrderLine, self).create(vals)
        for rec in res:
            if rec.product_id.qty_available <= 0:
                raise UserError(
                    _("You plan to sell'{}'  Unit(s) of {} but you only have{} Unit(s) available in YourCompany warehouse.".format(
                        rec.product_uom_qty, rec.product_id.qty_available, rec.product_id.name)))
            return res
        
    def write(self, vals):
        for rec in self:
            res = super(SaleOrderLine, self).write(vals)
            if rec.product_id.qty_available <= 0:
                raise UserError(
                    _("You plan to sell {}  Unit(s) of {} but you only have {} Unit(s) available in YourCompany warehouse.".format(
                        rec.product_uom_qty, rec.product_id.name, rec.product_id.qty_available)))
            return res
