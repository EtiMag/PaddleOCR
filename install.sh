#!bin/sh
# note: needs admin privilege
apt-get update && apt-get install libgl1
apt-get install libglib2.0-0
curl -sSL https://install.python-poetry.org | python3 -
export PATH=$PATH:~/.local/share/pypoetry/venv/bin
poetry --version
poetry install
# exemple: poetry run paddleocr --image_dir test-files/ticket-de-caisse-5.png --use_gpu false --lang en