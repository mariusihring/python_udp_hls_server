#!/bin/bash

brew install ffmpeg
brew install anaconda
conda create --name server
conda activate server
conda install pip
pip install flask
pip install flask_cors
