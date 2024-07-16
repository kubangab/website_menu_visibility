from odoo import models, fields, api, _

class Menu(models.Model):
    _inherit = "website.menu"

    group_ids = fields.Many2many('res.groups', string=_('User Groups'))
    visibility = fields.Selection([
        ('all', _('All Users')),
        ('portal', _('Portal Users')),
        ('public', _('Public Users')),
        ('internal', _('Internal Users'))
    ], string="Visibility", default='all', help=_("Specify which type of users can see this menu."))

    # Update the is_visible field to include recursive=True
    is_visible = fields.Boolean(compute='_compute_visible', recursive=True)

    @api.depends('group_ids', 'visibility', 'parent_id.is_visible')
    def _compute_visible(self):
        for menu in self:
            visible = True
            current_user = self.env.user

            if current_user.has_group('base.group_user'):
                visible = True
            # Visibility based on user type
            elif menu.visibility == 'portal' and not current_user.has_group('base.group_portal'):
                visible = False
            elif menu.visibility == 'public' and not current_user.has_group('base.group_public'):
                visible = False
            elif menu.visibility == 'internal' and not current_user.has_group('base.group_user'):
                visible = False

            if menu.parent_id and not menu.parent_id.is_visible:
                visible = False

            # Visibility based on group membership
            if visible and menu.group_ids:
                visible = current_user.groups_id & menu.group_ids

            menu.is_visible = visible