# Generated documentation for module arcpy.edit


class SimplifyByStraightLinesAndCircularArcs(object):
    """
    Simplifies polygon and line features by replacing consecutive line segments or edges with fewer line segments or edges. Lines segments and polygon edges are simplified based on a specified maximum allowable offset. Additionally, circular arcs can be created from consecutive line segments or polygon edges.
    """

    @property
    def description(self) -> str:
        return """

        SimplifyByStraightLinesAndCircularArcs_edit(in_features;in_features..., max_offset, {fitting_type}, {circular_arcs}, {max_arc_angle_step}, {min_vertex_count}, {min_radius}, {max_radius}, {min_arc_angle}, {closed_ends}, {anchor_points})

        Simplifies polygon and line features by replacing consecutive line
        segments or edges with fewer line segments or edges. Lines segments
        and polygon edges are simplified based on a specified maximum
        allowable offset. Additionally, circular arcs can be created from
        consecutive line segments or polygon edges.

     INPUTS:
      in_features (Feature Layer):
          The features to be simplified. Features can be lines or polygons. If
          using multiple inputs, the features must have the same spatial
          reference.
      max_offset (Linear Unit):
          The maximum distance the output feature edges can deviate from
          the input feature shapes. When theoption is specified for
          theparameter, the distance is measured between the input vertices and
          the output feature edges. When theoption is specified, the distance is
          measured between the input feature edges and the output feature edges.
          Fit to verticesFitting TypeFit to segments
      fitting_type {String}:
          Specifies how the output feature edges and circular arcs will be
          fitted to the input feature shapes. Ifis specified,
          theandparameters are not available. Fit
          to segmentsMaximum Arc Angle StepMinimum Number Of
          VerticesFIT_TO_VERTICES-The offset gap between the output feature
          edges and
          the input feature vertices will be minimized. Output feature edges and
          curves will be fitted approximately to the input feature vertex
          positions. This is the default.FIT_TO_SEGMENTS-The offset gap between
          the output feature edges and
          input feature edges will be minimized. Output edges and curves will be
          fitted approximately to the positions of the input feature shapes.
      circular_arcs {Boolean}:
          Specifies whether circular arcs will be created.CREATE-Circular arcs
          will be created. This is the
          default.NOT_CREATE-Circular arcs will not be created.
      max_arc_angle_step {Double}:
          The maximum arc angle step (decimal degrees) that will be used
          to construct circular arcs. The arc angle defines how wide the visual
          field can be, for each step, when locating vertices to construct
          circular curves. The arc angle is the central angle of the candidate
          curve (the curve that is being constructed). If vertices are found
          within each maximum arc angle step, a circular arc is constructed. For
          example, if vertices and edges are sparse, use a large arc angle step.
          The valid value range is from 2 through 95 decimal degrees. The
          default is 20 decimal degrees. This parameter is not available if
          theoption is specified for theparameter. Fit to segmentsFitting
          Type
      min_vertex_count {Long}:
          The minimum number of vertices required for a circular arc to
          be created. The value must be greater than 3. The default is 4. This
          parameter is not available if theoption is specified for theparameter.
          Fit to segmentsFitting Type
      min_radius {Linear Unit}:
          The smallest allowable radius for output circular arcs. The
          value must be greater than 0 and smaller than the value provided for.
          If no value is provided, the radius of the output circular arcs will
          not be checked (default). Maximum Radius
      max_radius {Linear Unit}:
          The largest allowable radius for output circular arcs. The
          value must be greater than the value provided for. If no value is
          provided, the radius of the output circular arcs will not checked
          (default). Minimum Radius
      min_arc_angle {Double}:
          The minimum arc angle (decimal degrees) that will be used to construct
          circular arcs. The minimum arc angle is the smallest allowable central
          angle in the output circular arcs. If the central angle of any output
          circular arc is less than this value, it will not be created. The
          valid value range is from 2 through 360 decimal degrees. The default
          is 2 decimal degrees.
      closed_ends {Boolean}:
          Specifies whether the endpoints of a closed line will be preserved. A
          closed line is a line that has coincident end points
          (loop).PRESERVE-The endpoints of closed lines will be preserved. This
          is the
          default.NOT_PRESERVE-The endpoints of closed lines will not be
          preserved; they
          can be moved or deleted.
      anchor_points {Feature Layer}:
          The path and name of the feature class that contains anchor points.
          Anchor points overlay vertices on the input features and indicate that
          they should not be moved or deleted in the simplify process.

        """