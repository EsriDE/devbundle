# Generated documentation for module arcpy.geoai


class ClassifyTextUsingDeepLearning(object):
    """
    Runs a trained text classification model on a text field in a feature class or table and updates each record with an assigned class or category label with each class having a confidence value.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyTextUsingDeepLearning_geoai(in_table, text_field, in_model_definition_file, {class_label_field}, {model_arguments;model_arguments...}, {explain}, {batch_size})

        Runs a trained text classification model on a text field in a feature
        class or table and updates each record with an assigned class or
        category label with each class having a confidence value.

     INPUTS:
      in_table (Feature Layer / Table View):
          The input point, line, or polygon feature class, or table, containing
          the text that will be classified and labelled.
      text_field (Field):
          A text field in the input feature class or table that contains the
          text that will be classified.
      in_model_definition_file (File):
          The trained model that will be used for classification. The model
          definition file can be an Esri model definition JSON file (.emd) or a
          deep learning model package (.dlpk) that is stored locally or hosted
          on ArcGIS Living Atlas (.dlpk_remote).
      class_label_field {String}:
          The name of the field that will contain the class or category
          label assigned by the model. The default field name is.
          ClassLabel
      model_arguments {Value Table}:
          Additional arguments, such as sequence_length or confidence_threshold,
          that will be used to adjust the model's output.The names of the
          arguments will be populated by the tool.The model argument
          confidence_threshold is only applicable for
          multilabel text classification.
      explain {Boolean}:
          ENABLE_SHAP-A SHAP explanation will be generated for each row in the
          output table.DISABLE_SHAP-No SHAP explanation will be generated. This
          is the
          default.
      batch_size {Double}:
          The number of training samples that will be processed at one time. The
          default value is 4.Increasing the batch size can improve tool
          performance; however, as
          the batch size increases, more memory is used. If an out of memory
          error occurs, use a smaller batch size.

        """