# Generated documentation for module arcpy.management


class SaveToolboxToVersion(object):
    """
    Analyzes and saves a toolbox for use with a specific version of ArcGIS software.
    """

    @property
    def description(self) -> str:
        return """

        SaveToolboxToVersion_management(in_toolbox, version, out_toolbox, {missing_tool}, {missing_param}, {invalid_param_value})

        Analyzes and saves a toolbox for use with a specific version of ArcGIS
        software.

     INPUTS:
      in_toolbox (Toolbox):
          The input toolbox (.tbx or .atbx file) that will be analyzed and
          saved. The file will not be modified.The Python toolbox format (.pyt
          file) is not supported as an input.
      version (String):
          Specifies the software version that will be used for toolbox
          compatibility issue analysis.10.6.0-ArcGIS Desktop 10.6.0 will be used
          for toolbox compatibility
          issue analysis. The output toolbox will be saved to this
          version.10.7.0-ArcGIS Desktop 10.7.0 will be used for toolbox
          compatibility
          issue analysis. The output toolbox will be saved to this
          version.10.8.0-ArcGIS Desktop 10.8.0 will be used for toolbox
          compatibility
          issue analysis. The output toolbox will be saved to this
          version.10.8.2-ArcGIS Desktop 10.8.2 will be used for toolbox
          compatibility
          issue analysis. The output toolbox will be saved to this
          version.2.2-ArcGIS Pro 2.2 will be used for toolbox compatibility
          issue
          analysis. The output toolbox will be saved to this version.2.3-ArcGIS
          Pro 2.3 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.2.4-ArcGIS
          Pro 2.4 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.2.5-ArcGIS
          Pro 2.5 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.2.6-ArcGIS
          Pro 2.6 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.2.7-ArcGIS
          Pro 2.7 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.2.8-ArcGIS
          Pro 2.8 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.2.9-ArcGIS
          Pro 2.9 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.3.0-ArcGIS
          Pro 3.0 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.3.1-ArcGIS
          Pro 3.1 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.3.2-ArcGIS
          Pro 3.2 will be used for toolbox compatibility issue
          analysis. The output toolbox will be saved to this version.
      missing_tool {Boolean}:
          Specifies whether an error will be produced if a tool is encountered
          that is not present at the target version.ERROR_ON_MISSING_TOOL-An
          error will be produced and the output toolbox
          will not be created. This is the default.WARN_ON_MISSING_TOOL-A
          warning message will be produced and the output
          toolbox will be created. For model tools, the problematic tool will be
          removed from the model, which will require manual editing.
      missing_param {Boolean}:
          Specifies whether an error will be produced if a parameter is
          encountered that is not present at the target version and that
          parameter has a value that is not its default
          value.ERROR_ON_MISSING_REQUIRED_PARAM-An error will be produced and
          the
          output toolbox will not be created. This is the
          default.WARN_ON_MISSING_REQUIRED_PARAM-A warning message will be
          produced, the
          parameter will be removed from the model, and the output toolbox will
          be created.
      invalid_param_value {Boolean}:
          Specifies whether an error will be produced if a parameter value is
          encountered that is not present in its parameter filter at the target
          version.ERROR_ON_INVALID_PARAM_VALUE-An error will be produced and the
          output
          toolbox will not be created. This is the
          default.WARN_ON_INVALID_PARAM_VALUE-A warning message will be produced
          and the
          output toolbox will be created. The output toolbox will produce an
          error with a value that is not in domain or is invalid.

     OUTPUTS:
      out_toolbox (Toolbox):
          The toolbox that will be created for use with ArcGIS software of the
          specified version parameter value.

        """