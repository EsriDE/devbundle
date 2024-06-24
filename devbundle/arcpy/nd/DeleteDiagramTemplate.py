# Generated documentation for module arcpy.nd


class DeleteDiagramTemplate(object):
    """
    Deletes a diagram template and all diagrams based on that template.
    """

    @property
    def description(self) -> str:
        return """

        DeleteDiagramTemplate_nd(in_utility_network, template_name)

        Deletes a diagram template and all diagrams  based on that template.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network related to the diagram template
          to delete.
      template_name (String):
          The name of the diagram template to delete.

        """