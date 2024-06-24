# Generated documentation for module arcpy.ia.Functions


class ConvertSARUnits(object):
    """
    Converts the scaling of the input synthetic aperture radar (SAR) data between amplitude and intensity, between linear and decibels (dB), and between complex and intensity.
    """

    @property
    def description(self) -> str:
        return """

        ConvertSARUnits_ia(in_radar_data, {conversion_type})

        Converts the scaling of the input synthetic aperture radar (SAR) data
        between amplitude and intensity, between linear and decibels (dB), and
        between complex and intensity.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      conversion_type {String}:
          Specifies the type of backscatter conversion that will be
          applied.LINEAR_TO_DB-The unitless values will be converted to dB
          values. This
          is the default.DB_TO_LINEAR-The dB values will be converted to
          unitless values.AMPLITUDE_TO_INTENSITY-The amplitude values will be
          converted to
          intensity values by squaring the amplitude.INTENSITY_TO_AMPLITUDE-The
          intensity values will be converted to
          amplitude values by applying the square root to the
          intensity.COMPLEX_TO_INTENSITY-The complex values will be converted
          to
          intensity values by adding the square of the real and imaginary
          components.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The converted radar dataset.

        """