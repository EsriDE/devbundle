# Generated documentation for module arcpy.topographic


class PopulateMapSheetInfo(object):
    """
    Populates text in graphic elements on a map layout.
    """

    @property
    def description(self) -> str:
        return """

        PopulateMapSheetInfo_topographic(in_layout, area_of_interest, lookup_table)

        Populates text in graphic elements on a map layout.

     INPUTS:
      in_layout (Layout):
          The input layout that contains graphic elements with tagged text
          strings to be updated.
      area_of_interest (Feature Layer):
          A feature layer with a selection set containing one AOI feature. This
          parameter only accepts only polygon features. The tool writes
          attribute values from this feature to tagged text strings in defense-
          specific graphic elements.
      lookup_table (Table View):
          An input table that contains theandfields.
          Field_NameDM_Tag

        """