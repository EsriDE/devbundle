# Generated documentation for module arcpy.edit


class UpdateCOGO(object):
    """
    Updates the COGO attributes of COGO-enabled line features to match their line shape geometries.
    """

    @property
    def description(self) -> str:
        return """

        UpdateCOGO_edit(in_line_features, {distances_type}, {distance_tolerance}, {direction_type}, {minimum_direction_difference}, {minimum_direction_lateral_offset}, {combined_scale_factor}, {direction_offset})

        Updates the COGO attributes of COGO-enabled line features to match
        their line shape geometries.

     INPUTS:
      in_line_features (Feature Layer):
          The COGO-enabled line features that will be updated.
      distances_type {String}:
          Specifies how the input line's,, andCOGO attributes will be
          updated. DistanceRadiusArc LengthOVERWRITE-All values
          (including NULL values) will be updated to match
          the shape length. This is the default.UPDATE_NULL_ONLY-Only NULL
          values will be updated to match the shape
          length.USE_MINIMUM_DIFFERENCE-Values that differ from the shape length
          by
          more than the specified tolerance will be updated to match the shape
          length.DO_NOT_UPDATE-Values will not be updated.
      distance_tolerance {Linear Unit}:
          The minimum distance difference between the line shape length
          and the value in the,, andfields. If the difference in the distances
          is larger than the specified tolerance, the attribute value in the,,
          orfields will be updated to match the line shape length. The default
          value is 0 meters. DistanceRadiusArc LengthDistanceRadiusArc
          Length
      direction_type {String}:
          Specifies how the input'sCOGO attributes will be updated.
          DirectionOVERWRITE-All values (including NULL values) will be updated
          to match
          shape direction. This is the default.UPDATE_NULL_ONLY-Only NULL values
          will be updated to match the shape
          direction.USE_MINIMUM_DIFFERENCE-Values that differ from the shape
          direction by
          more than the specified tolerance will be updated to match the shape
          direction.DO_NOT_UPDATE-Values will not be updated.
      minimum_direction_difference {Double}:
          The minimum direction difference (in seconds) between the line
          shape direction and the value in thefield. If the difference in the
          directions is larger than the specified tolerance, the attribute value
          in thefield will be updated to match the line shape direction. The
          default value is 0. DirectionDirection
      minimum_direction_lateral_offset {Linear Unit}:
          The minimum allowable distance between the endpoint of the
          line shape and the endpoint of the line drawn using the value in
          thefield. A lateral offset tolerance can be used for very long lines
          in which small changes in direction can result in large differences in
          line endpoints. The default value is 0 meters. Direction
      combined_scale_factor {Calculator Expression}:
          A scale factor based on a ground to grid correction that will
          be applied to the line's shape length. The scale factor can be
          provided as a number or derived from an Arcade expression using the
          line's attribute fields. The updated distance populated in the,,
          andfields is a result of the shape length multiplied by the scale
          factor. DistanceRadiusArc Length
      direction_offset {Calculator Expression}:
          A rotation based on a ground to grid correction that will be
          applied to the line's shape direction. The rotation offset can be
          provided as a value in seconds or derived from an Arcade expression
          using the line's attribute fields. The updated direction populated in
          the line'sfield is the line shape direction rotated by the specified
          direction offset. Direction

        """