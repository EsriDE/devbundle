# Generated documentation for module arcpy.conversion


class CADToGeodatabase(object):
    """
    Reads a CAD dataset and creates feature classes of the drawing. The feature classes are written to a geodatabase feature dataset.
    """

    @property
    def description(self) -> str:
        return """

        CADToGeodatabase_conversion(input_cad_datasets;input_cad_datasets..., out_gdb_path, out_dataset_name, reference_scale, {spatial_reference})

        Reads a CAD dataset and creates feature classes of the drawing. The
        feature classes are written to a geodatabase feature dataset.

     INPUTS:
      input_cad_datasets (CAD Drawing Dataset):
          The collection of CAD files that will be converted to geodatabase
          features.
      out_gdb_path (Workspace):
          The geodatabase where the output feature dataset will be created. This
          geodatabase must already exist.
      out_dataset_name (String):
          The name of the feature dataset that will be created.
      reference_scale (Double):
          This parameter is not needed for this tool, as CAD annotation is
          treated as points in ArcGIS Pro.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. To control other
          aspects of the spatial reference, such as the x-, y-, z-, and
          m-domains, resolutions, and tolerances, set the appropriate
          geoprocessing environments.

        """