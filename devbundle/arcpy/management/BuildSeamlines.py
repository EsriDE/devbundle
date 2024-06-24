# Generated documentation for module arcpy.management


class BuildSeamlines(object):
    """
    Generate or update seamlines for your mosaic dataset. Seamlines are used to sort overlapping imagery and produce a smoother-looking mosaic.
    """

    @property
    def description(self) -> str:
        return """

        BuildSeamlines_management(in_mosaic_dataset, {cell_size;cell_size...}, {sort_method}, {sort_order}, {order_by_attribute}, {order_by_base_value}, {view_point}, {computation_method}, {blend_width}, {blend_type}, {request_size}, {request_size_type}, {blend_width_units}, {area_of_interest}, {where_clause}, {update_existing}, {min_region_size}, {min_thinness_ratio}, {max_sliver_size})

        Generate or update seamlines for your mosaic dataset. Seamlines are
        used to sort overlapping imagery and produce a smoother-looking
        mosaic.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          Select the mosaic dataset on which to build seamlines.
      cell_size {Double}:
          Generate seamlines for raster datasets that fall within the following
          range of spatial resolutions.You can leave this parameter empty and
          the tool will automatically
          create seamlines at the appropriate levels.The units for this
          parameter are the same as the spatial reference of
          the input mosaic dataset.
      sort_method {String}:
          Set a rule to determine which raster will be used to generate
          seamlines when images overlap.NORTH_WEST-Select the raster datasets
          that have center points closest
          to the northwest corner of the boundary. This is the
          default.CLOSEST_TO_VIEWPOINT-Select raster datasets based on a user-
          defined
          location and a nadir location for the raster datasets using the
          Viewpoint tool.BY_ATTRIBUTE-Select raster datasets based on an
          attribute from the
          footprint attribute table. Commonly used attributes include
          acquisition date, cloud cover, or viewing angle.
      sort_order {Boolean}:
          Choose whether to sort the rasters in ascending order or descending
          order.ASCENDING-Sort the rasters in ascending order. This is the
          default.DESCENDING-Sort the rasters in descending order.
      order_by_attribute {Field}:
          Order the raster datasets based on this field when the sort
          method is BY_ATTRIBUTE. The default attribute is. ObjectID
      order_by_base_value {Variant}:
          Sort the rasters by their difference between this value and their
          value in the order_by_attribute parameter.
      view_point {Point}:
          Set the coordinate location to use when sort_method is
          CLOSEST_TO_VIEWPOINT.
      computation_method {String}:
          Choose how to build seamlines.GEOMETRY-Generate seamlines for
          overlapping areas based on the
          intersection of footprints. Areas with no overlapping imagery will
          merge the footprints. This is the default.RADIOMETRY-Generate
          seamlines based on the spectral patterns of
          features within the imagery.COPY_FOOTPRINT-Generate seamlines directly
          from the footprints.COPY_TO_SIBLING-Apply the seamlines from another
          mosaic dataset. The
          mosaic datasets have to be in the same group. For example, the extent
          of the panchromatic band does not always match the extent of the
          multispectral band. This option makes sure they share the same
          seamline.EDGE_DETECTION-Generate seamlines over intersecting areas
          based on the
          edges of features in the area.VORONOI-Generate seamlines using the
          area Voronoi diagram.DISPARITY-Generate seamlines based on the
          disparity images of stereo
          pairs. This method can avoid seamlines cutting through buildings.
          Theparameter applies to each computation method. Sort
          Method
      blend_width {Double}:
          Blending (feathering) occurs along a seamline between pixels where
          there are overlapping rasters. The blend width defines how many pixels
          will be blended.If the blend width value is 10, and you use BOTH as
          the blend type,
          then 5 pixels will be blended on the inside and outside of the
          seamline. If the value is 10, and the blend type is INSIDE, then 10
          pixels will be blended on the inside of the seamline.
      blend_type {String}:
          Determine how to blend one image into another, over the seamlines.
          Options are to blend inside the seamlines, outside the seamlines, or
          both inside and outside. BOTH-Blend using pixels on either
          side of the seamlines. For
          example, if theis 10 pixels, then five pixels will be blended on the
          inside and outside of the seamline. This is the default. Blend
          WidthINSIDE-Blend inside of the seamline.OUTSIDE-Blend outside of the
          seamline.
      request_size {Long}:
          Specify the number of columns and rows for resampling. The maximum
          value is 5,000. Increase or decrease this value based on the
          complexity of your raster data. Greater image resolution provides more
          detail in the raster dataset but also increases the processing time.
      request_size_type {String}:
          Set the units for the. Request Size
          PIXELS-Modify the request size based on the pixel size.
          This is the default option and resamples the closest image based on
          the raster pixel size. PIXELSIZE_FACTOR-Modify the request
          size by specifying a
          scaling factor. This option resamples the closest image by
          multiplying the raster
          pixel size (from cell size level table) with the pixel size factor.
      blend_width_units {String}:
          Specify the unit of measurement for blend width.PIXELS-Measure using
          the number of pixels. This is the
          default.GROUND_UNITS-Measure using the same units as the mosaic
          dataset.
      area_of_interest {Feature Set}:
          Build seamlines on all the rasters that intersect this polygon. To
          select an area of interest, use an input feature class.
      where_clause {SQL Expression}:
          SQL expression to build seamlines on specific raster datasets within
          the mosaic dataset.
      update_existing {Boolean}:
          Update seamlines that are affected by the addition or deletion of the
          mosaic dataset items.IGNORE_EXISTING-Regenerates seamlines for all
          items and ignores
          existing seamlines, if any. This is the default.UPDATE_EXISTING-Only
          update items without seamlines. If any new items
          overlap with the previously created seamlines, the existing seamlines
          may be affected.This parameter is ignored if seamlines do not exist.
      min_region_size {Long}:
          Specify the minimum region size, in pixel units. Any polygons smaller
          than this specified threshold will be removed in the seamline result.
          The default is 100 pixels.This parameter value should be smaller than
          the sliver area, which is
          (max_sliver_size) * (max_sliver_size).
      min_thinness_ratio {Double}:
          Define how thin a polygon can be, before it is considered a sliver.
          This is based on a scale from 0 to 1.0, where a value of 0.0
          represents a polygon that is almost a straight line, and a value of
          1.0 represents a polygon that is a circle.Slivers are removed when
          building seamlines.
      max_sliver_size {Long}:
          Specify the maximum size a polygon can be to still be
          considered a sliver. This parameter is specified in pixels and is
          based on the request_size, not the spatial resolution of the source
          raster. Any polygon that is less than the square of this value is
          considered a sliver. Any regions that are less than
          (max_sliver_size)are considered slivers. 2Slivers are removed
          when building seamlines.

        """