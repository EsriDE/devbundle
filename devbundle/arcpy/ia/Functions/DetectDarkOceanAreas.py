# Generated documentation for module arcpy.ia.Functions


class DetectDarkOceanAreas(object):
    """
    Identifies potential dark pixels belonging to oil spills or algae, and clusters these pixels, while masking out the synthetic aperture radar (SAR) data outside the region of interest.
    """

    @property
    def description(self) -> str:
        return """

        DetectDarkOceanAreas_ia(in_radar_data, {min_area}, {mask_features}, {feature_type}, {in_dem_raster}, {geoid}, {mask_tolerance})

        Identifies potential dark pixels belonging to oil spills or algae, and
        clusters these pixels, while masking out the synthetic aperture radar
        (SAR) data outside the region of interest.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      min_area {Areal Unit}:
          The minimum area to be detected.The size cannot be negative. The
          default value is 10000 square meters.
      mask_features {Feature Layer}:
          A land or water polygon feature. This polygon will be used to create a
          mask.
      feature_type {String}:
          Specifies the type of polygon the mask_features parameter value
          represents. This parameter is required if the mask_features parameter
          is specified.LAND-The mask input is a land polygon. An inverted mask
          will be
          created using this input.WATER-The mask input is a water polygon. A
          mask will be created using
          this input.
      in_dem_raster {Mosaic Layer / Raster Layer}:
          The input DEM.If the input radar data is not orthorectified, this DEM
          will be used
          to orthorectify it.If the mask_features parameter value is not
          provided, this DEM will
          also be used to create a land mask.
      geoid {Boolean}:
          Specifies whether the vertical reference system of the input DEM will
          be transformed to ellipsoidal height. Most elevation datasets are
          referenced to sea level orthometric height, so a correction is
          required in these cases to convert to ellipsoidal height.GEOID-A geoid
          correction will be made to convert orthometric height to
          ellipsoidal height (based on EGM96 geoid). This is the default.NONE-No
          geoid correction will be made. Use this option only if the DEM
          is provided in ellipsoidal height.
      mask_tolerance {Linear Unit}:
          The buffer distance surrounding the mask created from either the
          mask_features parameter or the in_dem_raster parameter. The distance
          cannot be negative. The default value is 100 meters.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output binary raster of the detected dark ocean areas. A value of
          1 corresponds to a detected dark area.

        """