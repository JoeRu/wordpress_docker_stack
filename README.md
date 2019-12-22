# wordpress_docker_stack

This *project* will generate a docker-compose file for a bunch of domains .... 

it uses traefik as reverseproxy and to take care of letsencrypt certfificates

* One MariaDB database configured for Galera-based clustering using swarm mode DNS for discovery
* One Traefik proxying/load balancing container 

# Usage

These services can be started using the following command:
    
```
docker stack deploy --compose-file docker-compose.yml traefiked-wordpress
```

This will bring up 2 wordpress containers, a single dbcluster
container, and a traefik container.

# References
This project uses the following Docker images:
* PHP 7.1/Apache version of the [Official Docker Wordpress image](https://hub.docker.com/_/wordpress/)
* ToughIQ's [MariaDB Galera Cluster image](https://hub.docker.com/r/toughiq/mariadb-cluster/)
* The [Traefik](https://hub.docker.com/_/traefik/) load balancer
