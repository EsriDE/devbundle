# Generated documentation for module arcpy.ia.Functions


class RemoveThermalNoise(object):
    """
    Corrects backscatter disturbances caused by thermal noise in the input synthetic aperture radar (SAR) data, resulting in a more seamless image.
    """

    @property
    def description(self) -> str:
        return """

        RemoveThermalNoise_ia(in_radar_data, {polarization_bands;polarization_bands...})

        Corrects backscatter disturbances caused by thermal noise in the input
        synthetic aperture radar (SAR) data, resulting in a more seamless
        image.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      polarization_bands {String}:
          The polarization bands that will be corrected.The first band is
          selected by default.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The thermal noise-corrected radar data.

        """