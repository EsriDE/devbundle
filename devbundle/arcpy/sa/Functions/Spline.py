# Generated documentation for module arcpy.sa.Functions


class Spline(object):
    """
    Interpolates a raster surface from points using a two-dimensional minimum curvature spline technique.
    """

    @property
    def description(self) -> str:
        return """

        Spline_sa(in_point_features, z_field, {cell_size}, {spline_type}, {weight}, {number_points})

        Interpolates a raster surface from points using a two-dimensional
        minimum curvature spline technique.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated
          into a surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This
          can be a numeric field or the Shape field if the input point
          features contain z-values.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      spline_type {String}:
          The type of spline to be used.REGULARIZED-Yields a smooth surface and
          smooth first
          derivatives.TENSION-Tunes the stiffness of the interpolant according
          to the
          character of the modeled phenomenon.
      weight {Double}:
          Parameter influencing the character of the surface interpolation.When
          the REGULARIZED option is used, it defines the weight of the
          third derivatives of the surface in the curvature minimization
          expression. If the TENSION option is used, it defines the weight of
          tension.The default weight is 0.1.
      number_points {Long}:
          The number of points per region used for local approximation.The
          default is 12.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.

        """