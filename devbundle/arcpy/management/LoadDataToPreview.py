# Generated documentation for module arcpy.management


class LoadDataToPreview(object):
    """
    Uses a Data Loading Workspace to load data from a source to a preview geodatabase. Use this tool to preview the results before loading data to the target schema.
    """

    @property
    def description(self) -> str:
        return """

        LoadDataToPreview_management(in_workbook, out_folder)

        Uses a Data Loading Workspace to load data from a source to a preview
        geodatabase. Use this tool to preview the results before loading data
        to the target schema.

     INPUTS:
      in_workbook (File):
          The path to the Data Reference Workbook defining the data source,
          target, and mapping workbook paths.
      out_folder (Folder):
          The output folder where the preview geodatabase will be created.

        """