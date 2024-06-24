# Generated documentation for module arcpy.ba


class AnalyzeMarketAreaGap(object):
    """
    Generates a layer that displays the gap between total customers and expected customers.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeMarketAreaGap_ba(customer_layer, target_profile, base_profile, geography_level, out_feature_class, target_group, core_target, developmental_target, {boundary_layer}, {create_report}, {report_title}, {report_folder}, {report_format;report_format...})

        Generates a layer that displays the gap between total customers and
        expected customers.

     INPUTS:
      customer_layer (Feature Layer):
          A point layer representing customers.
      target_profile (File):
          A segmentation profile representing the segments to be analyzed. The
          target profile usually represents your customer segmentation profile.
      base_profile (File):
          A segmentation profile representing the base profile segments. This is
          the segmentation used for comparison. The base profile usually
          represents your market area segmentation profile.
      geography_level (String):
          The geography level that will be used to define the market area gap
          analysis layer.
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
      boundary_layer {Feature Layer}:
          The boundary that determines the layer extent. If no value is
          provided, the entire country will be used.
      create_report {Boolean}:
          Specifies whether a gap analysis report will be
          created.CREATE_REPORT-A gap analysis report will be
          created.DO_NOT_CREATE_REPORT-A gap analysis report will not be
          created. This
          is the default.
      report_title {String}:
          The title of the report.
      report_folder {Folder}:
          The output location where the report will be saved.
      report_format {String}:
          The report output format. The default value is PDF. Additional
          available formats are XLSX, HTML, CSV, and PAGX.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the market area gap analysis.

        """