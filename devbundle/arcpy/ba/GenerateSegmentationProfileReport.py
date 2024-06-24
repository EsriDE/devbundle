# Generated documentation for module arcpy.ba


class GenerateSegmentationProfileReport(object):
    """
    Creates a report that displays segments of your customers and compares them to the study area (base profile).
    """

    @property
    def description(self) -> str:
        return """

        GenerateSegmentationProfileReport_ba(target_profile, base_profile, {report_title}, {report_folder}, {report_format;report_format...})

        Creates a report that displays segments of your customers and compares
        them to the study area (base profile).

     INPUTS:
      target_profile (File):
          A segmentation profile representing the segments to be profiled. The
          target profile usually represents your customer segmentation profile.
      base_profile (File):
          A segmentation profile representing the base profile segments. This is
          the segmentation used for comparison. The base profile usually
          represents your market area segmentation profile.
      report_title {String}:
          The title of the report.
      report_folder {Folder}:
          The output location where the report will be saved.
      report_format {String}:
          The report output format. The default value is PDF. Additional
          available formats are XLSX, HTML, CSV, and PAGX.

        """