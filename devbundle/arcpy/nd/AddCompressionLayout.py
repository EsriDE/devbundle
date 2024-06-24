# Generated documentation for module arcpy.nd


class AddCompressionLayout(object):
    """
    Adds the Compression layout algorithm to the layout list of the input diagram template so it automatically runs at the end of diagram buildings. This tool also presets the Compression layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddCompressionLayout_nd(in_utility_network, template_name, is_active, {are_containers_preserved}, {grouping_distance_absolute}, {vertices_removal_rule})

        Adds the Compression layout algorithm to the layout list of the input
        diagram template so it automatically runs at the end of diagram
        buildings. This tool also presets the Compression layout algorithm
        parameters for any diagram based on that template.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the layout algorithm will automatically run when
          generating diagrams based on the specified template.
          ACTIVE-The added layout algorithm will automatically run
          during the generation of any diagram that is based on the
          template_name parameter value. This is the default. The
          parameter values specified for the layout algorithm are used to
          run the layout during diagram generation. They are also loaded by
          default when the algorithm is to be run on any diagram based on the
          input template.INACTIVE-All the parameter values currently specified
          for the added
          layout algorithm will be loaded by default when the algorithm is to be
          run on any diagram based on the input template.
      are_containers_preserved {Boolean}:
          Specifies how containers will be processed by the Compression layout
          algorithm.PRESERVE_CONTAINERS-The Compression layout algorithm will
          apply to
          the top graph of the diagram so containers are preserved. This is the
          default.IGNORE_CONTAINERS-The Compression layout algorithm will apply
          to both
          content and noncontent features in the diagram.
      grouping_distance_absolute {Linear Unit}:
          The maximum distance that will be used to determine whether two
          connected junctions are close enough to be considered part of the same
          junctions group. A junctions group represents many junctions that are
          moved as a group during the layout algorithm process. The group can
          contain both junctions and containers. To group two junctions, they
          must also be connected in the diagram by an edge. The default is 20
          units in the diagram's coordinate system.
      vertices_removal_rule {String}:
          Specifies the edge vertices that will be removed from the
          diagram.ALL-All edge vertices will be removed from the diagram.
          OUTER-Any edge vertices that are within the detected
          junctions' groups will be maintained; edge vertices that are outside
          the detected junctions' groups will be removed. When
          containers in the diagram have edges that intersect the container
          polygons, a vertex will be added at the intersection of the edge and
          container polygon. This is the default. OUTER_EXCEPT_FIRST-Any
          edge vertices that are within the
          detected junctions' groups will be maintained; edge vertices that are
          outside the detected junctions' groups will be removed. When
          containers in the diagram have edges that intersect the container
          polygons, the first (or last) outside vertex will be preserved on
          edges that intersect a container polygon.A vertex will be inserted at
          the intersection of the edges and
          container polygons.

        """