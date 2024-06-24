# Generated documentation for module arcpy.gapro


class CalculateField(object):
    """
    Creates a layer with calculated field values.
    """

    @property
    def description(self) -> str:
        return """

        CalculateField_gapro(input_layer, output, field_to_calculate, {field_name}, {existing_field}, {field_type}, expression, {track_aware}, {track_fields;track_fields...}, {time_boundary_split}, {time_boundary_reference})

        Creates a layer with calculated field values.

     INPUTS:
      input_layer (Table View):
          The input features that will have a field calculated.
      field_to_calculate (String):
          Specifies whether values will be calculated for a newly created field
          or an existing field.NEW_FIELD-Values will be calculated for a newly
          created
          field.EXISTING_FIELD-Values will be calculated for an existing field.
      field_name {String}:
          The new field that will have values calculated.
      existing_field {Field}:
          The existing field that will have values calculated.
      field_type {String}:
          Specifies the field type for the calculated field.STRING-The new field
          will be of type text.INTEGER-The new field will
          be of type integer.FLOAT-The new field will be of type float.DATE-
          The new field will be of type date.
      expression (Calculator Expression):
          Calculates values in the field. Expressions are written in Arcade and
          can include operators and multiple fields. Calculated values are
          applied in the units of the spatial reference of the input unless you
          are using a geographic coordinate system, in which case they will be
          in meters.
      track_aware {Boolean}:
          Specifies whether the expression will use a track-aware
          expression.TRACK_AWARE-The expression will use a track-aware
          expression, and a
          track field must be specified.NOT_TRACK_AWARE-The expression will not
          use a track-aware expression.
          This is the default.
      track_fields {Field}:
          One or more fields that will be used to identify unique tracks.
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
          A new dataset with calculated fields.

        """