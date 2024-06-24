# Generated documentation for module arcpy.ba


class GenerateSurveyReportForProfile(object):
    """
    Displays characteristics from the consumer survey data for your target profile to determine customer lifestyle habits and preferences.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSurveyReportForProfile_ba(target_profile, base_profile, survey_category, report_folder, {sort_column}, {sort_order}, {report_title}, {report_format;report_format...})

        Displays characteristics from the consumer survey data for your target
        profile to determine customer lifestyle habits and preferences.

     INPUTS:
      target_profile (File):
          A segmentation profile representing the segments to be analyzed. The
          target profile usually represents your customer segmentation profile.
      base_profile (File):
          A segmentation profile representing the base profile segments. This is
          the segmentation used for comparison. The base profile usually
          represents your market area segmentation profile.
      survey_category (String):
          A category that contains characteristics from the consumer survey.
      report_folder (Folder):
          The output location where the report will be saved.
      sort_column {String}:
          Specifies the column to use to sort the report.EXPECTED_NUMBER-Sort is
          based on counts-for example, number of adults.
          This is the default.INDEX-Sort is based on rank.
      sort_order {String}:
          Specifies the order of the report, based on the sort column, in
          ascending or descending order.ASCENDING-Sort in ascending
          order.DESCENDING-Sort in descending order.
          This is the default.
      report_title {String}:
          The title of the report.
      report_format {String}:
          The report output format. The default value is PDF. Additional
          available formats are XLSX, HTML, CSV, and PAGX.

        """