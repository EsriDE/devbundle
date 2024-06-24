# Generated documentation for module arcpy.nd


class StoreDiagram(object):
    """
    Stores a temporary network diagram in the database. Access rights and tags can be assigned to control security and searchability of the diagram.
    """

    @property
    def description(self) -> str:
        return """

        StoreDiagram_nd(in_network_diagram_layer, out_name, {access_right_type}, {tags})

        Stores a temporary network diagram in the database. Access rights and
        tags can be assigned to control security and searchability of the
        diagram.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The temporary network diagram layer to be stored.
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
          Tags help with querying the stored diagram using thepane.
          Find DiagramsUse the # character to separate each tag and aid in
          efficient diagram
          searches.

     OUTPUTS:
      out_name (Diagram Layer):
          The name of the output network diagram.

        """