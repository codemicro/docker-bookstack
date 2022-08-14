#!/bin/bash
set -e

echo "Starting Migration..."
php artisan migrate --force

echo "Clearing caches..."
php artisan cache:clear
php artisan view:clear

trap "echo Catching SIGWINCH apache error and perventing it." SIGWINCH
exec apache2-foreground
