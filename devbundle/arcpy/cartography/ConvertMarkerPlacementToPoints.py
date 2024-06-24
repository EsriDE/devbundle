# Generated documentation for module arcpy.cartography


class ConvertMarkerPlacementToPoints(object):
    """
    Creates points from the markers of a marker placement in a symbolized polygon feature.
    """

    @property
    def description(self) -> str:
        return """

        ConvertMarkerPlacementToPoints_cartography(in_layer, out_feature_class, {create_multipoints}, {boundary_option}, {boundary_distance}, {boundary_distance_field}, {boundary_distance_unit}, {in_barriers;in_barriers...}, {keep_at_least_one_marker}, {displacement_method}, {minimum_marker_distance})

        Creates points from the markers of a marker placement in a symbolized
        polygon feature.

     INPUTS:
      in_layer (Layer):
          A polygon layer symbolized with a marker placement.
      create_multipoints {Boolean}:
          Specifies whether output point features will be
          multipoint.CREATE_MULTIPOINTS-A multipoint feature will be created for
          the
          markers in each input polygon. This is the default.CREATE_POINTS-A
          point feature will be created for each marker.
      boundary_option {String}:
          Specifies whether output points will be created for input markers that
          cross polygon boundaries.MAY_CROSS_BOUNDARY-Output points will be
          created for input markers
          that cross polygon boundaries. This is the
          default.FIXED_DISTANCE-Output points will not be created for input
          markers
          that are within the distance of polygon boundaries specified by the
          boundary_distance parameter.VALUE_FROM_FIELD-Output points will not be
          created for input markers
          that are within the distance of polygon boundaries specified by the
          boundary_distance_field parameter.
      boundary_distance {Double}:
          The minimum distance between the output point symbols and the polygon
          boundaries. This parameter is applied only when the boundary_option
          parameter is set to FIXED_DISTANCE. The default value is 0.
      boundary_distance_field {Field}:
          A numeric field from the input polygons that will be used to determine
          the boundary distance .This parameter is applied only when the
          boundary_option parameter is set to VALUE_FROM_FIELD.
      boundary_distance_unit {String}:
          Specifies the linear unit that will be used for boundary distance
          values.Kilometers-The unit will be kilometers.Meters-The unit will be
          meters.Decimeters-The unit will be decimeters.Centimeters-The unit
          will be centimeters.Millimeters-The unit will be millimeters.Nautical
          Miles-The unit will be nautical miles.Statute Miles-The unit will be
          statute miles.Yards-The unit will be yards.Feet-The unit will be
          feet.Inches-The unit will be inches.Degrees-The unit will be
          degreesPoints-The unit will be points. This is the default.
      in_barriers {Value Table}:
          The layers containing points, lines, or polygon features that
          are conflict barriers for input markers. Markers that conflict with
          barriers will not be created. The symbology of the barrier layers will
          be considered. barrier_layer-A layer containing points, lines,
          or polygon
          features.barrier_distance-A numeric value specifying the minimum
          distance
          between markers and the barrier. This will be ignored if the
          barrier_distance_field value is set. The default value is
          0.barrier_distance_field-A numerical field from the barrier layer that
          will be used as the barrier distance. This will override the
          barrier_distance value. The default value is
          <None>.barrier_distance_unit-The linear unit that will be used for
          barrier
          distance values. The default value is Points.
      keep_at_least_one_marker {Boolean}:
          Specifies whether a single marker will be created for input polygons
          when all markers conflict with boundaries or
          barriers.KEEP_AT_LEAST_ONE_MARKER-One marker will be created for input
          polygons
          when all markers conflict with boundaries or
          barriers.DO_NOT_KEEP_AT_LEAST_ONE_MARKER-No markers will be created
          for input
          polygons when all markers conflict with boundaries or barriers. This
          is the default.
      displacement_method {String}:
          Specifies the displacement method that will be used to move markers
          that are too close to each other. This parameter is applied only when
          markers are positioned randomly inside the
          polygons.DO_NOT_DISPLACE-Markers will not be displaced. This is the
          default.DISPLACE_TOWARD_GRID-Conflicting markers will be moved toward
          their
          original regular grid points.DISPLACE_APART-Conflicting markers will
          be moved away from each other.
      minimum_marker_distance {Linear Unit}:
          The minimum distance between individual markers. This parameter is
          applied only when markers are positioned randomly inside the polygons.
          The default value is 0.

     OUTPUTS:
      out_feature_class (Feature Class):
          A point feature class containing points created from markers in the
          input layer's marker placement settings. The points will be added to
          the active map as a layer symbolized with a unique value renderer
          using symbols from the input.

        """