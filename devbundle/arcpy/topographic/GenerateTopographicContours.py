# Generated documentation for module arcpy.topographic


class GenerateTopographicContours(object):
    """
    Creates and smooths contours from an input raster.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTopographicContours_topographic(in_rasters;in_rasters..., area_of_interest, contour_features, elevation_field, {contour_subtype}, {scale}, {resample_raster}, {contour_interval}, {base_contour}, {z_factor}, {zero_contour}, {code_field}, {index_interval}, {index_code}, {intermediate_code}, {depression_code}, {depression_intermediate_code}, {raster_smooth_tolerance}, {minimum_length}, {contour_smooth_tolerance}, {supplemental_contours}, {half_auxiliary_code}, {quarter_auxiliary_code}, {depression_auxiliary_code})

        Creates and smooths contours from an input raster.

     INPUTS:
      in_rasters (Raster Layer / Mosaic Layer):
          The input raster layers that will be used to derive the contour lines.
      area_of_interest (Feature Layer):
          A feature layer that will be used to clip the input raster before
          processing. A buffer is created before clipping the raster, which
          results in larger output contours that extend beyond the selected AOI.
          The feature layer must have only one selected feature.
      contour_features (Feature Layer):
          An existing line feature class or feature layer. Contours will be
          appended to this feature class.
      elevation_field (Field):
          The field from the input contours that will store the contour
          elevation value. This field defaults toorif a field with either of
          those names exists in the contour feature class. ZV2ZVH
      contour_subtype {String}:
          The subtype to which contours will be written if the input contours
          have subtypes.
      scale {String}:
          Specifies the scale that will be used to optimize contours. This is
          the scale of the cartographic product that will be printed. Specifying
          the scale will set the defaults of other parameters to values that are
          appropriate for the output scale. The default is the 1:50,000
          cartographic product scale.1:5,000-The 1:5,000 cartographic product
          scale will be
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
      resample_raster {Boolean}:
          Specifies whether the input raster will be resampled before creating
          contours.RESAMPLE_RASTER-The input raster will be resampled before
          creating
          contours.NO_RESAMPLE_RASTER-The input raster will not be resampled
          when
          creating contours. This is the default.
      contour_interval {Double}:
          The interval, or distance, between contour lines. This can be any
          positive number. The default is set by the scale value. If this
          parameter is left blank, the default scale value will be used.
      base_contour {Double}:
          The value that contours will be generated above and below to cover the
          entire value range of the input raster. The default is 0.
      z_factor {Double}:
          The unit conversion factor that will be used when generating contours.
          The default is 1.The contour lines are generated based on the z-values
          in the input
          raster, which are often measured in units of meters or feet. With the
          default value of 1, the contours will be in the same units as the
          z-values of the input raster. To create contours in a unit other than
          that of the z-values, set an appropriate value for the z-factor. It is
          not necessary that the ground x,y and surface z-units be consistent
          for this tool.For example, if the elevation values in the input raster
          are in meters
          but you want the contours to be generated in feet, set the z-factor to
          3.28084 (1 meter = 3.28084 feet).
      zero_contour {Boolean}:
          Specifies whether a zero contour will be created. A zero contour
          represents sea level. Zero contours, when generated along a coastline,
          can be created inside a water body. Specify ZERO_CONTOUR if you want
          contours generated on land areas that are at or below sea
          level.ZERO_CONTOUR-A zero contour will be created.NO_ZERO_CONTOUR-A
          zero
          contour will not be created. This is the
          default.
      code_field {Field}:
          The field from the input contour feature class where the
          appropriate code will be stored. The field defaults to thefield if it
          exists in the input contour feature class. HQC
      index_interval {Long}:
          The interval, or distance, between index contour lines. For example,
          if the contour interval is 20 meters and you want index contours every
          100 meters, specify 100. The default is set by the scale value.
      index_code {String}:
          The code value that will be stored in the code_field parameter
          value when an index contour is identified. The default code will be 1
          if thefield exists in the input contour feature class. HQC
      intermediate_code {String}:
          The code value that will be stored in the code_field parameter
          value when an intermediate contour is identified. The default code
          will be 2 if thefield exists in the input contour feature class.
          HQC
      depression_code {String}:
          The code value that will be stored in the code_field parameter
          value when a depression contour is identified. The default code will
          be 5 if thefield exists in the input contour feature class. HQC
      depression_intermediate_code {String}:
          The code value that will be stored in the code_field parameter
          value when a depression intermediate contour is identified. The
          default code will be 6 if thefield exists in the input contour feature
          class. HQC
      raster_smooth_tolerance {Double}:
          The amount of smoothing that will be applied to the input raster
          before creating the contour lines.
      minimum_length {Linear Unit}:
          The minimum length that will be used for an individual contour line.
          The default is set by the scale value. If the value is set to 0 or
          left blank, no contours will be deleted from the output contours based
          on their short length.
      contour_smooth_tolerance {Linear Unit}:
          The amount of smoothing that will be applied to the contour lines. The
          larger the value, the more generalized the contours. The default is
          set by the scale value. If this parameter is set to 0 or left blank,
          no smoothing will be applied to the output contours.
      supplemental_contours {String}:
          Specifies the interval at which a contour line will be placed between
          regularly spaced contours. This is used when the terrain change is not
          large enough to be depicted with consistent contour intervals.NONE-No
          supplemental contours will be created. This is the
          default.HALF_AUXILIARY-Supplemental contours will be created at one-
          half the
          contour interval.QUARTER_AUXILIARY-Supplemental contours will be
          created at one-quarter
          the contour interval.
      half_auxiliary_code {String}:
          The code value that will be stored in the code_field parameter
          value when a half auxiliary contour is identified. The default code
          will be 3 if thefield exists in the input contour feature class.
          HQC
      quarter_auxiliary_code {String}:
          The code value that will be stored in the code_field parameter
          value when a quarter auxiliary contour is identified. The default code
          will be 14 if thefield exists in the input contour feature class.
          HQC
      depression_auxiliary_code {String}:
          The code value that will be stored in the code_field parameter
          value when a depression auxiliary contour is identified. The default
          code will be 22 if thefield exists in the input contour feature class.
          HQC

        """