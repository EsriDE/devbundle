# Generated documentation for module arcpy.na


class PopulateAlternateIDFields(object):
    """
    Creates and populates additional fields on the turn feature classes that reference the edges by alternate IDs. The alternate IDs allow for another set of IDs that can help maintain the integrity of the turn features in case the source edges are being edited.
    """

    @property
    def description(self) -> str:
        return """

        PopulateAlternateIDFields_na(in_network_dataset, alternate_ID_field_name)

        Creates and populates additional fields on the turn feature classes
        that reference the edges by alternate IDs. The alternate IDs allow for
        another set of IDs that can help maintain the integrity of the turn
        features in case the source edges are being edited.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset whose turn feature classes are to receive
          alternate ID fields. The fields will be created on all of the turn
          feature classes added as a turn source to the network dataset.
      alternate_ID_field_name (String):
          The name of the alternate ID field on the edge feature sources of the
          network dataset. All edge feature sources referenced by turns must
          have the same name for the alternate ID field.

        """