# Website Menu Visibility

## Overview
The Website Menu Visibility module enhances Odoo's website menu functionality by allowing fine-grained control over menu item visibility based on user groups and types. This module is ideal for websites that require different navigation options for various user categories.

## Features
- Set visibility options for each menu item:
  - All Users
  - Portal Users
  - Public Users
  - Internal Users
- Assign specific user groups to menu items
- Hierarchical visibility: submenu visibility respects parent menu settings
- Seamless integration with Odoo's existing website menu structure

## Installation
1. Clone this repository into your Odoo addons directory.
2. Update your Odoo addons list.
3. Install the module through the Odoo Apps menu.

## Configuration
After installation, you can configure menu visibility:

1. Go to Website > Configuration > Menus
2. Edit a menu item
3. Set the 'Visibility' field to control who can see the menu
4. Optionally, assign specific user groups for more granular control

## Usage
Once configured, the module automatically handles menu visibility based on the current user's status and group memberships. No additional action is required by end-users.

## Compatibility
This module is compatible with Odoo 16.0.

## Support
For bugs or feature requests, please use the [issue tracker](https://github.com/yourusername/website_menu_visibility/issues) on GitHub.

## Contributors
- Lasse Larsson, Kubang AB

## License
This module is licensed under the LGPL-3 License.

## About Kubang AB
Kubang AB Value Added Distributor and Service Provider. Visit our website at https://www.kubang.eu for more information about our services.
