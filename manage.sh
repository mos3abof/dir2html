#!/bin/bash

print_usage() {
    echo "Usage: ./manage [option]      (Allowed options: dist, upload)"
}

INPUT=$1

if [ -z ${INPUT} ]; then
    print_usage
    exit 1
fi

if [ ${INPUT} == "dist" ]; then
    ./venv/bin/python3 setup.py sdist && ./venv/bin/python3 setup.py install
elif [ ${INPUT} == "run" ]; then
     ./venv/bin/python3 -m dir2html "${@:2}"
elif [ ${INPUT} == "upload" ]; then
    ./venv/bin/twine upload dist/*
else
    usage
    exit 1
fi

