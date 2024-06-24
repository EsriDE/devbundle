# Generated documentation for module arcpy.nd


class AddRelativeMainlineLayout(object):
    """
    Adds the Relative Mainline Layout algorithm to the list of layouts to be automatically chained at the end of the building of diagrams based on a given template. This tool also presets the Relative Mainline Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddRelativeMainlineLayout_nd(in_utility_network, template_name, is_active, line_attribute, {mainline_direction}, {offset_between_branches}, {breakpoint_angle}, {type_attribute}, {mainline_values;mainline_values...}, {branch_values;branch_values...}, {excluded_values;excluded_values...}, {is_compressing}, {compression_ratio}, {minimal_distance}, {alignment_attribute}, {initial_distances}, {length_attribute})

        Adds the Relative Mainline Layout algorithm to the list of layouts to
        be automatically chained at the end of the building of diagrams based
        on a given template. This tool also presets the Relative Mainline
        Layout algorithm parameters for any diagram based on that template.

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
      line_attribute (String):
          The name of the network attribute that will be used to identify the
          lines that comprise the straight lines. This network attribute must
          exist in the network line classes. Its values must be the same for all
          the edges that comprise a straight line, for example, Line 1, Line 2,
          and so on.
      mainline_direction {String}:
          Specifies the direction of the main line.FROM_LEFT_TO_RIGHT-The main
          line will be drawn as a horizontal line
          starting from the left and ending on the right. This is the
          default.FROM_TOP_TO_BOTTOM-The main line will be drawn as a vertical
          line
          starting from the top and ending at the bottom.
      offset_between_branches {Linear Unit}:
          The spacing between two adjacent branches along the axis perpendicular
          to the direction of the lines.
      breakpoint_angle {Double}:
          The angle that will be used to position the break point on the
          branches. It is a value between 30 and 90 degrees that is combined
          with the offset_between_branches parameter value to compute this
          position. When the break point angle value is 90 degrees, each branch
          displays orthogonally.
      type_attribute {String}:
          The name of the network attribute that will be used to qualify the
          lines. This network attribute may exist in the network line
          classes.The type_attribute and line_attribute parameter values can be
          the
          same.
      mainline_values {Value Table}:
          The type_attribute values that identify the main lines. When such
          values exist, they must be the same for any edge that comprises the
          main lines, regardless of their related network feature line classes
          or edge object tables.
      branch_values {Value Table}:
          The type_attribute values that identify the branches.
      excluded_values {Value Table}:
          The type_attribute values that identify the edges that will be
          excluded from the straight lines (crossovers or ladders).
      is_compressing {Boolean}:
          Specifies whether the graph will be
          compressed.USE_COMPRESSION-Compression will be used. An additional
          step is run at
          the end of the process to reduce the distances between adjacent groups
          of neighbor junctions along the direction while maintaining relative
          positioning between these groups. Neighbor junctions are junctions
          that are geographically close to each other without being directly
          connected.DO_NOT_USE_COMPRESSION-Compression will not be used. This is
          the
          default.
      compression_ratio {Double}:
          A value between 0 and 100 that is applied to the length of any edge
          after subtracting the minimal distance of its length. When the value
          is 100, the distance between each detected junction group is equal to
          the minimal distance.
      minimal_distance {Linear Unit}:
          The minimal distance between two adjacent groups of neighbor
          junctions. This minimal distance is also used to group neighbor
          junctions based on their projection along the direction axis. Two
          junctions projected on this axis will belong to the same group when
          the distance between the two projected points is less than this
          distance.
      alignment_attribute {String}:
          The name of the network attribute that will be used to align lines
          that are split. Lines with the same attribute value will be aligned.
      initial_distances {String}:
          Specifies how the length of the diagram edges will be assessed. This
          length determines the positions of the junctions along the direction.
          The distances between the connected junctions along the direction are
          not equidistant; they are relative to each other and depend on the
          current edge length and the length of the shortest
          edge.FROM_CURRENT_EDGE_GEOMETRY-The distances will be computed from
          the
          current edge geometry. This is the default.FROM_ATTRIBUTE_EDGE-The
          distances will be computed from a given
          attribute that exists on an edge.
      length_attribute {String}:
          The network attribute from which the distances will be computed when
          initial_distances is FROM_ATTRIBUTE_EDGE.

        """