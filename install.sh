#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
  exit 1
fi

apt update
apt-get install git python3 python3-pip -y
git clone https://github.com/stingsek/hangman_game.git
cd hangman_game
rm install.sh
rm README.md
git remote remove origin
rm -r .git
pip3 install -r requirements.txt
python3 ./app.py

