#!/bin/bash

npm --prefix frontend/frontend-sms run build

git add .

git add frontend/frontend-sms/dist -f

MYVAR=$(date +"%Y-%d-%m %I:%M%p")

git commit -m "$MYVAR"

git subtree push --prefix frontend/frontend-sms/dist origin gh-pagess