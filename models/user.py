#!/usr/bin/python3
"""
module: user.py
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User"""
    __email = ""
    password = ""
    first_name = ""
    last_name = ""
