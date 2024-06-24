# Generated documentation for module arcpy.indoorpositioning


class CreateIPSQualityDataset(object):
    """
    Creates a dataset that can be used to assess the quality of an ArcGIS IPS deployment.
    """

    @property
    def description(self) -> str:
        return """

        CreateIPSQualityDataset_indoorpositioning(target_workspace, coordinate_system, out_dataset_name)

        Creates a dataset that can be used to assess the quality of an ArcGIS
        IPS deployment.

     INPUTS:
      target_workspace (Workspace):
          The geodatabase where the IPS Quality dataset will be created. The
          value can be a file or an enterprise geodatabase.
      coordinate_system (Coordinate System):
          The spatial reference that will be used for the output IPS Quality
          dataset. The default is WGS84. You can specify the spatial reference
          in several ways, including the following:Reference a feature class or
          feature dataset with the spatial
          reference you want to apply, such as
          C:/workspace/myproject.gdb/IPS_Recordings.Use a SpatialReference
          object.Use the well-known text (WKT) string of a spatial reference.
          One way
          to determine the WKT of a spatial reference is to export a
          SpatialReference object to a string using the exportToString method.
      out_dataset_name (String):
          The name of the dataset that will be created. The default is
          IPS_Quality.

        """