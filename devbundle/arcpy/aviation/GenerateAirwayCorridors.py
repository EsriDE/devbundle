# Generated documentation for module arcpy.aviation


class GenerateAirwayCorridors(object):
    """
    Simplifies the creation of airway corridors and flares for specified ATS routes.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAirwayCorridors_aviation(in_features, enroute_information_table, designated_points, target_airspace_area_features, {floors_table}, {route_types;route_types...}, {flare_angle}, {min_distance}, {changeover_points})

        Simplifies the creation of airway corridors and flares for specified
        ATS routes.

     INPUTS:
      in_features (Feature Layer):
          The input route segment features (polyline) for which corridors and
          flares will be created.
      enroute_information_table (Table View):
          The table containing route information records that describe
          airways composed of one or more route segment polylines. Each record
          provides information such as theandattributes. Route
          lengthDoglegpoint_Id
      designated_points (Feature Layer):
          The feature class containing point features that start or end route
          segment features.
      target_airspace_area_features (Feature Layer):
          The feature class that will be used to store the generated corridor
          and flare features.
      floors_table {Table View}:
          The table containing airway floor descriptions that will be used to
          split the corridors and flares created for the route.
      route_types {String}:
          The route types that will have flares created. All route types will
          have corridors created, regardless of selection.
      flare_angle {Double}:
          The angle in degrees that will be used to create flares for routes.
      min_distance {Double}:
          The minimum distance or length in nautical miles for a route to have a
          flare created.
      changeover_points {Feature Layer}:
          The feature class containing change over points for routes.

        """