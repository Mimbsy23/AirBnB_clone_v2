#!/usr/bin/python3

from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBstorage
    storage = DBstorage()
else:
    """This module instantiates an object of class FileStorage"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
