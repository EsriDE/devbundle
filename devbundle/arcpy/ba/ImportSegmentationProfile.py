# Generated documentation for module arcpy.ba


class ImportSegmentationProfile(object):
    """
    Generates a segmentation profile from a table.
    """

    @property
    def description(self) -> str:
        return """

        ImportSegmentationProfile_ba(in_table, segmentation_base, out_profile, segment_id_field, count_field, {total_volume_field})

        Generates a segmentation profile from a table.

     INPUTS:
      in_table (Table View):
          The input table with segmentation information.
      segmentation_base (String):
          The segmentation base for the profile being created. Available options
          are provided by the segmentation dataset being used.
      segment_id_field (Field):
          A string field that contains the segmentation code.
      count_field (Field):
          A numeric field that contains segment count information.
      total_volume_field {Field}:
          A numeric field that contains volume information.

     OUTPUTS:
      out_profile (File):
          The name of the segmentation file that will be created.

        """