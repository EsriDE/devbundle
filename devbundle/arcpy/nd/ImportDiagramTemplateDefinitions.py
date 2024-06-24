# Generated documentation for module arcpy.nd


class ImportDiagramTemplateDefinitions(object):
    """
    Imports a network diagram rule and layout definitions file (.ndbd), a network diagram layer definition file (.ndld), or both into an existing template.
    """

    @property
    def description(self) -> str:
        return """

        ImportDiagramTemplateDefinitions_nd(in_utility_network, template_name, {ndbd_file}, {ndld_file})

        Imports a network diagram rule and layout definitions file (.ndbd), a
        network diagram layer definition file (.ndld), or both into an
        existing template.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template onto which the definitions will be
          imported.
      ndbd_file {File}:
          The network diagram rule and layout definitions file (.ndbd) that will
          be imported.This file is the result of using the Export Diagram
          Template
          Definitions tool on an existing template.At least one of the two input
          file parameters must be completed; that
          is, either the network diagram rule and layout definitions file
          (.ndbd) or the network diagram layer definition file (.ndld) must be
          completed.
      ndld_file {File}:
          The network diagram layer definition file (.ndld) that will be
          imported.This file is the result of using the Export Diagram Template
          Definitions or Export Diagram Layer Definition tool on an existing
          template.At least one of the two input file parameters must be
          completed; that
          is, either the network diagram rule and layout definitions file
          (.ndbd) or the network diagram layer definition file (.ndld) must be
          completed.When a diagram layer definition does not exist for the input
          diagram
          template and this parameter is not specified or loads an empty .ndld
          file, a default diagram layer definition is systematically initialized
          on the template.

        """