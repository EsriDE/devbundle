# Generated documentation for module arcpy.aviation


class ReportAviationChartChanges(object):
    """
    Compares feature classes in two enterprise geodatabase versions and returns the differences in a report. You can filter the reported changes to determine which charts are affected by the differing data sources. You can set filters based on areas of interest (AOI), definition queries, and Report Chart Changes preferences.
    """

    @property
    def description(self) -> str:
        return """

        ReportAviationChartChanges_aviation(aviation_workspace, base_version, comparison_version, report_preference, report_name, {aoi_features})

        Compares feature classes in two enterprise geodatabase versions and
        returns the differences in a report. You can filter the reported
        changes to determine which charts are affected by the differing data
        sources. You can set filters based on areas of interest (AOI),
        definition queries, and Report Chart Changes preferences.

     INPUTS:
      aviation_workspace (Workspace):
          The versioned enterprise ArcGIS Aviation Charting AIS geodatabase. The
          workspace cannot be a file geodatabase.
      base_version (String):
          The version of the ArcGIS Aviation Charting AIS geodatabase to be
          compared.
      comparison_version (String):
          The version of the ArcGIS Aviation Charting AIS geodatabase that will
          be compared to the base_version parameter value.
      report_preference (String):
          The Report Chart Changes preference setting from the preference table.
          This preference will define which feature classes will be included in
          the report.
      report_name (String):
          The unique name of the report, containing changes between the
          geodatabase versions.
      aoi_features {Feature Layer}:
          The boundary within which the features will be processed.

        """