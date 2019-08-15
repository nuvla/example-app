import os

#
# Add module to Nuvla server.
#
# The following environmental variables can/must be defined:
#
# NUVLA_ENDPOINT: endpoint of Nuvla server, defaults to localhost
# NUVLA_USERNAME: username to access Nuvla
# NUVLA_PASSWORD: password to access Nuvla
#

from nuvla.api import Api as nuvla_Api

nuvla_api = nuvla_Api(os.environ['NUVLA_ENDPOINT'], insecure=True)

nuvla_api.login_password(os.environ['NUVLA_USERNAME'], os.environ['NUVLA_PASSWORD'])

description = """An application composed of two services for demonstration and
learning purposes. The goal is to show how the application developer
can use environmental variables, secrets, configuration files, urls,
and output parameters. To make everything visible in this application
definition, no custom images have been used."""

def relative_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)

with open(relative_file('docker-compose.yml')) as x: docker_compose = x.read()

with open(relative_file('index.html')) as x: index_html = x.read()

with open(relative_file('my_config.txt')) as x: my_config_txt = x.read()

with open(relative_file('nuvla-app-demo.ipynb')) as x: nuvla_app_demo_ipynb = x.read()

application = {
    "author" : "sixsq",
    "urls" : [
        ["Nginx simple", "http://${hostname}:${nginx_simple.tcp.80}"],
        ["Jupyter advanced", "http://${hostname}:${jupyter_advanced.tcp.8888}"]
    ],
    "docker-compose" : docker_compose,
    "environmental-variables" : [
        {
            "name" : "MY_ENV",
            "required" : False,
            "value" : "my env value",
            "description" : "application defined environmental variable"
        }, {
            "name" : "GIVE_ME_SOME_INPUT",
            "required" : True,
            "description" : "Required environmental variable example"
        }
    ],
    "output-parameters" : [
        {
            "name" : "edit-me",
            "description" : "parameter to be set"
        }
    ],
    "files" : [
        {
            "file-name" : "jupyter_token.txt",
            "file-content" : "token-from-secret"
        }, {
            "file-name" : "index.html",
            "file-content" : index_html
        }, {
            "file-name" : "my_config.txt",
            "file-content" : my_config_txt
        }, {
            "file-name" : "nuvla-app-demo.ipynb",
            "file-content" : nuvla_app_demo_ipynb
        }
    ]
}

module = {"name": "My first application",
          "description": description,
          "logo-url": "/ui/images/noimage.png",
          "subtype": "application",
          
          "path": "examples/my-first-application",
          "parent-path": "examples",
          
          "data-accept-content-types": ["application/octet-stream"],
          "content": application}

module_response = nuvla_api.add('module', module)
module_id = module_response.data['resource-id']
print("module id: %s" % module_id)
