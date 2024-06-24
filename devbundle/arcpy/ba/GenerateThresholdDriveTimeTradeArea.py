# Generated documentation for module arcpy.ba


class GenerateThresholdDriveTimeTradeArea(object):
    """
    Creates a feature class of network distance trade areas that expand around point features until criteria is reached.
    """

    @property
    def description(self) -> str:
        return """

        GenerateThresholdDriveTimeTradeArea_ba(in_features, out_feature_class, threshold_variable, {threshold_values;threshold_values...}, distance_type, {units}, {id_field}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance}, {polygon_detail}, {iterations_limit}, {minimum_step}, {target_percent_diff}, {input_method}, {expression})

        Creates a feature class of network distance trade areas that expand
        around point features until criteria is reached.

     INPUTS:
      in_features (Feature Layer):
          The input point feature layer.
      threshold_variable (String):
          The selected Business Analyst dataset variable to which the threshold
          value will be applied.Threshold variables must be numeric. No other
          statistic type is
          supported.
      threshold_values {Double}:
          The threshold variable value that will determine the size of the
          output rings. The rings will expand until they contain the threshold
          value of the selected variable.
      distance_type (String):
          The method of travel that will be used to create the output polygons.
      units {String}:
          The distance units that will be used with the threshold values.
      id_field {Field}:
          The ID that uniquely identifies each input point and is included in
          the output as an attribute.
      travel_direction {String}:
          Specifies the direction of travel that will be used for output polygon
          creation.TOWARD_STORES-The direction of travel will be from customers
          to
          stores. This is the default.AWAY_FROM_STORES-The direction of travel
          will be from stores to
          customers.
      time_of_day {Date}:
          The time and date that will be used when calculating distance.
      time_zone {String}:
          Specifies the time zone that will be used for theparameter.
          Time of DayTIME_ZONE_AT_LOCATION-The time zone in which the
          territories are
          located will be used. This is the default.UTC-Coordinated universal
          time (UTC) will be used.
      search_tolerance {Linear Unit}:
          The maximum distance that input points can be from the network.The
          default value is 5,000 meters.
      polygon_detail {String}:
          Specifies the level of detail that will be used for the output drive
          time polygons.STANDARD-Polygons with a standard level of detail will
          be created.
          This is the default.GENERALIZED-Generalized polygons will be created
          using the hierarchy
          present in the network data source to produce results
          quickly.HIGH-Polygons with a high level of detail will be created for
          applications in which precise results are important.
      iterations_limit {Long}:
          Restricts the number of drive times that can be used to find the
          optimal threshold limit.
      minimum_step {Double}:
          The minimum distance between one threshold area candidate and the next
          as the model approaches the threshold value to prevent infinite
          iterations.
      target_percent_diff {Double}:
          The maximum percentage difference between the target value and
          threshold value that will be used when determining the threshold drive
          time, for example, 5 percent. The default value is 5.
      input_method {String}:
          Specifies the type of value that will be used for each drive
          time.VALUES-A constant value will be used (all trade areas will be the
          same
          size). This is the default.EXPRESSION-The values from a field or an
          expression will be used
          (trade areas can be different sizes).
      expression {SQL Expression}:
          A fields-based expression that will be used to calculate drive time.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the drive time polygons.

        """