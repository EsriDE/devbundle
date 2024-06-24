# Generated documentation for module arcpy.nd


class ReshapeDiagramEdgesLayout(object):
    """
    Processes simple operations on vertices along edges.
    """

    @property
    def description(self) -> str:
        return """

        ReshapeDiagramEdgesLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {reshape_type}, {is_path_preserved}, {offset_between_segment_absolute}, {breakpoint_absolute}, {shift_between_edge_absolute}, {angle_threshold}, {circular_arc_radius}, {circular_arc_position}, {run_async})

        Processes simple operations on vertices along edges.

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
      reshape_type {String}:
          Specifies how edges will be reshaped.REMOVE_VERTICES-Vertices along
          edges in the diagram will be
          removed.SQUARE_EDGES-Vertices will be placed along diagram edges, and
          the
          edges will be displayed with right angles. This is the
          default.SEPARATE_OVERLAPPING_EDGES-Edges that connect the same origin
          and
          extremity junctions will be separated when they are
          overlapping.REDUCE_VERTICES_BY_ANGLE-Some or all vertices displayed
          along diagram
          edges will be reduced according to the angle that separates the
          segments incident to those vertices.MARK_CROSSING_EDGES-The horizontal
          and vertical diagram edges that
          cross each other at a right angle in the diagram will be marked, and
          the geometry of one of the crossing edges will be reshaped to display
          a circular arc at this location.
      is_path_preserved {Boolean}:
          Specifies whether vertices along the edges that will be squared will
          be preserved. This parameter is enabled when reshape_type is
          SQUARE_EDGES.PRESERVE_PATH-The direction of any edge will be
          considered, and
          vertices along that edge will be preserved from the first vertex to
          the last. This is the default.IGNORE_PATH-Vertices along the diagram
          edges will not be considered,
          and the vertices will be removed.
      offset_between_segment_absolute {Linear Unit}:
          The spacing that will separate parallel segments of squared edges
          incident to the same junction. The default is 5 in the units of the
          diagram's coordinate system. This parameter is enabled when
          reshape_type is SQUARE_EDGES.
      breakpoint_absolute {Linear Unit}:
          The maximum distance between each junction to the first or last break
          point along edges incident to that junction when those edges are
          squared. The default is 8.66 in the units of the diagram's coordinate
          system. This parameter is enabled when reshape_type is SQUARE_EDGES.
      shift_between_edge_absolute {Linear Unit}:
          The absolute spacing that will separate two edges. The default is 0.5
          in the units of the diagram's coordinate system. This parameter is
          enabled when reshape_type is SEPARATE_OVERLAPPING_EDGES.
      angle_threshold {Double}:
          The angle formed by the incident segments over which the vertex
          related to these segments will be reduced. The wider the angle, the
          fewer number of vertices will be reduced. The default is 160 degrees.
          This parameter is enabled when reshape_type is
          REDUCE_VERTICES_BY_ANGLE.
      circular_arc_radius {Linear Unit}:
          The radius of the circular arc that will be added to the crossing edge
          locations. The default is 5.
      circular_arc_position {String}:
          Specifies the segment on which a circular arc will be
          placed.LEFT_OF_VERTICAL_SEGMENT-A circular arc will be placed to the
          left of
          the vertical segment.RIGHT_OF_VERTICAL_SEGMENT-A circular arc will be
          placed to the right
          of the vertical segment.ABOVE_HORIZONTAL_SEGMENT-A circular arc will
          be placed above the
          horizontal segment.BELOW_HORIZONTAL_SEGMENT-A circular arc will be
          placed below the
          horizontal segment.
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