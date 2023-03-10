"""
This type stub file was generated by pyright.
"""

"""Utils

This module defines the framework-agnostic logic for handling the multipart
request spec
"""

def place_files_in_operations(
    operations, files_map, files
):  # -> list[Unknown] | dict[Unknown, Unknown]:
    """Replaces None placeholders in operations with file objects in the files
    dictionary, by following the files_map logic as specified within the 'map'
    request parameter in the multipart request spec"""
    ...

def add_file_to_operations(
    operations, file_obj, path
):  # -> list[Unknown] | dict[Unknown, Unknown]:
    """Handles the recursive algorithm for adding a file to the operations
    object"""
    ...

def new_merged_dict(*dicts):  # -> dict[Unknown, Unknown]:
    """Merges dictionaries into a new dictionary. Necessary for python2 and
    python34 since neither have PEP448 implemented."""
    ...

def new_list_with_replaced_item(input_list, index, new_value):
    """Creates new list with replaced item at specified index"""
    ...