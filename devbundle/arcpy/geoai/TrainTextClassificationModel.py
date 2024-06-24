# Generated documentation for module arcpy.geoai


class TrainTextClassificationModel(object):
    """
    Trains a single or multilabel text classification model to assign a predefined category or label to unstructured text.
    """

    @property
    def description(self) -> str:
        return """

        TrainTextClassificationModel_geoai(in_table, text_field, label_field;label_field..., out_model, {pretrained_model_file}, {max_epochs}, {model_backbone}, {batch_size}, {model_arguments;model_arguments...}, {learning_rate}, {validation_percentage}, {stop_training}, {make_trainable}, {remove_html_tags}, {remove_urls})

        Trains a single or multilabel text classification model to assign a
        predefined category or label to unstructured text.

     INPUTS:
      in_table (Feature Class / Table View / Feature Layer):
          A feature class or table containing a text field with the input text
          for the model and a label field containing the target class labels.
      text_field (Field):
          A text field in the input feature class or table that contains the
          text that will be classified by the model.
      label_field (Field):
          A text field in the input feature class or table that contains the
          target class labels for training the model. In the case of multilabel
          text classification, specify more than one text field.
      pretrained_model_file {File}:
          A pretrained model that will be used to fine-tune the new model. The
          input can be an Esri model definition file (.emd) or a deep learning
          package file (.dlpk).A pretrained model with similar classes can be
          fine-tuned to fit the
          new model. The pretrained model must have been trained with the same
          model type and backbone model that will be used to train the new
          model.
      max_epochs {Long}:
          The maximum number of epochs for which the model will be trained. A
          maximum epoch value of 1 means the dataset will be passed forward and
          backward through the neural network one time. The default value is 5.
      model_backbone {String}:
          Specifies the preconfigured neural network that will serve as the
          encoder for the model and extract feature representations of the input
          text in the form of fixed length vectors. These vectors are then
          passed as input to the classification head of the model.bert-base-
          cased-The model will be trained using the BERT neural
          network. BERT is pretrained using the masked language modeling
          objective and next sentence prediction.roberta-base-The model will be
          trained using the RoBERTa neural
          network. RoBERTa modifies the key hyperparameters of BERT, eliminating
          the pretraining objective and training of the next sentence with small
          batches and higher learning rates.albert-base-v1-The model will be
          trained using the ALBERT neural
          network. ALBERT uses a self-supervised loss that focuses on modeling
          intersentence coherence, resulting in better scalability than
          BERT.xlnet-base-cased-The model will be trained using the XLNet neural
          network. XLNet is a generalized autoregressive pretraining method. It
          allows learning bidirectional contexts by maximizing the expected
          probability on all permutations of the factorization order, which
          overcomes BERT's drawbacks.xlm-roberta-base-The model will be trained
          using the XLM-RoBERTa
          neural network. XLM-RoBERTa is a multilingual model trained on 100
          different languages. Unlike some XLM multilingual models, it does not
          require language tensors to understand which language is used and
          identifies the correct language from the input IDs.distilroberta-
          base-The model will be trained using the DistilRoBERTa
          neural network. DistilRoBERTa is an English language model pretrained
          with the supervision of roberta-base solely on OpenWebTextCorpus, a
          reproduction of OpenAI's WebText dataset.distilbert-base-cased-The
          model will be trained using the DistilBERT
          neural network. DistilBERT is a smaller general-purpose language
          representation model.
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
          TextClassifier documentation for the list
          of supported model arguments that can be used.
      learning_rate {Double}:
          The step size indicating how much the model weights will be adjusted
          during the training process. If no value is specified, an optimal
          learning rate will be determined automatically.
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