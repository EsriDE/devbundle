# Generated documentation for module arcpy.management


class BatchProject(object):
    """
    Changes the coordinate system of a set of input feature classes or feature datasets to a common coordinate system. To change the coordinate system of a single feature class or dataset use the Project tool.
    """

    @property
    def description(self) -> str:
        return """

        BatchProject_management(Input_Feature_Class_or_Dataset;Input_Feature_Class_or_Dataset..., Output_Workspace, {Output_Coordinate_System}, {Template_dataset}, {Transformation})

        Changes the coordinate system of a set of input feature classes or
        feature datasets to a common coordinate system. To change the
        coordinate system of a single feature class or dataset use the Project
        tool.

     INPUTS:
      Input_Feature_Class_or_Dataset (Feature Layer / Feature Dataset):
          The input feature classes or feature datasets whose coordinates are to
          be converted.
      Output_Workspace (Workspace / Feature Dataset):
          The location of each new output feature class or feature dataset.
      Output_Coordinate_System {Coordinate System}:
          The coordinate system to be used to project the inputs.Valid values
          are a SpatialReference object, a file with a .prj
          extension, or a string representation of a coordinate system.
      Template_dataset {Geodataset}:
          The feature class or the feature dataset used to specify the output
          coordinate system used for projection.
      Transformation {String}:
          The name of the geographic transformation to be applied to convert
          data between two geographic coordinate systems (datums).

        """