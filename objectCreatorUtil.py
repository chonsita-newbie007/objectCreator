import maya.cmds as cmds

def createObject(self,name):
	sel = self.object_listWidget.currentItem()
	if not sel:
		cmds.warning('Please select primitive first.')
		return

	obj = sel.text()

	if obj == 'sphere':
		cmds.polySphere(name='{name}_GEO'.format(name=name))
	elif obj == 'cube':
		cmds.polyCube(name='{name}_GEO'.format(name=name))

	elif obj == 'cone':
		cmds.polyCone(name='{name}_GEO'.format(name=name))

	elif obj == 'torus':
		cmds.polyTorus(name='{name}_GEO'.format(name=name))
	else:
		cmds.warning(f'Unknown objitive: {obj}')