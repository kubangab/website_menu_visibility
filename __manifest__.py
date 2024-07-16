{
    'name': 'Website Menu Visibility',
    'version': '17.0.1.0.0',
    'author': 'Kubang AB, Lasse Larsson',
    'summary': 'Enhances website menu visibility based on user group',
    'license': 'LGPL-3',
    'sequence': 10,
    'description': """
With this module it is possible to make menus hidden or visible
Depending on what kind of user that are on the website.
There are four kinds of users to be selected, all user (default)
Guest users (non logged in), Portal Users (Logged in users) and
Internal Users (Backend users). Priority is as follows High to low.
Internal Users, Portal Users, Guest Users and All Users. If a top
menu has a higher settings (Internal User) all submenus are hidden
for any other type of users.
    """,
    'category': 'Website',
    'website': 'https://www.kubang.eu',
    'depends': ['base', 'website', 'portal'],
    'data': [
        'security/ir.model.access.xml',
        'views/website_menu.xml',
    ],
   'installable': True,
    'application': True,
    'auto_install': False,
}