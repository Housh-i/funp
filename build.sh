#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python src/manage.py collectstatic --no-input --ignore css/main.css

# Apply any outstanding database migrations
python src/manage.py migrate

python src/manage.py createsuperuser --noinput || true