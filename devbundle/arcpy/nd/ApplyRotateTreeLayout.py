# Generated documentation for module arcpy.nd


class ApplyRotateTreeLayout(object):
    """
    Rotates the tree or trees related to pivot junctions currently set up in a diagram to the specified angle.
    """

    @property
    def description(self) -> str:
        return """

        ApplyRotateTreeLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {rotation_angle}, {run_async}, {rotate_junction})

        Rotates the tree or trees related to pivot junctions currently set up
        in a diagram to the specified angle.

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
      rotation_angle {Double}:
          The angle in degrees that will be used to rotate the tree. The default
          is 45 degrees.
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
      rotate_junction {Boolean}:
          Specifies whether the rotation_angle parameter value will be
          added to the value of thefield for each processed diagram junction.
          rotation         ROTATE-The rotation_angle parameter value will be
          added to
          the value of thefield for each processed diagram junction.
          rotation         DO_NOT_ROTATE-The rotation_angle parameter value will
          not be
          added to the value of thefield. This is the default. rotation

        """