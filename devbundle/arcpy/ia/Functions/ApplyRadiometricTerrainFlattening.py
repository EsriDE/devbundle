# Generated documentation for module arcpy.ia.Functions


class ApplyRadiometricTerrainFlattening(object):
    """
    Corrects the input synthetic aperture radar (SAR) data for radiometric distortions due to topography.
    """

    @property
    def description(self) -> str:
        return """

        ApplyRadiometricTerrainFlattening_ia(in_radar_data, in_dem_raster, {geoid}, {polarization_bands;polarization_bands...}, {calibration_type}, {out_scattering_area}, {out_geometric_distortion}, {out_geometric_distortion_mask})

        Corrects the input synthetic aperture radar (SAR) data for radiometric
        distortions due to topography.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.The data that will have radiometric terrain
          flattening applied. The
          data must be radiometrically calibrated to beta nought.
      in_dem_raster (Mosaic Layer / Raster Layer):
          The input DEM.The DEM that will be used to estimate the local
          illuminated area and
          the local incidence angle.
      geoid {Boolean}:
          Specifies whether the vertical reference system of the input DEM will
          be transformed to ellipsoidal height. Most elevation datasets are
          referenced to sea level orthometric height, so a correction is
          required in these cases to convert to ellipsoidal height.GEOID-A geoid
          correction will be made to convert orthometric height to
          ellipsoidal height (based on EGM96 geoid). This is the default.NONE-No
          geoid correction will be made. Use this option only if the DEM
          is provided in ellipsoidal height.
      polarization_bands {String}:
          The polarization bands that will be radiometrically terrain
          flattened.The first band is selected by default.
      calibration_type {String}:
          Specifies whether the output will be terrain flattened using sigma
          nought or gamma nought.GAMMA_NOUGHT-The beta nought backscatter will
          be corrected using an
          accurate computation of an area using a DEM. This is the
          default.SIGMA_NOUGHT-The beta nought backscatter will be corrected
          using the
          unit area of a plane that is locally tangent to the DEM.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The radiometrically terrain-flattened radar data.
      out_scattering_area {Raster Dataset}:
          The scattering area radar dataset.
      out_geometric_distortion {Raster Dataset}:
          The 4-band geometric distortion radar dataset. The first band is the
          terrain slope, the second band is look angle, the third band is the
          foreshortening ratio, and the fourth band is the local incidence
          angle.
      out_geometric_distortion_mask {Raster Dataset}:
          The 1-band geometric distortion mask radar dataset. The pixels
          are classified using six unique values, one for each distortion type:
          Undetermined-Value of 0Foreshortening-Value of 1Lengthening-Value of
          2Shadow-Value of 3Layover-Value of 4Layover and shadow-Value of 5

        """