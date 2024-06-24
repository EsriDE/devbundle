# Generated documentation for module arcpy.locref


class EnableStationingFields(object):
    """
    Enables or modifies stationing fields so that you can manage stationing information for the registered LRS event.
    """

    @property
    def description(self) -> str:
        return """

        EnableStationingFields_locref(in_feature_class, {station_field}, {back_station_field}, {station_direction_field}, {station_measure_units}, {decreasing_station_values})

        Enables or modifies stationing fields so that you can manage
        stationing information for the registered LRS event.

     INPUTS:
      in_feature_class (Feature Layer):
          An existing event feature class or feature layer that is registered to
          an LRS.
      station_field {Field}:
          The field that will be used as the starting reference station.
      back_station_field {Field}:
          The field that will be used as the back station.
      station_direction_field {Field}:
          The field that will be used to indicate the direction of increasing
          stations, either increasing toward the direction of calibration of the
          route or away from it.
      station_measure_units {String}:
          Specifies the measure units that will be used for stationing.MILES-The
          unit of measure will be miles. This is the
          default.INCHES-The unit of measure will be inches.FEET-The unit of
          measure will be feet.YARDS-The unit of measure will be
          yards.NAUTICAL_MILES-The unit of measure will be nautical
          miles.INTFEET-The unit of measure will be international
          feet.MILLIMETERS-The unit of measure will be
          millimeters.CENTIMETERS-The unit of measure will be
          centimetersMETERS-The unit of measure will be meters.KILOMETERS-The
          unit of measure will be kilometers.DECIMETERS-The unit of measure will
          be decimeters.
      decreasing_station_values {String}:
          A comma-separated list of user-provided values.

        """