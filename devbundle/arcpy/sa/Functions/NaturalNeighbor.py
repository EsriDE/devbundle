# Generated documentation for module arcpy.sa.Functions


class NaturalNeighbor(object):
    """
    Interpolates a raster surface from points using a natural neighbor technique.
    """

    @property
    def description(self) -> str:
        return """

        NaturalNeighbor_sa(in_point_features, z_field, {cell_size})

        Interpolates a raster surface from points using a natural neighbor
        technique.

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

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.

        """