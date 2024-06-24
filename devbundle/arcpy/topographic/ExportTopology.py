# Generated documentation for module arcpy.topographic


class ExportTopology(object):
    """
    Exports a topology from a geodatabase to an .xml file.
    """

    @property
    def description(self) -> str:
        return """

        ExportTopology_topographic(topology, location, file_name)

        Exports a topology from a geodatabase to an .xml file.

     INPUTS:
      topology (Topology / Topology Layer):
          An existing topology in a geodatabase. All feature classes that
          participate in this topology will be listed in the output .xml file.
      location (Folder):
          The folder in which the .xml file will be written.
      file_name (String):
          The name of the topology .xml file that will be created by the tool.

        """