# Generated documentation for module arcpy.defense


class NumberFeatures(object):
    """
    Adds a sequential number to a new or existing field of a set of input features.
    """

    @property
    def description(self) -> str:
        return """

        NumberFeatures_defense(in_features, field_to_number, {in_area}, {spatial_sort_method}, {new_field_type}, {starting_number}, {increment_by}, {center_point}, {add_distance_and_bearing})

        Adds a sequential number to a new or existing field of a set of input
        features.

     INPUTS:
      in_features (Feature Set):
          The input features that will be numbered.
      field_to_number (Field):
          The input field that will be numbered. The field can be an existing
          short, long, or text field, or a new field.
      in_area {Feature Set}:
          The area that will limit the features to number; only features within
          this area will be numbered.
      spatial_sort_method {String}:
          Specifies how features will be spatially sorted for the purpose of
          numbering. Features are not reordered in the table.UR-Features will be
          sorted starting at the upper right corner. This is
          the default.UL-Features will be sorted starting at the upper left
          corner.LR-Features will be sorted starting at the lower right
          corner.LL-Features will be sorted starting at the lower left
          corner.PEANO-Features will be sorted using a space-filling curve
          algorithm,
          also known as a Peano curve.CENTER-Features will be sorted starting
          from a center point (the mean
          center will be used if no center is provided).CLOCKWISE-Features will
          be sorted starting from a center point and
          moving clockwise.COUNTERCLOCKWISE-Features will be sorted starting
          from a center point
          and moving counterclockwise.NONE-No spatial sort will be used. The
          same order as the feature class
          will be used.
      new_field_type {String}:
          Specifies the field type that will be used for the new field. This
          parameter is only used when the field name does not exist in the input
          table.SHORT-The field type will be short. This is the default.LONG-The
          field
          type will be long.TEXT-The field type will be text.
      starting_number {Long}:
          The value that will be used to begin numbering.
      increment_by {Long}:
          The value that will be used to increment by from the previous value.
      center_point {Feature Set}:
          The center point that will be used to sort and number features.
      add_distance_and_bearing {Boolean}:
          Specifies whether fields will be added to the output for distance and
          bearing to a center point.DONT_ADD_DISTANCE-No distance or bearing
          fields will be added to the
          output. This is the default. ADD_DISTANCE-andfields will be
          added to the output.
          DIST_TO_CENTERANGLE_TO_CENTER

        """