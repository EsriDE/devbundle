# Generated documentation for module arcpy.ra


class ClassifyObjectsUsingDeepLearning(object):
    """
    Runs a trained deep learning model on an input raster and an optional feature class to produce a feature class or table in which each input object or feature has an assigned class or category label.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyObjectsUsingDeepLearning_ra(inputRaster, inputModel, outputName, {inputFeatures}, {modelArguments;modelArguments...}, {classLabelField}, {processingMode})

        Runs a trained deep learning model on an input raster and an optional
        feature class to produce a feature class or table in which each input
        object or feature has an assigned class or category label.

     INPUTS:
      inputRaster (Image Service / Raster Layer / Map Server / Feature Layer / Map Server Layer / Internet Tiled Layer / String):
          The input image to classify. The image can be an image service URL, a
          raster layer, an image service, a map server layer, or an internet
          tiled layer.
      inputModel (File):
          The deep learning model that will be used to classify objects in the
          input image. The input is the URL of a deep learning package (.dlpk)
          item that contains the path to the deep learning binary model file,
          the path to the Python raster function to be used, and other
          parameters such as preferred tile size or padding.
      outputName (String):
          The name of the feature service containing the classified objects.
      inputFeatures {Feature Layer / Map Server Layer / String}:
          The feature service that identifies the location of each object or
          feature to be classified and labeled. Each row in the input feature
          service represents a single object or feature.If no input feature
          service is specified, each input image will be
          classified as a single object. If the input image or images use a
          spatial reference, the output from the tool is a feature class in
          which the extent of each image is used as the bounding geometry for
          each labeled feature class. If the input image or images are not
          spatially referenced, the output from the tool is a table containing
          the image ID values and the class labels for each image.
      modelArguments {Value Table}:
          The function model arguments to use for the classification. These are
          defined in the Python raster function class referenced by the input
          model. This is where you list additional deep learning parameters and
          arguments for experiments and refinement, such as a confidence
          threshold for adjusting the sensitivity. The names of the arguments
          are populated by the tool from the Python module on the Raster
          Analytics server.
      classLabelField {String}:
          The name of the field that will contain the class or category label in
          the output feature class. If a field name is not specified, a
          new field namedwill be
          generated in the output feature class. ClassLabel
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