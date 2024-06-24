# Generated documentation for module arcpy.sa.Functions


class PointDensity(object):
    """
    Calculates a magnitude-per-unit area from point features that fall within a neighborhood around each cell.
    """

    @property
    def description(self) -> str:
        return """

        PointDensity_sa(in_point_features, population_field, {cell_size}, {neighborhood}, {area_unit_scale_factor})

        Calculates a magnitude-per-unit area from point features that fall
        within a neighborhood around each cell.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features for which to calculate the density.
      population_field (Field):
          Field denoting population values for each point. The population field
          is the count or quantity to be used in the calculation of a continuous
          surface.Values in the population field can be integer or floating
          point.The options and default behaviors for the field are listed
          below. Useif no item or special value will be used and each
          feature
          will be counted once. None          You can use thefield if
          input features contain z-values.
          Shape          Otherwise, the default field is. The following
          conditions
          may also apply:          POPULATION           If there is nofield, but
          there is afield, it will be used
          by default. The 'abcd' can be any valid characters, for example,,, or.
          POPULATIONPOPULATIONabcdPOPULATION6POPULATION1974POPULATIONROADTYPE
          If there is nofield orfield, but there is afield, thefield
          will be used by default. POPULATIONPOPULATIONabcdPOPPOP
          If there is nofield,field, orfield, but there is afield,
          thefield will be used by default.
          POPULATIONPOPULATIONabcdPOPPOPabcdPOPabcd           If there is
          nofield,field,field, orfield,will be used by
          default. POPULATIONPOPULATIONabcdPOPPOPabcdNONE
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      neighborhood {Neighborhood}:
          Dictates the shape of the area around each cell used to calculate the
          density value.This is a Neighborhood class.There are four types of
          neighbourhood class: NbrAnnulus, NbrCircle,
          NbrRectangle, and NbrWedge.The forms and descriptions of the classes
          are:         NbrAnnulus ({innerRadius}, {outerRadius}, {units})
          A
          torus (donut shaped) neighborhood defined by an inner radius and an
          outer radius. NbrCircle ({radius}, {units})         A circular
          neighborhood
          with the given radius. NbrRectangle ({width}, {height},
          {units})         A
          rectangular neighborhood with the given width and height.
          NbrWedge ({radius}, {startAngle}, {endAngle}, {units})
          A wedge (pie) shaped neighborhood. A wedge is specified by a start
          angle, an end angle, and a radius. The wedge extends counterclockwise
          from the starting angle to the ending angle. Angles are specified in
          arithmetic degrees (counterclockwise from the positive x-axis).
          Negative angles may be used.Defines the units as either the number of
          cells or as value in map
          units.The default is NbrCircle, where radius is the shortest of the
          width or
          height of the output extent in the output spatial reference, divided
          by 30.
      area_unit_scale_factor {String}:
          Specifies the area units that will be used for the output density
          values.A default unit is determined based on the linear unit of the
          output
          spatial reference. You can change this to the appropriate unit to
          convert the density output. Values for line density convert the units
          of both length and area. If no output spatial reference is
          specified, the output
          spatial reference will be the same as the input feature class. The
          default output density units are determined by the linear units of the
          output spatial reference . If the output linear units are meters, the
          output area density units will be set to, outputting square kilometers
          for point features or kilometers per square kilometers for polyline
          features. If the output linear units are feet, the output area density
          units will be set to. Square kilometersSquare miles        If
          the output units are anything other than feet or meters,
          the output area density units will be set to. That is, the output
          density units will be the square of the linear units of the output
          spatial reference. For example, if the output linear units are
          centimeters, the output area density units will be, which will result
          in square centimeters. If the output linear units are kilometers, the
          output area density units will be, which will result in square
          kilometers. Square map unitsSquare map unitsSquare map unitsThe
          available options and their corresponding output density units are
          the following:SQUARE_MAP_UNITS-The square of the linear units of the
          output spatial
          reference will be used.SQUARE_MILES-U.S. miles will be
          used.SQUARE_KILOMETERS-Kilometers will be used.ACRES-U.S. acres will
          be used.HECTARES-Hectares will be used.SQUARE_YARDS-U.S. yards will be
          used.SQUARE_FEET-U.S. feet will be used.SQUARE_INCHES-U.S. inches will
          be used.SQUARE_METERS-Meters will be
          used.SQUARE_CENTIMETERS-Centimeters will be
          used.SQUARE_MILLIMETERS-Millimeters will be used.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output point density raster.It is always a floating point raster.

        """