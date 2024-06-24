# Generated documentation for module arcpy.ia.Functions


class ApplyGeometricTerrainCorrection(object):
    """
    Orthorectifies the input synthetic aperture radar (SAR) data using a range-Doppler backgeocoding algorithm.
    """

    @property
    def description(self) -> str:
        return """

        ApplyGeometricTerrainCorrection_ia(in_radar_data, {polarization_bands;polarization_bands...}, {in_dem_raster}, {geoid})

        Orthorectifies the input synthetic aperture radar (SAR) data using a
        range-Doppler backgeocoding algorithm.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      polarization_bands {String}:
          The polarization bands that will be corrected.The first band is
          selected by default.
      in_dem_raster {Raster Dataset / Raster Layer / Mosaic Layer}:
          The input DEM.If no DEM is specified or in areas that are not covered
          by a specified
          DEM, an approximated DEM, interpolated from metadata tie points, will
          be created.Use the tie-point approach for full ocean radar scenes
          only; specify a
          DEM whenever land features are included in the radar scene.
      geoid {Boolean}:
          Specifies whether the vertical reference system of the input DEM will
          be transformed to ellipsoidal height. Most elevation datasets are
          referenced to sea level orthometric height, so a correction is
          required in these cases to convert to ellipsoidal height.GEOID-A geoid
          correction will be made to convert orthometric height to
          ellipsoidal height (based on EGM96 geoid). This is the default.NONE-No
          geoid correction will be made. Use this option only if the DEM
          is provided in ellipsoidal height.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The corrected geometric terrain radar data.

        """