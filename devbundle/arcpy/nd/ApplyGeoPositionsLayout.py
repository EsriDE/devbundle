# Generated documentation for module arcpy.nd


class ApplyGeoPositionsLayout(object):
    """
    Moves each diagram junction and edge feature so they match the geographical positions of the associated network features.
    """

    @property
    def description(self) -> str:
        return """

        ApplyGeoPositionsLayout_nd(in_network_diagram_layer, {restore_edges_geo_positions}, {run_async})

        Moves each diagram junction and edge feature so they match the
        geographical positions of the associated network features.

     INPUTS:
      in_network_diagram_layer (Diagram Layer):
          The network diagram to which the layout will be applied.
      restore_edges_geo_positions {Boolean}:
          Indicates whether or not diagram edges will be restored to the
          geographic position of their
          vertices:RESTORE_EDGES_GEO_POSITIONS-Vertices along diagram edges will
          be
          restored when possible, moving them to match the geographic positions
          of the network features. This is the
          default.DO_NOT_RESTORE_EDGES_GEO_POSITIONS-Vertices along diagram
          edges will
          not be restored. They will appear as straight lines between their
          connecting junctions.
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