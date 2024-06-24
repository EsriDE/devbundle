# Generated documentation for module arcpy.na


class AddVehicleRoutingProblemRoutes(object):
    """
    Creates routes in a Vehicle Routing Problem (VRP) layer or Last Mile Delivery layer. This tool will append rows to the Routes sublayer and can add rows with specific settings while creating a unique name field.
    """

    @property
    def description(self) -> str:
        return """

        AddVehicleRoutingProblemRoutes_na(in_vrp_layer, number_of_routes, route_name_prefix, {start_depot_name}, {end_depot_name}, {earliest_start_time}, {latest_start_time}, {max_order_count}, {capacities;capacities...}, {route_constraints;route_constraints...}, {costs;costs...}, {additional_route_time;additional_route_time...}, {append_to_existing_routes}, {date_and_time;date_and_time...})

        Creates routes in a Vehicle Routing Problem (VRP) layer or Last Mile
        Delivery layer. This tool will append rows to the Routes sublayer and
        can add rows with specific settings while creating a unique name
        field.

     INPUTS:
      in_vrp_layer (Network Analyst Layer):
          The  Vehicle Routing Problem or Last Mile Delivery analysis layer to
          which routes will be added.
      number_of_routes (Long):
          The number of routes that will be added.
      route_name_prefix (String):
          A qualifier that will be added to the title of every route layer item.
          For example, a route name prefix of WeekdayRoute would be used as the
          starting text for every route's name with the object ID appended to it
          (WeekdayRoute1, WeekdayRoute2, and so on).
      start_depot_name {String}:
          The name of the starting depot for the route.If this value is null,
          the route will begin from the first order
          assigned. Omitting the start depot is useful when the vehicle's
          starting location is unknown or irrelevant to the problem.For Vehicle
          Routing Problem layers, when this value is null, the
          end_depot_name parameter value cannot also be null. Both start and end
          depots can be null for Last Mile Delivery layers.Virtual start depots
          are not allowed if orders or depots are in
          multiple time zones.
      end_depot_name {String}:
          The name of the ending depot for the route.If this value is null, the
          route will end at the last order assigned.For Vehicle Routing Problem
          layers, when this value is null, the
          start_depot_name parameter value cannot also be null. Both start and
          end depots can be null for Last Mile Delivery layers.
      earliest_start_time {Date}:
          The earliest allowable start time for the route in a Vehicle Routing
          Problem layer. This parameter is used by the solver in
          conjunction with the
          time window of the starting depot provided in the Depots sublayer by
          thefield, for determining feasible route start times. This parameter
          has a default time-only value of 8:00:00 a.m., which is interpreted as
          8:00:00 a.m. on the date provided by the Default Date property of the
          analysis layer. If no value is specified, the default value is used.
          TimeWindowStartThis parameter is not applicable and its value is
          ignored if the input
          layer is a Last Mile Delivery layer.
      latest_start_time {Date}:
          The latest allowable start time for the route in a Vehicle Routing
          Problem layer.This parameter has a default time-only value of 10:00:00
          a.m., which
          is interpreted as 10:00:00 a.m. on the date provided by the Default
          Date property of the analysis layer. If no value is specified, the
          default value is used.This parameter is not applicable and its value
          is ignored if the input
          layer is a Last Mile Delivery layer.
      max_order_count {Long}:
          The maximum allowable number of orders on the route. The default value
          is 30 for Vehicle Routing Problem layers and null for Last Mile
          Delivery layers. If no value is specified, the default value is used.
      capacities {Value Table}:
          The maximum amount (volume, weight, quantity, and so on) that can be
          carried by the vehicle. A null value is the same as zero. A maximum of
          nine capacity fields are allowed, but use only the number necessary to
          model the needs of the vehicles.
      route_constraints {Value Table}:
          The constraints that will be placed on routes to limit total
          time, total travel time, and total distance. Max Total Time-The
          maximum allowable route duration. The route
          duration includes travel times as well as service and wait times at
          orders, depots, and breaks. Max Total Travel Time-The maximum
          allowable travel time for
          the route. The travel time includes only the time spent driving on the
          network and does not include service or wait times. This field value
          can't be larger than the field value. MaxTotalTimeMax Total
          Distance-The maximum allowable travel distance for the
          route.
      costs {Value Table}:
          The costs that may be incurred by the route in a VRP solution.Fixed
          Cost-A fixed monetary cost that is incurred only if the route is
          used in a solution (that is, it has orders assigned to it).Cost Per
          Unit Time-The monetary cost incurred per unit of work time
          for the total route duration, including travel times and service and
          wait times at orders, depots, and breaks. The default is 1.Cost Per
          Unit Distance-The monetary cost incurred per unit of distance
          traveled for the route length (total travel distance).Overtime Start
          Time-The duration of regular work time before overtime
          computation begins. Cost Per Unit Overtime-The monetary cost
          incurred per time
          unit of overtime work. This field can contain null values; a null
          value indicates that thevalue is the same as thevalue. Cost
          Per Unit OvertimeCost Per Unit Time
      additional_route_time {Value Table}:
          Additional route time options. Start Depot Service
          Time-The service time at the starting depot. This
          can be used to model the time spent loading the vehicle.End Depot
          Service Time-The service time at the ending depot. This can
          be used to model the time spent unloading the vehicle.
          Arrive/Depart Delay-The amount of travel time needed to
          accelerate the vehicle to normal travel speeds, decelerate it to a
          stop, and move it off and on the network (for example, in and out of
          parking). By including anvalue, the solver is deterred from sending
          many routes to service physically coincident orders.
          Arrive/Depart Delay
      append_to_existing_routes {Boolean}:
          Specifies whether new routes will be appended to the existing routes
          attribute table.APPEND-New routes will be appended to the existing set
          in the routes
          attribute table. This is the default.CLEAR-Existing routes will be
          deleted and replaced with new routes.
      date_and_time {Value Table}:
          Additional date and time options for a Last Mile Delivery
          layer. Earliest Route Start Date-The earliest start date for
          added routes. If
          this property is not specified, the routes will use the layer's
          default earliest route start date.Earliest Route Start Time-The
          earliest start time of day for added
          routes. If this property is not specified, the routes will use the
          layer's default earliest route start time.Route Start
          Flexibility-Indicates how long after the earliest allowed
          route start time the route can start. The value can be null or zero,
          which means that there is no flexibility in the starting time, or a
          positive number. Specify the value in the input layer's time units.
          Specify theproperty using a datetime.date object and
          theproperty using a datetime.time object. Earliest Route Start
          DateEarliest Route Start TimeThis parameter is not applicable and its
          value is ignored if the input
          layer is a Vehicle Routing Problem layer.

        """