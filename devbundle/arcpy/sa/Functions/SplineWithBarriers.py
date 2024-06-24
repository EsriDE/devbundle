# Generated documentation for module arcpy.sa.Functions


class SplineWithBarriers(object):
    """
    Interpolates a raster surface, using barriers, from points using a minimum curvature spline technique. The barriers are entered as either polygon or polyline features.
    """

    @property
    def description(self) -> str:
        return """

        SplineWithBarriers_sa(in_point_features, Z_value_field, {Input_barrier_features}, {cell_size}, {Smoothing_Factor})

        Interpolates a raster surface, using barriers, from points using a
        minimum curvature spline technique. The barriers are entered as either
        polygon or polyline features.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated
          into a surface raster.
      Z_value_field (Field):
          The field that holds a height or magnitude value for each point.This
          can be a numeric field or the Shape field if the input point
          features contain z-values.
      Input_barrier_features {Composite Geodataset}:
          The optional input barrier features to constrain the interpolation.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      Smoothing_Factor {Double}:
          The parameter that influences the smoothing of the output surface.No
          smoothing is applied when the value is zero and the maximum amount
          of smoothing is applied when the factor equals 1.The default is 0.0.

     OUTPUTS:
      Output_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.

        """