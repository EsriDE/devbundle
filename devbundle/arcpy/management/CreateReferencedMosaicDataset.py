# Generated documentation for module arcpy.management


class CreateReferencedMosaicDataset(object):
    """
    Creates a separate mosaic dataset from items in an existing mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateReferencedMosaicDataset_management(in_dataset, out_mosaic_dataset, {coordinate_system}, {number_of_bands}, {pixel_type}, {where_clause}, {in_template_dataset}, {extent}, {select_using_features}, {lod_field}, {minPS_field}, {maxPS_field}, {pixelSize}, {build_boundary})

        Creates a separate mosaic dataset from items in an existing mosaic
        dataset.

     INPUTS:
      in_dataset (Mosaic Dataset / Mosaic Layer):
          The mosaic dataset from which items will be selected.
      coordinate_system {Coordinate System}:
          The projection for the output mosaic dataset.
      number_of_bands {Long}:
          The number of bands that the referenced mosaic dataset will have.
      pixel_type {String}:
          The bit depth, or radiometric resolution, of the mosaic dataset. If
          this is not defined, it will be taken from the first raster
          dataset.1_BIT-The pixel type will be a 1-bit unsigned integer. The
          values can
          be 0 or 1.2_BIT-The pixel type will be a 2-bit unsigned integer. The
          values
          supported can range from 0 to 3.4_BIT-The pixel type will be a 4-bit
          unsigned integer. The values
          supported can range from 0 to 15.8_BIT_UNSIGNED-The pixel type will be
          an unsigned 8-bit data type. The
          values supported can range from 0 to 255.8_BIT_SIGNED-The pixel type
          will be a signed 8-bit data type. The
          values supported can range from -128 to 127.16_BIT_UNSIGNED-The pixel
          type will be a 16-bit unsigned data type.
          The values can range from 0 to 65,535.16_BIT_SIGNED-The pixel type
          will be a 16-bit signed data type. The
          values can range from -32,768 to 32,767.32_BIT_UNSIGNED-The pixel type
          will be a 32-bit unsigned data type.
          The values can range from 0 to 4,294,967,295.32_BIT_SIGNED-The pixel
          type will be a 32-bit signed data type. The
          values can range from -2,147,483,648 to 2,147,483,647.32_BIT_FLOAT-The
          pixel type will be a 32-bit data type supporting
          decimals.64_BIT-The pixel type will be a 64-bit data type supporting
          decimals.
      where_clause {SQL Expression}:
          An SQL expression to select raster datasets that will be included in
          the output mosaic dataset.
      in_template_dataset {Raster Layer / Feature Layer}:
          Select raster datasets based on the extent of another image or
          feature class. Raster datasets that lay along the defined extent will
          be included in the mosaic dataset. To manually input the minimum and
          maximum coordinates for the extent, use theparameter. Extent
      extent {Envelope}:
          The minimum and maximum coordinates for the extent.
      select_using_features {Boolean}:
          Limit the extent to the shape or envelope when a feature class is
          specified in the in_template_dataset
          parameter.SELECT_USING_FEATURES-Select using the shape of the feature.
          This is
          the default.NO_SELECT_USING_FEATURES-Select using the extent of the
          data in the
          feature class.
      lod_field {Field}:
          Scale Field
      minPS_field {Field}:
          Specify a field from the footprint attribute table that defines the
          minimum cell size for displaying the mosaic dataset; otherwise, only a
          footprint will be displayed.
      maxPS_field {Field}:
          Specify a field from the footprint attribute table that defines the
          maximum cell size for displaying the mosaic dataset; otherwise, only a
          footprint will be displayed.
      pixelSize {Double}:
          Set a maximum cell size to display the mosaic instead of specifying a
          field. If you zoom out beyond this cell size, only the footprint will
          be displayed.
      build_boundary {Boolean}:
          Rebuild the boundary. If the selection covers a smaller area than the
          source mosaic dataset, this is recommended.This is only available if
          the mosaic dataset is created in a
          geodatabase.BUILD_BOUNDARY-The boundary will be generated or updated.
          This is the
          default.NO_BOUNDARY-The boundary will not be generated.

     OUTPUTS:
      out_mosaic_dataset (Mosaic Dataset):
          The referenced mosaic dataset to be created.

        """