# Generated documentation for module arcpy.ia.Functions


class Deburst(object):
    """
    Merges the multiple bursts from the input Sentinel-1 Single Look Complex (SLC) synthetic aperture radar (SAR) data and outputs a single, seamless subswath raster.
    """

    @property
    def description(self) -> str:
        return """

        Deburst_ia(in_radar_data, {polarization_bands;polarization_bands...})

        Merges the multiple bursts from the input Sentinel-1 Single Look
        Complex (SLC) synthetic aperture radar (SAR) data and outputs a
        single, seamless subswath raster.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      polarization_bands {String}:
          The polarization bands that will be corrected.The first band is
          selected by default.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The debursted radar data.

        """