# Generated documentation for module arcpy.nd


class ApplyGridLayout(object):
    """
    Positions diagram junctions relative to a predefined magnetic grid.
    """

    @property
    def description(self) -> str:
        return """

        ApplyGridLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {cell_width_absolute}, {cell_height_absolute}, {run_async})

        Positions diagram junctions relative to a predefined magnetic grid.

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
      cell_width_absolute {Linear Unit}:
          The width of each grid cell. The default is 2 in the units of the
          diagram's coordinate system.
      cell_height_absolute {Linear Unit}:
          The height of each grid cell. The default is 2 in the units of the
          diagram's coordinate system.
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