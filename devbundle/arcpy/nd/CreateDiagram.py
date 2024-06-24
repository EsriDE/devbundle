# Generated documentation for module arcpy.nd


class CreateDiagram(object):
    """
    Creates a temporary network diagram from network elements currently selected in the active map or from layers created from a Python script.
    """

    @property
    def description(self) -> str:
        return """

        CreateDiagram_nd(in_utility_network, template_name, {features;features...})

        Creates a temporary network diagram from network elements currently
        selected in the active map or from layers created from a Python
        script.

     INPUTS:
      in_utility_network (Utility Network / Trace Network / Utility Network Layer / Trace Network Layer):
          The utility network or trace network from which the diagram will be
          created.
      template_name (String):
          The name of the template that will be used to create the diagram.
      features {Feature Layer}:
          One or more feature layers that will be used as input for diagram
          generation.

        """