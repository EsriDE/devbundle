# Generated documentation for module arcpy.nd


class AddDiagramTemplate(object):
    """
    Adds a new diagram template to a network. A network diagram rule and layout definitions file (.ndbd) and a network diagram layer definition file (.ndld) can be imported.
    """

    @property
    def description(self) -> str:
        return """

        AddDiagramTemplate_nd(in_utility_network, template_name, {ndbd_file}, {ndld_file})

        Adds a new diagram template to a network. A network diagram rule and
        layout definitions file (.ndbd) and a network diagram layer definition
        file (.ndld) can be imported.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network to which the template will be
          added.
      template_name (String):
          The name of the output diagram template.
      ndbd_file {File}:
          The network diagram rule and layout definitions file (.ndbd) that will
          be imported. This file can be created using the Export Diagram
          Template Definitions tool on an existing template.
      ndld_file {File}:
          The diagram layer definition file (.ndld) that will be imported. This
          file can be created using the Export Diagram Template Definitions or
          Export Diagram Layer Definition tool on an existing template.When this
          parameter is not specified or loads an empty .ndld file, a
          default diagram layer definition is systematically initialized on the
          input diagram template.

        """