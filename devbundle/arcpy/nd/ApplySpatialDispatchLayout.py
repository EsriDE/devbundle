# Generated documentation for module arcpy.nd


class ApplySpatialDispatchLayout(object):
    """
    Separates diagram junctions that are visibly close to overlapping.
    """

    @property
    def description(self) -> str:
        return """

        ApplySpatialDispatchLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {iterations_number}, {maximum_shift_factor}, {run_async})

        Separates diagram junctions that are visibly close to overlapping.

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
          The number of iterations to process. The default is 5.
      maximum_shift_factor {Double}:
          The maximum value used to increase the diagram junctions' displacement
          for junctions that are very close together. The greater the shift
          factor, the larger the separation between the diagram junctions that
          almost overlap. The default is 2.
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