# Generated documentation for module arcpy.maritime


class ParseS58LogFile(object):
    """
    Parses log files produced by the Validate S-57 File tool and third- party validation software against S-58 (recommended ENC validation checks). Critical errors and warnings are imported as records in a Data Reviewer table.
    """

    @property
    def description(self) -> str:
        return """

        ParseS58LogFile_maritime(in_s58_log_file, in_s57_file, in_production_database_workspace, in_reviewer_workspace, reviewer_session, {in_update_cells;in_update_cells...})

        Parses log files produced by the Validate S-57 File tool and third-
        party validation software against S-58 (recommended ENC validation
        checks). Critical errors and warnings are imported as records in a
        Data Reviewer table.

     INPUTS:
      in_s58_log_file (File):
          The S-58 log file that contains validation errors. It can be an *.S58,
          *.ANL, or *.VLD file.
      in_s57_file (File):
          The base cell file (*.000) from which the validation result was
          produced. The name of the ENC cell referenced in this parameter must
          match the name of the ENC cell referenced in the validation log file.
      in_production_database_workspace (Workspace):
          The workspace to validate and correct. This workspace contains the
          data used to generate the S-57 format file.
      in_reviewer_workspace (Workspace):
          The path to the Data Reviewer workspace where the features or table
          records will be written. A Data Reviewer workspace must be created for
          each ENC product.
      reviewer_session (String):
          An existing Data Reviewer session.
      in_update_cells {File}:
          The cell files (*.001 - *.999) that will be updated.

        """