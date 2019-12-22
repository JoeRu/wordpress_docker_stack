#!/usr/bin/python
from string import Template
import logging
import argparse
import os

parser = argparse.ArgumentParser(description='Generator f. dockerized wordpress traefik container-set')
parser.add_argument('-i', '--input', default='domains.config.txt', type=str, help='configuration-file with a list of domains working with wordpress')
parser.add_argument('-o', '--output_dc', default='docker-compose.yml', type=str, help='output will overwrite "docker-compose.yml" in default - please take care of modifcations')
parser.add_argument('-oe', '--output_env', default='.env', type=str, help='output will overwrite ".env" in default - please take care of modifcations')

args = parser.parse_args()
INPUT = args.input
output_dc = args.output_dc
output_env = args.output_env

#-------------Output Logger
# create logger
logger = logging.getLogger(os.path.basename(__file__))
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)
#-------------Output Logger

class MyTemplate(Template):
    delimiter = "@"
    idpattern = "[a-z][a-z0-9]*"

logger.info('Reading template files')
fo = open(os.path.join("templates","docker-compose.template.yml"), "r")
dc_template = MyTemplate(fo.read())

#read templates
#environment variables
env_temp = open(os.path.join("templates","env.template.txt"), "r")
env_template = MyTemplate(env_temp.read())
env_temp.close()
#docker-compose generator
dockercompose_fix = open(os.path.join("templates","docker-compose.template.const.yml"))
dc_fix = dockercompose_fix.read()
dockercompose_fix.close()

#defining Volumes - bit of messy no template - but...
#volumes:
volumes_template = MyTemplate(
"""
  @DOMAIN_socket:
  @DOMAIN_wp:
  @DOMAIN_db:
""")

logger.info('Open outputfiles for writing')
#open for creation
env_file = open(output_env,"w")
dockercompose = open(output_dc, "w")

volumes = ""
environment = "TZ=Europe/Berlin"

#print(dc_template.substitute(d))
logger.info('write docker-compose-file {}:'.format(output_dc))
dockercompose.write(dc_fix)
logger.debug(dc_fix)


with open(INPUT) as f:
    content = f.readlines()
    content = [x.strip() for x in content] #strip whitespaces in each line
    logger.info('generating Domains: {}'.format(content))

for each in content:
    domain = dict(DOMAIN=each)

    dockercompose.write(dc_template.substitute(domain))
    logger.debug(dc_template.substitute(domain))

    environment = environment + env_template.substitute(domain)
    volumes = volumes + volumes_template.substitute(domain)


logger.debug('environment file')
logger.debug(environment)
logger.info('writing env-File: {}'.format(output_env))
env_file.write(environment)

dockercompose.write("""
volumes:
""")
dockercompose.write(volumes)

dockercompose.close()
env_file.close()
logger.warning('Please take care of .env-File Passwords!!!!')
