# Generated documentation for module arcpy.nd


class ExportDiagramTemplateDefinitions(object):
    """
    Exports the network diagram rule and layout definitions and the network diagram layer definition to .ndbd and .ndld files, respectively.
    """

    @property
    def description(self) -> str:
        return """

        ExportDiagramTemplateDefinitions_nd(in_utility_network, template_name, {out_ndbd_file}, {out_ndld_file})

        Exports the network diagram rule and layout definitions and the
        network diagram layer definition to .ndbd and .ndld files,
        respectively.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network referencing the diagram template
          definitions to export.
      template_name (String):
          The name of the diagram template with definitions to be exported.

     OUTPUTS:
      out_ndbd_file {File}:
          The network diagram rule and layout definitions file (.ndbd) to be
          created.
      out_ndld_file {File}:
          The network diagram layer definition file (.ndld) to be created.

        """