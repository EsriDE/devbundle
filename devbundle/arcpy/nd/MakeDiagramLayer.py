# Generated documentation for module arcpy.nd


class MakeDiagramLayer(object):
    """
    Creates a network diagram layer from a network diagram.
    """

    @property
    def description(self) -> str:
        return """

        MakeDiagramLayer_nd(in_utility_network, network_diagram_name, out_layer)

        Creates a network diagram layer from a network diagram.

     INPUTS:
      in_utility_network (Utility Network / Trace Network / Utility Network Layer / Trace Network Layer):
          The utility network or trace network the diagram is related to.
      network_diagram_name (String):
          The network diagram name.

     OUTPUTS:
      out_layer (Diagram Layer):
          The name of the diagram layer that will be created.The output diagram
          layer can be used as input to geoprocessing tools
          that accept a diagram layer as input, including the Store Diagram,
          Update Diagram, and Apply Smart Tree Layout tools.

        """