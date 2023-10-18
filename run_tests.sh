#!/bin/sh

num_tests=5

green_color="\033[32m"
red_color="\033[31m"
reset_color="\033[0m"

for ((i = 1; i <= num_tests; i++)); do
    python manage.py test || {
        echo -e "${red_color}Error: test failed${reset_color}"
        exit 1
    }
done

echo -e "${green_color}All tests passed${reset_color}"
