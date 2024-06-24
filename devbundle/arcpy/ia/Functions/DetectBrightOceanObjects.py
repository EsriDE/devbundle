# Generated documentation for module arcpy.ia.Functions


class DetectBrightOceanObjects(object):
    """
    Detects potential bright human-made objects-such as ships, oil rigs, and windmills-while masking out the synthetic aperture radar (SAR) data outside the region of interest.
    """

    @property
    def description(self) -> str:
        return """

        DetectBrightOceanObjects_ia(in_radar_data, out_feature_class, {out_type}, {min_object_width}, {max_object_width}, {min_object_length}, {max_object_length}, {mask_features}, {feature_type}, {in_dem_raster}, {geoid}, {mask_tolerance})

        Detects potential bright human-made objects-such as ships, oil rigs,
        and windmills-while masking out the synthetic aperture radar (SAR)
        data outside the region of interest.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      out_type {String}:
          Specifies the type of boundary that will be used for the output
          feature class.BOUNDS-The minimum bounding box of the detected object
          will be used.
          This is the default.PERIMETER-An outline of the perimeter of the
          detected object will be
          used.
      min_object_width {Linear Unit}:
          The minimum width of an object to be detected. The width must be a
          positive value.The default value is 10 meters.
      max_object_width {Linear Unit}:
          The maximum width of an object to be detected. The width must be a
          positive value.The default value is 100 meters.
      min_object_length {Linear Unit}:
          The minimum length of an object to be detected. The length must be a
          positive value.The default value is 50 meters.
      max_object_length {Linear Unit}:
          The maximum length of an object to be detected. The length must be a
          positive value.The default value is 500 meters.
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
      out_feature_class (Feature Class):
          The output feature class of detected bright ocean objects.

        """