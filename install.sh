#!/bin/bash
sudo apt-get update && sudo apt-get -y install libgl1
sudo apt-get -y install libglib2.0-0
curl -sSL https://install.python-poetry.org | python3 -
echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc
export PATH=$PATH:$HOME/.local/bin
echo "output of poetry --version = (poetry --version)"
poetry install