# Generated documentation for module arcpy.ba


class SummaryReports(object):
    """
    Creates infographic and summary reports for a boundary layer using standard or custom templates.
    """

    @property
    def description(self) -> str:
        return """

        SummaryReports_ba(in_features, report_templates;report_templates..., reports_folder, {summarization_options}, {single_report}, {formats;formats...}, {store_id_field}, {store_name_field}, {store_address_field}, {store_latitude_field}, {store_longitude_field}, {ring_id_field}, {area_description_field}, {title}, {subtitle}, {report_per_feature}, {add_infographic_header}, {add_infographic_footer}, {add_infographic_data_source})

        Creates infographic and summary reports for a boundary layer using
        standard or custom templates.

     INPUTS:
      in_features (Feature Layer):
          The boundary layer containing one or more polygons that will be used
          to create reports.
      report_templates (String):
          One or more report templates that will be used to create the summary
          report. You must be signed in to ArcGIS Online or have Business
          Analyst Data installed.
      reports_folder (Folder):
          The output location where the summary reports will be saved.
      summarization_options {String}:
          Specifies how the data will be displayed in a
          report.INDIVIDUAL_FEATURES-Selected report templates will be returned
          for
          each individual trade area polygon. This is the
          default.WHOLE_LAYER-Selected report templates will be returned
          representing
          only the full extent of the trade
          area.BOTH_FEATURES_AND_LAYER-Selected report templates will be
          returned for
          both individual features and the whole layer.
      single_report {Boolean}:
          Specifies whether a single output will be created or a separate file
          will be created for each report.CREATE_SINGLE_REPORT-All reports will
          be combined into a single
          output.CREATE_REPORT_PER_TEMPLATE-A separate file will be created for
          each
          selected report. This is the default.
      formats {String}:
          The report output format. The default value is PDF.
      store_id_field {Field}:
          The field that will be used to group data for each site in output
          reports. These field values are not displayed in the header.
      store_name_field {Field}:
          The field values that will be displayed in the output report headers
          that identify the site corresponding to each polygon's data.
      store_address_field {Field}:
          The store address associated with each trade area.
      store_latitude_field {Field}:
          The field that will contain the latitude coordinates (y field).
      store_longitude_field {Field}:
          The field that will contain the longitude coordinates (x field).
      ring_id_field {Field}:
          The field that will control the presentation order of data for inputs
          with multiple polygons per site.
      area_description_field {Field}:
          The field that will be displayed as the output template header with
          values corresponding to each input polygon's data.
      title {String}:
          The title in the report header.
      subtitle {String}:
          The subtitle in the report header. The default value is Prepared by
          Business Analyst Pro.
      report_per_feature {Boolean}:
          Specifies whether a single report or multiple reports will be
          created.CREATE_REPORT_PER_FEATURE-A report will be created per
          feature.CREATE_SINGLE_REPORT-A single report will be created. This is
          the
          default.
      add_infographic_header {Boolean}:
          Specifies whether a header will be added to the
          infographic.ENABLE_INFOGRAPHIC_HEADER-A header will be added to the
          infographic.DISABLE_INFOGRAPHIC_HEADER-A header will not be added to
          the
          infographic. This is the default.
      add_infographic_footer {Boolean}:
          Specifies whether a footer will be added to the
          infographic.ENABLE_INFOGRAPHIC_FOOTER-A footer will be added to the
          infographic.DISABLE_INFOGRAPHIC_FOOTER-A footer will not be added to
          the
          infographic. This is the default.
      add_infographic_data_source {Boolean}:
          Specifies whether the data source will be added to the
          infographic.ENABLE_INFOGRAPHIC_DATA_SOURCE-The data source will be
          added to the
          infographic.DISABLE_INFOGRAPHIC_DATA_SOURCE-The data source will not
          be added to
          the infographic. This is the default.

        """