# Generated documentation for module arcpy.nd


class OverwriteDiagram(object):
    """
    Overwrites the contents of a network diagram with the network elements currently selected in the specified map. These network elements become the new initial content of the diagram.
    """

    @property
    def description(self) -> str:
        return """

        OverwriteDiagram_nd(in_network_diagram_layer, map)

        Overwrites the contents of a network diagram with the network elements
        currently selected in the specified map. These network elements become
        the new initial content of the diagram.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram that will be overwritten.
      map (Map):
          The map referencing the set of selected network elements that will be
          used to overwrite the input network diagram.

        """