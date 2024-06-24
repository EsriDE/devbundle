# Generated documentation for module arcpy.na


class UpdateByAlternateIDFields(object):
    """
    Updates all the edge references in turn feature classes using an alternate ID field. This tool should be used after making edits to the input line features that are referenced by the turn features to synchronize the turn features based on the alternate ID fields.
    """

    @property
    def description(self) -> str:
        return """

        UpdateByAlternateIDFields_na(in_network_dataset, alternate_ID_field_name)

        Updates all the edge references in turn feature classes using an
        alternate ID field. This tool should be used after making edits to the
        input line features that are referenced by the turn features to
        synchronize the turn features based on the alternate ID fields.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset whose turn feature classes are being updated by
          their alternate ID fields.
      alternate_ID_field_name (String):
          The name of the alternate ID field on the edge feature sources of the
          network dataset. All edge feature sources referenced by turns must
          have the same name for the alternate ID field.

        """