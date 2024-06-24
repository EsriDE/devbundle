# Generated documentation for module arcpy.gapro


class Forest(object):
    """
    Creates models and generates predictions using an adaptation of the random forest algorithm, which is a supervised machine learning method developed by Leo Breiman and Adele Cutler. Predictions can be performed for both categorical variables (classification) and continuous variables (regression). Explanatory variables can take the form of fields in the attribute table of the training features. In addition to validation of model performance based on the training data, predictions can be made to features.
    """

    @property
    def description(self) -> str:
        return """

        Forest_gapro(prediction_type, in_features, output_trained_features, variable_predict, {treat_variable_as_categorical}, {explanatory_variables;explanatory_variables...}, {features_to_predict}, {variable_of_importance}, {output_predicted}, {explanatory_variable_matching;explanatory_variable_matching...}, {number_of_trees}, {minimum_leaf_size}, {maximum_tree_depth}, {sample_size}, {random_variables}, {percentage_for_validation})

        Creates models and generates predictions using an adaptation of the
        random forest algorithm, which is a supervised machine learning method
        developed by Leo Breiman and Adele Cutler. Predictions can be
        performed for both categorical variables (classification) and
        continuous variables (regression). Explanatory variables can take the
        form of fields in the attribute table of the training features. In
        addition to validation of model performance based on the training
        data, predictions can be made to features.

     INPUTS:
      prediction_type (String):
          Specifies the operation mode of the tool. The tool can be run to train
          a model to only assess performance, predict features, or create a
          prediction surface.TRAIN-A model will be trained, but no predictions
          will be generated.
          Use this option to assess the accuracy of your model before generating
          predictions. This option will output model diagnostics in the messages
          window and a chart of variable importance. This is the
          defaultTRAIN_AND_PREDICT-Predictions or classifications will be
          generated for
          features. Explanatory variables must be provided for both the training
          features and the features to be predicted. The output of this option
          will be a feature class, model diagnostics in the messages window, and
          an optional table of variable importance.
      in_features (Table View):
          The feature class containing the variable_predict parameter and the
          explanatory training variables fields.
      variable_predict (Field):
          The variable from the in_features parameter containing the values to
          be used to train the model. This field contains known (training)
          values of the variable that will be used to predict at unknown
          locations.
      treat_variable_as_categorical {Boolean}:
          CATEGORICAL-variable_predict is a categorical variable and the tool
          will perform classification.NUMERIC-variable_predict is continuous and
          the tool will perform
          regression. This is the default.
      explanatory_variables {Value Table}:
          A list of fields representing the explanatory variables that help
          predict the value or category of variable_predict. Use the
          treat_variable_as_categorical parameter for any variables that
          represent classes or categories (such as land cover or presence or
          absence). Specify the variable as true for any that represent classes
          or categories such as land cover or presence or absence and false if
          the variable is continuous.
      features_to_predict {Table View}:
          A feature layer representing locations where predictions will be made.
          This feature layer must also contain any explanatory variables
          provided as fields that correspond to those used from the training
          data.
      explanatory_variable_matching {Value Table}:
          A list of explanatory_variables specified from in_features on the
          right and their corresponding fields from features_to_predict on the
          left, for example, [["LandCover2000", "LandCover2010"], ["Income",
          "PerCapitaIncome"]].
      number_of_trees {Long}:
          The number of trees to create in the forest model. More trees will
          generally result in more accurate model prediction, but the model will
          take longer to calculate. The default number of trees is 100.
      minimum_leaf_size {Long}:
          The minimum number of observations required to keep a leaf (that is,
          the terminal node on a tree without further splits). The default
          minimum for regression is 5, and the default for classification is 1.
          For very large data, increasing these numbers will decrease the run
          time of the tool.
      maximum_tree_depth {Long}:
          The maximum number of splits that will be made down a tree. Using a
          large maximum depth, more splits will be created, which may increase
          the chances of overfitting the model. The default is data driven and
          depends on the number of trees created and the number of variables
          included.
      sample_size {Long}:
          The percentage of in_features used for each decision tree. The default
          is 100 percent of the data. Samples for each tree are taken randomly
          from two-thirds of the data specified.Each decision tree in the forest
          is created using a random sample or
          subset (approximately two-thirds) of the training data available.
          Using a lower percentage of the input data for each decision tree
          increases the speed of the tool for very large datasets.
      random_variables {Long}:
          The number of explanatory variables used to create each decision
          tree.Each decision tree in the forest is created using a random subset
          of
          the explanatory variables specified. Increasing the number of
          variables used in each decision tree will increase the chances of
          overfitting your model, particularly if there is one or more dominant
          variables. A common practice is to use the square root of the total
          number of explanatory variables if variable_predict is numeric, or
          divide the total number of explanatory variables by 3 if
          variable_predict is categorical.
      percentage_for_validation {Long}:
          The percentage (between 10 percent and 50 percent) of in_features to
          reserve as the test dataset for validation. The model will be trained
          without this random subset of data, and the observed values for those
          features will be compared to the predicted value. The default is 10
          percent.

     OUTPUTS:
      output_trained_features (Feature Class / Table):
          The output feature layer name.
      variable_of_importance {Table}:
          A table containing information describing the importance of each
          explanatory variable to be used in the created model.
      output_predicted {Feature Class / Table}:
          The output feature class that will receive the results of the
          prediction results.

        """