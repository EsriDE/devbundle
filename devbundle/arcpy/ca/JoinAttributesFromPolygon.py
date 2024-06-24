# Generated documentation for module arcpy.ca


class JoinAttributesFromPolygon(object):
    """
    Joins attributes from input polygon features to input point features.
    """

    @property
    def description(self) -> str:
        return """

        JoinAttributesFromPolygon_ca(target_features, in_features, {fields;fields...}, {overwrite_option})

        Joins attributes from input polygon features to input point features.

     INPUTS:
      target_features (Feature Layer):
          The point features that will be updated with attributes from the
          in_features parameter value.
      in_features (Feature Layer):
          The input polygon features.
      fields {Field}:
          The fields from the input polygon features that will be appended to
          the target point features.
      overwrite_option {Boolean}:
          Specifies whether existing fields in the target_features parameter
          value that have names that match fields in the fields parameter value
          will be overwritten.OVERWRITE-The matching fields will be
          overwritten.NO_OVERWRITE-The
          existing fields will not be overwritten, and new
          fields will be generated. This is the default.

        """