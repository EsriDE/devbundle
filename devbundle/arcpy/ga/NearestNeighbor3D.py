# Generated documentation for module arcpy.ga


class NearestNeighbor3D(object):
    """
    Creates a voxel layer source file (netCDF) from categorical 3D points by assigning each voxel the categories of the nearest neighbor in 3D.
    """

    @property
    def description(self) -> str:
        return """

        NearestNeighbor3D_ga(in_features, category_field;category_field..., out_netcdf_file, {x_spacing}, {y_spacing}, {elevation_spacing}, {elev_inflation_factor}, {in_study_area}, {min_elev_raster}, {max_elev_raster})

        Creates a voxel layer source file (netCDF) from categorical 3D points
        by assigning each voxel the categories of the nearest neighbor in 3D.

     INPUTS:
      in_features (Feature Layer):
          The input points representing locations with known categories in 3D.
          The points must be in a projected coordinate system, and there must be
          at least three points.
      category_field (Field):
          The fields of the input features containing the categories of each
          point. For each field, the unique values of the field represent the
          categories of the field. Each field must be Text, Short, or Long
          type.For example, you can provide a field of soil classes (shale,
          sand,
          clay, and so on) and a second field of the color of the soil (yellow,
          brown, white, and so on). Each voxel in the output netCDF file will
          store the nearest soil class and soil color as separate variables.
      x_spacing {Linear Unit}:
          The spacing between each gridded point in the x-dimension. The default
          value creates 40 points along the output x-extent.
      y_spacing {Linear Unit}:
          The spacing between each gridded point in the y-dimension. The default
          value creates 40 points along the output y-extent.
      elevation_spacing {Linear Unit}:
          The spacing between each gridded point in the elevation (z) dimension.
          The default value creates 40 points along the output z-extent.
      elev_inflation_factor {Double}:
          A constant value that is multiplied to the elevation (z-coordinates)
          of the input points prior to finding the nearest neighbor. Values
          larger than 1 will search farther horizontally than vertically to find
          the nearest neighbor. For example, a value of 10 means that each voxel
          will search 10 times farther horizontally than vertically to find the
          closest neighbor. The default is 1, meaning that the elevations are
          not adjusted. The value must be between 1 and 1,000.Elevation
          inflation is only used to find the nearest neighbor, and all
          elevations are returned to the original scale before creating the
          output netCDF file. Elevation inflation is recommended when the
          categories of the input points tend to be similar along horizontal
          strata, such as with soil classes and rock types.
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
          The output netCDF file containing categories in a 3D grid. Each point
          in the 3D grid is assigned the category of the closest input point.
          This file can be used as the data source of a voxel layer.

        """