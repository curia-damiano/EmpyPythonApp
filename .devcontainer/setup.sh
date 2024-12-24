# setup.sh
#!/bin/bash

npm install
npm run build:debug
echo \\e[32mNode stuff installed.\\e[0m

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -r requirements.txt
echo \\e[32mPython stuff installed.\\e[0m

echo \\e[32mInstallation of dev containers completed successfully.\\e[0m
