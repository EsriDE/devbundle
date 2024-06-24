# Generated documentation for module arcpy.edit


class TransferAttributes(object):
    """
    Finds where the source line features spatially match the target line features and transfers specified attributes from source features to matched target features.
    """

    @property
    def description(self) -> str:
        return """

        TransferAttributes_edit(source_features, target_features, transfer_fields;transfer_fields..., search_distance, {match_fields;match_fields...}, {out_match_table}, {transfer_rule_fields;transfer_rule_fields...})

        Finds where the source line features spatially match the target line
        features and transfers specified attributes from source features to
        matched target features.

     INPUTS:
      source_features (Feature Layer):
          The line features from which attributes will be transferred.
      target_features (Feature Layer):
          The line features to which attributes will be transferred. The
          transfer fields will be added to the target features.
      transfer_fields (Field):
          A list of source fields that will be transferred to target features.
          At least one field must be provided.
      search_distance (Linear Unit):
          The distance that will be used to search for match candidates. A
          distance must be specified and it must be greater than zero. You can
          choose a preferred unit. The default is the feature unit.
      match_fields {Value Table}:
          Lists of fields from source and target features. If provided, each
          pair of fields are checked for match candidates to help determine the
          right match.
      transfer_rule_fields {Value Table}:
          The rules that control which source feature will be used to transfer
          attributes from when multiple source features matched target features.
          The source feature that will be used for the transfer is determined by
          the specified rule fields and the ruling values, which are ranked from
          high to low priority as they appear in the specified list. If no rules
          are set, the longest of the multiple matched source features will be
          used for the transfer.Available rule types are as follows:MIN-The
          minimum value for an integer or date field. For a date field,
          use the most recent date.MAX-The maximum value for an integer or date
          field. For a date field,
          use the oldest date.A text or integer value that may exist in the
          source features.

     OUTPUTS:
      out_match_table {Table}:
          The output table containing complete feature matching information.

        """