##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## toto
##
run:
	     python3 main.py

install:
	     pip3 install -r requirements.txt && ./install.sh

test:
	     python3 test.py

prod:
	     gunicorn main:app -c gunicorn.conf.py

stop:
	     sudo kill -9 `sudo lsof -t -i:$(port)`
