#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.book import Book
from models.author import Author



Book.create_table()
Author.create_table()
ipdb.set_trace()
