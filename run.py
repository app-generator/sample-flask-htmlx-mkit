# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app import app, db

# Disable debug in production
if __name__ == "__main__":
    app.run(debug=True)

