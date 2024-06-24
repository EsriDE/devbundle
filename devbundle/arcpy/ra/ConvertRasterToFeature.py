# Generated documentation for module arcpy.ra


class ConvertRasterToFeature(object):
    """
    Converts a raster to a feature dataset as points, lines, or polygons.
    """

    @property
    def description(self) -> str:
        return """

        ConvertRasterToFeature_ra(inputRaster, {field}, {outputType}, {simplifyLinesOrPolygons}, outputName, {createMultipartFeatures}, {maxVerticesPerFeature})

        Converts a raster to a feature dataset as points, lines, or polygons.

     INPUTS:
      inputRaster (Image Service / Raster Layer / String):
          The input raster layer.
      field {String}:
          A field that specifies the conversion value.It can be any integer or
          text value.A field containing floating-point values can only be used
          if the
          output is to a point dataset. The default is thefield, which
          contains the value in each
          raster cell. Value
      outputType {String}:
          Specifies the output type.POINT-The raster will be converted to a
          point dataset. This is the
          default.LINE-The raster will be converted to a line feature
          dataset.POLYGON-The raster will be converted to a polygon feature
          dataset.
      simplifyLinesOrPolygons {Boolean}:
          Specifies whether lines or polygons will be simplified (smoothed). The
          smoothing is done in such a way that the line contains a minimum
          number of segments while remaining as close as possible to the
          original raster cell edges.SIMPLIFY-The line or polygon features will
          be smoothed to produce a
          more generalized result. This is the default.NO_SIMPLIFY-The line or
          polygon features will not be smoothed and will
          follow the cell boundaries of the raster dataset.This parameter is
          only supported if outputType is LINE or POLYGON.
      outputName (String):
          The output feature class that will contain the converted points,
          lines, or polygons.
      createMultipartFeatures {Boolean}:
          Specifies whether the output polygons will consist of single-part or
          multipart features.MULTIPLE_OUTER_PART-Multipart features will be
          created based on
          polygons that have the same value.SINGLE_OUTER_PART-Individual
          (single-part) features will be created
          for each polygon. This is the default.This parameter is only supported
          if outputType is POLYGON.
      maxVerticesPerFeature {Long}:
          The vertex limit used to subdivide a polygon into smaller polygons.
          This parameter produces similar output as that created by the Dice
          tool in the Data Management toolbox.If left empty, the output polygons
          will not be split. This is the
          default.This parameter is only supported if outputType is POLYGON.

        """