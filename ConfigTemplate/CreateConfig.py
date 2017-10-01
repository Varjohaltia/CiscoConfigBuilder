#!/usr/bin/env python

import yaml
from jinja2 import Environment, FileSystemLoader

vlanDict = {123: 'TEST-VLAN-123', 234: 'TEST-VLAN-234', 345: 'TEST-VLAN-345'}

# Create Jinja2 environment object and refer to templates directory
env = Environment(loader=FileSystemLoader('./Templates/'))

# Create Jinja2 template object based off of template named
template = env.get_template('test.j2')

# Render the template, and print it to console
print template.render(vlanDict=vlanDict)
