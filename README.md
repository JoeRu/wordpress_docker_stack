# wordpress_docker_stack

This *project* will generate a docker-compose file for a bunch of domains ....

it uses traefik as reverseproxy and to take care of letsencrypt certfificates.

There is pretty much only one variable in the templates which is ```@domain```. The '@' Symbol replaces the regular '$'-Symbol from yml in the templates to not mix up things.

Domains are configured in domains.config.txt - where each line is a domain; per default traefik is covering 'www.'. If there is a need to adapt Traefik Host variable the file "templates/docker-dockercompose.template.yml" can be adapted.

For more easy migration every wordpress and wordpress-db is covered in its own volume. Docker-volumes can be found according to docker-documentation. (in Linux mostly '/var/lib/docker/volumes/')

**Be aware any existing docker-compose.yml files will be overwritten without further warning!**
** Please take care of the .env file - as it containes Database-Passwords**

* One MariaDB database configured
* One Traefik proxying/load balancing container

# Usage

```
python .\generate_docker_compose.py

usage: generate_docker_compose.py [-h] [-i INPUT] [-o OUTPUT_DC] [-oe OUTPUT_ENV]

Generator f. dockerized wordpress traefik container-set

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        configuration-file with a list of domains working with wordpress
  -o OUTPUT_DC, --output_dc OUTPUT_DC
                        output will overwrite "docker-compose.yml" in default - please take care of modifcations
  -oe OUTPUT_ENV, --output_env OUTPUT_ENV
                        output will overwrite ".env" in default - please take care of modifcations
```
**Please take care to change Password in '.env' file after regeneration***
# References
This project uses the following Docker images:
* The [Official Docker Wordpress image](https://hub.docker.com/_/wordpress/)
* MariaDB
* The [Traefik](https://hub.docker.com/_/traefik/) load balancer
