import os
import xml.etree.ElementTree as ET

for filename in os.listdir('data/images/train/'):
	if filename.endswith('.xml'):
		tree = ET.parse('data/images/train/'+filename)
		root = tree.getroot()
		for elem in root:
			if elem.tag == "filename":
				elem.text = filename[:-4]+'.jpg'
			if elem.tag == "folder":
				elem.text = 'train'
			if elem.tag == "path":
				elem.text = os.path.abspath('data/images/train/'+filename[:-4]+'.jpg')
			if (elem.tag=="object" and "slide" in [child.text for child in elem]) or elem.tag != "object":
				pass
			else:
				root.remove(elem)
		tree.write("data/images/train/"+filename) 
