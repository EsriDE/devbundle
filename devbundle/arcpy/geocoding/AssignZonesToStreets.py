# Generated documentation for module arcpy.geocoding


class AssignZonesToStreets(object):
    """
    Assigns left and right administrative zone values-such as neighborhood, city, metro, or postal code-to street line segments for street addresses.
    """

    @property
    def description(self) -> str:
        return """

        AssignZonesToStreets_geocoding(in_street_features, zone_features, zone_fields;zone_fields..., out_streets, {tolerance})

        Assigns left and right administrative zone values-such as
        neighborhood, city, metro, or postal code-to street line segments for
        street addresses.

     INPUTS:
      in_street_features (Feature Layer):
          The input street feature class or layer.
      zone_features (Feature Layer):
          The input administrative zone feature class or layer.
      zone_fields (Field):
          The fields from the zone_features parameter value that will be
          assigned to the in_street_features parameter value.
      tolerance {Double}:
          The tolerance of the in_street_features parameter value that increases
          the width of the line feature on both sides to determine which
          zone_features values will be on the left and the right to account for
          data and digitization quality issues.The default value is 10 meters.

     OUTPUTS:
      out_streets (Dataset):
          The output street feature class or layer that contains the
          administrative zone assigned to the left and right sides of the street
          segment based on the direction the line was digitized.

        """