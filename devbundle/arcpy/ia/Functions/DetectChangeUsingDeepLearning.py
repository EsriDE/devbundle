# Generated documentation for module arcpy.ia.Functions


class DetectChangeUsingDeepLearning(object):
    """
    Runs a trained deep learning model to detect change between two rasters.
    """

    @property
    def description(self) -> str:
        return """

        DetectChangeUsingDeepLearning_ia(from_raster, to_raster, in_model_definition, {arguments;arguments...})

        Runs a trained deep learning model to detect change between two
        rasters.

     INPUTS:
      from_raster (Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer):
          The input raster before the change.
      to_raster (Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer):
          The input raster after the change.
      in_model_definition (File / String):
          The in_model_definition parameter value can be an Esri model
          definition JSON file (.emd), a JSON string, or a deep learning model
          package (.dlpk). A JSON string is useful when this tool is used on the
          server so you can paste the JSON string rather than upload the .emd
          file. The .dlpk file must be stored locally.It contains the path to
          the deep learning binary model file, the path
          to the Python raster function to be used, and other parameters such as
          preferred tile size or padding.
      arguments {Value Table}:
          The information from the in_model_definition parameter will be used to
          set the default values for this parameter. These arguments vary,
          depending on the model architecture. The following are supported model
          arguments for models trained in ArcGIS. ArcGIS pretrained models and
          custom deep learning models may have additional arguments that the
          tool supports.padding-The number of pixels at the border of image
          tiles from which
          predictions are blended for adjacent tiles. To smooth the output while
          reducing artifacts, increase the value. The maximum value of the
          padding can be half of the tile size value. The argument is available
          for all model architectures.batch_size-The number of image tiles
          processed in each step of the
          model inference. This depends on the memory of your graphic card. The
          argument is available for all model architectures.

     OUTPUTS:
      out_classified_raster (Raster Dataset):
          The output classified raster that shows the change.

        """