# Generated documentation for module arcpy.geoai


class TransformTextUsingDeepLearning(object):
    """
    Runs a trained sequence-to-sequence model on a text field in a feature class or table and updates it with a new field containing the converted, transformed, or translated text.
    """

    @property
    def description(self) -> str:
        return """

        TransformTextUsingDeepLearning_geoai(in_table, text_field, in_model_definition_file, {result_field}, {model_arguments;model_arguments...}, {batch_size}, {minimum_sequence_length}, {maximum_sequence_length})

        Runs a trained sequence-to-sequence model on a text field in a feature
        class or table and updates it with a new field containing the
        converted, transformed, or translated text.

     INPUTS:
      in_table (Feature Layer / Table View / Feature Class):
          The input point, line, or polygon feature class, or table, containing
          the text that will be transformed.
      text_field (Field):
          A text field in the input feature class or table that contains the
          text that will be transformed.
      in_model_definition_file (File):
          The trained model that will be used for classification. The model
          definition file can be an Esri model definition JSON file (.emd), or a
          deep learning model package (.dlpk) that is stored locally or hosted
          on ArcGIS Living Atlas (.dlpk_remote).
      result_field {String}:
          The name of the field that will contain the transformed text
          in the output feature class or table. The default field name is.
          Result
      model_arguments {Value Table}:
          Additional arguments, such as a confidence threshold, that will be
          used to adjust the sensitivity of the model.The names of the arguments
          will be populated by the tool.
      batch_size {Double}:
          The number of training samples that will be processed at one time. The
          default value is 4.Increasing the batch size can improve tool
          performance; however, as
          the batch size increases, more memory is used. If an out of memory
          error occurs, use a smaller batch size.
      minimum_sequence_length {Double}:
          The minimum number of characters for the output text string. The
          default value is 20.
      maximum_sequence_length {Double}:
          The maximum number of characters for the output text string. The
          default value is 50.

        """