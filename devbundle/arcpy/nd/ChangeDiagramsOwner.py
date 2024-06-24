# Generated documentation for module arcpy.nd


class ChangeDiagramsOwner(object):
    """
    Changes ownership of stored network diagrams.
    """

    @property
    def description(self) -> str:
        return """

        ChangeDiagramsOwner_nd(in_diagrams, target_owner, {source_owner}, {diagram_names;diagram_names...})

        Changes ownership of stored network diagrams.

     INPUTS:
      in_diagrams (Utility Network / Trace Network / Utility Network Layer / Trace Network Layer / Diagram Layer):
          The input network layer or network diagram layer related to the
          utility network or trace network of interest with the stored network
          diagrams whose ownership will be transferred.
      target_owner (String):
          The name of the user that will become the new owner of the specified
          diagrams.
      source_owner {String}:
          The name of the user whose ownership of the network diagrams will be
          changed.This parameter is only used when there are no specified
          diagram names.
          When diagram names are specified, it will be ignored.
      diagram_names {String}:
          The names of the diagrams to be processed.

        """