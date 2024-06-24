# Generated documentation for module arcpy.nd


class ApplyAngleDirectedLayout(object):
    """
    Moves a diagram's edges in specified alignment directions.
    """

    @property
    def description(self) -> str:
        return """

        ApplyAngleDirectedLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {iterations_number}, {number_of_directions}, {run_async})

        Moves a diagram's edges in specified alignment directions.

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
          The number of iterations to process. The default is 1.
      number_of_directions {String}:
          The number of directions that will be used to align the diagram edges
          and their connected junctions.TWELVE_DIRECTIONS-The edges will move so
          they progressively approach
          one of the 12 axes, starting with the edge's origin junction and
          inclined at 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, or 360
          degrees.EIGHT_DIRECTIONS-The edges will move so they progressively
          approach
          one of the 8 axes, starting with the edge's origin junction and
          inclined at 45, 90, 135, 180, 225, 270, 315, or 360 degrees. This is
          the default.FOUR_DIRECTIONS-The edges will move so they progressively
          approach one
          of the 4 axes, starting with the edge's origin junction and inclined
          at 90, 180, 270, or 360 degrees.
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