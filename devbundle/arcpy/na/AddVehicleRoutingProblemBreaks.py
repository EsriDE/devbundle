# Generated documentation for module arcpy.na


class AddVehicleRoutingProblemBreaks(object):
    """
    Creates breaks in a Vehicle Routing Problem (VRP) layer.
    """

    @property
    def description(self) -> str:
        return """

        AddVehicleRoutingProblemBreaks_na(in_vrp_layer, {target_route}, {break_type}, {time_window_properties;time_window_properties...}, {travel_time_properties;travel_time_properties...}, {work_time_properties;work_time_properties...}, {append_to_existing_breaks})

        Creates breaks in a Vehicle Routing Problem (VRP) layer.

     INPUTS:
      in_vrp_layer (Network Analyst Layer):
          The vehicle routing problem analysis layer to which the breaks will be
          added.
      target_route {String}:
          The route for the break parameters.  If this parameter is not
          specified, breaks will be created for each existing route.
      break_type {String}:
          Specifies the type of breaks that will be taken for the current VRP
          layer. All breaks must be of the same type.TIME_WINDOW_BREAK-Breaks
          will take place during a specific time
          window. This is the default.MAXIMUM_TRAVEL_TIME_BREAK-Breaks will
          take place after a certain
          amount of travel time. These values are either the amount of time
          until the first break or the amount of time between
          breaks.MAXIMUM_WORK_TIME_BREAK-Breaks will take place after a certain
          amount
          of cumulative time. These values are an amount of elapsed time since
          the start of the route.
      time_window_properties {Value Table}:
          Specifies a time range within which the break will begin. To set up a
          time window break, use two time-of-day values. The options
          below are enabled when theparameter is set to.
          Break TypeTime Window BreakIs Paid-A Boolean value indicating whether
          the break is paid.Break
          Duration-The duration of the break. This property can't contain
          null values and has a default value of 60.Time Window Start-The start
          time of the time window.Time Window End-The end time of the time
          window.Maximum Violation Time-The maximum allowable violation time for
          a time
          window break. A time window is considered violated if the arrival time
          falls outside the time range. A zero value indicates that the time
          window cannot be violated, that is, the time window is hard. A nonzero
          value indicates the maximum delay time. For example, the break can
          begin up to 30 minutes beyond the end of its time window but the delay
          is penalized pursuant to the Time Window Violation Importance setting,
          which rates the importance of honoring time windows without causing
          violations.
      travel_time_properties {Value Table}:
          Specifies how long a person can drive before the break is required.
          The properties below are enabled when theparameter is set to.
          Break TypeMaximum Travel Time BreakIs Paid-A Boolean value indicating
          whether the break is paid.Break
          Duration-The duration of the break. This property can't contain
          null values and has a default value of 60. Maximum Travel
          Time Between Breaks-The maximum amount of
          travel time that can be accumulated before the break is taken. The
          travel time is accumulated either from the end of the previous break
          or, if a break has not yet been taken, from the start of the route.
          If this is the route's final break, Thefield also indicates
          the maximum travel time that can be accumulated from the final break
          to the end depot. MaxTravelTimeBetweenBreaks           This
          field limits how long a person can drive until a break
          is required. For example, if theparameter (time_units in Python) of
          the analysis is set to, and thefield has a value of 120, the driver
          will get a break after two hours of driving. To assign a second break
          after two additional hours of driving, the second break'sfield value
          must be 120. Time Field
          UnitsMinutesMaxTravelTimeBetweenBreaksMaxTravelTimeBetweenBreaks
          The unit for this field value is specified by theparameter
          (time_units in Python). Time Field Units
      work_time_properties {Value Table}:
          Specifies how long a person can work before a break is required.
          The properties below are enabled when theparameter is set to.
          Break TypeMaximum Work Time BreakIs Paid-A Boolean value indicating
          whether the break is paid.Break
          Duration-The duration of the break. This property can't contain
          null values and has a default value of 60. Maximum Cumulative
          Work Time-The maximum amount of work time
          that can be accumulated before the break is taken. Work time is
          accumulated from the beginning of the route. Work time is the sum of
          travel time and service times at orders, depots, and breaks. However,
          it excludes wait time, which is the time a route (or driver) spends
          waiting at an order or depot for a time window to begin.
          Thefield also indicates the maximum amount of work time
          that can be accumulated before the break is taken.
          MaxCumulWorkTime           This field limits how long a person can
          work until a break
          is required. For example, if theparameter (time_units in Python) is
          set to, thefield has a value of 120, and thefield has a value of 15,
          the driver will get a 15-minute break after 2 hours of work.
          Time Field UnitsMinutesMaxCumulWorkTimeServiceTime
          Continuing with this example, assume a second break is
          needed after 3 additional hours of work. To specify this break, you
          would enter 315 (5 hours and 15 minutes) as the second break'sfield
          value. This number includes theandfield values of the preceding break,
          along with the 3 additional hours of work time before granting the
          second break. To avoid taking maximum work time breaks prematurely,
          remember that work time is accumulated from the beginning of the route
          and it includes the service time at previously visited depots, orders,
          and breaks. MaxCumulWorkTimeMaxCumulWorkTimeServiceTime
      append_to_existing_breaks {Boolean}:
          Specifies whether new breaks will be appended to the existing breaks
          attribute table.APPEND-New breaks will be appended to the existing set
          in the breaks
          attribute table. This is the default.CLEAR-Existing breaks will be
          replaced with new breaks.

        """