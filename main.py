#!/usr/bin/python3

import yaml
import jinja2


with open('api-example.yml', 'r') as f:
    config = yaml.safe_load(f.read())


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('.'),
    autoescape=jinja2.select_autoescape()
)
template = env.get_template('main.sh.j2')
print(template.render(config=config))
