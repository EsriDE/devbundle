# Generated documentation for module arcpy.management


class LasDatasetStatistics(object):
    """
    Calculates or updates statistics for a LAS dataset and generates an optional statistics report.
    """

    @property
    def description(self) -> str:
        return """

        LasDatasetStatistics_management(in_las_dataset, {calculation_type}, {out_file}, {summary_level}, {delimiter}, {decimal_separator})

        Calculates or updates statistics for a LAS dataset and generates an
        optional statistics report.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed.
      calculation_type {Boolean}:
          Specifies whether statistics will be calculated for all lidar files or
          only for those that do not have statistics:SKIP_EXISTING_STATS-LAS
          files with up-to-date statistics will be
          skipped, and statistics will only be calculated for newly added LAS
          files or ones that were updated since the initial calculation. This is
          the default.OVERWRITE_EXISTING_STATS-Statistics will be calculated for
          all LAS
          files, including ones that have up-to-date statistics. This is useful
          if the LAS files were modified in an external application that went
          undetected by ArcGIS.
      summary_level {String}:
          Specify the type of summary contained in the report.DATASET-The report
          will summarize statistics for the entire LAS
          dataset. This is the default.LAS_FILES-The report will summarize
          statistics for the LAS files
          referenced by the LAS dataset.
      delimiter {String}:
          The delimiter that will be used to indicate the separation of entries
          in the columns of the text file table.SPACE-A space will be used to
          delimit field values. This is the
          default.COMMA-A comma will be used to delimit field values. This
          option is not
          applicable if the decimal separator is also a comma.
      decimal_separator {String}:
          The decimal character that will be used in the text file to
          differentiate the integer of a number from its fractional
          part.DECIMAL_POINT-A point will be used as the decimal character. This
          is
          the default.DECIMAL_COMMA-A comma will be used as the decimal
          character.

     OUTPUTS:
      out_file {Text File}:
          The output text file that will contain the summary of the LAS dataset
          statistics.

        """