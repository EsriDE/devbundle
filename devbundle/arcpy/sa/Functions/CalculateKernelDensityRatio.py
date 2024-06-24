# Generated documentation for module arcpy.sa.Functions


class CalculateKernelDensityRatio(object):
    """
    Calculates a spatial relative risk surface using two input feature datasets. The numerator in the ratio represents cases, such as number of crimes or number of patients, and the denominator represents the control, such as the total population.
    """

    @property
    def description(self) -> str:
        return """

        CalculateKernelDensityRatio_sa(in_features_numerator, in_features_denominator, population_field_numerator, population_field_denominator, {cell_size}, {search_radius_numerator}, {search_radius_denominator}, {out_cell_values}, {method}, {in_barriers_numerator}, {in_barriers_denominator})

        Calculates a spatial relative risk surface using two input feature
        datasets. The numerator in the ratio represents cases, such as number
        of crimes or number of patients, and the denominator represents the
        control, such as the total population.

     INPUTS:
      in_features_numerator (Feature Layer):
          The input features (point or line) of the cases for which density will
          be calculated.
      in_features_denominator (Feature Layer):
          The input features (point or line) of the control for which density
          will be calculated.
      population_field_numerator (Field):
          The field denoting population values for each feature. The population
          field is the count or quantity to be spread across the landscape to
          create a continuous surface.Use OID or FID if no item or special value
          will be used and each
          feature will be counted once.Values in the population field can be
          integer or floating point. You can use thefield if input
          features contain z-values.
          Shape
      population_field_denominator (Field):
          The field denoting population values for each feature. The population
          field is the count or quantity to be spread across the landscape to
          create a continuous surface.Use OID or FID if no item or special value
          will be used and each
          feature will be counted once.Values in the population field can be
          integer or floating point. You can use thefield if input
          features contain z-values.
          Shape
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      search_radius_numerator {Double}:
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
      search_radius_denominator {Double}:
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
          spheroid (geodesic) distance will be used.PLANAR-The planar distance
          between features will be used. This is the
          default.GEODESIC-The geodesic distance between features will be
          used.The geodesic method only supports points as input features.
      in_barriers_numerator {Feature Layer}:
          The dataset that defines the barriers.The barriers can be a feature
          layer of polyline or polygon features.
      in_barriers_denominator {Feature Layer}:
          The dataset that defines the barriers.The barriers can be a feature
          layer of polyline or polygon features.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output kernel density raster.It is always a floating point raster.

        """