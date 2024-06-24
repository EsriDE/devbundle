# Generated documentation for module arcpy.md


class NetCDFTimeSeriesToFeatureClass(object):
    """
    Creates a feature class from timeseries in netCDF files. In the Climate and Forecast (CF) metadata convention, a timeseries is a type of discrete sampling geometry (DSG).
    """

    @property
    def description(self) -> str:
        return """

        NetCDFTimeSeriesToFeatureClass_md(in_files_or_folders;in_files_or_folders..., target_workspace, out_point_name, {observation_variables;observation_variables...}, {out_table_name}, {instance_variables;instance_variables...}, {include_subdirectories}, {in_cf_metadata}, {analysis_extent}, {out_join_layer})

        Creates a feature class from timeseries in netCDF files. In the
        Climate and Forecast (CF) metadata convention, a timeseries is a type
        of discrete sampling geometry (DSG).

     INPUTS:
      in_files_or_folders (Folder / File):
          The input netCDF files that will be used to create a feature class.
          Individual netCDF files, as well as folders that contain multiple
          netCDF files, can be used.The input netCDF files must have the same
          DSG feature type and schema.
      target_workspace (Workspace):
          The enterprise or file geodatabase in which the output feature class
          and table will be created. This must be an existing workspace.
      out_point_name (String):
          The name of the feature class that will contain the locations from the
          netCDF variables. These variables will be added as fields from the
          instance_variables parameter.
      observation_variables {String}:
          The netCDF variables that contain all the observation values at each
          location and each vertical level. These will be added as fields to the
          output table
      out_table_name {String}:
          The name of the output table that will contain all the records from
          the observation_variables parameter.
      instance_variables {String}:
          The netCDF variables that differentiate individual features and
          represent the locations where observations are made. These variables
          will be added as fields to the output feature class.
      include_subdirectories {Boolean}:
          Specifies whether the files residing in the subdirectories of an input
          folder will be used.INCLUDE_SUBDIRECTORIES-All netCDF files in all
          subdirectories will be
          used.DO_NOT_INCLUDE_SUBDIRECTORIES-Only files in the input folder will
          be
          used. This is the default.
      in_cf_metadata {File}:
          The XML format file with an .ncml extension that will supply missing
          or altered CF information for the input netCDF files.
      analysis_extent {Extent}:
          The Extent class determines the extent for the output raster dataset.
          The form of the Extent class is as follows:
          Extent (XMin, YMin, XMax, YMax)                     where:
          XMin-The extent XMin valueYMin-The extent
          YMin valueXMax-The extent
          XMax valueYMax-The extent YMax value

     OUTPUTS:
      out_join_layer {Feature Layer}:
          The output layer that will be created by joining the output table to
          the output feature class. This is an optional output.

        """