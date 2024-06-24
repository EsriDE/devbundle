# Generated documentation for module arcpy.server


class GetReportTemplatesInfo(object):
    """
    Returns the content of report files and templates in JSON format. Report files (.rptx) and report templates (.rptt) are used to store report definitions.
    """

    @property
    def description(self) -> str:
        return """

        GetReportTemplatesInfo_server({Report_Templates_Folder}, {Report_Item_ID})

        Returns the content of report files and templates in JSON format.
        Report files (.rptx) and report templates (.rptt) are used to store
        report definitions.

     INPUTS:
      Report_Templates_Folder {Folder}:
          The full path to the folder where the report files (.rptx or .rptt)
          that will be used as report templates are located. The default
          location is <install_directory>\Resources\ArcToolBox\Templates\ExportW
          ebMapTemplates.
      Report_Item_ID {String}:
          The portal ID (in JSON format) of the report item that will be used
          for the templates. Use the format {"id": "<portal-id>"}.

        """