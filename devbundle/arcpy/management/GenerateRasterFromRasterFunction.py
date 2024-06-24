# Generated documentation for module arcpy.management


class GenerateRasterFromRasterFunction(object):
    """
    Generates a raster dataset from an input raster function or function chain.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRasterFromRasterFunction_management(raster_function, out_raster_dataset, {raster_function_arguments;raster_function_arguments...}, {raster_properties;raster_properties...}, {format}, {process_as_multidimensional})

        Generates a raster dataset from an input raster function or function
        chain.

     INPUTS:
      raster_function (File / String):
          The name of a raster function, raster function JSON object, or
          function chain (in .rft.xml format).
      raster_function_arguments {Value Table}:
          The parameters associated with the function chain. For example, if the
          function chain applies the Hillshade raster function, set the data
          source, azimuth, and altitude.
      raster_properties {Value Table}:
          The output raster dataset key properties, such as the sensor or
          wavelength.
      format {String}:
          The output raster format.The default format will be derived from the
          file extension specified
          in the output_raster_dataset value.TIFF-Tagged Image File Format for
          raster datasets will be used.Cloud
          Optimized GeoTIFF-Cloud Optimized GeoTIFF will be used.IMAGINE
          Image-ERDAS IMAGINE raster data format will be used.Esri Grid-Esri
          Grid raster dataset format will be used.CRF-Cloud Raster Format will
          be used.MRF-Meta Raster Format will be used.
      process_as_multidimensional {Boolean}:
          Specifies whether the input mosaic dataset will be processed as a
          multidimensional raster dataset.CURRENT_SLICE-The input will not be
          processed as a multidimensional
          raster dataset. If the input is multidimensional, only the slice that
          is currently displayed will be processed. This is the
          default.ALL_SLICES-The input will be processed as a multidimensional
          raster
          dataset and all slices will be processed to produce a new
          multidimensional raster dataset. Set the format parameter to CRF to
          use this option.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The output raster dataset.

        """