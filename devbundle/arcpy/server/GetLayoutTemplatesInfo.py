# Generated documentation for module arcpy.server


class GetLayoutTemplatesInfo(object):
    """
    Returns the content of layout templates in JSON format. Layout files (.pagx files) located in a folder are used as layout templates.
    """

    @property
    def description(self) -> str:
        return """

        GetLayoutTemplatesInfo_server({Layout_Templates_Folder}, {Layout_Item_ID})

        Returns the content of layout templates in JSON format. Layout files
        (.pagx files) located in a folder are used as layout templates.

     INPUTS:
      Layout_Templates_Folder {Folder}:
          The full path to the folder where the layout files (.pagx files) that
          will be used as layout templates are located. The default location is
          <install_directory>\Resources\ArcToolBox\Templates\ExportWebMapTemplat
          es.
      Layout_Item_ID {String}:
          The portal ID (in JSON format) of the layout item that will be used
          for templates. Use the format: {"id": "<portal-id>"}.

        """