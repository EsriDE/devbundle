# Generated documentation for module arcpy.nd


class AddMainlineTreeLayout(object):
    """
    Adds the Mainline Tree Layout algorithm to the list of layouts to be automatically chained at the end of the building of diagrams based on a given template. This tool also presets the Mainline Tree Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddMainlineTreeLayout_nd(in_utility_network, template_name, is_active, {are_containers_preserved}, {tree_direction}, {branches_placement}, {is_unit_absolute}, {perpendicular_absolute}, {perpendicular_proportional}, {along_absolute}, {along_proportional}, {disjoined_graph_absolute}, {disjoined_graph_proportional}, {are_edges_orthogonal}, {breakpoint_position}, {edge_display_type}, {offset_absolute}, {offset_proportional})

        Adds the Mainline Tree Layout algorithm to the list of layouts to be
        automatically chained at the end of the building of diagrams based on
        a given template. This tool also presets the Mainline Tree Layout
        algorithm parameters for any diagram based on that template.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the layout algorithm will automatically run when
          generating diagrams based on the specified template.
          ACTIVE-The added layout algorithm will automatically run
          during the generation of any diagram that is based on the
          template_name parameter value. This is the default. The
          parameter values specified for the layout algorithm are used to
          run the layout during diagram generation. They are also loaded by
          default when the algorithm is to be run on any diagram based on the
          input template.INACTIVE-All the parameter values currently specified
          for the added
          layout algorithm will be loaded by default when the algorithm is to be
          run on any diagram based on the input template.
      are_containers_preserved {Boolean}:
          Specifies how the algorithm will process
          containers.PRESERVE_CONTAINERS-The layout algorithm will apply to the
          top graph
          of the diagram so containers are preserved.IGNORE_CONTAINERS-The
          layout algorithm will apply to both content and
          noncontent features in the diagram. This is the default.
      tree_direction {String}:
          Specifies the direction of the main line.FROM_LEFT_TO_RIGHT-The main
          line will be drawn as a horizontal line
          starting from the left and ending on the right. This is the
          default.FROM_RIGHT_TO_LEFT-The main line will be drawn as a horizontal
          line
          starting from the right and ending on the left.FROM_BOTTOM_TO_TOP-The
          main line will be drawn as a vertical line
          starting from the bottom and ending at the top.FROM_TOP_TO_BOTTOM-The
          main line will be drawn as a vertical line
          starting from the top and ending at the bottom.
      branches_placement {String}:
          Specifies how branches from the main line will be relatively placed
          with regard to its direction.BOTH_SIDES-Branches will be placed on
          both the left and right sides of
          the main line. This is the default.LEFT_SIDE-Branches will only be
          placed on the left side of the main
          line.RIGHT_SIDE-Branches will only be placed on the right side of the
          main
          line.
      is_unit_absolute {Boolean}:
          Specifies how parameters representing distances will be
          interpreted.ABSOLUTE_UNIT-The layout algorithm will interpret distance
          values as
          linear units.PROPORTIONAL_UNIT-The layout algorithm will interpret
          distance values
          as relative units to an estimation of the average of the junction
          sizes in the current diagram extent. This is the default.
      perpendicular_absolute {Linear Unit}:
          The spacing between diagram junctions that are displayed along the
          axis perpendicular to the main line. The default is 2 in the diagram's
          coordinate system. This parameter can only be used with absolute
          units.
      perpendicular_proportional {Double}:
          The spacing between diagram junctions that are displayed along the
          axis perpendicular to the main line. The default is 2. This parameter
          can only be used with proportional units.
      along_absolute {Linear Unit}:
          The spacing between diagram junctions that are displayed along the
          main line, as well as the spacing between diagram junctions that are
          displayed along the axis parallel to the main line. This parameter can
          only be used with absolute units. The default is 2 in the units of the
          diagram's coordinate system.
      along_proportional {Double}:
          The spacing between diagram junctions that are displayed along the
          main line, as well as the spacing between diagram junctions that are
          displayed along the axis parallel to the main line. This parameter is
          used with proportional units. The default is 2.
      disjoined_graph_absolute {Linear Unit}:
          The minimum spacing that will separate features belonging to disjoined
          graphs when the diagram contains such graphs. This parameter is used
          with absolute units. The default is 4 in the units of the diagram's
          coordinate system.
      disjoined_graph_proportional {Double}:
          The minimum spacing that will separate features belonging to disjoined
          graphs when the diagram contains such graphs. This parameter is used
          with proportional units. The default is 4.
      are_edges_orthogonal {Boolean}:
          Specifies how diagram edges that are related to the tree branches will
          display.ORTHOGONAL_EDGES-All diagram edges related to the tree
          branches will
          display with right angles.SLANTED_EDGES-All diagram edges related to
          the tree branches will not
          display with right angles. This is the default.
      breakpoint_position {Double}:
          The relative position of the break point that will be inserted
          along the diagram edges whenis set to(edge_display_type =
          "REGULAR_EDGES" in Python) oris set to(edge_display_type =
          "ORTHOGONAL_EDGES" in Python). It is a percentage between 0 and 100.
          Edge Display TypeRegular edgesEdge Display TypeOrthogonal edgesWith a
          Break Point Relative Position (%) value of 0, the break point
          is positioned at the x-coordinate of the edge's from junction and at
          the y-coordinate of the edge's to junction for a horizontal tree. It
          is positioned at the y-coordinate of the edge's from junction and at
          the x-coordinate of the edge's to junction for a vertical tree.With a
          Break Point Relative Position (%) value of 100, there is no
          break point inserted on the diagram edges; each diagram edge directly
          connects its from and to junctions.With a Break Point Relative
          Position (%) value of N between 0 and 100,
          the break point is positioned at N% of the length of the [XY] segment,
          X being the x-coordinate of the edge's from junction and Y being the
          y-coordinate of the edge's to junction for a horizontal tree. It is
          positioned at N% of the length of the [YX] segment, Y being the
          y-coordinate of the edge's from junction and X being the x-coordinate
          of the edge's to junction for a vertical tree. The relative
          position of the two inflection points that will
          be inserted along the diagram edges to compute the curved edges
          geometry whenis set to(edge_display_type = "CURVED_EDGES" in Python).
          It is a percentage between 15 and 40. With a Break Point Relative
          Position (%) value of N between 15 and 40:        Edge Display
          TypeCurved edges          X being the x-coordinate of the edge's from
          junction and Y
          being the y-coordinate of the edge's to junction for a horizontal
          tree:          The first inflection point will be positioned at N% of
          the length of
          the [XY] segment.The second inflection point will be positioned at
          (100 - N)% of the
          length of the [XY] segment. Y being the y-coordinate of the
          edge's from junction and X
          being the x-coordinate of the edge's to junction for a vertical tree:
          The first inflection point will be positioned at N% of the length of
          the [YX] segment.The second inflection point will be positioned at
          (100 - N)% of the
          length of the [XY] segment.The concept of the from and to junctions
          above is relative to the tree
          direction; it has nothing to do with the real topology of the edge
          feature or edge object in the network.
      edge_display_type {String}:
          Specifies the type of display for the diagram edges related to the
          tree branches.REGULAR_EDGES-All diagram edges related to the tree
          branches will not
          display with right angles. This is the default.ORTHOGONAL_EDGES-All
          diagram edges related to the tree branches will
          display with right angles.CURVED_EDGES-All diagram edges related to
          the tree branches will be
          curved.
      offset_absolute {Linear Unit}:
          The offset that will be used to separate overlapping segments when
          is_unit_absolute = "ABSOLUTE_UNIT" and edge_display_type =
          "ORTHOGONAL_EDGES". The value cannot exceed 10 percent of the smallest
          value specified for the other spacing parameters. The default is 0.
      offset_proportional {Double}:
          The offset that will be used to separate overlapping segments when
          is_unit_absolute = "PROPORTIONAL_UNIT" and edge_display_type =
          "ORTHOGONAL_EDGES". It is a double value that cannot exceed 10 percent
          of the smallest value specified for the other spacing parameters. The
          default is 0.

        """