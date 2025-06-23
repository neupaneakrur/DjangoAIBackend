#!/usr/bin/env python
"""
PostgreSQL Setup Script for Technology Channel AI
This script helps you configure PostgreSQL database settings.
"""

import os
import sys

def setup_postgres():
    print("🚀 PostgreSQL Setup for Technology Channel AI")
    print("=" * 50)
    
    print("\n📋 Prerequisites:")
    print("1. PostgreSQL must be installed on your system")
    print("2. PostgreSQL service must be running")
    print("3. You need to know your PostgreSQL password")
    
    print("\n🔧 Configuration Steps:")
    print("1. Create a database named 'technologychannelai_db'")
    print("2. Update the database settings in settings.py")
    
    print("\n📝 Manual Database Creation:")
    print("Run these commands in your PostgreSQL client (psql):")
    print("CREATE DATABASE technologychannelai_db;")
    print("CREATE USER technologychannelai_user WITH PASSWORD 'your_secure_password';")
    print("GRANT ALL PRIVILEGES ON DATABASE technologychannelai_db TO technologychannelai_user;")
    
    print("\n⚙️  Alternative: Update settings.py with your existing PostgreSQL credentials")
    print("Edit the DATABASES section in technologychannelai/settings.py:")
    print("- Change 'USER' to your PostgreSQL username")
    print("- Change 'PASSWORD' to your PostgreSQL password")
    print("- Change 'NAME' to your database name if different")
    
    print("\n🔍 To check if PostgreSQL is running:")
    print("Windows: Check Services app for 'postgresql-x64-15' (or similar)")
    print("Linux/Mac: sudo systemctl status postgresql")
    
    print("\n📊 After setup, run these Django commands:")
    print("python manage.py migrate")
    print("python manage.py createsuperuser")
    print("python manage.py runserver")

if __name__ == "__main__":
    setup_postgres() 