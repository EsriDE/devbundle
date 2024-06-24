# Generated documentation for module arcpy.locref


class ConfigureLookupTable(object):
    """
    Configures a lookup table for one or more fields used in a multifield route ID.
    """

    @property
    def description(self) -> str:
        return """

        ConfigureLookupTable_locref(in_feature_class, lookup_table, field_applied_to, lookup_key, {lookup_display}, {allow_any_lookup_value})

        Configures a lookup table for one or more fields used in a multifield
        route ID.

     INPUTS:
      in_feature_class (Feature Layer):
          The input LRS Network feature class in which the lookup table will be
          configured. The network must have a multifield route ID.
      lookup_table (Table View):
          A table that contains a list of street names and their corresponding
          GNIS codes. It can be a stand-alone table or reside in an SDE.
      field_applied_to (String):
          The route ID field in the LRS Network in which the lookup_table will
          be configured.
      lookup_key (String):
          The key field in the lookup_table.
      lookup_display {String}:
          The lookup_table description field. This field appears in the text box
          for the multifield route ID.
      allow_any_lookup_value {Boolean}:
          Specifies whether a value that is not in the lookup table can be
          added. The lookup_display parameter cannot be configured when this
          option is checked.DO_NOT_ALLOW_ANY_VALUE-Allow a value to be
          configured when one is not
          present in the table.ALLOW_ANY_VALUE-Don't allow a lookup display
          value to be configured.
          This is the default.

        """