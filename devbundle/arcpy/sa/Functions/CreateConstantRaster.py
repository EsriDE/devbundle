# Generated documentation for module arcpy.sa.Functions


class CreateConstantRaster(object):
    """
    Creates a raster of a constant value within the extent and cell size of the analysis window.
    """

    @property
    def description(self) -> str:
        return """

        CreateConstantRaster_sa(constant_value, {data_type}, {cell_size}, {extent})

        Creates a raster of a constant value within the extent and cell size
        of the analysis window.

     INPUTS:
      constant_value (Double):
          The constant value with which to populate all the cells in the output
          raster.
      data_type {String}:
          Data type of the output raster dataset.INTEGER-An integer raster will
          be created.FLOAT-A floating-point
          raster will be created.If the specified data type is floating-point,
          the values of the cells
          in the output raster will only be accurate to the constant value of 7
          decimal places, regardless of the output format.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      extent {Envelope / Extent}:
          The extent for the output raster dataset.The Extent is a Python class.
          In this tool, it is in the form Extent(XMin, YMin, XMax, YMax)
          where XMin and YMin define the lower left coordinate of the extent,
          and XMax and YMax define the upper right coordinate.The coordinates
          are specified in the same map units as the Output
          Coordinate System environment setting.The extent will be the value in
          the environment if specifically set.
          If not specifically set, the default is 0, 0, 250, 250.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster for which each cell will have the specified constant
          value.

        """