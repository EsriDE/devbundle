# Generated documentation for module arcpy.na


class MakeLastMileDeliveryAnalysisLayer(object):
    """
    Creates a last mile delivery network analysis layer and sets its analysis properties. A last mile delivery analysis layer is useful for optimizing a set of routes using a fleet of vehicles. The layer can be created using a local network dataset or a service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeLastMileDeliveryAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {time_units}, {distance_units}, {earliest_route_start_date}, {earliest_route_start_time}, {max_route_total_time}, {time_zone_for_time_fields}, {sequence_gap}, {ignore_invalid_order_locations}, {line_shape}, {generate_directions_on_solve})

        Creates a last mile delivery network analysis layer and sets its
        analysis properties. A last mile delivery analysis layer is useful for
        optimizing a set of routes using a fleet of vehicles. The layer can be
        created using a local network dataset or a service hosted online or in
        a portal.

     INPUTS:
      network_data_source (Network Dataset Layer / String):
          The network dataset or service on which the network analysis will be
          performed. Use the portal URL for a service.The network must have at
          least one travel mode, one cost attribute
          with time units, and one cost attribute with distance units, as well
          as a time zone attribute.
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
          parameter.The travel mode's impedance attribute must have units of
          time.
      time_units {String}:
          Specifies the time units that will be used by the analysis layer's
          properties and the temporal fields of the analysis layer's sublayers
          and tables (network analysis classes). This value does not need to
          match the units of the time cost attribute.Minutes-The time units will
          be minutes. This is the
          default.Seconds-The time units will be seconds.Hours-The time units
          will be hours.Days-The time units will be days.
      distance_units {String}:
          Specifies the distance units that will be used by the analysis layer's
          properties and the distance fields of the analysis layer's sublayers
          and tables (network analysis classes). This value does not need to
          match the units of the optional distance cost attribute.Miles-The
          distance units will be miles. This is the
          default.Kilometers-The distance units will be kilometers.Feet-The
          distance units will be feet.Yards-The distance units will be
          yards.Meters-The distance units will be meters.Inches-The distance
          units will be inches.Centimeters-The distance units will be
          centimeters.Millimeters-The distance units will be
          millimeters.Decimeters-The distance units will be
          decimeters.NauticalMiles-The distance units will be nautical miles.
          The Inches, Centimeters, Millimeters, and Decimeters options
          are not available when the network data source is a service.
      earliest_route_start_date {Date}:
          The default earliest start date for routes. This date is used
          for all routes for which thefield in the Routes sublayer is null. When
          no parameter value is specified, all rows in the Routes sublayer must
          specify a value in thefield.
          EarliestStartDateEarliestStartDateSpecify this parameter value using a
          datetime.date object. Although the other Network Analyst
          solvers allow you to use
          special dates to model a day of the week or the current date instead
          of a specific, static date, the last mile delivery solver does not.
          You must choose a specific date.
      earliest_route_start_time {Date}:
          The default earliest start time for routes. This time of day
          is used for all routes for which thefield in the Routes sublayer is
          null. When no parameter value is specified, all rows in the Routes
          sublayer must specify a value in thefield.
          EarliestStartTimeEarliestStartTimeSpecify this parameter value using a
          datetime.time object.
      max_route_total_time {Double}:
          The maximum allowed total time for each route. The value can be any
          positive number. The value is used for all routes for which
          thefield in the
          Routes sublayer is null. When no parameter value is specified, all
          rows in the Routes sublayer must specify a value in thefield.
          MaxTotalTimeMaxTotalTimeThe value is interpreted in the units
          specified in the time_units
          parameter.
      time_zone_for_time_fields {String}:
          Specifies the time zone that will be used for the input date-time
          fields supported by the tool.LOCAL_TIME_AT_LOCATIONS-The date-time
          values associated with the
          orders or depots will be in the time zone in which the orders and
          depots are located. For routes, the date-time values are based on the
          time zone in which the starting depot for the route is located. If a
          route does not have a starting depot, all orders and depots across all
          the routes must be in a single time zone. This is the default.UTC-The
          date-time values associated with the orders, depots, and
          routes will be in coordinated universal time (UTC) and are not based
          on the time zone in which the orders or depots are located.Specifying
          the date-time values in UTC is useful if you do not know
          the time zone in which the orders or depots are located or when you
          have orders and depots in multiple time zones and you want all the
          date-time values to start simultaneously.
      sequence_gap {Long}:
          The gap in numerical values to leave in thefield in the Orders
          sublayer between adjacent orders when the analysis is solved. The
          value acts as a multiplier for the actual sequence of orders on each
          route. For example, if the gap is 5, the first order on the route will
          have afield value of 5, the second order on the route will have afield
          value of 10, the third 15, and so on. This parameter helps support
          inserting orders after the initial route plan has been created because
          the new orders can be inserted into the sequence gaps.
          SequenceSequenceSequenceThe value must be a positive integer. The
          default is 1. The first time the analysis is solved, thefield
          values will be
          populated with sequential values using the designated sequence gap. On
          subsequent solves of the same analysis, thefield values of existing
          orders will be maintained, and new orders will be inserted into the
          gaps using available integer values for thefield that are not in use
          by other orders. If the sequence gap is set to 1, the sequence values
          will always be updated to contiguous values for every solve.
          SequenceSequenceSequence
      ignore_invalid_order_locations {Boolean}:
          Specifies whether invalid order locations will be ignored.SKIP-Invalid
          order locations will be ignored so that the analysis will
          succeed using only valid locations.HALT-Invalid order locations will
          not be ignored and will cause the
          analysis to fail. This is the default.
      line_shape {String}:
          Specifies the shape type that will be used for the route features that
          are output by the analysis.ALONG_NETWORK-The output routes will have
          the exact shape of the
          underlying network sources. The output includes route measurements for
          linear referencing. The measurements increase from the first stop and
          record the cumulative impedance to reach a given position.NO_LINES-No
          shape will be generated for the output routes.
          STRAIGHT_LINES-The output route shape will be a single
          straight line between the stops. This is the
          default.Regardless of the output shape type specified, the best route
          is
          always determined by the network impedance, never Euclidean distance.
          This means that only the route shapes are different, not the
          underlying traversal of the network.
      generate_directions_on_solve {Boolean}:
          Specifies whether directions will be generated when the analysis is
          solved.DIRECTIONS-Turn-by-turn directions will be generated on
          solve.NO_DIRECTIONS-Turn-by-turn directions will not be generated on
          solve.
          This is the default.

        """