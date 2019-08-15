# Example Application

An example application that consists of two components: an nginx web
server and a Jupyter notebook.

## How to register this application in a Nuvla installation

To register this container on your Nuvla on-premise installation,
clone the sources from the
[nuvla/example-app](https://github.com/nuvla/example-app) GitHub.

Define the following environmental variables:

 - `NUVLA_ENDPOINT`: The endpoint of the Nuvla server,
   e.g. `https://nuvla.io`. 

 - `NUVLA_USERNAME`: The username of the account to use.

 - `NUVLA_PASSWORD`: The password of the account to use.
 
Then run the following commands:

```sh
pip install nuvla-api
python add-module.py
```

You should now see the module component in the App Store called *My
first application*.
