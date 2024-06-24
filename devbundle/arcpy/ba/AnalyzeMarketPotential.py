# Generated documentation for module arcpy.ba


class AnalyzeMarketPotential(object):
    """
    Generates a layer that displays expected customers by a selected geography level.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeMarketPotential_ba(target_profile, base_profile, geography_level, out_feature_class, {boundary_layer}, {create_report}, {report_title}, {report_folder}, {report_format;report_format...})

        Generates a layer that displays expected customers by a selected
        geography level.

     INPUTS:
      target_profile (File):
          A segmentation profile representing the segments to be analyzed. The
          target profile usually represents your customer segmentation profile.
      base_profile (File):
          A segmentation profile representing the base profile segments. This is
          the segmentation used for comparison. The base profile usually
          represents your market area segmentation profile.
      geography_level (String):
          The geography level that will be used to define the market potential
          layer.
      boundary_layer {Feature Layer}:
          The boundary that determines the layer extent. If no value is
          provided, the entire country will be used.
      create_report {Boolean}:
          Specifies whether a market potential report will be
          created.CREATE_REPORT-A market potential report will be
          created.DO_NOT_CREATE_REPORT-A market potential report will not be
          created.
          This is the default.
      report_title {String}:
          The title of the report.
      report_folder {Folder}:
          The output location where the report will be saved.
      report_format {String}:
          The report output format. The default value is PDF. Additional
          available formats are XLSX, HTML, CSV, and PAGX.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the market potential analysis.

        """