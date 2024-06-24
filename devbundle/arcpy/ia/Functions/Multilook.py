# Generated documentation for module arcpy.ia.Functions


class Multilook(object):
    """
    Averages the input synthetic aperture radar (SAR) data by looks in range and azimuth to approximate square pixels, mitigates speckle, and reduces SAR tool processing time.
    """

    @property
    def description(self) -> str:
        return """

        Multilook_ia(in_radar_data, {polarization_bands;polarization_bands...}, {range_looks}, {azimuth_looks})

        Averages the input synthetic aperture radar (SAR) data by looks in
        range and azimuth to approximate square pixels, mitigates speckle, and
        reduces SAR tool processing time.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      polarization_bands {String}:
          The polarization bands that will be corrected.The first band is
          selected by default.
      range_looks {Long}:
          The integer number of looks in the range direction. If no value is
          provided, the minimum number of looks required to create an
          approximate square pixel will be used.
      azimuth_looks {Long}:
          The integer number of looks in the azimuth direction. If no value is
          provided, the minimum number of looks required to create an
          approximate square pixel will be used.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The output multilook radar data.

        """