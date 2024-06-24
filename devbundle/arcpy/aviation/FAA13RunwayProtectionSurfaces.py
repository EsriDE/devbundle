# Generated documentation for module arcpy.aviation


class FAA13RunwayProtectionSurfaces(object):
    """
    Generates runway protection surfaces based on the FAA Advisory Circular AC 150/5300-13B specification.
    """

    @property
    def description(self) -> str:
        return """

        FAA13RunwayProtectionSurfaces_aviation(in_features, target, surfaces_to_generate;surfaces_to_generate..., {visibility_minimums}, {approach_category}, {approach_design_group}, {aircraft_type}, {approach_guidance}, {runway_direction}, {airport_elevation}, {airport_control_point_feature_class}, {runway_end_features}, {last_low_light}, {last_high_light}, {custom_json_file})

        Generates runway protection surfaces based on the FAA Advisory
        Circular AC 150/5300-13B specification.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target (Feature Layer):
          The target feature class that will contain the generated OIS.
      surfaces_to_generate (String):
          Specifies the type of surface that will be
          generated.RUNWAY_SAFETY_AREA-A runway safety area (RSA) will be
          generated.RUNWAY_OBJECT_FREE_AREA-A runway object free area (ROFA)
          will be
          generated.RUNWAY_OBSTACLE_FREE_ZONE-A runway obstacle free zone (ROFZ)
          will be
          generated.PRECISION_OBSTACLE_FREE_ZONE-A precision obstacle free zone
          (POFZ)
          will be generated.APPROACH_RUNWAY_PROTECTION_ZONE-An approach runway
          protection zone
          (RPZ) will be generated.DEPARTURE_RUNWAY_PROTECTION_ZONE-A departure
          runway protection zone
          (RPZ) will be generated.
      visibility_minimums {String}:
          Specifies the visibility minimums that will be used for the
          runways.VISUAL-Visual flight rules will be used. This is the
          default.NOT_LOWER_THAN_1_MILE-Visibility minimums will not be lower
          than 1
          mile.NOT_LOWER_THAN_3_4_MILE-Visibility minimums will not be lower
          that 3/4
          mile.LOWER_THAN_3_4_MILE-Visibility minimums will be lower than 3/4
          mile.
      approach_category {String}:
          Specifies the approach category that will be used to generate
          surfaces.A-The approach category A will be used. This is the
          default.B-The
          approach category B will be used.C-The approach category C will be
          used.D-The approach category D will be used.E-The approach category E
          will be used.
      approach_design_group {String}:
          Specifies the approach design group that will be used to generate
          surfaces.I-The approach design group I will be used. This is the
          default.II-The
          approach design group II will be used.III-The approach design group
          III will be used.IV-The approach design group IV will be used.V-The
          approach design group V will be used.VI-The approach design group VI
          will be used.
      aircraft_type {String}:
          Specifies whether surfaces will be generated with the small
          aircraft design matrix. This parameter only applies when the
          approach_category parameter is
          set to A or B.SMALL_AIRCRAFT-Surfaces will be generated with the small
          aircraft
          design matrix.NOT_SMALL_AIRCRAFT-Surfaces will not be generated with
          the small
          aircraft design matrix. This is the default.
      approach_guidance {String}:
          Specifies the type of approach guidance that will be used at the end
          of the runway.PRECISION_CAT_I-Precision Category I approach operations
          will be used
          for the runway. This is the default.PRECISION_CAT_II-Precision
          Category II approach operations will be
          used for the runway.PRECISION_CAT_IIIA-Precision Category III A
          approach operations will
          be used for the runway.PRECISION_CAT_IIIB-Precision Category III B
          approach operations will
          be used for the runway.PRECISION_CAT_IIIC-Precision Category III C
          approach operations will
          be used for the runway.PRECISION_CAT_IIID-Precision Category III D
          approach operations will
          be used for the runway.NON_VERTICAL-Nonvertical approach operations
          (nonprecision approach
          category) will be used for the runway.VERTICAL-Vertically guided
          approach operations will be used for the
          runway.VISUAL-Only visual approach operations will be used for the
          runway.
      runway_direction {String}:
          Specifies the end of the runway where the approach surface will be
          created.HIGH_END_TO_LOW_END-The approach surface will be created from
          the high
          end of the runway to the low end. If a displaced threshold point
          exists at the high end of the runway, that point will be honored when
          creating the OIS.LOW_END_TO_HIGH_END-The approach surface will be
          created from the low
          end of the runway to the high end. If a displaced threshold point
          exists at the low end of the runway, that point will be honored when
          creating the OIS.BOTH_END-The approach surface will be created from
          both the low end
          and high end of the runway.
      airport_elevation {Double}:
          The highest elevation on any of the runways of the airport. The value
          should be in the vertical coordinate system linear units of the target
          feature class. If no value is provided, the highest point from the
          in_features parameter value will be used.
      airport_control_point_feature_class {Feature Layer}:
          The point features containing an airport_elevation parameter feature,
          displaced threshold features, or both. Values provided for the
          airport_elevation parameter will take precedence over these point
          features.
      runway_end_features {Feature Layer}:
          The input runway end point features associated with each runway. The
          corresponding field values in this layer will override the values
          specified in the approach_category, approach_design_group, and
          approach_guidance parameters.
      last_low_light {Double}:
          The distance in feet of the Approach Lighting System (ALS) from the
          end of the low end of the runway. If no value is provided, it is
          assumed that there is no ALS at the low end of the runway. The unit of
          measurement is based on the input runway features.
      last_high_light {Double}:
          The distance in feet of the Approach Lighting System (ALS) from the
          end of the high end of the runway. If no value is provided, it is
          assumed that there is no ALS at the high end of the runway. The unit
          of measurement is based on the input runway features.
      custom_json_file {File}:
          The import configuration, in JSON format, that will create the custom
          OIS.

        """