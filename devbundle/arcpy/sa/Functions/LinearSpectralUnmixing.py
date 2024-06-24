# Generated documentation for module arcpy.sa.Functions


class LinearSpectralUnmixing(object):
    """
    Performs subpixel classification and calculates the fractional abundance of different land-cover types for individual pixels.
    """

    @property
    def description(self) -> str:
        return """

        LinearSpectralUnmixing_sa(in_raster, out_raster, in_spectral_profile_file, {value_option;value_option...})

        Performs subpixel classification and calculates the fractional
        abundance of different land-cover types for individual pixels.

     INPUTS:
      in_raster (Raster Dataset / Mosaic Dataset / Mosaic Layer / Raster Layer / File / Image Service):
          The input raster dataset.
      in_spectral_profile_file (Feature Layer / File / String):
          The spectral information for the different land-cover classes.This can
          be provided as polygon features, a classifier definition file
          (.ecd) generated from the Train Maximum Likelihood Classifier tool, or
          a JSON format file (.json) that contains the class spectral profiles.
      value_option {String}:
          Specifies how the output pixel values will be defined.SUM_TO_ONE-Class
          values for each pixel will be provided in decimal
          format with the sum of all classes equal to 1. For example, Class1 =
          0.16; Class2 = 0.24; Class3 = 0.60.NON_NEGATIVE-There will be no
          negative output values.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output multiband raster dataset.

        """