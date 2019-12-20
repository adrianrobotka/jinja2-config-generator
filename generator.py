#!/usr/bin/env python3
import os
import jinja2
import yaml

if __name__ == "__main__":
    config_data = yaml.safe_load(open('data.yaml'))
    print(config_data)

    #jinja2.Environment.keep_trailing_newline = True
    #jinja2.Environment.trim_blocks = False
    #jinja2.Environment.lstrip_blocks = False
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
    templateEnv = jinja2.Environment(loader=templateLoader)

    for filename in os.listdir('templates'):
        output = templateEnv.get_template(filename).render(config_data)

        f = open("out/" + filename, "w+")
        f.write(output)
        f.close()

    print("OK")
