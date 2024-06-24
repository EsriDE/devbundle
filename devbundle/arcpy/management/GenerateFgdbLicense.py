# Generated documentation for module arcpy.management


class GenerateFgdbLicense(object):
    """
    Generates a license file (.sdlic) for displaying the contents in a licensed file geodatabase created by the Generate Licensed File Geodatabase tool.
    """

    @property
    def description(self) -> str:
        return """

        GenerateFgdbLicense_management(in_lic_def_file, out_lic_file, {allow_export}, {exp_date})

        Generates a license file (.sdlic) for displaying the contents in a
        licensed file geodatabase created by the Generate Licensed File
        Geodatabase tool.

     INPUTS:
      in_lic_def_file (File):
          The license definition file (.licdef) created by the Generate Licensed
          File Geodatabase tool.
      allow_export {String}:
          Specifies whether the export of vector data will be
          allowed.DENY_EXPORT-Vector data cannot be exported with the data
          license file
          (.sdlic) installed. This is the default.ALLOW_EXPORT-Vector data can
          be exported with the data license file
          (.sdlic) installed.
      exp_date {Date}:
          The expiration date of the data license file, after which the file
          geodatabase's contents can no longer be displayed. The default value
          is empty (blank), which means the data license file will never expire.

     OUTPUTS:
      out_lic_file (File):
          The license file (.sdlic) for distribution.

        """