# Generated documentation for module arcpy.aviation


class GenerateAirspaceAreas(object):
    """
    Generates AirspaceArea features from Airspace features.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAirspaceAreas_aviation(in_airspace_features, target_airspace_area_features, aoi_features, preference_table, preference, {derived_airspace_part_features}, {vertical_limit_override_table})

        Generates AirspaceArea features from Airspace features.

     INPUTS:
      in_airspace_features (Feature Layer):
          The input Airspace features. These features adhere to the AIS
          geodatabase schema.
      target_airspace_area_features (Feature Layer):
          The target AirspaceArea feature class. These features adhere to the
          AIS geodatabase schema.
      aoi_features (Feature Layer):
          The area of interest boundary within which features will be processed.
      preference_table (Table View):
          The table containing the specified preferences.
      preference (String):
          The preference derived from the preference_table parameter that will
          be used to process the airspace features at the chosen altitudes..
      derived_airspace_part_features {Feature Layer}:
          The feature class that will be updated with airspace features
          derived from theparameter. Input Airspace FeaturesThe feature
          class that will be updated with airspace features derived
          from the in_airspace_features parameter.
      vertical_limit_override_table {Table View}:
          A table that overrides the vertical height values set in the
          preference table.

        """