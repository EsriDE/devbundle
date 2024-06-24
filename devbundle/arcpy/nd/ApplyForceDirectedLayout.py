# Generated documentation for module arcpy.nd


class ApplyForceDirectedLayout(object):
    """
    Emphasizes loops contained in a network diagram.
    """

    @property
    def description(self) -> str:
        return """

        ApplyForceDirectedLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {iterations_number}, {repel_factor}, {degree_freedom}, {breakpoint_position}, {edge_display_type}, {run_async})

        Emphasizes loops contained in a network diagram.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram to which the layout will be applied.
      are_containers_preserved {Boolean}:
          Specifies how the algorithm will process
          containers.PRESERVE_CONTAINERS-The layout algorithm will apply to the
          top graph
          of the diagram so containers are preserved.IGNORE_CONTAINERS-The
          layout algorithm will apply to both content and
          noncontent features in the diagram. This is the default.
      iterations_number {Long}:
          The number of iterations to process. The default is 20.
      repel_factor {Double}:
          Adds distance between diagram junctions that are close together. The
          larger the repel factor, the greater the distance that will be added
          between nearly overlapping diagram junctions. The default is 1.
      degree_freedom {String}:
          Specifies the area used to move the diagram junctions during each
          algorithm iteration.LOW-The area used to move the diagram junctions
          will be limited. This
          is the default.HIGH-The area used to move the diagram junctions will
          be large.MEDIUM-The area used to move the diagram junctions will be
          moderate.
      breakpoint_position {Double}:
          The relative position of the two inflexion points that will be
          inserted along the diagram edges to compute the curved edges geometry
          whenis set to(edges_display_type = "CURVED_EDGES" in Python). It is a
          percentage between 15 and 40; the default is 30. For example, with
          aparameter value of N between 15 and 40, the following is true:
          Edge Display TypeCurved edgesBreak Point Relative Position (%)
          X being the x-coordinate of the edge's from junction and Y
          being the y-coordinate of the edge's to junction for a horizontal
          tree:          The first inflexion point will be positioned at N% of
          the length of
          the [XY] segmentThe second inflexion point will be positioned at (100
          - N)% of the
          length of the [XY] segment          Y being the y-coordinate of the
          edge's from junction and X
          being the x-coordinate of the edge's to junction for a vertical tree:
          The first inflexion point will be positioned at N% of the length of
          the [YX] segmentThe second inflexion point will be positioned at (100
          - N)% of the
          length of the [XY] segmentThe concept of the from and to junctions
          above is relative to the tree
          direction; it is not related to the topology of the network feature or
          object edge. This parameter is ignored when theparameter is set
          to(edges_display_type = "REGULAR_EDGES" in Python). Edge
          Display TypeRegular edges
      edge_display_type {String}:
          Specifies the type of display for the diagram edges.REGULAR_EDGES-All
          diagram edges display as straight lines. This is the
          default.CURVED_EDGES-All diagram edges are curved.
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