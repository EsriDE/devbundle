# Generated documentation for module arcpy.maritime


class GenerateLightSector(object):
    """
    Creates navigational light sector lines and arcs based on attributes in a specified point feature class.
    """

    @property
    def description(self) -> str:
        return """

        GenerateLightSector_maritime(in_features, sector_line_length, sector_arc_radius, sector_unit, {reference_scale}, {coordinate_system})

        Creates navigational light sector lines and arcs based on attributes
        in a specified point feature class.

     INPUTS:
      in_features (Feature Layer):
          The feature class that contains the light features.
      sector_line_length (Double / Field):
          The length of the boundary lines for the light sector. This is the
          line that appears on the chart. The value for the line length can be
          populated based on a specified value or from a field.Double-The line
          length will be determined by the specified value.
          Field-The line length will be determined by an appropriate
          field you are using for the line sectors. One field that can be used
          is. Value of Nominal Range (VALNMR)
      sector_arc_radius (Double / Field):
          The value that represents where the radius for the line sectors will
          be generated in relation to the light. The arc falls between two
          boundaries of the light sector. The radius is generated at a distance
          from the light sector using the units of measurement you select. You
          can specify a value for the radius or choose a field in the feature
          class that contains the radius values.Double-The radius will be
          generated based on the specified
          value.Field-The radius will be generated based on the value in the
          specified
          field.
      sector_unit (String):
          Specifies the unit of measurement that will be used for the radius arc
          that extends between the two light sector boundaries.To use page
          units, the map must be projected and the reference scale
          must be set.CENTIMETERS-The page units will be
          centimeters.DECIMAL_DEGREES-The map
          units will be decimal degrees.DECIMETERS-The map units will be
          decimeters.FEET-The map units will be feet.INCHES-The page units will
          be inches.KILOMETERS-The map units will be kilometers.METERS-The map
          units will be meters.MILLIMETERS-The page units will be
          millimeters.NAUTICAL_MILES-The map units will be nautical
          miles.POINTS-The page units will be points.YARDS-The map units will be
          yards.
      reference_scale {Long}:
          The scale at which the features will be generated when using page
          units.
      coordinate_system {Coordinate System}:
          The coordinate system that will be used when creating the output
          features. The default is the current map coordinate system.

        """