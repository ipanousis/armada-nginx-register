#!/usr/bin/python

import json, os, shutil
import logging
import re

CLUSTER_NAME=os.environ['FLOCKER_DOMAIN']

containers = json.loads(open('/tmp/containers.json','r').read())['containers']

# delete all existing nginx https redirects
shutil.rmtree('/etc/nginx/https-redirects/*')

# create https redirect file
def write_redirect_rule(subdomain, external_port):
  redirect_template = """
if ($host ~ ^%s.*$) {
  rewrite ^ https://flocker-1.ciscocloudsecurity.com:%s$request_uri permanent;
}
"""
  open('/etc/nginx/https-redirects/%s.conf' % subdomain).write(redirect_template % (subdomain, external_port))
 
for container in containers:
  for port in container['ports']:
    if int(port['internal']) == 443:
      service_name = container['name'].replace('flocker--','')
      write_redirect_rule(service_name, port['external'])

