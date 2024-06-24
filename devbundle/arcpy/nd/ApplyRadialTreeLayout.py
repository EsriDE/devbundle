# Generated documentation for module arcpy.nd


class ApplyRadialTreeLayout(object):
    """
    Arranges diagram features hierarchically and places them in a radial tree.
    """

    @property
    def description(self) -> str:
        return """

        ApplyRadialTreeLayout_nd(in_network_diagram_layer, {are_containers_preserved}, {is_unit_absolute}, {initial_radius_absolute}, {initial_radius_proportional}, {disjoined_graph_absolute}, {disjoined_graph_proportional}, {radius_factor}, {run_async})

        Arranges diagram features hierarchically and places them in a radial
        tree.

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
      is_unit_absolute {Boolean}:
          Specifies how parameters representing distances will be
          interpreted.ABSOLUTE_UNIT-The layout algorithm will interpret distance
          values as
          linear units.PROPORTIONAL_UNIT-The layout algorithm will interpret
          distance values
          as relative units to an estimation of the average of the junction
          sizes in the current diagram extent. This is the default.
      initial_radius_absolute {Linear Unit}:
          The radius of the first concentric circle whose center is the radial
          tree root junction-that is, the radius of the circle around which the
          diagram junctions belonging to the first hierarchical level are
          placed. The default is 5 in the units of the diagram's coordinate
          system. This parameter can only be used with absolute units.
      initial_radius_proportional {Double}:
          The radius of the first concentric circle whose center is the radial
          tree root junction-that is, the radius of the circle around which the
          diagram junctions belonging to the first hierarchical level are
          placed. The default is 5. This parameter can only be used with
          proportional units.
      disjoined_graph_absolute {Linear Unit}:
          The minimum spacing that will separate features belonging to disjoined
          graphs when the diagram contains such graphs. This parameter is used
          with absolute units. The default is 4 in the units of the diagram's
          coordinate system.
      disjoined_graph_proportional {Double}:
          The minimum spacing that will separate features belonging to disjoined
          graphs when the diagram contains such graphs. This parameter is used
          with proportional units. The default is 4.
      radius_factor {Double}:
          The multiplicative factor used to increase or decrease the radius of
          each concentric circle. It is also the distance that separates each
          concentric circle related to a hierarchical level. When using a radius
          factor less than 1, the distance that separates the diagram junctions
          belonging to the (n) hierarchical level and the (n+1) hierarchical
          level progressively decreases. With a factor greater than 1, the
          distance between the hierarchical levels increases progressively. The
          default is 1.
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