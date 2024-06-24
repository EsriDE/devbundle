# Generated documentation for module arcpy.edit


class Densify(object):
    """
    Adds vertices along line or polygon features and replaces curve segments (Bezier, circular arcs, and elliptical arcs) with line segments.
    """

    @property
    def description(self) -> str:
        return """

        Densify_edit(in_features, {densification_method}, {distance}, {max_deviation}, {max_angle}, {max_vertex_per_segment})

        Adds vertices along line or polygon features and replaces curve
        segments (Bezier, circular arcs, and elliptical arcs) with line
        segments.

     INPUTS:
      in_features (Feature Layer):
          The polygon or line feature class to be densified.
      densification_method {String}:
          Specifies the feature densification method to be
          used.DISTANCE-Straight lines and curves will be densified using the
          specified distance. This is the default.OFFSET-Curves will be
          densified using the specified maximum offset
          deviation.ANGLE-Curves will be densified using the specified maximum
          deflection
          angle.
      distance {Linear Unit}:
          The maximum distance between vertices. This distance will always be
          applied to line segments and to simplify curves. The default value is
          a function of the data's x,y tolerance.New vertices may not be
          inserted at this exact interval along the
          line, rather they will be inserted within this distance of the
          previous vertex. There is no way to ensure that a vertex is added
          exactly at the specified interval along the line segment.
      max_deviation {Linear Unit}:
          The maximum distance the output segment will be from the original.
          This parameter only affects curves. The default value is a function of
          the data's x,y tolerance.
      max_angle {Double}:
          The maximum angle the output geometry can be from the input geometry.
          The valid range is 0 to 90. The default value is 10. This parameter
          only affects curves.
      max_vertex_per_segment {Long}:
          The maximum vertex count allowed per segment. If no value or an
          invalid value (0 or less) is entered, there will be no vertex limit
          for linear segments, and curve segments will have a default of 12000.

        """