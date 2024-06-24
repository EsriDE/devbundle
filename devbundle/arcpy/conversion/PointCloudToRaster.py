# Generated documentation for module arcpy.conversion


class PointCloudToRaster(object):
    """
    Creates a raster surface from height values in a point cloud scene layer package file (*.slpk).
    """

    @property
    def description(self) -> str:
        return """

        PointCloudToRaster_conversion(in_point_cloud, cell_size, out_raster, {cell_assignment}, {void_fill}, {z_factor})

        Creates a raster surface from height values in a point cloud scene
        layer package file (*.slpk).

     INPUTS:
      in_point_cloud (Scene Layer / File):
          The point cloud scene layer package file (*.slpk) or I3S point cloud
          scene layer service that will be used to generate an elevation raster.
          An I3S point cloud scene layer service must have the export property
          enabled in order to be processed.
      cell_size (Linear Unit):
          The length and width of each cell in the output raster.
      cell_assignment {String}:
          Specifies the method that will be used for assigning values to cells
          containing points.AVERAGE-The cell value will be defined by the
          average of the z-values
          for all points in the cell. This is the default.MINIMUM-The cell value
          will be defined by the lowest z-value from the
          points in the cell.MAXIMUM-The cell value will be defined by the
          highest z-value from the
          points in the cell.NEAREST-The cell value will be assigned based on
          the height of the
          point closest to the cell center.
      void_fill {String}:
          Specifies the method that will be used for interpolating the values of
          cells within the interpolation zone that do not contain points.NONE-No
          value will be assigned to raster cells that do not contain
          points.SIMPLE-The z-value of points located in the cells that
          immediately
          surround the empty cell will be averaged to eliminate small
          voids.LINEAR-Void areas will be triangulated and linear interpolation
          will
          be used to assign the cell value. This is the
          default.NATURAL_NEIGHBOR-Natural neighbor interpolation will be used
          to
          determine the cell value.
      z_factor {Double}:
          The factor by which z-values will be multiplied. This is typically
          used to convert z linear units to match x,y linear units. The default
          is 1, which leaves the z-values unchanged.

     OUTPUTS:
      out_raster (Raster Dataset):
          The location and name of the output raster. When storing a raster
          dataset in a geodatabase or in a folder such as an Esri Grid, do not
          add a file extension to the name of the raster dataset. A file
          extension can be provided to define the raster's format when storing
          it in a folder, such as .tif to generate a GeoTIFF or .img to generate
          an ERDAS IMAGINE format file.If the raster is stored as a .tif file or
          in a geodatabase, the raster
          compression type and quality can be specified using geoprocessing
          environment settings.

        """