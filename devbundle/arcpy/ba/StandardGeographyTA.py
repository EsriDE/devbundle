# Generated documentation for module arcpy.ba


class StandardGeographyTA(object):
    """
    Creates trade areas based on predefined named statistical areas. This tool does not consume credits.
    """

    @property
    def description(self) -> str:
        return """

        StandardGeographyTA_ba(geography_level, out_feature_class, {input_type}, {in_ids_table}, {geography_key_field}, {ids_list}, {summarize_duplicates}, {group_field}, {dissolve_output})

        Creates trade areas based on predefined named statistical areas. This
        tool does not consume credits.

     INPUTS:
      geography_level (String):
          The geography level that will be used to define the trade area.
      input_type {String}:
          Specifies whether the geography IDs will be from a table or a
          list.TABLE-The input IDs will be from a table.LIST-The input IDs will
          be
          from a list. This is the default.
      in_ids_table {Table View}:
          The input table with IDs that will be used to select geographies that
          will define the trade area.
      geography_key_field {Field}:
          A field with in_ids_table that identifies the records that will be
          included in the output.
      ids_list {String}:
          The input list of comma-separated geography IDs.
      summarize_duplicates {Boolean}:
          Specifies whether duplicate fields in the table containing matching
          geography IDs will be summarized.SUMMARIZE_DUPLICATES-The numeric
          fields for all duplicate records will
          be summarized.USE_FIRST-The data of the first record will be appended.
          Other records
          will be ignored. This is the default.
      group_field {Field}:
          The field that will be used to perform a group by operation.
      dissolve_output {Boolean}:
          Specifies whether the output will be dissolved based on the
          group_field parameter value.DISSOLVE-The output will be
          dissolved.DONT_DISSOLVE-The output will
          not be dissolved. This is the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature containing the trade area.

        """