# Generated documentation for module arcpy.cartography


class CalculateUTMZone(object):
    """
    Calculates the UTM zone of each feature based on the center point and stores this spatial reference string in a specified field. This field can be used with a spatial map series to update the spatial reference to the correct UTM zone for each map.
    """

    @property
    def description(self) -> str:
        return """

        CalculateUTMZone_cartography(in_features, in_field)

        Calculates the UTM zone of each feature based on the center point and
        stores this spatial reference string in a specified field. This field
        can be used with a spatial map series to update the spatial reference
        to the correct UTM zone for each map.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer.
      in_field (Field):
          The string field that stores the spatial reference string for the
          coordinate system. The field should have sufficient length (more than
          600 characters) to hold the spatial reference string.

        """