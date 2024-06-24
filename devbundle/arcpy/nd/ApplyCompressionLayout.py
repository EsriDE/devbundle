# Generated documentation for module arcpy.nd


class ApplyCompressionLayout(object):
    """
    Compresses the diagram features toward the middle of the diagram.
    """

    @property
    def description(self) -> str:
        return """

        ApplyCompressionLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {grouping_distance_absolute}, {vertices_removal_rule}, {run_async})

        Compresses the diagram features toward the middle of the diagram.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram to which the layout will be applied.
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
      run_async {Boolean}:
          Specifies whether the layout algorithm will run asynchronously or
          synchronously on the server.RUN_ASYNCHRONOUSLY-The layout algorithm
          will run asynchronously on the
          server. This option dedicates server resources to run the layout
          algorithm with a longer time-out. Running asynchronously is
          recommended for layouts that are time consuming and may exceed the
          server time-out (for example, Partial Overlapping Edges) and applying
          to large diagrams (more than 25,000 features).RUN_SYNCHRONOUSLY-The
          layout algorithm will run synchronously on the
          server. It can fail without completion if it exceeds the service
          default time-out value of 600 seconds. This is the default.

        """