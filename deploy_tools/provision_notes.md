Provisioning a new site
=======================

## Required packages:
* nginx
* python 3.9
* virtualenv + pip
* Git

eg, on Ubuntu:
	
	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get install nginx git python3.9 python3.9-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace 47.111.5.43 with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace 47.111.5.43 with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|---sites
	|---47.111.5.43
		|---database
		|---source
		|---static
		|---virtualenv