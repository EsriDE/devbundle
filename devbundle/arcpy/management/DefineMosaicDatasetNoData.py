# Generated documentation for module arcpy.management


class DefineMosaicDatasetNoData(object):
    """
    Specifies one or more values to be represented as NoData.
    """

    @property
    def description(self) -> str:
        return """

        DefineMosaicDatasetNoData_management(in_mosaic_dataset, num_bands, {bands_for_nodata_value;bands_for_nodata_value...}, {bands_for_valid_data_range;bands_for_valid_data_range...}, {where_clause}, {Composite_nodata_value})

        Specifies one or more values to be represented as NoData.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset where you want to update the NoData values.
      num_bands (Long):
          The number of bands in the mosaic dataset.
      bands_for_nodata_value {Value Table}:
          Define values for each or all bands. Each band can have a unique
          NoData value defined, or the same value can be specified for all
          bands. If you want to define multiple NoData values for each band
          selection, use a space delimiter between each NoData value within the
          bands_for_nodata_value parameter.The Mask function inserted by this
          tool is inserted before the
          Composite Bands function in the function chain. Therefore, if the
          function chain for each raster within the mosaic dataset contains the
          Composite Bands function, or if your raster data was added with a
          raster type that adds the Composite Bands function to each raster's
          function chain, then any value you specify will apply to all bands.
      bands_for_valid_data_range {Value Table}:
          Specify a range of values to display for each band. Values outside of
          this range will be classified as NoData. When working with composite
          bands, the range will apply to all bands.
      where_clause {SQL Expression}:
          An SQL statement to select specific raster in the mosaic dataset. Only
          the selected rasters will have their NoData values changed.
      Composite_nodata_value {Boolean}:
          Choose whether all bands must be NoData in order for the pixel to be
          classified as NoData.NO_COMPOSITE_NODATA-If any of the bands have
          pixels of NoData, then
          the pixel is classified as NoData. This is the
          default.COMPOSITE_NODATA-All of the bands must have pixels of NoData
          in order
          for the pixel to be classified as NoData.

        """