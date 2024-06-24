# Generated documentation for module arcpy.intelligence


class FindCotravelers(object):
    """
    Extracts unique identifiers that are moving through space and time at specified intervals in a point track dataset.
    """

    @property
    def description(self) -> str:
        return """

        FindCotravelers_intelligence(input_features, out_featureclass, id_field, {search_distance}, {time_difference}, {input_type}, {secondary_features}, {secondary_id_field}, {create_summary_table}, {out_summary_table}, {include_min_cotraveling_duration}, {min_cotraveling_duration})

        Extracts unique identifiers that are moving through space and time at
        specified intervals in a point track dataset.

     INPUTS:
      input_features (Feature Layer):
          The time-enabled features representing the known identifier that will
          be used to find cotravelers. The unique identifiers, time stamps, and
          locations will be transferred to the output layer to assist with
          calculating the time and spatial separation.
      id_field (Field):
          A field from the input_features parameter that will be used to obtain
          the unique identifiers per point track. The field will be copied to
          the output feature class.
      search_distance {Linear Unit}:
          The maximum distance that can separate features before they are
          considered not to be cotraveling features. The default is 100 feet.
      time_difference {Time Unit}:
          The maximum time difference that can separate features before they are
          considered not to be cotraveling features. The default is 10 seconds.
      input_type {String}:
          Specifies whether cotravelers will be detected in one feature class or
          across two.ONE_FEATURECLASS-Cotravelers will be detected in one
          feature class.
          This is the default.TWO_FEATURECLASSES-Cotravelers will be detected
          across two feature
          classes.
      secondary_features {Feature Layer}:
          A second feature class that will identify cotravelers.
          Potential cotravelers will be evaluated using the following:
          Cotravelers are cotraveling inside the input features.Cotravelers are
          cotraveling inside the secondary features.Cotravelers are cotraveling
          between the input features and secondary
          features.
      secondary_id_field {Field}:
          A field from the secondary_features parameter that will be used to
          obtain the unique identifiers per point track. The field will be
          copied to the output feature class.
      create_summary_table {Boolean}:
          Specifies whether an output summary table will be
          created.NO_SUMMARY_TABLE-A summary table will not be created. This is
          the
          default.CREATE_SUMMARY_TABLE-A summary table will be created.
      include_min_cotraveling_duration {Boolean}:
          Specifies whether a filter that only returns cotravelers who
          meet a minimum time of traveling together will be applied.
          Checked-The minimum cotraveler duration filter will be
          applied.Unchecked-The minimum cotraveler duration filter will not be
          applied.
          This is the default.Specifies whether a minimum cotraveler duration
          filter will be
          applied.MIN_COTRAVELING_DURATION-The minimum cotraveler duration
          filter will
          be applied.NO_MIN_COTRAVELING_DURATION-The minimum cotraveler duration
          filter
          will not be applied. This is the default.
      min_cotraveling_duration {Time Unit}:
          The minimum amount of time that two features must be moving through
          space and time together before they will be considered cotravelers.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class that will contain the point track segments
          identified as cotraveling with the input source layers. This feature
          class will include the source with which the specified point track
          segment is associated. Time and spatial separation will be calculated
          for each point track feature.
      out_summary_table {Table}:
          The output table that will store the summary information. This
          parameter is only enabled when the create_summary_table parameter
          value is set to CREATE_SUMMARY_TABLE. Output files must be tables in a
          file geodatabase, text files, or comma-separated value files (.csv).

        """