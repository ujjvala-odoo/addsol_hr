# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
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

from openerp.osv import fields, osv
from openerp.tools import config

class documnet_ftp_setting(osv.osv_memory):
    _name = 'knowledge.config.settings'
    _inherit = 'knowledge.config.settings'
    _columns = {
        'document_ftp_url': fields.char('Browse Documents', size=128,
            help ="""Click the url to browse the documents""", readonly=True),
        'document_ftp_user': fields.char('FTP Username', required=True),
        'document_ftp_passwd': fields.char('FTP Password', required=True),
    }

    def get_default_ftp_config(self, cr, uid, fields, context=None):
        user = self.pool.get('res.users').browse(cr, uid, uid, context)
        action = self.pool.get('ir.model.data').get_object(cr, uid, 'document_ftp', 'action_document_browse')
        return {
                'document_ftp_url': action.url,
                'document_ftp_user': user.company_id.document_ftp_user,
                'document_ftp_passwd': user.company_id.document_ftp_passwd
        }
    
    def set_default_ftp_config(self, cr, uid, ids, context=None):
        configdata = self.browse(cr, uid, ids[0], context)
        user = self.pool.get('res.users').browse(cr, uid, uid, context)
        user.company_id.write({
            'document_ftp_url': configdata.document_ftp_url,
            'document_ftp_user': configdata.document_ftp_user,
            'document_ftp_passwd': configdata.document_ftp_passwd
        })

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
