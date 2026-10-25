import xml.etree.ElementTree as ET

def generate_kml_export(nodes: list, output_filename: str = "forensic_nodes.kml"):
    """
    Creates a Google Earth compatible KML file from a list of node locations.
    nodes format: [{'name': 'Node A', 'lat': 37.7749, 'lon': -122.4194, 'desc': 'EVM RPC Node'}]
    """
    kml = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, "Document")
    
    for node in nodes:
        placemark = ET.SubElement(document, "Placemark")
        name = ET.SubElement(placemark, "name")
        name.text = node.get("name", "Unknown Node")
        
        description = ET.SubElement(placemark, "description")
        description.text = node.get("desc", "")
        
        point = ET.SubElement(placemark, "Point")
        coordinates = ET.SubElement(point, "coordinates")
        coordinates.text = f"{node.get('lon')},{node.get('lat')},0"
        
    tree = ET.ElementTree(kml)
    tree.write(output_filename, encoding="utf-8", xml_declaration=True)
    print(f"Google Earth KML successfully exported to {output_filename}")

if __name__ == "__main__":
    sample_nodes = [
        {"name": "Primary RPC Node", "lat": 37.7749, "lon": -122.4194, "desc": "Ethereum Mainnet Archive Node"}
    ]
    generate_kml_export(sample_nodes)
  
