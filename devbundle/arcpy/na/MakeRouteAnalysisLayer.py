# Generated documentation for module arcpy.na


class MakeRouteAnalysisLayer(object):
    """
    Makes a route network analysis layer and sets its analysis properties. A route network analysis layer is useful for determining the best route between a set of network locations based on a specified network cost. The layer can be created using a local network dataset or a routing service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeRouteAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {sequence}, {time_of_day}, {time_zone}, {line_shape}, {accumulate_attributes;accumulate_attributes...}, {generate_directions_on_solve}, {time_zone_for_time_fields}, {ignore_invalid_locations})

        Makes a route network analysis layer and sets its analysis properties.
        A route network analysis layer is useful for determining the best
        route between a set of network locations based on a specified network
        cost. The layer can be created using a local network dataset or a
        routing service hosted online or in a portal.

     INPUTS:
      network_data_source (Network Dataset Layer / String):
          The network dataset or service on which the network analysis will be
          performed. Use the portal URL for a service.
      layer_name {String}:
          The name of the network analysis layer to create.
      travel_mode {String}:
          The name of the travel mode to use in the analysis. The travel mode
          represents a collection of network settings, such as travel
          restrictions and U-turn policies, that determine how a pedestrian,
          car, truck, or other medium of transportation moves through the
          network. Travel modes are defined on your network data source.An
          arcpy.na.TravelMode object and a string containing the valid JSON
          representation of a travel mode can also be used as input to the
          parameter.
      sequence {String}:
          Specifies whether the input stops must be visited in a particular
          order when calculating the optimal route. This option changes the
          route analysis from a shortest-path problem to a traveling salesperson
          problem (TSP).USE_CURRENT_ORDER-The stops will be visited in the input
          order. This
          is the default.FIND_BEST_ORDER-The stops will be reordered to find the
          optimal route.
          This option changes the route analysis from a shortest-path problem to
          a traveling salesperson problem (TSP).PRESERVE_BOTH-The first and last
          stops will be preserved by input
          order. The rest will be reordered to find the optimal
          route.PRESERVE_FIRST-The first stop will be preserved by input order.
          The
          rest will be reordered to find the optimal route.PRESERVE_LAST-The
          last stop will be preserved by input order. The rest
          will be reordered to find the optimal route.
      time_of_day {Date}:
          The start date and time for the route. Route start time is typically
          used to find routes based on the impedance attribute that varies with
          the time of the day. For example, a start time of 7:00 a.m. can be
          used to find a route that considers rush hour traffic. The default
          value for this parameter is 8:00 a.m. A date and time can be specified
          as 10/21/05 10:30 AM. If the route spans multiple days and only the
          start time is specified, the current date is used.After the solve, the
          start and end times of the route are populated in
          the output routes. These start and end times are also used when
          directions are generated. Configure your analysis to use one of
          the following special
          dates to model a day of the week or the current date instead of a
          specific, static date:
          Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-1/2/1900Wednes
          day-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-1/6/1900
      time_zone {String}:
          Specifies the time zone of the time_of_day parameter.
          LOCAL_TIME_AT_LOCATIONS-The time_of_day parameter refers to
          the time zone in which the first stop of a route is located. This is
          the default. If you are generating many routes that start in
          multiple times zones,
          the start times are staggered in coordinated universal time (UTC). For
          example, a time_of_day value of 10:00 a.m., 2 January, means a start
          time of 10:00 a.m. eastern standard time (3:00 p.m. UTC) for routes
          beginning in the eastern time zone and 10:00 a.m. central standard
          time (4:00 p.m. UTC) for routes beginning in the central time zone.
          The start times are offset by one hour in UTC.The arrival and
          departure times and dates recorded in the output Stops
          feature class will refer to the local time zone of the first stop for
          each route. UTC-The time_of_day parameter refers to
          coordinated universal
          time (UTC). Choose this option if you want to generate a route for a
          specific time, such as now, but aren't certain in which time zone the
          first stop will be located. If you are generating many routes
          spanning multiple times zones, the
          start times in UTC are simultaneous. For example, a time_of_day value
          of 10:00 a.m., 2 January, means a start time of 5:00 a.m. eastern
          standard time (10:00 a.m. UTC) for routes beginning in the eastern
          time zone and 4:00 a.m. central standard time (10:00 a.m. UTC) for
          routes beginning in the central time zone. Both routes start at 10:00
          a.m. UTC.The arrival and departure times and dates recorded in the
          output Stops
          feature class will refer to UTC.
      line_shape {String}:
          Specifies the shape type that will be used for the route features that
          are output by the analysis.ALONG_NETWORK-The output routes will have
          the exact shape of the
          underlying network sources. The output includes route measurements for
          linear referencing. The measurements increase from the first stop and
          record the cumulative impedance to reach a given position.NO_LINES-No
          shape will be generated for the output routes.STRAIGHT_LINES-The
          output route shape will be a single straight line
          between the stops.Regardless of the output shape type specified, the
          best route is
          always determined by the network impedance, never Euclidean distance.
          This means that only the route shapes are different, not the
          underlying traversal of the network.
      accumulate_attributes {String}:
          A list of cost attributes to be accumulated during analysis. These
          accumulated attributes are for reference only; the solver only uses
          the cost attribute used by the designated travel mode when solving the
          analysis.For each cost attribute that is accumulated, a
          Total_[Impedance]
          property is populated in the network analysis output features.This
          parameter is not available if the network data source is an
          ArcGIS Online service or the network data source is a service on a
          version of Portal for ArcGIS that does not support accumulation.
      generate_directions_on_solve {Boolean}:
          Specifies whether directions will be generated when running the
          analysis.DIRECTIONS-Turn-by-turn directions will be generated on
          solve. This is
          the default.NO_DIRECTIONS-Turn-by-turn directions will not be
          generated on solve.For an analysis in which generating turn-by-turn
          directions is not
          needed, using the NO_DIRECTIONS option will reduce the time it takes
          to solve the analysis.
      time_zone_for_time_fields {String}:
          Specifies the time zone that will be used to interpret the time fields
          included in the input tables, such as the fields used for time
          windows.LOCAL_TIME_AT_LOCATIONS-The dates and times in the time fields
          for the
          stop will be interpreted according to the time zone in which the stop
          is located. This is the default.UTC-The dates and times in the time
          fields for the stop refer to
          coordinated universal time (UTC).
      ignore_invalid_locations {Boolean}:
          Specifies whether invalid input locations will be ignored. Typically,
          locations are invalid if they cannot be located on the network. When
          invalid locations are ignored, the solver will skip them and attempt
          to perform the analysis using the remaining locations.SKIP-Invalid
          input locations will be ignored and only valid locations
          will be used. This is the default.HALT-All input locations will be
          used. Invalid locations will cause
          the analysis to fail.

        """