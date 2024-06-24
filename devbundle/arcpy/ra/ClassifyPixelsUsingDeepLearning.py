# Generated documentation for module arcpy.ra


class ClassifyPixelsUsingDeepLearning(object):
    """
    Runs a trained deep learning model on an input image to produce a classified raster published as a hosted imagery layer in your portal.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyPixelsUsingDeepLearning_ra(inputRaster, inputModel, outputName, {modelArguments;modelArguments...}, {processingMode})

        Runs a trained deep learning model on an input image to produce a
        classified raster published as a hosted imagery layer in your portal.

     INPUTS:
      inputRaster (Image Service / Raster Layer / Map Server / Map Server Layer / Internet Tiled Layer / String):
          The input image to classify. It can be an image service URL, a raster
          layer, an image service, a map server layer, or an Internet tiled
          layer.
      inputModel (File):
          The input is a URL of a deep learning package (.dlpk) item. It
          contains the path to the deep learning binary model file, the path to
          the Python raster function to be used, and other parameters such as
          preferred tile size or padding.
      outputName (String):
          The name of the image service of the classified pixels.
      modelArguments {Value Table}:
          The function arguments are defined in the Python raster function class
          referenced by the input model. This is where you list additional deep
          learning parameters and arguments for experiments and refinement, such
          as a confidence threshold for adjusting the sensitivity. The names of
          the arguments are populated by the tool from reading the Python module
          on the RA server.
      processingMode {String}:
          Specifies how all raster items in a mosaic dataset or an image service
          will be processed. This parameter is applied when the input raster is
          a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_IMAGE-All
          raster items in the mosaic dataset or
          image service will be mosaicked together and processed. This is the
          default.PROCESS_ITEMS_SEPARATELY-All raster items in the mosaic
          dataset or
          image service will be processed as separate images.

        """