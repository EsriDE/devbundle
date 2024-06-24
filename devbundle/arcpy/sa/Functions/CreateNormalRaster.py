# Generated documentation for module arcpy.sa.Functions


class CreateNormalRaster(object):
    """
    Creates a raster of random values with a normal (Gaussian) distribution within the extent and cell size of the analysis window.
    """

    @property
    def description(self) -> str:
        return """

        CreateNormalRaster_sa({cell_size}, {extent})

        Creates a raster of random values with a normal (Gaussian)
        distribution within the extent and cell size of the analysis window.

     INPUTS:
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
          The output raster of normally distributed values with a mean of 0.0
          and a standard deviation of 1.0.

        """