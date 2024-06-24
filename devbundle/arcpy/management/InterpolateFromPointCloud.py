# Generated documentation for module arcpy.management


class InterpolateFromPointCloud(object):
    """
    Interpolates a digital terrain model (DTM) or a digital surface model (DSM) from a point cloud.
    """

    @property
    def description(self) -> str:
        return """

        InterpolateFromPointCloud_management(in_container, out_raster, cell_size, interpolation_method, smooth_method, {surface_type}, {fill_dem})

        Interpolates a digital terrain model (DTM) or a digital surface model
        (DSM) from a point cloud.

     INPUTS:
      in_container (Folder / File / Feature Class / Feature Layer):
          The path and name of the file, folder, or feature layer. The input can
          be a folder of LAS files or a solution point table from orthomapping
          tools. For cloud storage, provide the cloud storage path, such as
          C:\Temp\Cloud.acs\lasfolder.The LAS files can be the output from the
          Generate Point Cloud tool, in
          which LAS points are categorized as ground and above ground. The
          solution point table is output from either the Compute Block
          Adjustments tool or the Compute Camera Model tool.
      cell_size (Double):
          The cell size of the output raster dataset.
      interpolation_method (String):
          Specifies the method that will be used to interpolate the output
          raster dataset from the point cloud.TRIANGULATION-The triangulation
          method will be used. It is also known
          as triangulated irregular network (TIN) linear interpolation and is
          designed for irregularly distributed sparse points, such as solution
          points from block adjustment computation.NATURAL_NEIGHBOR-The natural
          neighbor method will be used. It is
          similar to triangulation but generates a smoother surface and is more
          computationally intensive.IDW-The inverse distance weighted (IDW)
          average method will be used.
          It is used for regularly distributed dense points, such as point cloud
          LAS files from the Generate Point Cloud tool. The IDW search radius is
          automatically computed based on average point density.
      smooth_method (String):
          Specifies the filter that will be used to smooth the output raster
          dataset.GAUSS3x3-A Gaussian filter with a 3 by 3 window will be
          used.GAUSS5x5-A Gaussian filter with a 5 by 5 window will be
          used.GAUSS7x7-A Gaussian filter with a 7 by 7 window will be
          used.GAUSS9x9-A Gaussian filter with a 9 by 9 window will be
          used.NONE-No smoothing filter will be used.
      surface_type {String}:
          Specifies whether a digital terrain model or a digital surface model
          will be created.DTM-A digital terrain model will be created by
          interpolating only the
          ground points.DSM-A digital surface model will be created by
          interpolating all the
          points.
      fill_dem {Raster Dataset / Raster Layer / Mosaic Dataset / Mosaic Layer}:
          A DEM raster input that is used to fill NoData areas. Areas of NoData
          may exist where pixels do not have enough information from the input
          to generate values.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset location, name, and file extension. You can
          also save the output raster dataset by providing a cloud storage path
          such as C:\Temp\Cloud.acs\lasfolder.The output can be created in most
          writable raster formats, such as
          TIFF, CRF, or IMG.

        """