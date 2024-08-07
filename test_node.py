from .node import Node


def test_node():
    # Create a new node
    node = Node("Node1")

    # Add files to the node
    node.add_file("file1.txt", "This is file 1")
    node.add_file("file2.txt", "This is file 2")

    # Check if files are added correctly
    assert node.list_files() == ["file1.txt", "file2.txt"]

    # Get the contents of a file
    assert node.get_file("file1.txt") == "This is file 1"

    # Remove a file
    node.remove_file("file1.txt")

    # Check if the file is removed
    assert node.list_files() == ["file2.txt"]

    # Try to get a removed file
    assert node.get_file("file1.txt") is None

    # Add a new file
    node.add_file("file3.txt", "This is file 3")

    # Check if the new file is added
    assert node.list_files() == ["file2.txt", "file3.txt"]

    print("All tests passed!")


# Run the test
test_node()
