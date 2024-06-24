# Generated documentation for module arcpy.intelligence


class PointsToTrackSegments(object):
    """
    Converts time-enabled sequences of input point data, such as GPS points, to a series of output paths.
    """

    @property
    def description(self) -> str:
        return """

        PointsToTrackSegments_intelligence(in_features, date_field, out_feature_class, {group_field}, {include_velocity}, {out_point_feature_class}, {error_on_duplicate_timestamps}, {keep_input_fields})

        Converts time-enabled sequences of input point data, such as GPS
        points, to a series of output paths.

     INPUTS:
      in_features (Feature Layer):
          The point features as point positions along the tracks to be created.
      date_field (Field):
          The date field that will be used to order the in_features points.
      group_field {Field}:
          A field from the in_features parameter that will be used to group the
          input points. Each unique group will create a separate track.
      include_velocity {Boolean}:
          Specifies whether output velocity fields (,,, and) will be
          included in the out_feature_class parameter value.
          speed_mpsspeed_mphspeed_kphspeed_kntINCLUDE_VELOCITY-Output velocity
          fields will be included in the
          output. This is the default.EXCLUDE_VELOCITY-Output velocity fields
          will not be included in the
          output.
      error_on_duplicate_timestamps {Boolean}:
          Specifies whether duplicate time stamps in the date_field parameter
          value or in each group in the group_field parameter value will be
          accepted or cause the tool to
          fail.ERROR_DUPLICATE_TIMESTAMPS-Duplicate time stamps will cause the
          tool
          to fail. This is the default.
          ALLOW_DUPLICATE_TIMESTAMPS-Duplicate time stamps will be
          accepted. The sequence of the duplicate time stamps is based on
          thevalue. ObjectID
      keep_input_fields {Boolean}:
          Specifies whether fields will be transferred from the in_features
          parameter value to the out_point_feature_class parameter
          value.KEEP_INPUT_FIELDS-Fields will be transferred from the
          in_features
          parameter value to the out_point_feature_class parameter
          value.DISCARD_INPUT_FIELDS-Fields will not be transferred from the
          in_features parameter value to the out_point_feature_class parameter
          value. This is the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output track line features.
      out_point_feature_class {Feature Class}:
          The output point features. The output will include afield that
          contains the order that will be used for the path created in the
          out_feature_class parameter. SEQUENCE

        """