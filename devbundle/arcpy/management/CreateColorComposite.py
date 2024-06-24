# Generated documentation for module arcpy.management


class CreateColorComposite(object):
    """
    Creates a three-band raster dataset from a multiband raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateColorComposite_management(in_raster, out_raster, method, red_expression, green_expression, blue_expression)

        Creates a three-band raster dataset from a multiband raster dataset.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer):
          The input multiband raster data.
      method (String):
          Specifies the method that will be used to extract bands.BAND_NAMES-The
          band name representing the wavelength interval on the
          electromagnetic spectrum (such as Red, Near Infrared, or Thermal
          Infrared) or the polarization (such as VH, VV, HH, or HV) will be
          used. This is the default.BAND_IDS-The band number (such as B1, B2,
          or B3) will be used.
      red_expression (String):
          The calculation that will be assigned to the first band.A band name,
          band ID, or an algebraic expression using the bands.The supported
          operators are unary: plus (+), minus (-), times (*), and
          divide (/).
      green_expression (String):
          The calculation that will be assigned to the second band.A band name,
          band ID, or an algebraic expression using the bands.The supported
          operators are unary: plus (+), minus (-), times (*), and
          divide (/).
      blue_expression (String):
          The calculation that will be assigned to the third band.A band name,
          band ID, or an algebraic expression using the bands.The supported
          operators are unary: plus (+), minus (-), times (*), and
          divide (/).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output three-band composite raster.

        """