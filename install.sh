#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
  exit 1
fi

apt update
apt-get install git python3 python3-pip python3-tk -y
pip3 install tk
export DISPLAY=:0.0
git clone https://github.com/stingsek/hangman_game.git
cd hangman_game
rm install.sh
rm README.md
git remote remove origin
rm -r .git
pip3 install -r requirements.txt
pyinstaller ./app.py --onefile --noconsole