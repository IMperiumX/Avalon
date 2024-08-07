import random
from typing import List

from .node import Node


class ReplicationManager:
    def __init__(self, replication_factor: int, available_nodes: List[Node]):
        self.replication_factor = replication_factor
        self.available_nodes = available_nodes

    def choose_replica_nodes(self) -> List[str]:
        """
        Selects 'm' (replication_factor) nodes from the available nodes for replication.
        """
        if len(self.available_nodes) < self.replication_factor:
            raise ValueError("Not enough available nodes for replication")

        # For simplicity, we use random selection here.
        # In a real system, you might use more sophisticated algorithms
        # considering factors like node load, network latency, etc.
        return random.sample(self.available_nodes, self.replication_factor)

    def replicate_file(self, file_path: str, data: bytes):
        """
        Replicates the file data to the chosen replica nodes.
        """
        replica_nodes = self.choose_replica_nodes()
        for node in replica_nodes:
            # In a real system, you would use a network protocol
            # to transfer the data to each node.
            print(f"Replicating file '{file_path}' to node '{node}'")
            # TODO: (Implementation for data transfer to the node) ...


# Example usage
replication_manager = ReplicationManager(
    replication_factor=3, available_nodes=["node1", "node2", "node3", "node4"]
)
replication_manager.replicate_file("my_file.txt", b"This is the file data")
