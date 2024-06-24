# Generated documentation for module arcpy.management


class MakeMosaicLayer(object):
    """
    Creates a mosaic layer from a mosaic dataset or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved as a layer file or the map is saved.
    """

    @property
    def description(self) -> str:
        return """

        MakeMosaicLayer_management(in_mosaic_dataset, out_mosaic_layer, {where_clause}, {template}, {band_index;band_index...}, {mosaic_method}, {order_field}, {order_base_value}, {lock_rasterid}, {sort_order}, {mosaic_operator}, {cell_size}, {processing_template})

        Creates a mosaic layer from a mosaic dataset or layer file. The layer
        that is created by the tool is temporary and will not persist after
        the session ends unless the layer is saved as a layer file or the map
        is saved.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The path and name of the input mosaic dataset.
      where_clause {SQL Expression}:
          Define a query using SQL.
      template {Extent}:
          The output extent can be specified by defining the four coordinates or
          by using the extent of an existing layer.MAXOF-The maximum extent of
          all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      band_index {Value Table}:
          The bands that will be exported for the layer. If no bands are
          specified, all the bands will be used in the output.
      mosaic_method {String}:
          Choose the mosaic method. The mosaic method defines how the layer is
          created from different rasters in the mosaic
          dataset.CLOSEST_TO_CENTER-Sorts rasters based on an order where
          rasters that
          have their center closest to the view center are placed on
          top.NORTH_WEST-Sorts rasters based on an order where rasters that have
          their center closest to the northwest are placed on
          top.LOCK_RASTER-Enables a user to lock the display of single or
          multiple
          rasters, based on an ID or name. When you choose this option, you need
          to specify the Lock Raster ID.BY_ATTRIBUTE-Sorts rasters based on an
          attribute field and its
          difference from the base value. When this option is chosen, the order
          field and order base value parameters also need to be
          set.CLOSEST_TO_NADIR-Sorts rasters based on an order where rasters
          that
          have their nadir position closest to the view center are placed on
          top. The nadir point can be different from the center point,
          especially in oblique imagery.CLOSEST_TO_VIEWPOINT-Sorts rasters based
          on an order where the nadir
          position is closest to the user-defined viewpoint location and are
          placed on top.SEAMLINE-Cuts the rasters using the predefined seamline
          shape for each
          raster using optional feathering along the seams. The ordering is
          predefined during seamline generation. The LAST mosaic operator is not
          valid with this mosaic method.
      order_field {String}:
          Choose the order field. When the mosaic method is BY_ATTRIBUTE, the
          default field to use when ordering rasters needs to be set. The list
          of fields is defined as those in the service table that are of type
          metadata.
      order_base_value {String}:
          The order base value. The images are sorted based on the difference
          between this value and the attribute value in the specified field.
      lock_rasterid {String}:
          The Raster ID or raster name to which the service should be locked so
          that only the specified rasters are displayed. If left undefined, it
          will be similar to the system default. Multiple IDs can be defined as
          a semicolon-delimited list.
      sort_order {String}:
          Choose whether the sort order is ascending or descending.ASCENDING-The
          sort order will be ascending. This is the
          default.DESCENDING-The sort order will be descending.
      mosaic_operator {String}:
          Choose the mosaic operator to use. When two or more rasters have the
          same sort priority, this parameter is used to further refine the sort
          order.FIRST-The first raster in the list will be on top. This is the
          default.LAST-The last raster in the list will be on top.MIN-The raster
          with the lowest value will be on top.MAX-The raster with the highest
          value will be on top.MEAN-The average pixel value will be on
          top.BLEND-The output cell value will be a blend of values; this blend
          value relies on an algorithm that is weight based and dependent on the
          distance from the pixel to the edge within the overlapping
          area.SUM-The output cell value will be the aggregate of all
          overlapping
          cells.
      cell_size {Double}:
          The cell size of the output mosaic layer.
      processing_template {String}:
          The raster function processing template that can be applied on the
          output mosaic layer.None-No processing template.

     OUTPUTS:
      out_mosaic_layer (Mosaic Layer):
          The name of the output mosaic layer.

        """