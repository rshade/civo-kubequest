import pulumi
import pulumi_civo as civo
from pulumi import export

# Create a network
kubeQuestNetwork = civo.Network("kubeQuestNetwork", label="kubeQuest-Network")
kubeQuestFirewall = civo.Firewall("kubeQuestFirewall", network_id=kubeQuestNetwork.id, create_default_rules=True)

kubeQuestCluster = civo.KubernetesCluster('civo-k3s-cluster', name='kubequestCluster',
                                        num_target_nodes=3, target_nodes_size='g3.k3s.medium', 
                                        network_id=kubeQuestNetwork.id, firewall_id=kubeQuestFirewall.id)

export('cluster_id', kubeQuestCluster.id)
export('cluster_name', kubeQuestCluster.name)
export('cluster_api_endpoint', kubeQuestCluster.api_endpoint)
export('cluster_dns_entry', kubeQuestCluster.dns_entry)
export('cluster_kubeconfig', kubeQuestCluster.kubeconfig)