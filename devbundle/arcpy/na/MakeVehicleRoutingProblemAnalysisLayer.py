# Generated documentation for module arcpy.na


class MakeVehicleRoutingProblemAnalysisLayer(object):
    """
    Creates a vehicle routing problem (VRP) network analysis layer and sets its analysis properties. A VRP analysis layer is useful for optimizing a set of routes using a fleet of vehicles. The layer can be created using a local network dataset or a service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeVehicleRoutingProblemAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {time_units}, {distance_units}, {default_date}, {time_zone_for_time_fields}, {line_shape}, {time_window_factor}, {excess_transit_factor}, {generate_directions_on_solve}, {spatial_clustering}, {ignore_invalid_locations})

        Creates a vehicle routing problem (VRP) network analysis layer and
        sets its analysis properties. A VRP analysis layer is useful for
        optimizing a set of routes using a fleet of vehicles. The layer can be
        created using a local network dataset or a service hosted online or in
        a portal.

     INPUTS:
      network_data_source (Network Dataset Layer / String):
          The network dataset or service on which the network analysis will be
          performed. Use the portal URL for a service.
      layer_name {String}:
          The name of the VRP network analysis layer to create.
      travel_mode {String}:
          The name of the travel mode to use in the analysis. The travel mode
          represents a collection of network settings, such as travel
          restrictions and U-turn policies, that determine how a pedestrian,
          car, truck, or other medium of transportation moves through the
          network. Travel modes are defined on your network data source. An
          arcpy.na.TravelMode object and a string containing the valid JSON
          representation of a travel mode can also be used as input to the
          parameter.
      time_units {String}:
          Specifies the time units to be used by the temporal fields of the
          analysis layer's sublayers and tables (network analysis classes). This
          value does not need to match the units of the time cost
          attribute.Minutes-The time units will be minutes. This is the
          default.Seconds-The time units will be seconds.Hours-The time units
          will be hours.Days-The time units will be days.
      distance_units {String}:
          Specifies the distance units to be used by the distance fields of the
          analysis layer's sublayers and tables (network analysis classes). This
          value does not need to match the units of the optional distance cost
          attribute.Miles-The distance units will be miles. This is the
          default.Kilometers-The distance units will be kilometers.Feet-The
          distance units will be feet.Yards-The distance units will be
          yards.Meters-The distance units will be meters.Inches-The distance
          units will be inches.Centimeters-The distance units will be
          centimeters.Millimeters-The distance units will be
          millimeters.Decimeters-The distance units will be
          decimeters.NauticalMiles-The distance units will be nautical miles.
      default_date {Date}:
          The implied date for time field values that don't have a date
          specified with the time. If a time field for an order object, such as,
          has a time-only value, the date is assumed to be the default date. The
          default date has no effect on time field values that already have a
          date. TimeWindowStart        Configure your analysis to use one
          of the following special
          dates to model a day of the week or the current date instead of a
          specific, static date:
          Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-1/2/1900Wednes
          day-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-1/6/1900
      time_zone_for_time_fields {String}:
          Specifies the time zone to be used for the input date-time fields
          supported by the tool.LOCAL_TIME_AT_LOCATIONS-The date-time values
          associated with the
          orders or depots will be in the time zone in which the orders and
          depots are located. For routes, the date-time values are based on the
          time zone in which the starting depot for the route is located. If a
          route does not have a starting depot, all orders and depots across all
          the routes must be in a single time zone. For breaks, the date-time
          values are based on the time zone of the routes. This is the
          default.UTC-The date-time values associated with the orders or depots
          will be
          in coordinated universal time (UTC) and are not based on the time zone
          in which the orders or depots are located.Specifying the date-time
          values in UTC is useful if you do not know
          the time zone in which the orders or depots are located or when you
          have orders and depots in multiple time zones and you want all the
          date-time values to start simultaneously. The UTC option is applicable
          only when your network dataset defines a time zone attribute.
          Otherwise, all the date-time values are treated as the time zone
          corresponding to that location.
      line_shape {String}:
          Specifies the shape type that will be used for the route features that
          are output by the analysis.ALONG_NETWORK-The output routes will have
          the exact shape of the
          underlying network sources. The output includes route measurements for
          linear referencing. The measurements increase from the first stop and
          record the cumulative impedance to reach a given position.NO_LINES-No
          shape will be generated for the output routes.
          STRAIGHT_LINES-The output route shape will be a single
          straight line between the stops. This option is not available
          if the selected network data source is a
          service.Regardless of the output shape type specified, the best route
          is
          always determined by the network impedance, never Euclidean distance.
          This means that only the route shapes are different, not the
          underlying traversal of the network.
      time_window_factor {String}:
          Specifies the importance of honoring time windows without causing
          violations. A time window violation occurs when a route arrives at an
          order, depot, or break after a time window has closed. The violation
          is the interval between the end of the time window and the arrival
          time of a route. High-The solver searches for a solution that
          minimizes time
          window violations at the expense of increasing the overall travel
          time. Choose this setting if arriving on time at orders is more
          important than minimizing the overall solution cost. This may be the
          case if you are meeting customers at your orders and you don't want to
          inconvenience them with late arrivals (another option is to use rigid
          time windows that cannot be violated). Given other
          constraints of a vehicle routing problem, it may
          be impossible to visit all the orders within their time windows. In
          this case, even asetting may produce violations.
          HighMedium-The solver searches for a balance between meeting time
          windows
          and reducing the overall solution cost. This is the default.Low-The
          solver searches for a solution that minimizes overall travel
          time, regardless of time windows. Choose this setting if respecting
          time windows is less important than reducing the overall solution
          cost. You may want to use this setting if you have a growing backlog
          of service requests. For the purpose of servicing more orders in a day
          and reducing the backlog, you can choose this setting even though
          customers may be inconvenienced with your fleet's late arrivals.
      excess_transit_factor {String}:
          Specifies the importance of reducing excess transit time. Excess
          transit time is the amount of time exceeding the time required to
          travel directly between paired orders. The excess time results from
          breaks or travel to other orders or depots between visits to the
          paired orders. This parameter is only relevant if you're using Order
          Pairs.High-The solver searches for a solution with less excess transit
          time
          between paired orders at the expense of increasing the overall travel
          costs. Use this setting if you are transporting people between paired
          orders and you want to shorten their ride time. This is characteristic
          of taxi services.Medium-The solver searches for a balance between
          reducing excess
          transit time and reducing the overall solution cost. This is the
          default.Low-The solver searches for a solution that minimizes overall
          solution
          cost, regardless of excess transit time. This setting is commonly used
          with courier services. Since couriers transport packages as opposed to
          people, ride time is not as important. Using this setting allows
          couriers to service paired orders in the proper sequence and minimize
          the overall solution cost.
      generate_directions_on_solve {Boolean}:
          Specifies whether directions will be generated.DIRECTIONS-Turn-by-turn
          directions will be generated on solve. This is
          the default.NO_DIRECTIONS-Turn-by-turn directions will not be
          generated on solve.
      spatial_clustering {Boolean}:
          Specifies whether spatial clustering will be used.CLUSTER-The orders
          assigned to an individual route will be spatially
          clustered. Clustering orders tends to keep routes in smaller areas and
          reduce how often route lines intersect one another; however,
          clustering can increase overall travel times. This is the
          default.NO_CLUSTER-The solver will not prioritize spatially clustering
          orders
          and the route lines may intersect. Use this option if route zones are
          specified.
      ignore_invalid_locations {Boolean}:
          Specifies whether invalid input locations will be ignored.SKIP-Invalid
          input locations will be ignored so that the analysis will
          succeed using only valid locations.HALT-Invalid locations will not be
          ignored and will cause the analysis
          to fail. This is the default.

        """