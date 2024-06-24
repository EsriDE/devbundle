# Generated documentation for module arcpy.td


class SetTerritoryDistanceParameters(object):
    """
    Defines the type of distance calculation or distance constraints to use when creating territories.
    """

    @property
    def description(self) -> str:
        return """

        SetTerritoryDistanceParameters_td(in_territory_solution, level, {distance_type}, {units}, {max_radius}, {buffer_distance}, {min_distance}, {network_datasource}, {build_index}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance})

        Defines the type of distance calculation or distance constraints to
        use when creating territories.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution layer that will be used in the analysis.
      level (String):
          The level to which the distance parameters will be applied.
      distance_type {String}:
          Specifies the method of travel that will be used for the distance
          calculation.STRAIGHT_LINE-Straight line, or Euclidean distance, will
          be used as
          the distance measure. This is the default.When a network data source
          is selected, additional travel mode options
          will be dynamically populated. The following distance methods
          are supported:        Driving
          TimeDriving DistanceTrucking TimeTrucking DistanceWalking
          TimeWalking DistanceRural Trucking TimeRural Trucking Distance
      units {String}:
          Specifies the type of measuring units that will be used.METERS-The
          distance unit will be meters.MILES-The distance unit will
          be miles.NAUTICAL_MILES-The distance unit will be nautical
          miles.KILOMETERS-The distance unit will be kilometers.YARDS-The
          distance unit will be yards.FEET-The distance unit will be
          feet.INCHES-The distance unit will be inches.DECIMETERS-The distance
          unit will be decimeters.CENTIMETERS-The distance unit will be
          centimeters.MILLIMETERS-The distance unit will be
          millimeters.DECIMAL_DEGREES-The distance unit will be decimal
          degrees.MINUTES-The time unit will be minutes.HOURS-The time unit will
          be hours.DAYS-The time unit will be days.SECONDS-The time unit will be
          seconds.
      max_radius {Double}:
          The maximum radius of the territory.
      buffer_distance {Double}:
          The radius of the territory buffer.
      min_distance {Double}:
          The minimum distance between territory centers.
      network_datasource {Network Dataset Layer}:
          The network dataset on which the network distance calculation will be
          performed. The parameter requires a locally installed dataset.
      build_index {Boolean}:
          Specifies whether a network index will be built. A network index will
          improve performance when solving the territory solution.BUILD_INDEX-A
          network index will be built. This is the
          default.DO_NOT_BUILD_INDEX-A network index will not be built.
      travel_direction {String}:
          Specifies the direction of travel between stores and
          customers.TOWARD_STORES-Direction of travel will be from customers to
          stores.
          This is the default.AWAY_FROM_STORES-Direction of travel will be from
          stores to customers.
      time_of_day {Date}:
          The time and date that will be used when calculating distance.
      time_zone {String}:
          Specifies the time zone of the time_of_day
          parameter.TIME_ZONE_AT_LOCATION-The time zone in which the territories
          are
          located will be used. This is the default.UTC-Coordinated universal
          time (UTC) will be used.
      search_tolerance {Linear Unit}:
          The search tolerance that will be used for locating territories on the
          network. Territories that are outside the search tolerance will be
          left unlocated.This parameter requires a distance value and units for
          the tolerance.
          The default value is 5000 meters.

        """