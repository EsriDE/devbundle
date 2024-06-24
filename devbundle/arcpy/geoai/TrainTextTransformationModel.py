# Generated documentation for module arcpy.geoai


class TrainTextTransformationModel(object):
    """
    Trains a text transformation model to transform, translate, or summarize text.
    """

    @property
    def description(self) -> str:
        return """

        TrainTextTransformationModel_geoai(in_table, text_field, label_field, out_model, {pretrained_model_file}, {max_epochs}, {model_backbone}, {batch_size}, {model_arguments;model_arguments...}, {learning_rate}, {validation_percentage}, {stop_training}, {make_trainable}, {remove_html_tags}, {remove_urls})

        Trains a text transformation model to transform, translate, or
        summarize text.

     INPUTS:
      in_table (Feature Class / Table View / Feature Layer):
          A feature class or table containing a text field with the input text
          for the model and a label field containing the target transformed
          text.
      text_field (Field):
          A text field in the input feature class or table that contains the
          input text that will be transformed by the model.
      label_field (Field):
          A text field in the input feature class or table that contains the
          target transformed text for training the model.
      pretrained_model_file {File}:
          A pretrained model that will be used to fine-tune the new model. The
          input can be an Esri model definition file (.emd) or a deep learning
          package file (.dlpk).A pretrained model that performs a similar task
          can be fine-tuned to
          fit the training data. The pretrained model must have been trained
          with the same model type and backbone model that will be used to train
          the new model.
      max_epochs {Long}:
          The maximum number of epochs for which the model will be trained. A
          maximum epoch value of 1 means the dataset will be passed forward and
          backward through the neural network one time. The default value is 5.
      model_backbone {String}:
          Specifies the preconfigured neural network that will be used as the
          architecture for training the new model.t5-small-The new model will be
          trained using the T5 neural network. T5
          is a unified framework that converts every language problem into a
          text-to-text format. t5-small is the small variant of T5.t5-base-The
          new model will be trained using the T5 neural network. T5
          is a unified framework that converts every language problem into a
          text-to-text format. t5-base is the medium variant of T5.t5-large-The
          new model will be trained using the T5 neural network. T5
          is a unified framework that converts every language problem into a
          text-to-text format. t5-large is the large variant of T5.
      batch_size {Double}:
          The number of training samples that will be processed at one time. The
          default value is 2.Increasing the batch size can improve tool
          performance; however, as
          the batch size increases, more memory is used. If an out of memory
          error occurs, use a smaller batch size.
      model_arguments {Value Table}:
          Additional arguments for initializing the model, such as seq_len for
          the maximum sequence length of the training data, that will be
          considered for training the model.See keyword arguments in the
          SequenceToSequence documentation for the
          list of supported models arguments that can be used.
      learning_rate {Double}:
          The step size indicating how much the model weights will be adjusted
          during the training process. If no value is specified, an optimal
          learning rate will be deduced automatically.
      validation_percentage {Double}:
          The percentage of training samples that will be used for validating
          the model. The default value is 10.
      stop_training {Boolean}:
          Specifies whether model training will stop when the model is no longer
          improving or until the max_epochs parameter value is
          reached.STOP_TRAINING-The model training will stop when the model is
          no longer
          improving, regardless of the max_epochs parameter value specified.
          This is the default.CONTINUE_TRAINING-The model training will continue
          until the
          max_epochs parameter value is reached.
      make_trainable {Boolean}:
          Specifies whether the backbone layers in the pretrained model will be
          frozen, so that the weights and biases remain as originally
          designed.TRAIN_MODEL_BACKBONE-The backbone layers will not be frozen,
          and the
          weights and biases of the model_backbone parameter value can be
          altered to fit the training samples. This takes more time to process
          but typically produces better results. This is the
          default.FREEZE_MODEL_BACKBONE-The backbone layers will be frozen, and
          the
          predefined weights and biases of the model_backbone parameter value
          will not be altered during training.
      remove_html_tags {Boolean}:
          Specifies whether HTML tags will be removed from the input
          text.REMOVE_HTML_TAGS-The HTML tags in the input text will be removed.
          This
          is the default.DO_NOT_REMOVE_HTML_TAGS-The HTML tags in the input text
          will not be
          removed.
      remove_urls {Boolean}:
          Specifies whether URLs will be removed from the input
          text.REMOVE_URLS-The URLs in the input text will be removed. This is
          the
          default.DO_NOT_REMOVE_URLS-The URLs in the input text will not be
          removed.

     OUTPUTS:
      out_model (Folder):
          The output folder location that will store the trained model.

        """