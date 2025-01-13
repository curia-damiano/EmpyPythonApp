#!/bin/bash

rm -rf .ruff_cache
rm -rf .venv
rm -rf node_modules
rm -rf src/__pycache__
rm -rf src/static/dist/*
rm -rf tests/__pycache__
echo \\e[32mCleaned all files successfully.\\e[0m
