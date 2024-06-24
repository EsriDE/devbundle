# Generated documentation for module arcpy.geoai


class TrainUsingAutoML(object):
    """
    Trains a deep learning model by building training pipelines and automating much of the training process. This includes exploratory data analysis, feature selection, feature engineering, model selection, hyperparameter tuning, and model training. Its outputs include performance metrics of the best model on the training data, as well as the trained deep learning model package (.dlpk) that can be used as input for the Predict Using AutoML tool to predict on a new dataset.
    """

    @property
    def description(self) -> str:
        return """

        TrainUsingAutoML_geoai(in_features, out_model, variable_predict, {treat_variable_as_categorical}, {explanatory_variables;explanatory_variables...}, {distance_features;distance_features...}, {explanatory_rasters;explanatory_rasters...}, {total_time_limit}, {autoML_mode}, {algorithms;algorithms...}, {validation_percent}, {out_report}, {out_importance}, {out_features}, {add_image_attachments}, {sensitive_feature;sensitive_feature...}, {fairness_metric})

        Trains a deep learning model by building training pipelines and
        automating much of the training process. This includes exploratory
        data analysis, feature selection, feature engineering, model
        selection, hyperparameter tuning, and model training. Its outputs
        include performance metrics of the best model on the training data, as
        well as the trained deep learning model package (.dlpk) that can be
        used as input for the Predict Using AutoML tool to predict on a new
        dataset.

     INPUTS:
      in_features (Feature Layer / Table View / Feature Class):
          The input feature class that will be used to train the model.
      variable_predict (Field):
          A field from the in_features parameter that contains the values that
          will be used to train the model. This field contains known (training)
          values of the variable that will be used to predict at unknown
          locations.
      treat_variable_as_categorical {Boolean}:
          Specifies whether the variable_predict parameter value will be treated
          as a categorical variable.CATEGORICAL-The variable_predict parameter
          value will be treated as a
          categorical variable and classification will be
          performed.CONTINUOUS-The variable_predict parameter value will be
          treated as
          continuous and regression will be performed. This is the default.
      explanatory_variables {Value Table}:
          A list of fields representing the explanatory variables that will help
          predict the value or category of the variable_predict parameter value.
          Pass the true value ("<name_of_variable> true") for any variables that
          represent classes or categories (such as land cover, presence, or
          absence).
      distance_features {Feature Layer}:
          The features whose distances from the input training features will be
          estimated automatically and added as more explanatory variables.
          Distances will be calculated from each of the input explanatory
          training distance features to the nearest input training features.
          Point and polygon features are supported, and if the input explanatory
          training distance features are polygons, the distance attributes will
          be calculated as the distance between the closest segments of the pair
          of features.
      explanatory_rasters {Value Table}:
          The rasters whose values will be extracted from the raster and
          considered as explanatory variables for the model. Each layer forms
          one explanatory variable. For each feature in the input training
          features, the value of the raster cell will be extracted at that exact
          location. Bilinear raster resampling will be used when extracting the
          raster value for continuous rasters. Nearest neighbor assignment will
          be used when extracting a raster value from categorical rasters. If
          the in_features parameter value has polygons, and you provided a value
          for this parameter, one raster value for each polygon will be used in
          the model. Each polygon is assigned the average value for continuous
          rasters and the majority for categorical rasters. Pass the true value
          using "<name_of_raster> true" for any raster that depicts classes or
          categories such as land cover, vegetation, or soil type.
      total_time_limit {Double}:
          The total time limit in minutes it takes for AutoML model training.
          The default is 240 (4 hours).
      autoML_mode {String}:
          Specifies the goal of AutoML and how intensive the AutoML search will
          be.BASIC-Basic is used to explain the significance of the different
          variables and the data. Feature engineering, feature selection, and
          hyperparameter tuning will not be performed. Full descriptions and
          explanations for model learning curves, feature importance plots
          generated for tree-based models, and SHAP plots for all other models
          will be included in reports. This mode takes the least amount of
          processing time. This is the default.INTERMEDIATE-Intermediate is used
          to train a model that will be used
          in real-life use cases. This mode uses 5-fold cross validation (CV)
          and produces output of learning curves and importance plots in the
          reports, but SHAP plots are not available.ADVANCED-Advanced is used
          for machine learning competitions (for
          maximum performance). This mode uses 10-fold cross validation (CV) and
          performs feature engineering, feature selection, and hyperparameter
          tuning. Input training features are assigned to multiple spatial grids
          of different sizes based on their location, and the corresponding grid
          IDs are passed as additional categorical explanatory variables to the
          model. The report only includes learning curves; model explainability
          is not available.
      algorithms {String}:
          Specifies the algorithms that will be used during the
          training.LINEAR-The Linear regression supervised algorithm will be
          used to
          train a regression machine learning model. If this is the only option
          specified, ensure that the total number of records is less than 10.000
          and the number of columns is less than 1,000. Other models can
          accommodate larger datasets and it is recommended that you use this
          option with other algorithms and not as the sole algorithm.RANDOM
          TREES-The Random Trees decision tree-based supervised machine
          learning algorithm will be used. It can be used for both
          classification and regression.XGBOOST-The XGBoost (extreme gradient
          boosting) supervised machine
          learning algorithm will be used. It can be used for both
          classification and regression.LIGHT GBM-The Light GBM gradient
          boosting ensemble algorithm, which is
          based on decision trees, will be used. It can be used for both
          classification and regression. Light GBM is optimized for high
          performance with distributed systems.DECISION TREE-The Decision Tree
          supervised machine learning
          algorithm, which classifies or regresses the data using true and false
          answers to certain questions, will be used. Decision trees are easily
          understood and are good for explainability.EXTRA TREE-The Extra Tree
          (extremely randomized trees) ensemble
          supervised machine learning algorithm, which uses decision trees, will
          be used. This algorithm is similar to Random Trees but can be
          faster.CATBOOST-The CatBoost algorithm will be used. It uses decision
          trees
          for classification and regression. This option can use a combination
          of categorical and noncategorical explanatory variables without
          preprocessing.By default, all the algorithms will be used.
      validation_percent {Long}:
          The percentage of input data that will be used for validation. The
          default value is 10.
      add_image_attachments {Boolean}:
          Specifies whether images will be used as explanatory variables from
          the in_features parameter value for training a multimodal or mixed
          data model. Training a multimodal or mixed data tabular model involves
          using machine and deep learning backbones in AutoML to learn from
          multiple types of data formats by a single model. The input data can
          consist of a combination of explanatory variables from a diverse set
          of data sources such as text descriptions, corresponding images, and
          any additional categorical and continuous variables.TRUE-The image
          attachments will be downloaded and treated as
          explanatory variables and multimodal data training will be
          performed.FALSE-The image attachments will not be used during the
          training. This
          is the default.
      sensitive_feature {Value Table}:
          Assesses and improves the fairness of the trained models for
          tabular data for classification and regression models. Set the
          following two components for this parameter:        Sensitive
          Features-An attribute such as race, gender, socioeconomic
          status, or age that can introduce bias in machine learning or deep
          learning models. By selecting sensitive features such as race, gender,
          socioeconomic status, or age, biases associated with the specific
          sensitive features are mitigated for an unbiased model.Underprivileged
          Groups-The discriminated group from the Sensitive
          Features value provided.
      fairness_metric {String}:
          Specifies the fairness metrics that will be used for measuring
          fairness for classification and regression problems, which are used
          for grid searches for selecting the best fair
          model.DEMOGRAPHIC_PARITY_RATIO-This metric is used in classification
          models.
          The ratio of selection rates between different groups of individuals
          will be measured. The selection rate is the proportion of individuals
          who are classified as positive by the model. The ideal value for this
          metric is 1, which indicates that the selection rates for different
          groups are equal. Fairness for this metric is between 0.8 to 1,
          meaning that the ratio of selection rates between groups should be no
          more than 20 percent.DEMOGRAPHIC_PARITY_DIFFERENCE-This metric is used
          in classification
          models. It is similar to the demographic parity ratio metric, but the
          difference in selection rates between different groups of individuals
          will be measured, rather than the ratio. The selection rate is the
          proportion of individuals who are classified as positive by the model.
          The ideal value for this metic is 0, which indicates that there is no
          difference in selection rates between groups. Fairness for this metric
          is between 0 to 0.25, meaning that differences in selection rates
          between groups should be no more than 25
          percent.EQUALISED_ODDS_RATIO-This metric is used in classification
          models. The
          ratio of error rates between groups of individuals, such as different
          racial ro gender groups, will be measured. The ideal value for this
          metric is 1, which indicates that the error rates for different groups
          are equal. Fairness for this metric is between 0.8 to 1, meaning that
          the ratio of error between groups should be no more than 20
          percent.EQUALISED_ODDS_DIFFERENCE-This metric is used in
          classification
          models. It is similar to the equalized odds ratio metric, but the
          difference in error between different groups of individuals will be
          measured, rather than the ratio. The ideal value for this metric is 0,
          which indicates that there is no difference in error between groups.
          Fairness for this metric is between 0 to 0.25, meaning that difference
          in error between groups should be no more than 25
          percent.GROUP_LOSS_RATIO-This metric is used in regression models. The
          ratio
          of the average loss or error for one subgroup compared to another
          subgroup will be measured. It provides a relative measure of the
          disparity in losses between groups. A value of 1 indicates no
          difference in losses between the groups, while values greater or
          smaller than 1 indicate relative disparities.

     OUTPUTS:
      out_model (File):
          The output trained model that will be saved as a deep learning package
          (.dlpk file).
      out_report {File}:
          The output report that will be generated as an .html file. If the path
          provided is not empty, the report will be created in a new folder
          under the provided path. The report will contain details of the
          various models as well as details of the hyperparameters that were
          used during the evaluation and the performance of each model.
          Hyperparameters are parameters that control the training process. They
          are not updated during training and include model architecture,
          learning rate, number of epochs, and so on.
      out_importance {Table}:
          An output table containing information about the importance of each
          explanatory variable (fields, distance features, and rasters) used in
          the model.
      out_features {Feature Class}:
          The feature layer containing the predicted values by the best
          performing model on the training feature layer. It can be used to
          verify model performance by visually comparing the predicted values
          with the ground truth.

        """