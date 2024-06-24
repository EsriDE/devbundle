# Generated documentation for module arcpy.indoors


class UpdateOccupantFeatures(object):
    """
    Updates the Occupants feature class that conforms to the ArcGIS Indoors Information Model.
    """

    @property
    def description(self) -> str:
        return """

        UpdateOccupantFeatures_indoors(target_occupant_features, {in_unit_features}, {in_occupant_table}, {occupant_id_from_target_occupant_features}, {occupant_id_from_input_table}, {unit_id_from_units_features}, {unit_id_from_input_table;unit_id_from_input_table...}, {occupant_attributes_mapping}, {allow_insert}, {allow_delete}, {home_office_identifier})

        Updates the Occupants feature class that conforms to the ArcGIS
        Indoors Information Model.

     INPUTS:
      target_occupant_features (Feature Layer):
          The target feature layer, feature class, or feature service to which
          occupant records will be added, updated, or deleted. The input must
          contain unique values that identify each occupant and must conform to
          the Occupants feature class in the Indoors model.
      in_unit_features {Feature Layer}:
          The input polygon features representing building spaces that may be
          occupied. The input must be a feature layer, feature class, or feature
          service that conforms to the Units feature class in the Indoors model.
          The centroid of each space will be used as the point location of the
          occupant or occupants.
      in_occupant_table {Table View}:
          The input table that contains information about building occupants.The
          input table must be a geodatabase table, a sheet in a Microsoft
          Excel workbook (.xls or .xlsx file), a comma-delimited text file
          (.csv), or an OLE DB table.
      occupant_id_from_target_occupant_features {Field}:
          The field in the target_occupant_features parameter value that will be
          used as the primary key to associate occupants with the
          in_occupant_table parameter values. The field values must be unique.
      occupant_id_from_input_table {Field}:
          The field in the in_occupant_table parameter value that will be used
          as the primary key to associate occupants with the
          target_occupant_features parameter values. The field values must be
          unique.
      unit_id_from_units_features {Field}:
          The field in the in_unit_features parameter value that stores the
          unique space identification information that will match the unit
          identifier from the in_occupant_table parameter value. The field
          values must be unique.
      unit_id_from_input_table {Field}:
          The field or fields in the in_occupant_table parameter value that will
          be used as the primary key to associate occupant space assignment with
          the in_unit_features parameter value. If a field value is empty, the
          occupant will be loaded as unassigned.This parameter supports multiple
          fields from an input occupant table
          that stores more than one space assignment of an occupant. Only the
          fields provided will be used to update the Occupants feature class.If
          no parameter value is provided, the occupant's seating assignments
          will not be updated in the Occupants feature class. Instead, the
          records in the Occupants feature class will be matched to records in
          the input occupant table, and attributes mapped in the
          occupant_attributes_mapping parameter will be updated.
      occupant_attributes_mapping {Field Mappings}:
          The attribute fields in the target_occupant_features parameter value
          that will be populated with field values from the in_occupant_table
          parameter value. The fields must exist in the target_occupant_features
          parameter value before running the tool. It is recommended that you
          map fields from the in_occupant_table parameter value to fields from
          the target_occupant_features parameter value that have the same field
          type.
      allow_insert {Boolean}:
          Specifies whether unmatched occupant records for the in_occupant_table
          parameter value will be added to the target occupant features
          layer.INSERT_OCCUPANTS-Unmatched occupant records will be added to the
          target occupant features layer. This is the
          default.NO_INSERT_OCCUPANTS-Unmatched occupant records will not be
          added to
          the target occupant features layer.
      allow_delete {Boolean}:
          Specifies whether unmatched occupant records for the in_occupant_table
          parameter value will be deleted from the target occupant features
          layer.DELETE_OCCUPANTS-Unmatched occupant records will be deleted from
          the
          target occupant features layer. This is the
          default.NO_DELETE_OCCUPANTS-Unmatched occupant records will not be
          deleted
          from the target occupant features layer.
      home_office_identifier {SQL Expression}:
          A SQL query that defines the field and field value from the input
          occupant table that indicates an occupant is assigned to a home
          office.

        """