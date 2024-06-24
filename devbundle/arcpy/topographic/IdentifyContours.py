# Generated documentation for module arcpy.topographic


class IdentifyContours(object):
    """
    Identifies types of contours and applies hypsographic codes to input features.
    """

    @property
    def description(self) -> str:
        return """

        IdentifyContours_topographic(in_contour_features, in_rasters;in_rasters..., contour_height_field, contour_code_field, {contour_index_interval}, {index_code}, {intermediate_code}, {depression_code}, {depression_intermediate_code}, {depression_contours_count}, {area_of_interest}, {z_factor}, {supplemental_contours}, {half_auxiliary_code}, {quarter_auxiliary_code}, {depression_auxiliary_code}, {contour_interval}, {base_contour})

        Identifies types of contours and applies hypsographic codes to input
        features.

     INPUTS:
      in_contour_features (Feature Layer):
          The input contours that will be updated with the specified contour
          codes.
      in_rasters (Raster Layer / Mosaic Layer):
          The rasters that will be used to derive elevations of points inside
          contours to correctly identify the types of contours.
      contour_height_field (Field):
          The field in the input contour feature class that contains elevation
          values. This field type must be numeric.
      contour_code_field (Field):
          The field in the input contour feature class that will be updated with
          the appropriate domain code.
      contour_index_interval {Long}:
          The interval, or distance, between index contour lines. The default is
          100.
      index_code {String}:
          The value that will be used to populate the contour_code_field
          parameter value when index contours are identified. The default is 1.
      intermediate_code {String}:
          The value that will be used to populate the contour_code_field
          parameter value when intermediate contours are identified. The default
          is 2.
      depression_code {String}:
          The value that will be used to populate the contour_code_field
          parameter value when depression contours are identified. The default
          is 5.
      depression_intermediate_code {String}:
          The value that will be used to populate the contour_code_field
          parameter value when depression intermediate contours are identified.
          The default is 6.
      depression_contours_count {Long}:
          The number of contours in a depression that will be coded as
          depressions. The value provided must be greater than zero. If no value
          is provided, all of the contours in the depression will be coded as
          depressions.
      area_of_interest {Feature Layer}:
          The layer that defines the processing extent. The layer must have only
          one selected feature.
      z_factor {Double}:
          The conversion factor that will be used to convert the contour
          elevation value unit of measurement to match the raster's unit of
          measurement. The default is 1.For example, if the elevation values in
          the input raster are in meters
          but the contours are in feet, set the z-factor to 3.28084 (1 meter =
          3.28084 feet).
      supplemental_contours {String}:
          Specifies the interval at which supplemental contours will be created.
          Supplemental contours are used when the terrain change is not large
          enough to be depicted with consistent contour intervals.NONE-No
          supplemental contours will be created. This is the
          default.HALF_AUXILIARY-Supplemental contours will be created at one-
          half the
          contour interval.QUARTER_AUXILIARY-Supplemental contours will be
          created at one-quarter
          the contour interval.
      half_auxiliary_code {String}:
          The code value that will be stored in the contour_code_field
          parameter value when a half auxiliary contour is identified. The
          default code will be 3 if thefield exists in the input contour feature
          class. HQC
      quarter_auxiliary_code {String}:
          The code value that will be stored in the contour_code_field
          parameter value when a quarter auxiliary contour is identified. The
          default code will be 14 if thefield exists in the input contour
          feature class. HQC
      depression_auxiliary_code {String}:
          The code value that will be stored in the contour_code_field
          parameter value when a depression auxiliary contour is identified. The
          default code will be 22 if thefield exists in the input contour
          feature class. HQC
      contour_interval {Double}:
          The interval, or distance, between contour lines. This can be any
          positive number. The default is 20.
      base_contour {Double}:
          The value that contours will be generated above and below to cover the
          entire value range of the input raster. The default is 0.

        """