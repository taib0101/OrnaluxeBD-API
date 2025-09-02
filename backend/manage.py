"""
    Author: Mustain Mustain Taib
    Designation: Software Engineer
"""


import os
import sys
import uvicorn
from django.core.management import execute_from_command_line

def main() -> None:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    execute_from_command_line(sys.argv)

def run_uvicorn() -> None:
    uvicorn.run(
        "backend.asgi:application", 
        host="127.0.0.1", 
        port=8000, 
        reload=True, 
        log_level="info"
    )


if __name__ == '__main__':
    if "runuvicorn" in sys.argv:
        run_uvicorn()
    else:
        main()