# Generated documentation for module arcpy.ia.Functions


class ExtractWater(object):
    """
    Finds water bodies using input synthetic aperture radar (SAR) data and a DEM.
    """

    @property
    def description(self) -> str:
        return """

        ExtractWater_ia(in_radar_data, out_feature_class, {min_area}, {in_dem_raster}, {geoid})

        Finds water bodies using input synthetic aperture radar (SAR) data and
        a DEM.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      min_area {Areal Unit}:
          The minimum area to extract as a water body. The default value is
          50,000 square meters.
      in_dem_raster {Mosaic Layer / Raster Layer}:
          The input DEM.If the input radar data is not orthorectified, this DEM
          will be used
          to orthorectify it.This DEM will also be used to optimize the polygon
          construction.
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
      out_feature_class (Feature Class):
          The output polygon feature class that depicts water and land polygons.

        """