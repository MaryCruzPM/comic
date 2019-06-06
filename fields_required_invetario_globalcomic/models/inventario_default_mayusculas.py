# -*- coding:utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class add_fields(models.Model):
    """docstring for ClassName"""
    _inherit = 'product.template'


    
    @api.model
    def create(self, vals):
        producto_creado = super(add_fields, self).create(vals)
        # s='hola'
        # print(s.upper()) 
        valor=producto_creado.name
        # print(valor) 
        # print(valor.upper()) #funtion para hacer mayusculas todas las letras
        mayusculas=valor.upper()
        producto_creado.name=mayusculas
        return producto_creado

    @api.multi
    def write(self, vals):        
        ac=super(add_fields,self).write(vals) #el metodo write regresa un boolean que indica un true o un false si fue cambiado el campo
        valor=self.name
        # print(valor)
        vals['name']=valor.upper()
        # print(vals['name'])
        ac=super(add_fields, self).write(vals)
        return ac
