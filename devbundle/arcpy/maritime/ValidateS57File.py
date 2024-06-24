# Generated documentation for module arcpy.maritime


class ValidateS57File(object):
    """
    Validates an ENC, IENC, or bIENC file and generates an .S58 file and a shapefile as a result.
    """

    @property
    def description(self) -> str:
        return """

        ValidateS57File_maritime(in_s57_file, out_directory, {in_update_cells;in_update_cells...}, {regional_rules}, {in_ignore_list}, {exclude_shapefile})

        Validates an ENC, IENC, or bIENC file and generates an .S58 file and a
        shapefile as a result.

     INPUTS:
      in_s57_file (File):
          The base cell file (*.000).
      out_directory (Folder):
          The location where the validated S-57 log will be created.
      in_update_cells {File}:
          The update cell files (*.001 - *.999).
      regional_rules {String}:
          Specifies the region that will be used to set the Recommended Inland
          ENC Validation Checks for that region.For IENC and bIENC cells, some
          validation rules don't apply in certain
          regions, or they check for different objects and
          attribution.BR-Brazilian validation rules will be applied.EU-European
          validation
          rules will be applied.RU-Russian Federation validation rules will be
          applied.US-United States validation rules will be applied.
      in_ignore_list {File}:
          A text file containing a list of checks to ignore in the output log
          file.
      exclude_shapefile {Boolean}:
          Specifies whether a shapefile will be generated.EXCLUDE_SHAPEFILE-A
          shapefile will not be generated. Only the .s58
          file will be created.DO_NOT_EXCLUDE_SHAPEFILE-A shapefile will be
          generated, along with the
          .s58 file. This is the default.

        """