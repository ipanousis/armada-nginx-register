#!/usr/bin/python

import json, os, shutil
import logging
import re

CLUSTER_DOMAIN=os.environ['CLUSTER_DOMAIN']

containers = json.loads(open('/tmp/containers.json','r').read())['containers']

# delete all existing nginx https redirects
shutil.rmtree('/etc/nginx/https-redirects/*')

# create https redirect file
def write_redirect_rule(subdomain, external_port):
  redirect_template = """
if ($host ~ ^%s.*$) {
  rewrite ^ https://%s:%s$request_uri permanent;
}
"""
  open('/etc/nginx/https-redirects/%s.conf' % subdomain).write(redirect_template % (subdomain, CLUSTER_DOMAIN, external_port))
 
for container in containers:
  for port in container['ports']:
    if int(port['internal']) == 443:
      service_name = container['name'].replace('flocker--','')
      write_redirect_rule(service_name, port['external'])

