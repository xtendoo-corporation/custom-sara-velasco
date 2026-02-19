{
    "name": "Sara Velasco Custom Invoice",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "summary": "Customization of invoice external layout bubble",
    "description": """
        Este módulo hereda y personaliza la vista web.external_layout_bubble
        para facturas personalizadas de Sara Velasco.
    """,
    "author": "Sara Velasco",
    "website": "",
    "license": "LGPL-3",
    "depends": ["web", "account"],
    "data": [
        'views/invoice_form_view.xml',
        "views/external_layout_bubble.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
