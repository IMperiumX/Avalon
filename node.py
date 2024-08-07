import hashlib


class Node:
    """
    basic file storage on a single node.
    """

    def __init__(self, name):
        self.name = name
        self.files = {}

    def add_file(self, file_name, file_contents):
        self.files[file_name] = file_contents

    def get_file(self, file_name):
        return self.files.get(file_name)

    def remove_file(self, file_name):
        del self.files[file_name]

    def list_files(self):
        return list(self.files.keys())
