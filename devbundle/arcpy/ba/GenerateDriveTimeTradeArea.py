# Generated documentation for module arcpy.ba


class GenerateDriveTimeTradeArea(object):
    """
    Creates a feature class of trade areas around point features based on travel time and distance.
    """

    @property
    def description(self) -> str:
        return """

        GenerateDriveTimeTradeArea_ba(in_features, out_feature_class, distance_type, {distances;distances...}, {units}, {id_field}, {dissolve_option}, {remove_overlap}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance}, {polygon_detail}, {input_method}, {expression})

        Creates a feature class of trade areas around point features based on
        travel time and distance.

     INPUTS:
      in_features (Feature Layer):
          The input point feature layer.
      distance_type (String):
          The method of travel that will be used for drive time calculation.
      distances {Double}:
          The distances that will be used for drive time calculations.
      units {String}:
          The units that will be used for the distance values. The default value
          is miles.
      id_field {Field}:
          A unique ID field for existing facilities.
      dissolve_option {String}:
          Specifies whether overlapping or nonoverlapping service areas for a
          single location will be used when multiple distances are
          specified.OVERLAP-Each polygon will include the area reachable from
          the
          facility up to the distance value. This is the default.SPLIT-Each
          polygon will include only the area between consecutive
          distance values.
      remove_overlap {Boolean}:
          Specifies whether overlapping concentric rings will be created or
          overlap will be removed from multiple locations in relation to one
          another.REMOVE_OVERLAP-Polygons will be split and the overlap between
          output
          features will be removed.KEEP_OVERLAP-Output features will be created
          with overlap. This is the
          default.
      travel_direction {String}:
          Specifies the direction of travel that will be used between stores and
          customers.TOWARD_STORES-The direction of travel will be from customers
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
          The maximum distance that input points can be from the network. Points
          located beyond the search tolerance will be excluded from
          processing.This parameter requires a distance value and units for the
          tolerance.
          The default value is 5000 meters.
      polygon_detail {String}:
          Specifies the level of detail that will be used for the output drive
          time polygons.STANDARD-Polygons with a standard level of detail will
          be created.
          This is the default.GENERALIZED-Generalized polygons will be created
          using the hierarchy
          present in the network data source to produce results quickly.HIGH-
          Polygons with a high level of detail will be created for
          applications in which precise results are important.
      input_method {String}:
          Specifies the type of value that will be used for each drive
          time.VALUES-A constant value will be used (all trade areas will be the
          same
          size). This is the default.EXPRESSION-The values from a field or an
          expression will be used
          (trade areas can be different sizes).
      expression {SQL Expression}:
          A fields-based expression used to calculate drive time.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the drive time polygons.

        """