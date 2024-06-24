# Generated documentation for module arcpy.management


class AnalyzeToolsForPro(object):
    """
    Analyzes Python scripts and custom geoprocessing tools and toolboxes for functionality that is not supported in ArcGIS Pro.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeToolsForPro_management(input, {report})

        Analyzes Python scripts and custom geoprocessing tools and toolboxes
        for functionality that is not supported in ArcGIS Pro.

     INPUTS:
      input (Toolbox / String / File):
          The input can be a geoprocessing toolbox, Python file, or a tool
          name.If a tool name is specified, the tool will need to be loaded
          first
          using the arcpy.ImportToolbox function to be recognized. Tool names
          should include the toolbox alias.

     OUTPUTS:
      report {File}:
          An output text file that includes all issues.

        """