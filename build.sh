#!/bin/bash

source backend/venv/Scripts/activate


cd backend/sms_backend
python manage.py runserver &

cd ../../

npm --prefix Frontend/frontend-sms run dev