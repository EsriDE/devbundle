# Generated documentation for module arcpy.ba


class GenerateSurveyReportForTargets(object):
    """
    Displays the top characteristics, in each of the selected survey categories, of your Core and Developmental target groups, as well as your overall customer profile.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSurveyReportForTargets_ba(target_profile, target_group, core_target, developmental_target, report_folder, {report_type}, {survey_categories;survey_categories...}, {report_title}, {report_format;report_format...})

        Displays the top characteristics, in each of the selected survey
        categories, of your Core and Developmental target groups, as well as
        your overall customer profile.

     INPUTS:
      target_profile (File):
          A segmentation profile representing the segments to be analyzed. The
          target profile usually represents your customer segmentation profile.
      target_group (File):
          A collection of segments grouped into targets. Targets represent
          segments that are selected based on similar characteristics-for
          example, segments that have high index and percent composition.
      core_target (String):
          A group of segments that make up a large percentage of your customer
          base and have an above average index, indicating likelihood to be a
          customer.
      developmental_target (String):
          A group of segments that make up a significant percentage of your
          customers and of the market area but do not have an above average
          index.
      report_folder (Folder):
          The output location where the report will be saved.
      report_type {String}:
          Specifies the survey categories to be added to the
          report.UNDERSTANDING_YOUR_TARGET-Media-related characteristics-for
          example,
          reading, watching, and listening
          related.DEVELOPING_MARKET_STRATEGIES-Leisure-related
          characteristics-for
          example, leisure, sports, and travel.CUSTOM-User-defined
          characteristics. This is the default.
      survey_categories {String}:
          A category that contains the characteristics from the consumer survey.
      report_title {String}:
          The title of the report.
      report_format {String}:
          The report output format. The default value is PDF. Additional
          available formats are XLSX, HTML, CSV, and PAGX.

        """