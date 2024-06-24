# Generated documentation for module arcpy.conversion


class BIMFileToGeodatabase(object):
    """
    Imports the contents of one or more BIM file workspaces into a single geodatabase feature dataset.
    """

    @property
    def description(self) -> str:
        return """

        BIMFileToGeodatabase_conversion(in_bim_file_workspace;in_bim_file_workspace..., out_gdb_path, out_dataset_name, {spatial_reference}, {identifier}, {include_floorplan})

        Imports the contents of one or more BIM file workspaces into a single
        geodatabase feature dataset.

     INPUTS:
      in_bim_file_workspace (BIM File Workspace):
          The BIM file or files that will be converted to geodatabase feature
          classes.
      out_gdb_path (Workspace):
          The geodatabase where the output feature dataset will be created. This
          must be an existing geodatabase.
      out_dataset_name (String):
          The building dataset name.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset.To control other
          aspects of the spatial reference, such as the x,y-,
          z-, and m-domains, resolutions, and tolerances, set the appropriate
          geoprocessing environments.
      identifier {String}:
          A unique building identifier that will be added to all output feature
          classes. The identifier allows you to add unique names to each
          building to be used at a later time.
      include_floorplan {Boolean}:
          Specifies whether the output dataset will include the floorplan
          feature classes.INCLUDE_FLOORPLAN-The output dataset will include the
          floorplan
          feature classes. This is the default.EXCLUDE_FLOORPLAN-The output
          dataset will exclude the floorplan
          feature classes.

        """