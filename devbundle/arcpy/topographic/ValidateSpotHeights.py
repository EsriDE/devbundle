# Generated documentation for module arcpy.topographic


class ValidateSpotHeights(object):
    """
    Validates that spot heights are higher than or equal to their respective contour top, and based on the contour interval, that a contour top is not missing a contour line between it and a spot height.
    """

    @property
    def description(self) -> str:
        return """

        ValidateSpotHeights_topographic(in_contour_features, contour_height_field, contour_interval, in_rasters;in_rasters..., in_spot_features, spot_height_field, {area_of_interest}, {z_factor}, {use_rasters})

        Validates that spot heights are higher than or equal to their
        respective contour top, and based on the contour interval, that a
        contour top is not missing a contour line between it and a spot
        height.

     INPUTS:
      in_contour_features (Feature Layer):
          The contour features that will be used to validate the spot heights.
      contour_height_field (Field):
          The field that contains elevation values for the in_contour_features
          parameter value. The field type must be numeric.
      contour_interval (Long):
          The interval, or distance, between contour lines. The value can be any
          positive number. The default is 20.
      in_rasters (Raster Layer / Mosaic Layer):
          The rasters that will be used to derive elevations of points inside
          contours.
      in_spot_features (Feature Layer):
          An existing point feature layer that contains spot heights that will
          be validated.
      spot_height_field (Field):
          The field that contains elevation values for the in_spot_features
          parameter value.
      area_of_interest {Feature Layer}:
          The extent that contains the spot heights that will be validated. This
          parameter does not accept point layers as valid input and must have
          only one selected feature.
      z_factor {Double}:
          The unit conversion factor that will be used when validating spot
          heights to convert the contour elevation value unit of measurement to
          match the raster's unit of measurement. The default is 1.For example,
          if the input raster's elevation values are in meters but
          the contours are in feet, set the z-factor to 3.28084 (1 meter =
          3.28084 feet).
      use_rasters {Boolean}:
          Specifies whether the rasters provided will be used to validate the
          spot heights.USE_RASTERS-The in_rasters parameter value will be used
          to validate
          the spot heights. This is the default.NO_USE_RASTERS-The in_rasters
          parameter value will not be used to
          validate the spot heights.

        """