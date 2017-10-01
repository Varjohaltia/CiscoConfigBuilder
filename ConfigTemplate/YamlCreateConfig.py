#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import yaml
from jinja2 import Environment, FileSystemLoader, Template

vlanDict = {123: 'TEST-VLAN-123', 234: 'TEST-VLAN-234', 345: 'TEST-VLAN-345'}

# Create Jinja2 environment object and refer to templates directory
env = Environment(loader=FileSystemLoader('./Templates/'))

# Load the config variables from a yaml file into a Python dictionary
with open("config-variables.yaml") as confvars:
    confvars =  yaml.load(confvars)

# Create Jinja2 template object based off of template named
template = env.get_template('config-template.j2')

# Render the template, and print it to console
print template.render(confvars=confvars)
