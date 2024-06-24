# Generated documentation for module arcpy.nd


class ApplyPartialOverlappingEdgesLayout(object):
    """
    Spaces out collinear edges or collinear portions of edges (edge segments) inside a given buffer zone.
    """

    @property
    def description(self) -> str:
        return """

        ApplyPartialOverlappingEdgesLayout_nd(in_network_diagram_layer, buffer_width_absolute, offset_absolute, {optimize_edges}, {run_async})

        Spaces out collinear edges or collinear portions of edges (edge
        segments) inside a given buffer zone.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram to which the layout will be applied.
      buffer_width_absolute (Linear Unit):
          The width of the buffer zone in which to search for collinear edge
          segments.
      offset_absolute (Linear Unit):
          The distance that will separate the detected edge segments.
      optimize_edges {Boolean}:
          Specifies how segments will be placed along edges:OPTIMIZE_EDGES-The
          placement of segments will be optimized in each set
          of collinear segments. This is done by focusing on their connections
          instead of their positions. Segments that cross each other can be
          repositioned so they do not cross.DO_NOT_OPTIMIZE_EDGES-The initial
          position of each segment will be
          maintained in the collinear segment set and crossings will be
          preserved. This is the default.
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