# Generated documentation for module arcpy.ga


class GALayer3DToNetCDF(object):
    """
    Exports one or more 3D geostatistical layers created using the Empirical Bayesian Kriging 3D tool to netCDF format (*.nc file). The output file is displayed as a voxel layer in a local scene.
    """

    @property
    def description(self) -> str:
        return """

        GALayer3DToNetCDF_ga(in_3d_geostat_layers;in_3d_geostat_layers..., out_netcdf_file, {export_locations}, {x_spacing}, {y_spacing}, {elevation_spacing}, {in_points_3d}, {output_variables;output_variables...}, {in_study_area}, {min_elev_raster}, {max_elev_raster})

        Exports one or more 3D geostatistical layers created using the
        Empirical Bayesian Kriging 3D tool to netCDF format (*.nc file). The
        output file is displayed as a voxel layer in a local scene.

     INPUTS:
      in_3d_geostat_layers (Geostatistical Layer):
          The 3D geostatistical layers that will be exported to an output netCDF
          file.
      export_locations {String}:
          Specifies the locations to export from the in_3d_geostat_layers
          parameter value. If you choose the 3D_GRIDDED_POINTS option, you must
          provide values for the x_spacing, u_spacing, and elevation_spacing
          parameters that represent the distance between each gridded point in
          all dimensions. If you choose the CUSTOM_3D_POINTS option, you must
          provide 3D point features in the in_points_3d parameter representing
          the locations to export.3D_GRIDDED_POINTS-Prediction locations are 3D
          gridded points. This is
          the default.CUSTOM_3D_POINTS-Prediction locations are defined by
          custom 3D point
          features.
      x_spacing {Linear Unit}:
          The spacing between each gridded point in the x-dimension. The default
          value creates 40 points along the output x-extent.
      y_spacing {Linear Unit}:
          The spacing between each gridded point in the y-dimension. The default
          value creates 40 points along the output y-extent.
      elevation_spacing {Linear Unit}:
          The spacing between each gridded point in the elevation (z) dimension.
          The default value creates 40 points along the output z-extent.
      in_points_3d {Feature Layer}:
          The 3D point features representing locations to export. The point
          features must have their elevations stored in the Shape.Z geometry
          attribute.
      output_variables {Value Table}:
          Specifies the output types for thevalues. You can specify one
          or more output types for each of the layers or you can apply an output
          type to all input geostatistical layers. By default, the predictions
          for all layers will be exported. Input 3D geostatistical layers
          To export other output types, specify the layer to export (or
          chooseto specify all layers) in the first entry of the value table.
          Specify the output type in the second entry of the value table. If you
          chooseoras the output type, specify the threshold value (for
          probability) or the quantile value (for quantile) in the third entry
          of the value table. If you chooseoras the output type, you can leave
          the third entry in the value table empty.
          AllProbabilityQuantilePredictionPrediction standard error
      in_study_area {Feature Layer}:
          The polygon features that represent the study area. Only points that
          are within the study area are saved in the output netCDF file. When
          visualized as a voxel layer, only voxels within the study area will
          display in the scene. Points are determined to be inside or outside
          the study area using only their x- and y-coordinates.
      min_elev_raster {Raster Layer}:
          The elevation raster that will be used to clip the bottom of the voxel
          layer. Only voxels above this elevation raster will be assigned
          predictions. For example, if you use a ground elevation raster, the
          voxel layer will only display above the ground. It can also be used
          for bedrock surfaces or the bottom of a shale deposit.The raster must
          be in a projected coordinate system, and the elevation
          values must be in the same unit as the vertical unit of the raster.
      max_elev_raster {Raster Layer}:
          The elevation raster that will be used to clip the top of the voxel
          layer. Only voxels below this elevation raster will be assigned
          predictions. For example, if you use a ground elevation raster, the
          voxel layer will only display below the ground. It can also be used to
          clip voxels to the top of a restricted airspace.The raster must be in
          a projected coordinate system, and the elevation
          values must be in the same unit as the vertical unit of the raster.

     OUTPUTS:
      out_netcdf_file (File):
          The output netCDF file containing the exported values from the input
          geostatistical layers. The results of each geostatistical layer are
          saved as different variables in the netCDF file.

        """