# Generated documentation for module arcpy.management


class GenerateRasterCollection(object):
    """
    Performs batch analysis or processing on image collections contained in a mosaic dataset. The images in the input mosaic dataset can be processed individually or as groups.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRasterCollection_management(out_raster_collection, collection_builder, collection_builder_arguments;collection_builder_arguments..., {raster_function}, {raster_function_arguments;raster_function_arguments...}, {collection_properties;collection_properties...}, {generate_rasters}, {out_workspace}, {format}, {out_base_name})

        Performs batch analysis or processing on image collections contained
        in a mosaic dataset. The images in the input mosaic dataset can be
        processed individually or as groups.

     INPUTS:
      collection_builder (String):
          The input image collection. It can be seen as a template that contains
          arguments such as the source mosaic dataset path, filters to extract a
          subset from the input data source, and so on.Currently, this tool only
          supports SIMPLE_COLLECTION, which allows you
          to define a single data source and a query filter for the data
          source.SIMPLE_COLLECTION-Allows you to define a data source and a
          query
          filter.
      collection_builder_arguments (Value Table):
          The list of arguments to create a subset collection of the mosaic
          dataset.This tool only supports the data source and filter to subset
          the
          mosaic dataset. The DataSource and WhereClause values must be
          completed, otherwise the tool cannot be executed.DataSource-The path
          of the data source.WhereClause-The filter used to
          subset the mosaic dataset.
      raster_function {File / String}:
          The path to a raster function template file (.rft.xml or
          .rft.json). The raster function template will be applied to every item
          in the input mosaic dataset. Thecan be used to create the template. If
          no RFT is defined, this tool will create the output mosaic based on
          the collection_builder_arguments parameter. Function Editor
      raster_function_arguments {Value Table}:
          The parameters associated with the function chain. For example,
          if the function chain applies the NDVI function,
          set the visible and infrared IDs. The raster variable name of the RFT
          should be thefield value in the input data source. Tag
      collection_properties {Value Table}:
          The output mosaic dataset key properties. The key metadata
          properties that are available is based on the
          type of sensor that captured the imagery. Some examples of key
          metadata properties include the following:
          SensorNameProductNameAcquisitionDateCloudCoverSunAzimuthSunElevationSe
          nsorAzimuthSensorElevationOff-nadirAngleBandNameMinimumWavelengthMaxim
          umWavelengthRadianceGainRadianceBiasSolarIrradianceReflectanceGainRefl
          ectanceBias
      generate_rasters {Boolean}:
          Choose to generate raster dataset files of the mosaic dataset items,
          after the application of the RFT.NO_GENERATE_RASTERS-The processing
          defined by the raster function
          template will be appended to the image items from the input data
          source to produce an image item in the output mosaic dataset. This is
          the default.GENERATE_RASTERS-Create raster datasets on disk. You will
          also need to
          specify the out_workspace and format.
      out_workspace {Folder / String}:
          Defines the output location for the persisted raster datasets, if the
          generate_rasters parameter is set to GENERATE_RASTERS.The naming
          convention for the output raster files is
          oid_<oid#>_<Unique_GUID>.
      format {String}:
          The format type of the raster to be generated.TIFF-Tagged Image File
          Format (TIFF)IMAGINE Image-ERDAS IMAGINE
          fileCRF-Cloud Raster Format. This is the default.MRF-Meta Raster
          Format
      out_base_name {String}:
          Defines the output base name for the persisted raster datasets, if the
          generate_rasters parameter is set to GENERATE_RASTERS.

     OUTPUTS:
      out_raster_collection (Mosaic Dataset):
          The full path of the mosaic dataset to be created. The mosaic dataset
          must be stored in a geodatabase.

        """