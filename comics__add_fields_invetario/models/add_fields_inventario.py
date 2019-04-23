# -*- coding:utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models


class add_fields(models.Model):
    """docstring for ClassName"""
    _inherit = 'product.template'


    x_autor = fields.Many2many('res.partner', #modelo de donde saca los atributos
                               string="autor",
                               help="Se agregará automáticamente a la descripción"
                               )
	
    x_editorial = fields.Many2one('res.partner',
                                  string="editorial",
                                  help="Se agregará automáticamente a la descripción"
                                  )

    @api.model
    def create(self, vals):
        producto_creado = super(add_fields, self).create(vals)
        #Actualiza la descripción después de guardar el producto
        editoriales = ""
        authores = ""
        for editorial in producto_creado.x_editorial:
            editoriales += editorial.name
        for author in producto_creado.x_autor:
            authores += author.name + ", "
        descripcion=producto_creado.description_sale
        if descripcion==False:
            producto_creado.description_sale=" * Autor(es): "+authores+" Editorial: "+editoriales
        else:
            producto_creado.description_sale=descripcion+" * Autor(es): "+authores+" Editorial: "+editoriales
        return producto_creado
    
    @api.multi
    def write(self, vals):
        self.ensure_one()
        producto_actualizado=super(add_fields, self).write(vals)    
        #generar la nueva descripción del producto
        editoriales = ""
        authores = ""
        nueva_descripcion=""
        for editorial in self.x_editorial:
            editoriales += editorial.name
        for author in self.x_autor:
            authores += author.name + ", "
        descripcion=self.description_sale
        if descripcion==False:
            nueva_descripcion=" * Autor(es): "+authores+" Editorial: "+editoriales
        else:
            lista=descripcion.split("*")
            nueva_descripcion=lista[0]
            nueva_descripcion=descripcion+" * Autor(es): "+authores+" Editorial: "+editoriales
        
        vals['description_sale']=nueva_descripcion
        producto_actualizado=super(add_fields, self).write(vals)
