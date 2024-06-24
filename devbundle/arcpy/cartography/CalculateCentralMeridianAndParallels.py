# Generated documentation for module arcpy.cartography


class CalculateCentralMeridianAndParallels(object):
    """
    Calculates the central meridian and optional standard parallels based on the center point of a feature's extent; stores this coordinate system as a spatial reference string in a specified text field; and repeats this for a set, or subset, of features. This field can be used with a spatial map series to update the data frame coordinate system for each page.
    """

    @property
    def description(self) -> str:
        return """

        CalculateCentralMeridianAndParallels_cartography(in_features, in_field, {standard_offset})

        Calculates the central meridian and optional standard parallels based
        on the center point of a feature's extent; stores this coordinate
        system as a spatial reference string in a specified text field; and
        repeats this for a set, or subset, of features. This field can be used
        with a spatial map series to update the data frame coordinate system
        for each page.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer.
      in_field (Field):
          The text field where the coordinate system string will be stored.
      standard_offset {Double}:
          The percentage of the height of the input feature used to offset the
          standard parallels from the center latitude of the input feature. The
          default is 25 percent or 0.25. Negative values and values greater than
          1 are acceptable inputs.

        """