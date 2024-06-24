# Generated documentation for module arcpy.management


class ConsolidateToolbox(object):
    """
    Consolidates one or more toolboxes into a specified output folder.
    """

    @property
    def description(self) -> str:
        return """

        ConsolidateToolbox_management(in_toolbox;in_toolbox..., output_folder, {version})

        Consolidates one or more toolboxes into a specified output folder.

     INPUTS:
      in_toolbox (Toolbox):
          The toolboxes to be consolidated.
      version {String}:
          Specifies the version of the consolidated toolbox. Specifying a
          version allows toolboxes to be shared with previous versions of ArcGIS
          and supports backward compatibility.CURRENT-The consolidated folder
          will contain tools compatible with the
          version of the current release. This is the default.2.2-The
          consolidated folder will contain tools compatible with
          version 2.2.2.3-The consolidated folder will contain tools compatible
          with version
          2.3.2.4-The consolidated folder will contain tools compatible with
          version
          2.4.2.5-The consolidated folder will contain tools compatible with
          version
          2.5.2.6-The consolidated folder will contain tools compatible with
          version
          2.6.2.7-The consolidated folder will contain tools compatible with
          version
          2.7.2.8-The consolidated folder will contain tools compatible with
          version
          2.8.2.9-The consolidated folder will contain tools compatible with
          version
          2.9.3.0-The consolidated folder will contain tools compatible with
          version
          3.0.3.1-The consolidated folder will contain tools compatible with
          version
          3.1.3.2-The consolidated folder will contain tools compatible with
          version
          3.2.3.3-The consolidated folder will contain tools compatible with
          version
          3.3.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the consolidated toolbox.If the
          specified folder does not exist, a folder will be created.

        """