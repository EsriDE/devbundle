# Generated documentation for module arcpy.management


class BuildFootprints(object):
    """
    Computes the extent of every raster in a mosaic dataset. This tool is used when you have added or removed raster datasets from a mosaic dataset and want to recompute the footprints.
    """

    @property
    def description(self) -> str:
        return """

        BuildFootprints_management(in_mosaic_dataset, {where_clause}, {reset_footprint}, {min_data_value}, {max_data_value}, {approx_num_vertices}, {shrink_distance}, {maintain_edges}, {skip_derived_images}, {update_boundary}, {request_size}, {min_region_size}, {simplification_method}, {edge_tolerance}, {max_sliver_size}, {min_thinness_ratio})

        Computes the extent of every raster in a mosaic dataset. This tool is
        used when you have added or removed raster datasets from a mosaic
        dataset and want to recompute the footprints.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that contains the raster datasets whose footprints
          you want to compute.
      where_clause {SQL Expression}:
          An SQL expression to select specific raster datasets within the mosaic
          dataset.
      reset_footprint {String / Boolean}:
          Refine the footprints using one of the following methods:RADIOMETRY-
          Exclude pixels with a value outside of a defined range.
          This option is generally used to exclude border areas, which do not
          contain valid data. This is the default.GEOMETRY-Restore the
          footprint to its original geometry.COPY_TO_SIBLING-Replace the
          panchromatic footprint with the
          multispectral footprint when using a pan-sharpened raster type. This
          can occur when the panchromatic and multispectral images do not have
          identical geometries.NONE-Do not redefine the footprints.
      min_data_value {Double}:
          Exclude pixels with a value less than this number.
      max_data_value {Double}:
          Exclude pixels with a value greater than this number.
      approx_num_vertices {Long}:
          Choose between 4 and 10,000. More vertices will improve accuracy but
          can extend processing time. A value of -1 will calculate all vertices.
          More vertices will increase accuracy but also the processing time.
      shrink_distance {Double}:
          Clip the footprint by this distance. This can eliminate artifacts from
          using lossy compression, which causes the edges of the image to
          overlap into NoData areas.Shrinking of the polygon is used to
          counteract effects of lossy
          compression, which causes edges of the image to overlap into NoData
          areas.
      maintain_edges {Boolean}:
          Use this parameter when using raster datasets that have been tiled and
          are adjacent (line up along the seams with little to no
          overlap).NO_MAINTAIN_EDGES-Remove the sheet edges from all the
          footprints. This
          is the default.MAINTAIN_EDGES-Maintain the footprints in their
          original state.
      skip_derived_images {Boolean}:
          Adjust the footprints of overviews.SKIP_DERIVED_IMAGES-Do not adjust
          the footprints of overviews. This is
          the default.NO_SKIP_DERIVED_IMAGES-Adjust the footprints of overviews
          and
          associated raster datasets.
      update_boundary {Boolean}:
          Update the boundary of the mosaic dataset if you have added or removed
          imagery that changes the extent.UPDATE_BOUNDARY-Update the boundary.
          This is the
          default.NO_BOUNDARY-Do not update the boundary.
      request_size {Long}:
          Set the resampled extent (in columns and rows) for the raster when
          building footprints. Greater image resolution provides more detail in
          the raster dataset but increases the processing time. A value of -1
          will compute the footprint at the original resolution.
      min_region_size {Long}:
          Avoid small holes in your imagery when using pixel values to create a
          mask. For example, your imagery may have a range of values from 0 to
          255, and to mask clouds, you've excluded values from 245 to 255, which
          may cause other, noncloud pixels to be masked as well. If those areas
          are smaller than the number of pixels specified here, they will not be
          masked out.
      simplification_method {String}:
          Reduce the number of vertices in the footprint to improve
          performance.NONE-Do not limit the number of vertices. This is the
          default.CONVEX_HULL-Use the minimum bounding box to simplify the
          footprint.ENVELOPE-Use the envelope of each mosaic dataset item to
          simplify the
          footprint.
      edge_tolerance {Double}:
          Snap the footprint to the sheet edge if it is within this tolerance.
          Units are the same as those in the mosaic dataset coordinate system.
          This is used when maintain_edges is set to MAINTAIN_EDGES.By default,
          the value is empty for which the tolerance is computed
          based on the pixel size corresponding to the requested resampled
          raster.A value of -1 will compute the tolerance using the average
          pixel size
          of the mosaic dataset.
      max_sliver_size {Long}:
          Identify all polygons that are smaller than the square of this value.
          The value is specified in pixels and is based on the request_size, not
          the spatial resolution of the source raster. Regions less than
          the (max_sliver_size)and less than the
          min_thinness_ratio are considered slivers and will be removed.
          2
      min_thinness_ratio {Double}:
          Define the thinness of slivers on a scale from 0 to 1.0, where 1.0
          represents a circle and 0.0 represents a polygon that approaches a
          straight line.Polygons that are below both the max_sliver_size and
          min_thinness_ratio will be removed from the footprint.

        """