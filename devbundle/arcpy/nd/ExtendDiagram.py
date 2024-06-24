# Generated documentation for module arcpy.nd


class ExtendDiagram(object):
    """
    Extends a network diagram one network element level based on network connectivity or traversability or on containment or structural attachment associations.
    """

    @property
    def description(self) -> str:
        return """

        ExtendDiagram_nd(in_network_diagram_layer, {ignore_traversability}, {extension_type})

        Extends a network diagram one network element level based on network
        connectivity or traversability or on containment or structural
        attachment associations.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram to extend.
      ignore_traversability {Boolean}:
          Specifies whether traversability or connectivity will be used to
          extend the diagram.IGNORE_TRAVERSABILITY-The traversability of the
          network will be
          ignored. This is the default.HONOR_TRAVERSABILITY-The traversability
          of the network will be
          honored.
      extension_type {String}:
          Specifies how the diagram will be extended.BY_CONNECTIVITY-The network
          diagram will be extended one network
          element level based on network connectivity. This is the
          default.BY_TRAVERSABILITY-The network diagram will be extended one
          network
          element level based on network traversability.BY_ATTACHMENT-The
          network diagram will be extended one network element
          level based on structural attachment associations.BY_CONTAINMENT-The
          network diagram will be extended one network
          element level based on containment associations.

        """