# Generated documentation for module arcpy.nd


class AlterDiagramProperties(object):
    """
    Alters properties for a stored network diagram.
    """

    @property
    def description(self) -> str:
        return """

        AlterDiagramProperties_nd(in_network_diagram_layer, {out_name}, {access_right_type}, {tags})

        Alters properties for a stored network diagram.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The stored network diagram to alter.
      out_name {String}:
          The new name for the input network diagram.
      access_right_type {String}:
          Specifies the access right level of the input diagram.PUBLIC-Other
          users will have full access to the diagram; everyone can
          see, edit, update, and overwrite the diagram. However, no one except
          the diagram owner and the portal utility network owner-in the case of
          diagrams related to a utility network in an enterprise geodatabase-can
          use the Alter Diagram Properties tool to change the access right
          level. This is the default.PROTECTED-Other users will have read-only
          access to the diagram. They
          cannot edit, update, or overwrite the diagram. PRIVATE-Other
          users will not have access to the diagram. The
          corresponding diagram item will be hidden from other users in thepane.
          Find Diagrams
      tags {String}:
          One or several tags that will help find the stored diagram.
          These tags can be used in thepane. Find DiagramsTo add several
          tags, use the number sign (#) to separate each tag.
          This also allows a more thorough and efficient diagram search.

        """