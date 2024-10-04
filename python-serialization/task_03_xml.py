#!/usr/bin/env python3
"""
    Python - Serialization - task3
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serialize the dictionary into XML and save to the file """
    root_node = ET.Element("data")
    for key, value in dictionary.items():
        child_node = ET.Element(key)
        child_node.text = value
        root_node.append(child_node)

    xml_data = ET.tostring(root_node)

    with open(filename, 'wb') as file:
        file.write(xml_data)


def deserialize_from_xml(filename):
    """
        Read the XML data from that file and
        return a deserialized Python dictionary
    """
    new_dict = {}

    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
        new_dict[child.tag] = child.text

    return new_dict
