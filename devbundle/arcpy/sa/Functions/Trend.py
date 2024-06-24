# Generated documentation for module arcpy.sa.Functions


class Trend(object):
    """
    Interpolates a raster surface from points using a trend technique.
    """

    @property
    def description(self) -> str:
        return """

        Trend_sa(in_point_features, z_field, {cell_size}, {order}, {regression_type}, {out_rms_file})

        Interpolates a raster surface from points using a trend technique.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated
          into a surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This
          can be a numeric field or the Shape field if the input point
          features contain z-values.If the regression type is Logistic, the
          values in the field can only
          be 0 or 1.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      order {Long}:
          The order of the polynomial.This must be an integer between 1 and 12.
          A value of 1 will fit a flat
          plane to the points, and a higher value will fit a more complex
          surface. The default is 1.
      regression_type {String}:
          The type of regression to be performed.LINEAR-Polynomial regression is
          performed to fit a least-squares
          surface to the set of input points. This is applicable for continuous
          types of data.LOGISTIC-Logistic trend surface analysis is performed.
          It generates a
          continuous probability surface for binary, or dichotomous, types of
          data.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.
      out_rms_file {File}:
          File name for the output text file that contains information about the
          RMS error and the Chi-Square of the interpolation.The extension must
          be .txt.

        """