
from odoo import models, api, fields


class Mostrar_Wizard(models.TransientModel ):
    _name = "mostrar.wizard"
    _inherit = ['stock.picking']
    picking_quantity = fields.Selection([
        ('picking', 'Transferir cantidades'),
        ('custom', 'Personalizado'),
        ], string="Cantidad para imprimir" )
    formatear = fields.Selection([('11cm x 15cm', '11cm x 15cm'),],string="Formatear")
    extra_html=fields.Html(string="Contenido extra")

    def create_report(self):
        return self.env.ref('tag_print.report_etiqueta').report_action(self)
    
    #me tira error que no encuentra el registro o que fue eliminado
    #def create_report(self):
    #    return self.env["ir.actions.actions"]._for_xml_id("tag_print.report_etiqueta")
    
    #def create_report(self):     stock.stock_reception_action
    #    action = self.env['ir.actions.act_window']._for_xml_id('product.action_open_label_layout')
    #    action['context'] = {'default_product_ids': self.ids}
    #    return action
    
    #def create_report(self):
    #    view = self.env.ref('stock.product_label_layout_form_picking')
    #    return {
    #        'name': _('Choose Labels Layout'),
    #        'type': 'ir.actions.act_window',
    #        'res_model': 'product.label.layout',
    #        'views': [(view.id, 'form')],
    #        'target': 'new',
    #        'context': {
    #            'default_product_ids': self.move_lines.product_id.ids,
    #            'default_move_line_ids': self.move_line_ids.ids,
    #            'default_picking_quantity': 'picking'},
    #    }
    
    