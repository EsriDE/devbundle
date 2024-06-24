# Generated documentation for module arcpy.ia.Functions


class ComputeSARIndices(object):
    """
    Computes various SAR indices for synthetic aperture radar (SAR) data, such as Radar Vegetation Index (RVI), Radar Forest Degradation Index (RFDI), and Canopy Structure Index (CSI).
    """

    @property
    def description(self) -> str:
        return """

        ComputeSARIndices_ia(in_radar_data, {index}, {polarization_bands})

        Computes various SAR indices for synthetic aperture radar (SAR) data,
        such as Radar Vegetation Index (RVI), Radar Forest Degradation Index
        (RFDI), and Canopy Structure Index (CSI).

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      index {String}:
          Specifies the SAR index that will be computed.RVI-The Radar Vegetation
          Index will be used. RVI is the ratio of
          cross-polarized backscatter to the total backscatter from all
          polarizations. The values range between 0 and 1. RVI values near 0
          indicate barren landscapes, while larger values indicate vegetated
          landscapes. This is the default.RFDI-The Radar Forest Degradation
          Index will be used. RFDI is the
          normalized difference between co- and cross-polarized backscatter.
          Lower RFDI values (less than 0.3) indicate a denser forest. Moderate
          RFDI values (between 0.4 and 0.6) correspond to degraded forests.
          Higher RFDI values (greater than 0.6) indicate deforested
          landscapes.CSI-The Canopy Structure Index will be used. CSI is the
          normalized
          difference of co-polarized backscatter (HH, VV). The values range
          between -1 and +1 in which canopies dominated with vertical structures
          will have CSI values near -1, while those dominated with horizontal
          structures will have CSI values near 1. This option is only supported
          when the input radar data contains HH and VV bands.
      polarization_bands {String}:
          Specifies the polarization bands that will be used in the index
          computation.This parameter is only supported when the in_radar_data
          parameter
          value is a quad-polarized SAR dataset and the index parameter value is
          RVI or RFDI.HH_HV-The horizontal-horizontal and horizontal-vertical
          bands will be
          used in the index computation (dual-polarization). This is the
          default.VV_VH-The vertical-vertical and vertical-horizontal bands will
          be used
          in the index computation (dual-polarization).HH_HV_VH_VV-The
          horizontal-horizontal, horizontal-vertical, vertical-
          horizontal, and vertical-vertical bands will be used in the index
          computation (quad-polarization).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output SAR index raster.

        """