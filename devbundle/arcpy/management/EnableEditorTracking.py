# Generated documentation for module arcpy.management


class EnableEditorTracking(object):
    """
    Enables editor tracking for a feature class, table, feature dataset, or relationship class in a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        EnableEditorTracking_management(in_dataset, {creator_field}, {creation_date_field}, {last_editor_field}, {last_edit_date_field}, {add_fields}, {record_dates_in})

        Enables editor tracking for a feature class, table, feature dataset,
        or relationship class in a geodatabase.

     INPUTS:
      in_dataset (Dataset / Topology / Network Dataset):
          The feature class, table, feature dataset, or relationship class in
          which editor tracking will be enabled.
      creator_field {String}:
          The name of the field that will store the names of users who create
          features or records. If this field already exists, it must be a string
          field.
      creation_date_field {String}:
          The name of the field that will store the date that features or
          records are created. If this field already exists, it must be a low
          precision date field.
      last_editor_field {String}:
          The name of the field that will store the names of users who last
          edited features or records. If this field already exists, it must be a
          string field.
      last_edit_date_field {String}:
          The name of the field that will store the date that features or
          records were last edited. If this field already exists, it must be a
          low precision date field.
      add_fields {Boolean}:
          Specifies whether fields will be added if they don't
          exist.NO_ADD_FIELDS-Fields will not be added. Fields specified must
          already
          exist in the in_dataset parameter value. This is the
          default.ADD_FIELDS-Fields will be added if they do not exist. You must
          specify
          the names of the fields to add in the creator_field,
          creation_date_field, last_editor_field, and last_edit_date_field
          parameters.
      record_dates_in {String}:
          Specifies the time format in which the created date and last edited
          date will be recorded.UTC-Dates will be recorded in UTC. This is the
          default.DATABASE_TIME-Dates will be recorded in the time zone in which
          the
          database is located.

        """