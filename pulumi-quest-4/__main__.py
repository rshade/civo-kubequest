"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.yaml import ConfigGroup
from pulumi_kubernetes.yaml import ConfigFile
from pulumi import export

civo_quest_4_deployment = ConfigFile("quest4_deployment", "../quest-4/deployment.yaml")
deployment = civo_quest_4_deployment.get_resource("apps/v1/Deployment", "hello-world")
civo_quest4_service = ConfigFile("quest4_service", "../quest-4/service.yaml")
frontend = civo_quest4_service.get_resource("v1/Service", "hello-world")
civo_quest_4_ingrest = ConfigFile("quest4_ingress", "../quest-4/ingress.yaml")
export(
  name="privateIp",
  value=frontend.spec.cluster_ip)

export("name", deployment.metadata["name"])
