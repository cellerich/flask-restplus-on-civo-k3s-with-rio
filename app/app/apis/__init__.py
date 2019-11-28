from flask import Flask, Blueprint
from flask_restplus import Api


from .ns_systeminfo import api as nsSystemInfo


api = Api(
    title="The famous system Info API",
    version="1.0",
    description="A test API to find out how to make FLASK RESTPLUS API's and deploy them to a Kubernetes Cluster with Rancher RIO",
    contact="cello@cello.ch",
    # All API metadatas
)

api.add_namespace(nsSystemInfo, path="/system")
