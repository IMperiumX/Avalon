class ConsistentHash:
    def __init__(self, num_servers, total_slots, num_virtual_servers):
        self.num_servers = num_servers
        self.total_slots = total_slots
        self.num_virtual_servers = num_virtual_servers
        self.servers = {}

    # print : index and server_id
    def print_servers(self):
        for i in range(self.total_slots):
            if i in self.servers:
                print(f"Index: {i} Server: {self.servers[i]}")

    def hash_function_request(self, request_id):
        return (request_id**2 + 2 * request_id + 17) % self.total_slots

    def hash_function_server(self, server_id, virtual_server_id):
        return (
            server_id**2 + virtual_server_id**2 + 2 * virtual_server_id + 25
        ) % self.total_slots

    def add_server(self, server_id):
        for j in range(self.num_virtual_servers):
            virtual_server_id = f"{server_id}-{j}"
            slot = self.hash_function_server(server_id, j)

            # Apply linear probing if the slot is already occupied
            while slot in self.servers.keys():
                slot = (slot + 1) % self.total_slots  # Linear probing
                # Alternatively, you can use quadratic probing
                # slot = (slot + (j**2)) % self.total_slots  # Quadratic probing

            self.servers[slot] = server_id

    def remove_server(self, server_id):

        # server_id does not exist in self.servers
        if server_id not in self.servers.values():
            print(f"Server {server_id} does not exist")
            return

        for j in range(self.num_virtual_servers):
            virtual_server_id = f"{server_id}-{j}"
            slot = self.hash_function_server(server_id, j)

            # Remove the server from the hash map
            while True:
                if slot in self.servers.keys() and self.servers[slot] == server_id:
                    del self.servers[slot]
                    break
                slot = (slot + 1) % self.total_slots  # Move to the next slot

    def get_server_for_request(self, request_id):

        # no servers exist
        if len(self.servers) == 0:
            print("No servers exist")
            return None

        slot = self.hash_function_request(request_id)
        sorted_slots = sorted(self.servers.keys())

        # Finding the first slot greater than or equal to the request's slot
        for s in sorted_slots:
            if s >= slot:
                return self.servers[s]

        # If no slot is found greater than or equal to the request's slot, return the first slot in the sorted list
        return self.servers[sorted_slots[0]]


if __name__ == "__main__":

    # Example usage:
    num_servers = 3
    total_slots = 512
    num_virtual_servers = 9  # int(math.log2(total_slots))

    consistent_hashing = ConsistentHash(num_servers, total_slots, num_virtual_servers)

    # Add servers to the consistent hash map
    for i in range(num_servers):
        consistent_hashing.add_server(i)
    consistent_hashing.print_servers()
    # Get server for a specific request
    for request_id in range(10):
        request_hash = consistent_hashing.hash_function_request(request_id)
        print(request_hash)
        selected_server = consistent_hashing.get_server_for_request(request_id)
    consistent_hashing.remove_server(0)
    consistent_hashing.remove_server(1)
    consistent_hashing.remove_server(2)
    consistent_hashing.print_servers()

    for request_id in range(10):
        request_hash = consistent_hashing.hash_function_request(request_id)
        print(request_hash)
        selected_server = consistent_hashing.get_server_for_request(request_id)
        print(f"Selected Server: {selected_server}")
