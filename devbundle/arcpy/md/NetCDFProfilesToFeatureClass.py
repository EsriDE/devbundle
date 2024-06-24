# Generated documentation for module arcpy.md


class NetCDFProfilesToFeatureClass(object):
    """
    Creates a feature class from profiles in netCDF files. In the Climate and Forecast (CF) metadata convention, a profile is a type of discrete sampling geometry (DSG).
    """

    @property
    def description(self) -> str:
        return """

        NetCDFProfilesToFeatureClass_md(in_files_or_folders;in_files_or_folders..., target_workspace, out_point_or_polyline_name, {observation_variables;observation_variables...}, {out_table_name}, {instance_variables;instance_variables...}, {out_schema}, {include_subdirectories}, {in_cf_metadata}, {analysis_extent}, {out_join_layer})

        Creates a feature class from profiles in netCDF files. In the Climate
        and Forecast (CF) metadata convention, a profile is a type of discrete
        sampling geometry (DSG).

     INPUTS:
      in_files_or_folders (Folder / File):
          The input netCDF files that will be used to create a feature class.
          Individual netCDF files, as well as folders that contain multiple
          netCDF files, can be used.The input netCDF files must have the same
          DSG feature type and schema.
      target_workspace (Workspace):
          The enterprise or file geodatabase in which the output feature class
          and table will be created. This must be an existing workspace.
      out_point_or_polyline_name (String):
          The name of the feature class that will contain the locations from the
          netCDF variables. These variables will be added as fields from the
          instance_variables parameter.
      observation_variables {String}:
          The netCDF variables that contain all the observation values at each
          location and each vertical level. These will be added as fields to the
          output table
      out_table_name {String}:
          The name of the output table that will contain all the records from
          the observation variables.
      instance_variables {String}:
          The netCDF variables that differentiate individual features and
          represent the locations where observations are made. These variables
          will be added as fields to the output feature class.
      out_schema {String}:
          Specifies the output feature class type that will be
          created.INSTANCE_AND_OBSERVATION-A feature class containing 2D points
          that
          contain the location of each instance and a related table containing
          all the observation variables will be created. This is the
          default..ROUTE_AND_EVENT-A vertical polyline feature class with 3D
          vertexes and
          a linear event table for the observation variables will be
          created.POINT_3D-A 3D feature class with all instances at all vertical
          levels
          will be created.
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
          the output feature class. This is an optional output and is only
          available when the INSTANCE_AND_OBSERVATION option is specified for
          the out_schema parameter.

        """