# Generated documentation for module arcpy.gapro


class DetectIncidents(object):
    """
    Creates a layer that detects features that meet a given condition.
    """

    @property
    def description(self) -> str:
        return """

        DetectIncidents_gapro(input_layer, output, track_fields;track_fields..., start_condition, {end_condition}, {output_mode}, {time_boundary_split}, {time_boundary_reference})

        Creates a layer that detects features that meet a given condition.

     INPUTS:
      input_layer (Table View):
          The input features that contain potential incidents.
      track_fields (Field):
          A field or fields that will be used to identify unique tracks.
      start_condition (Calculator Expression):
          The condition that will be used to identify incidents. Expressions are
          written in Arcade and can include [+ - * / ] operators and multiple
          fields.
      end_condition {Calculator Expression}:
          The condition that will be used to end incidents. If no end condition
          is specified, incidents will end when the start condition is no longer
          true.
      output_mode {String}:
          Specifies the features that will be returned.ALL_FEATURES-All the
          input features will be returned. This is the
          default.INCIDENTS-Only features that were found to be incidents will
          be
          returned.
      time_boundary_split {Time Unit}:
          A time span to split the input data into for analysis. A time boundary
          allows you to analyze values within a defined time span. For example,
          if you use a time boundary of 1 day, and set the time boundary
          reference to January 1, 1980, tracks will be split at the beginning of
          every day.
      time_boundary_reference {Date}:
          The reference time used to split the input data into for analysis.
          Time boundaries will be created for the entire span of the data, and
          the reference time does not need to occur at the start. If no
          reference time is specified, January 1, 1970, is used.

     OUTPUTS:
      output (Feature Class / Table):
          A new output dataset that contains incidents.

        """