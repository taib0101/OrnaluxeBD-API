# spectaclur_defaults links: https://drf-spectacular.readthedocs.io/en/latest/settings.html
from typing import Dict, Any

SPECTACULAR_DEFAULTS: Dict[str, Any] = {
    'TITLE': 'OrnaluxeBD API',            # API title
    'DESCRIPTION': '',                    # Short description
    'VERSION': '1.0.0',                   # API version

    # OpenAPI version
    'OAS_VERSION': '3.0.3',

    # Schema generator class (usually you don't change this)
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',

    # Basic Swagger UI settings
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
    },

    # Optional: separate request/response schemas (good for client generators)
    'COMPONENT_SPLIT_PATCH': True,
    'COMPONENT_SPLIT_REQUEST': True,

    # Serve settings for swagger lock icon
    'SERVE_INCLUDE_SCHEMA': True,
    'SERVE_PUBLIC': False,
    'SERVE_PERMISSIONS': [],

    # Disables all auth in Swagger
    # "AUTHENTICATION_WHITELIST": [],
    
    # Register the Bearer scheme
    "SECURITY_SCHEMES": {
        "BearerAuth": {
            "name": "Authorization",
            "type": "http",
            "scheme": "bearer",
            "in": "header",
            "bearerFormat": "JWT"
        }
    }
}