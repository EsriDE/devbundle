# Generated documentation for module arcpy.topographic


class GenerateSpotHeights(object):
    """
    Creates elevation point features based on contour tops and depressions. Elevation points are created in each top and depression. Point height values are populated based on a digital elevation model.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSpotHeights_topographic(in_contour_features, in_raster;in_raster..., target_spot_features, contour_height_field, spot_height_field, {spot_height_subtype}, {area_of_interest}, {scale}, {z_factor})

        Creates elevation point features based on contour tops and
        depressions. Elevation points are created in each top and depression.
        Point height values are populated based on a digital elevation model.

     INPUTS:
      in_contour_features (Feature Layer):
          The contours from which spot heights will be computed.
      in_raster (Raster Layer / Mosaic Layer):
          The rasters used to derive the highest or lowest elevations in contour
          tops or depressions.
      target_spot_features (Feature Layer):
          An existing point feature layer or feature class in which spot heights
          will be created.
      contour_height_field (Field):
          The field in the input contours that contains elevation values. The
          field type must be numeric.
      spot_height_field (Field):
          The field in the output spot heights where elevation values will be
          written.
      spot_height_subtype {String}:
          The spot height subtype value that will be assigned to new spot height
          features.
      area_of_interest {Feature Layer}:
          The polygon features that represent the extent of the region where
          spot heights will be created. The tool uses the outer extent of the
          selected polygon features within the area_of_interest parameter value.
          If this parameter is left blank, the tool uses the outer extent of the
          selected contour features within the in_contour_features parameter
          value. If this parameter is left blank and no contour features are
          selected, the tool uses the extent of the raster.
      scale {String}:
          Specifies the scale that will be used to optimize spot heights (the
          scale of the cartographic product that will be printed). Setting a
          scale will set the default of the z_factor parameter to a value that
          is appropriate for the scale value.1:5,000-The 1:5,000 cartographic
          product scale will be
          used.1:10,000-The 1:10,000 cartographic product scale will be
          used.1:12,500-The 1:12,500 cartographic product scale will be
          used.1:25,000-The 1:25,000 cartographic product scale will be
          used.1:50,000-The 1:50,000 cartographic product scale will be used.
          This is
          the default.1:100,000-The 1:100,000 cartographic product scale will be
          used.1:250,000-The 1:250,000 cartographic product scale will be
          used.1:500,000-The 1:500,000 cartographic product scale will be
          used.1:1,000,000-The 1:1,000,000 cartographic product scale will be
          used.
      z_factor {Double}:
          The unit conversion factor that will be used when generating spot
          heights. The default is 1.The spot heights are generated based on the
          z-values in the input
          raster, which are often measured in units of meters or feet. With the
          default value of 1, the spot heights will be in the same units as the
          z-values of the input raster. To create spot heights in a unit other
          than that of the z-values, set an appropriate value for the z-factor.
          It is not necessary that the ground x,y and surface z-units be
          consistent for this tool.For example, if the elevation values in the
          input raster are in feet,
          but you want the spot heights to be generated in meters, set the
          z-factor to 0.3048 (1 foot = 0.3048 meters).

        """