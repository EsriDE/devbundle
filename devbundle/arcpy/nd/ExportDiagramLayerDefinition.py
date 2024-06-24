# Generated documentation for module arcpy.nd


class ExportDiagramLayerDefinition(object):
    """
    Exports the diagram layer definition currently set up for the input diagram layer into a network diagram layer definition file (.ndld).
    """

    @property
    def description(self) -> str:
        return """

        ExportDiagramLayerDefinition_nd(in_network_diagram_layer, out_ndld_file)

        Exports the diagram layer definition currently set up for the input
        diagram layer into a network diagram layer definition file (.ndld).

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram layer from which the layer definition will be
          exported.

     OUTPUTS:
      out_ndld_file (File):
          The network diagram layer definition file (.ndld) to be created.

        """