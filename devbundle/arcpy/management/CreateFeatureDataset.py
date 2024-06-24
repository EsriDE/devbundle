# Generated documentation for module arcpy.management


class CreateFeatureDataset(object):
    """
    Creates a feature dataset in the output location: an existing enterprise, file, or mobile geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateFeatureDataset_management(out_dataset_path, out_name, {spatial_reference})

        Creates a feature dataset in the output location: an existing
        enterprise, file, or mobile geodatabase.

     INPUTS:
      out_dataset_path (Workspace):
          The enterprise, file, or mobile geodatabase where the output feature
          dataset will be created.
      out_name (String):
          The name of the feature dataset to be created.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. You can
          specify the spatial reference in the following ways:        Enter the
          path to a .prj file, such as
          C:/workspace/watershed.prj.Reference a feature class or feature
          dataset whose spatial reference
          you want to apply, such as
          C:/workspace/myproject.gdb/landuse/grassland.Define a spatial
          reference object before using this tool, such as sr =
          arcpy.SpatialReference("Sinusoidal (Africa)"), which you then use as
          the spatial reference parameter.

        """