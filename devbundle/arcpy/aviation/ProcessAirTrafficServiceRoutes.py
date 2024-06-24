# Generated documentation for module arcpy.aviation


class ProcessAirTrafficServiceRoutes(object):
    """
    Identifies overlapping Air Traffic Service (ATS) routes and calculates fields in the Target Cartographic Route Features to aid in cartographic display.
    """

    @property
    def description(self) -> str:
        return """

        ProcessAirTrafficServiceRoutes_aviation(in_route_features, target_carto_route_features, aoi_features, preference_table, preference)

        Identifies overlapping Air Traffic Service (ATS) routes and calculates
        fields in the Target Cartographic Route Features to aid in
        cartographic display.

     INPUTS:
      in_route_features (Feature Layer):
          The polyline feature layer containing ATS route data. This data will
          be used to update features in the target_carto_route_features
          parameter value.
      target_carto_route_features (Feature Layer):
          The cartographic feature layer containing ATS routes. The attributes
          of these features will be modified to simplify the display of
          overlapping routes.
      aoi_features (Feature Layer):
          The polygon feature class containing AOI features.
      preference_table (Table View):
          The table of preferences that control how ATS routes will be
          processed.
      preference (String):
          The name of a preference from the preference_table parameter. The
          preference controls how ATS routes will be processed.

        """