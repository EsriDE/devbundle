# Generated documentation for module arcpy.ga


class IDW3D(object):
    """
    Interpolates the values of 3D points using inverse distance weighting (IDW) and creates a voxel layer and source file (.nc) of the predicted values.
    """

    @property
    def description(self) -> str:
        return """

        IDW3D_ga(in_features, value_field, out_netcdf_file, {power}, {elev_inflation_factor}, {out_cv_features}, {x_spacing}, {y_spacing}, {elevation_spacing}, {in_study_area}, {min_elev_raster}, {max_elev_raster}, {search_neighborhood})

        Interpolates the values of 3D points using inverse distance weighting
        (IDW) and creates a voxel layer and source file (.nc) of the predicted
        values.

     INPUTS:
      in_features (Feature Layer):
          The 3D point features that contain the field that will be
          interpolated. The points must be in a projected coordinate system.
      value_field (Field):
          The field from the input features containing the measured values that
          will be interpolated.
      power {Double}:
          The power value that will be used to weight the values of neighboring
          features when calculating predictions. A higher power results in
          higher influence to closer points. The value must be between 1 and
          100. The default is 2.
      elev_inflation_factor {Double}:
          A constant value that is multiplied to the z-coordinates of the input
          features prior to finding neighbors and calculating distances. For
          most 3D data, the values of the points change faster vertically than
          horizontally, and this factor stretches the locations of the points so
          that one unit of distance vertically is equivalent to one unit of
          distance horizontally. The locations of the points will be moved back
          to their original locations before returning the result of the
          interpolation. If no value is provided, one will be estimated while
          the tool runs and will be displayed as a geoprocessing message. The
          estimated value is determined by minimizing the root mean square cross
          validation error. The value must be between 1 and 1,000.
      x_spacing {Linear Unit}:
          The spacing between each gridded point in the x-dimension. The default
          value creates 40 points along the output x-extent.
      y_spacing {Linear Unit}:
          The spacing between each gridded point in the y-dimension. The default
          value creates 40 points along the output y-extent.
      elevation_spacing {Linear Unit}:
          The spacing between each gridded point in the elevation (z) dimension.
          The default value creates 40 points along the output z-extent.
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
      search_neighborhood {Geostatistical Search Neighborhood}:
          Specifies the number and orientation of the neighbors using the
          SearchNeighborhoodStandard3D class.Standard3Dradius-The length of the
          radius of the search neighborhood. If no
          value is provided, a value will be estimated while the tool runs, and
          the estimated value will be displayed as a geoprocessing
          message.nbrMax-The maximum number of neighbors per sector that will be
          used to
          estimate the value at the unknown location.nbrMin-The minimum number
          of neighbors per sector that will be used to
          estimate the value at the unknown location. sectorType-The
          geometry of the 3D neighborhood. Sectors are
          used to ensure that neighbors are used in different directions around
          the prediction location. All sector types are formed from the Platonic
          solids. ONE_SECTOR-The closest neighbors from any direction
          will be
          used.FOUR_SECTORS-Space will be divided into 4 regions, and neighbors
          will
          be used in each of the 4 regions.SIX_SECTORS-Space will be divided
          into 6 regions, and neighbors will
          be used in each of the 6 regions.EIGHT_SECTORS-Space will be divided
          into 8 regions, and neighbors will
          be used in each of the 8 regions.TWELVE_SECTORS-Space will be divided
          into 12 regions, and neighbors
          will be used in each of the 12 regions.TWENTY_SECTORS-Space will be
          divided into 20 regions, and neighbors
          will be used in each of the 20 regions.

     OUTPUTS:
      out_netcdf_file (File):
          The output netCDF file that will contain the predicted values in a 3D
          grid. This file can be used as the data source of a voxel layer.
      out_cv_features {Feature Class}:
          A feature class of the cross validation statistics for each input
          point. The feature class will contain two scatter plots.

        """