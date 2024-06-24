# Generated documentation for module arcpy.analysis


class TabulateIntersection(object):
    """
    Computes the intersection between two feature classes and cross tabulates the area, length, or count of the intersecting features.
    """

    @property
    def description(self) -> str:
        return """

        TabulateIntersection_analysis(in_zone_features, zone_fields;zone_fields..., in_class_features, out_table, {class_fields;class_fields...}, {sum_fields;sum_fields...}, {xy_tolerance}, {out_units})

        Computes the intersection between two feature classes and cross
        tabulates the area, length, or count of the intersecting features.

     INPUTS:
      in_zone_features (Feature Layer):
          The features used to identify zones.
      zone_fields (Field):
          The attribute field or fields that will be used to define zones.
      in_class_features (Feature Layer):
          The features used to identify classes.
      class_fields {Field}:
          The attribute field or fields used to define classes.
      sum_fields {Field}:
          The fields that will be summed from the in_class_features parameter.
      xy_tolerance {Linear Unit}:
          The distance that determines the range in which features or their
          vertices are considered equal. By default, this is the x,y tolerance
          of the in_zone_features parameter value.Changing this parameter's
          value may cause failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.
      out_units {String}:
          Specifies the units that will be used to calculate area or length
          measurements. Setting output units when the input class features are
          points is not supported.UNKNOWN-The units will be
          unknown.KILOMETERS-The units will be
          kilometers.METERS-The units will be meters.DECIMETERS-The units will
          be decimeters.CENTIMETERS-The units will be
          centimeters.MILLIMETERS-The units will be
          millimeters.MILES_INTERNATIONAL-The units will be statute
          miles.NAUTICAL_MILES_INTERNATIONAL-The units will be international
          nautical
          miles.YARDS_INTERNATIONAL-The units will be international
          yards.FEET_INTERNATIONAL-The units will be international
          feet.INCHES_INTERNATIONAL-The units will be international
          inches.MILES-The units will be US survey miles.NAUTICAL_MILES-The
          units will be US survey nautical miles.YARDS-The units will be US
          survey yards.FEET-The units will be US survey feet.INCHES-The units
          will be US survey inches.DECIMAL_DEGREES-The units will be decimal
          degrees.POINTS-The units will be points.ARES-The units will be
          ares.SQUARE_KILOMETERS-The units will be square
          kilometers.SQUARE_METERS-The units will be square
          meters.SQUARE_DECIMETERS-The units will be square
          decimeters.SQUARE_CENTIMETERS-The units will be square
          centimeters.SQUARE_MILLIMETERS-The units will be square
          millimeters.SQUARE_MILES-The units will be square statute
          miles.SQUARE_YARDS-The units will be square international
          yards.SQUARE_FEET-The units will be square international
          feet.SQUARE_INCHES-The units will be square international
          inches.SQUARE_MILES_US-The units will be square US survey
          miles.SQUARE_YARDS_US-The units will be square US survey
          yards.SQUARE_FEET_US-The units will be square US survey
          feet.SQUARE_INCHES_US-The units will be square US survey
          inches.ACRES_US-The units will be US survey acres.HECTARES-The units
          will be hectares.ACRES-The units will be international acres.

     OUTPUTS:
      out_table (Table):
          The table that will contain the cross tabulation of intersections
          between zones and classes.

        """