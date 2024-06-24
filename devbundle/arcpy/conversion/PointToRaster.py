# Generated documentation for module arcpy.conversion


class PointToRaster(object):
    """
    Converts point features to a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        PointToRaster_conversion(in_features, value_field, out_rasterdataset, {cell_assignment}, {priority_field}, {cellsize}, {build_rat})

        Converts point features to a raster dataset.

     INPUTS:
      in_features (Feature Layer):
          The point or multipoint input feature dataset to be converted to a
          raster.
      value_field (Field):
          The field used to assign values to the output raster.It can be any
          field of the input feature dataset's attribute table. If
          thefield of a point or multipoint dataset contains z- or
          m-values, either of these can be used. Shape
      cell_assignment {String}:
          The method to determine how the cell will be assigned a value when
          more than one feature falls within a cell. MOST_FREQUENT-If
          there is more than one feature within the
          cell, the one with the most common attribute, in the, is assigned to
          the cell. If they have the same number of common attributes, the one
          with the lowest FID is used. Value fieldSUM-The sum of the
          attributes of all the points within the cell (not
          valid for string data).MEAN-The mean of the attributes of all the
          points within the cell (not
          valid for string data).STANDARD_DEVIATION-The standard deviation of
          attributes of all the
          points within the cell. If there are less than two points in the cell,
          the cell is assigned NoData (not valid for string data).MAXIMUM-The
          maximum value of the attributes of the points within the
          cell (not valid for string data).MINIMUM-The minimum value of the
          attributes of the points within the
          cell (not valid for string data).RANGE-The range of the attributes of
          the points within the cell (not
          valid for string data).COUNT-The number of points within the cell.
      priority_field {Field}:
          This field is used when a feature should take preference over another
          feature with the same attribute. Priority field is only used
          with thecell assignment type
          option. Most frequent
      cellsize {Analysis Cell Size}:
          The cell size of the output raster being created.This parameter can be
          defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value is
          used, if specified; otherwise, additional rules are used to calculate
          it from the other inputs. See Usages for more detail.
      build_rat {Boolean}:
          Specifies whether the output raster will have a raster attribute
          table.This parameter only applies to integer rasters.BUILD-The output
          raster will have a raster attribute table. This is
          the default.DO_NOT_BUILD-The output raster will not have a raster
          attribute table.

     OUTPUTS:
      out_rasterdataset (Raster Dataset):
          The output raster dataset to be created.If the output raster will not
          be saved to a geodatabase, specify .tif
          for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE
          file format, or no extension for Esri Grid raster format.

        """