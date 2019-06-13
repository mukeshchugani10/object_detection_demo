# Selects images from test/ which have atleast one eq in them and places them in data/images/test
# Ensure that data/images/test is empty

import os
import xml.etree.ElementTree as ET

for filename in os.listdir('test/'):
	if filename.endswith('.xml'):
		tree = ET.parse('test/'+filename)
		root = tree.getroot()
		for elem in root:
			if (elem.tag=="object" and "eq" in [child.text for child in elem]) or elem.tag != "object":
				pass
			else:
				root.remove(elem)
		tree.write('data/images/test/'+filename)
		os.rename('test/'+filename[:-3]+'jpg','data/images/test/'+filename[:-3]+'jpg')