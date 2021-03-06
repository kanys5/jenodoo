# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def action_see_quality_control_points(self):
        action = super().action_see_quality_control_points()
        action['context'].update({'search_default_quality_points': 1})
        return action

    def action_see_quality_checks(self):
        action = super().action_see_quality_checks()
        action['context'].update({'search_default_quality_checks': 1})
        return action

class ProductProduct(models.Model):
    _inherit = "product.product"

    def action_see_quality_control_points(self):
        action = super().action_see_quality_control_points()
        action['context'].update({'search_default_quality_points': 1})
        return action

    def action_see_quality_checks(self):
        action = super().action_see_quality_checks()
        action['context'].update({'search_default_quality_checks': 1})
        return action

    def _additional_quality_point_where_clause(self):
        return super(ProductProduct, self)._additional_quality_point_where_clause() + """
            AND operation_id IN (
                    SELECT ope.id FROM mrp_routing_workcenter AS ope
                INNER JOIN mrp_bom as bom
                        ON ope.bom_id = bom.id
                     WHERE bom.active = 't' )
        """
