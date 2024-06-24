# Generated documentation for module arcpy.sa.Functions


class CreateRandomRaster(object):
    """
    Creates a raster of random floating-point values between 0.0 and 1.0 within the extent and cell size of the analysis window.
    """

    @property
    def description(self) -> str:
        return """

        CreateRandomRaster_sa({seed_value}, {cell_size}, {extent})

        Creates a raster of random floating-point values between 0.0 and 1.0
        within the extent and cell size of the analysis window.

     INPUTS:
      seed_value {Double}:
          A value to be used to reseed the random number generator.This may be
          an integer or floating-point number. Rasters are not
          permitted as input. The random number generator is
          automatically seeded with the
          current value of the system clock (seconds since January 1, 1970). The
          range of permissible values for the seed value is -2+ 1 to 2(or
          -2,147,483,647 to 2,147,483,648). 3131
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
          The output raster of randomly distributed values with a range of 0.0
          to 1.0

        """