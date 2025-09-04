"""
    Author: Mustain Mustain Taib
    Designation: Software Engineer
"""

import os
import sys
import uvicorn
from django.core.management import execute_from_command_line
from django.conf import settings

def run_uvicorn():
    uvicorn.run(
        "backend.asgi:application", 
        host=settings.HOST, 
        port=settings.BIND_PORT, 
        reload=True, 
        log_level="info"
    )

def main():
    sys_argv_list = sys.argv.copy()

    if "runuvicorn" in sys.argv:
        sys.argv.remove("runuvicorn")

    if "production" in sys.argv:
        settings_module = "backend.settings.production"
        sys.argv.remove("production")
    else:
        settings_module = "backend.settings.development"
        sys.argv.remove("development")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    execute_from_command_line(sys.argv)

    if "runuvicorn" in sys_argv_list:
        run_uvicorn()


if __name__ == '__main__':
    main()