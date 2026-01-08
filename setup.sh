#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=== Backend Setup ==="
cd backend/

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/Scripts/activate

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Navigating to Django project directory..."
cd sms_backend/

echo "Applying database migrations..."
python manage.py migrate

echo "Starting Django development server..."
python manage.py runserver &
DJANGO_PID=$!

cd ../../

echo "=== Frontend ==="
cd frontend/

echo "=== Frontend Setup ==="
cd frontend-sms/

echo "Installing frontend dependencies..."
npm install

echo "Starting frontend development server..."
npm run dev &
VITE_PID=$!

# Wait for background jobs
wait $DJANGO_PID $VITE_PID
