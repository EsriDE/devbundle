# Generated documentation for module arcpy.ba


class GenerateApproximateDriveTimes(object):
    """
    Creates trade areas that approximate the size, shape, and area of existing polygons using available routes from the selected distance type.
    """

    @property
    def description(self) -> str:
        return """

        GenerateApproximateDriveTimes_ba(in_features, out_feature_class, distance_type, {units}, {in_stores_layer}, {store_id_field}, {link_field}, {iterations_limit}, {minimum_step}, {target_percent_diff}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance}, {polygon_detail})

        Creates trade areas that approximate the size, shape, and area of
        existing polygons using available routes from the selected distance
        type.

     INPUTS:
      in_features (Feature Layer):
          The input polygon feature layer.
      distance_type (String):
          The method of travel used to create the output polygons.
      units {String}:
          The distance units to be used with the threshold values.
      in_stores_layer {Feature Layer}:
          A point layer that will be used as the starting point for creating
          network service areas.
      store_id_field {Field}:
          The ID that uniquely identifies each in_stores_layer point.
      link_field {Field}:
          The ID that uniquely identifies each in_features point.
      iterations_limit {Long}:
          The maximum number of drive times that can be used to find the optimal
          threshold limit.
      minimum_step {Double}:
          The minimum increment distance or time-for example, 1 mile or 1
          min-that will be used between iterations to expand until the threshold
          is reached.
      target_percent_diff {Double}:
          The maximum difference between the target value and threshold value
          when determining the threshold drive time, for example, 5 percent. The
          default value is 5.
      travel_direction {String}:
          Specifies the direction of travel for output polygon
          creation.TOWARD_STORES-The direction of travel will be from customers
          to
          stores. This is the default.AWAY_FROM_STORES-The direction of travel
          will be from stores to
          customers.
      time_of_day {Date}:
          The time and date that will be used when calculating distance.
      time_zone {String}:
          Specifies the time zone that will be used for the time_of_day
          parameter.TIME_ZONE_AT_LOCATION-The time zone in which the territories
          are
          located will be used. This is the default.UTC-Coordinated universal
          time (UTC) will be used.
      search_tolerance {Linear Unit}:
          The maximum distance that input points can be from the network.The
          default value is 5000 meters.
      polygon_detail {String}:
          Specifies the level of detail that will be used for the output drive
          time polygons.STANDARD-Polygons with a standard level of detail will
          be created.
          This is the default.GENERALIZED-Generalized polygons will be created
          using the hierarchy
          present in the network data source to produce results
          quickly.HIGH-Polygons with a high level of detail will be created for
          applications in which precise results are important.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the drive time polygons.

        """