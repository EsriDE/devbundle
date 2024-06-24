# Generated documentation for module arcpy.management


class ProjectRaster(object):
    """
    Transforms a raster dataset from one coordinate system to another.
    """

    @property
    def description(self) -> str:
        return """

        ProjectRaster_management(in_raster, out_raster, out_coor_system, {resampling_type}, {cell_size}, {geographic_transform;geographic_transform...}, {Registration_Point}, {in_coor_system}, {vertical})

        Transforms a raster dataset from one coordinate system to another.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster dataset that will be transformed into a new projection.
      out_coor_system (Coordinate System):
          The coordinate system of the new raster dataset. Valid values
          for this parameter are the following:        An
          existing feature class, feature dataset, raster dataset (basically
          anything with a coordinate system)An ArcPy SpatialReference object
      resampling_type {String}:
          Specifies the resampling technique that will be used. The
          default is. NearestNEAREST-The nearest neighbor technique will
          be used. It minimizes
          changes to pixel values since no new values are created and is the
          fastest resampling technique. It is suitable for discrete data, such
          as land cover.BILINEAR-The bilinear interpolation technique will be
          used. It
          calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding four pixels. It is suitable
          for continuous data.CUBIC-The cubic convolution technique will be
          used. It calculates the
          value of each pixel by fitting a smooth curve based on the surrounding
          16 pixels. This produces the smoothest image but can create values
          outside of the range found in the source data. It is suitable for
          continuous data.MAJORITY-The majority resampling technique will be
          used. It determines
          the value of each pixel based on the most popular value in a 4 by 4
          window. It is suitable for discrete data. Theandoptions are
          used for categorical data, such as a land-
          use classification. Theoption is the default. It is the quickest and
          does not change the pixel values. Do not use either of these options
          for continuous data, such as elevation surfaces.
          NearestMajorityNearest        Theandoptions are most appropriate for
          continuous data. It is
          recommended that you do not use either of these options with
          categorical data because the pixel values may be altered.
          BilinearCubic
      cell_size {Cell Size XY}:
          The cell size of the new raster using an existing raster dataset or by
          specifying its width (x) and height (y).
      geographic_transform {String}:
          The geographic transformation when projecting from one geographic
          system or datum to another. A transformation is required when the
          input and output coordinate systems have different datums.
      Registration_Point {Point}:
          The lower left point for anchoring the output cells. This point does
          not have to be a corner coordinate or fall within the raster dataset.
          TheEnvironment setting will take priority over theparameter.
          To set the registration point, make sureis not set. Snap
          RasterRegistration PointSnap Raster
      in_coor_system {Coordinate System}:
          The coordinate system of the input raster dataset.
      vertical {Boolean}:
          Specifies whether a vertical transformation will be performed.This
          parameter is only enabled when the input and output coordinate
          systems have a vertical coordinate system and the input feature class
          coordinates have z-values.When the VERTICAL keyword is used, the
          geographic_transform parameter
          can include ellipsoidal transformations and transformations between
          vertical datums. For example,
          “~NAD_1983_To_NAVD88_CONUS_GEOID12B_Height + NAD_1983_To_WGS_1984_1”
          transforms geometry vertices that are defined on NAD 1983 datum with
          NAVD 1988 heights into vertices on the WGS 1984 ellipsoid (with
          z-values representing ellipsoidal heights). The tilde (~) indicates
          reversed direction of transformation.NO_VERTICAL-No vertical
          transformation is applied. The z-values of
          geometry coordinates will be ignored and the z-values will not be
          modified. This is the default.VERTICAL-The transformation specified in
          the geographic_transform
          parameter is applied. The Project Raster tool transforms x-, y-, and
          z-values of geometry coordinates.Many vertical transformations require
          additional data files that must
          be installed using the ArcGIS Coordinate Systems Data installation
          package.

     OUTPUTS:
      out_raster (Raster Dataset):
          The raster dataset with the new projection that will be created.When
          storing the raster dataset in a file format, specify the file
          extension as follows:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri GridWhen
          storing a raster dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, a TIFF format file, or a geodatabase, you can
          specifyandvalues in the geoprocessing environments. Compression
          TypeCompression Quality

        """