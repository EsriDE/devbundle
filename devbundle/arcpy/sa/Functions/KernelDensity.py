# Generated documentation for module arcpy.sa.Functions


class KernelDensity(object):
    """
    Calculates a magnitude-per-unit area from point or polyline features using a kernel function to fit a smoothly tapered surface to each point or polyline. A barrier can be used to alter the influence of a feature while calculating kernel density.
    """

    @property
    def description(self) -> str:
        return """

        KernelDensity_sa(in_features, population_field, {cell_size}, {search_radius}, {area_unit_scale_factor}, {out_cell_values}, {method}, {in_barriers})

        Calculates a magnitude-per-unit area from point or polyline features
        using a kernel function to fit a smoothly tapered surface to each
        point or polyline. A barrier can be used to alter the influence of a
        feature while calculating kernel density.

     INPUTS:
      in_features (Composite Geodataset):
          The input features (point or line) for which to calculate the density.
      population_field (Field):
          The field denoting population values for each feature. The population
          field is the count or quantity to be spread across the landscape to
          create a continuous surface.Values in the population field can be
          integer or floating point.The options and default behaviors for the
          field are listed below. Useif no item or special value will
          be used and each feature
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
      search_radius {Double}:
          The search radius within which density will be calculated. Units are
          based on the linear unit of the projection of the output spatial
          reference.For example, if the units are meters-to include all features
          within a
          one-mile neighborhood-set the search radius equal to 1609.344 (1 mile
          = 1609.344 meters).The default search radius is computed specifically
          for the input
          dataset using a spatial variant of Silverman's Rule of Thumb
          (Silverman, 1986) that is robust enough for spatial outliers (points
          that are far away from the rest of the points). See the usage tips for
          a description of the algorithm.
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
      out_cell_values {String}:
          Specifies what the values in the output raster represent.DENSITIES-The
          output values represent the calculated density value per
          unit area for each cell. This is the default.EXPECTED_COUNTS-The
          output values represent the calculated density
          value per cell area.Since the cell value is linked to the specified
          cell size, the
          resulting raster cannot be resampled to a different cell size.
      method {String}:
          Specifies whether the flat earth (planar) or the shortest path on a
          spheroid (geodesic) method will be used.PLANAR-The planar distance
          between features will be used. This is the
          default.GEODESIC-The geodesic distance between features will be
          used.The geodesic method only supports points as input features.
      in_barriers {Composite Geodataset}:
          The dataset that defines the barriers.The barriers can be a feature
          layer of polyline or polygon features.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output kernel density raster.It is always a floating point raster.

        """