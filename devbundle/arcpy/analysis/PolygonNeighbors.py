# Generated documentation for module arcpy.analysis


class PolygonNeighbors(object):
    """
    Creates a table with statistics based on polygon contiguity (overlaps, coincident edges, or nodes).
    """

    @property
    def description(self) -> str:
        return """

        PolygonNeighbors_analysis(in_features, out_table, {in_fields;in_fields...}, {area_overlap}, {both_sides}, {cluster_tolerance}, {out_linear_units}, {out_area_units})

        Creates a table with statistics based on polygon contiguity (overlaps,
        coincident edges, or nodes).

     INPUTS:
      in_features (Feature Layer):
          The input polygon features.
      in_fields {Field}:
          The input attribute field or fields that will be used to identify
          unique polygons or polygon groups and represent them in the output.
      area_overlap {Boolean}:
          Specifies whether overlapping relationships will be analyzed and
          included in the output.NO_AREA_OVERLAP-Overlapping relationships will
          not be analyzed or
          included in the output. This is the default.AREA_OVERLAP-Overlapping
          relationships will be analyzed and included
          in the output.
      both_sides {Boolean}:
          Specifies whether both sides of neighbor relationships will be
          included in the output.BOTH_SIDES-For a pair of neighboring polygons,
          both neighboring
          information of one polygon being the source and the other being the
          neighbor and vice versa will be included. This is the
          default.NO_BOTH_SIDES-For a pair of neighboring polygons, only
          neighboring
          information of one polygon being the source and the other being the
          neighbor will be included. The reciprocal relationship will not be
          included.
      cluster_tolerance {Linear Unit}:
          The minimum distance between coordinates before they will be
          considered equal. By default, this is the x,y tolerance of the input
          features.Changing this parameter's value may cause failure or
          unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.
      out_linear_units {String}:
          Specifies the units that will be used to report the total length of
          the coincident edge between neighboring polygons. The default is the
          input feature units.UNKNOWN-The length unit will be
          unknown.KILOMETERS-The length unit
          will be kilometers.METERS-The length unit will be
          meters.DECIMETERS-The length unit will be decimeters.CENTIMETERS-The
          length unit will be centimeters.MILLIMETERS-The length unit will be
          millimeters.MILES_INTERNATIONAL-The length unit will be statute
          miles.NAUTICAL_MILES_INTERNATIONAL-The length unit will be
          international
          nautical miles.YARDS_INTERNATIONAL-The length unit will be
          international yards.FEET_INTERNATIONAL-The length unit will be
          international feet.INCHES_INTERNATIONAL-The length unit will be
          international inches.MILES-The length unit will be US survey
          miles.NAUTICAL_MILES-The length unit will be US survey nautical
          miles.YARDS-The length unit will be US survey yards.FEET-The length
          unit will be US survey feet.INCHES-The length unit will be US survey
          inches.DECIMAL_DEGREES-The length unit will be decimal
          degrees.POINTS-The length unit will be points.
      out_area_units {String}:
          Specifies the units that will be used to report the area overlap of
          neighboring polygons. The default is the input feature units. This
          parameter is only enabled when the area_overlap parameter is set to
          AREA_OVERLAP.UNKNOWN-The area unit will be square
          unknown.SQUARE_KILOMETERS-The
          area unit will be square kilometers.SQUARE_METERS-The area unit will
          be square meters.SQUARE_DECIMETERS-The area unit will be square
          decimeters.SQUARE_CENTIMETERS-The area unit will be square
          centimeters.SQUARE_MILLIMETERS-The area unit will be square
          millimeters.SQUARE_MILES-The area unit will be square statute
          miles.SQUARE_YARDS-The area unit will be square international
          yards.SQUARE_FEET-The area unit will be square international
          feet.SQUARE_INCHES-The area unit will be square international
          inches.SQUARE_MILES_US-The area unit will be square US survey
          miles.SQUARE_YARDS_US-The area unit will be square US survey
          yards.SQUARE_FEET_US-The area unit will be square US survey
          feet.SQUARE_INCHES_US-The area unit will be square US survey
          inches.ACRES_US-The area unit will be US survey acres.HECTARES-The
          area unit will be hectares.ACRES-The area unit will be international
          acres.ARES-The area unit will be ares.

     OUTPUTS:
      out_table (Table):
          The output table.

        """