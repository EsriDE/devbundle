# Generated documentation for module arcpy.nd


class DeleteDiagram(object):
    """
    Deletes one or more stored network diagrams, which are optionally filtered by their diagram template names, related to a given network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteDiagram_nd(in_diagrams, {template_names;template_names...}, {diagram_names;diagram_names...})

        Deletes one or more stored network diagrams, which are optionally
        filtered by their diagram template names, related to a given network.

     INPUTS:
      in_diagrams (Utility Network / Trace Network / Utility Network Layer / Trace Network Layer / Diagram Layer):
          The input network diagram layer to delete, or the utility network or
          trace network layer on which the set of specified input diagram names
          to delete are based.
      template_names {String}:
          The names of the templates for which the related diagrams will be
          processed.
      diagram_names {String}:
          The names of the diagrams to be processed.

        """