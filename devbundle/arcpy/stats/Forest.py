# Generated documentation for module arcpy.stats


class Forest(object):
    """
    Creates models and generates predictions using one of two supervised machine learning methods: an adaptation of the random forest algorithm developed by Leo Breiman and Adele Cutler or the Extreme Gradient Boosting (XGBoost) algorithm developed by Tianqi Chen and Carlos Guestrin. Predictions can be performed for both categorical variables (classification) and continuous variables (regression). Explanatory variables can take the form of fields in the attribute table of the training features, raster datasets, and distance features used to calculate proximity values for use as additional variables. In addition to validation of model performance based on the training data, predictions can be made to either features or a prediction raster.
    """

    @property
    def description(self) -> str:
        return """

        Forest_stats(prediction_type, in_features, {variable_predict}, {treat_variable_as_categorical}, {explanatory_variables;explanatory_variables...}, {distance_features;distance_features...}, {explanatory_rasters;explanatory_rasters...}, {features_to_predict}, {output_features}, {output_raster}, {explanatory_variable_matching;explanatory_variable_matching...}, {explanatory_distance_matching;explanatory_distance_matching...}, {explanatory_rasters_matching;explanatory_rasters_matching...}, {output_trained_features}, {output_importance_table}, {use_raster_values}, {number_of_trees}, {minimum_leaf_size}, {maximum_depth}, {sample_size}, {random_variables}, {percentage_for_training}, {output_classification_table}, {output_validation_table}, {compensate_sparse_categories}, {number_validation_runs}, {calculate_uncertainty}, {output_trained_model}, {model_type}, {reg_lambda}, {gamma}, {eta}, {max_bins}, {optimize}, {optimize_algorithm}, {optimize_target}, {num_search}, {model_param_setting;model_param_setting...}, {output_param_tuning_table}, {include_probabilities})

        Creates models and generates predictions using one of two supervised
        machine learning methods: an adaptation of the random forest algorithm
        developed by Leo Breiman and Adele Cutler or the Extreme Gradient
        Boosting (XGBoost) algorithm developed by Tianqi Chen and Carlos
        Guestrin. Predictions can be performed for both categorical variables
        (classification) and continuous variables (regression). Explanatory
        variables can take the form of fields in the attribute table of the
        training features, raster datasets, and distance features used to
        calculate proximity values for use as additional variables. In
        addition to validation of model performance based on the training
        data, predictions can be made to either features or a prediction
        raster.

     INPUTS:
      prediction_type (String):
          Specifies the operation mode that will be used. The tool can be run to
          train a model to only assess performance, predict features, or create
          a prediction surface.TRAIN-A model will be trained, but no predictions
          will be generated.
          Use this option to assess the accuracy of the model before generating
          predictions. This option will output model diagnostics in the messages
          window and a chart of variable importance. This is the
          default.PREDICT_FEATURES-Predictions or classifications will be
          generated for
          features. Explanatory variables must be provided for both the training
          features and the features to be predicted. The output of this option
          will be a feature class, model diagnostics in the messages window, and
          an optional table and chart of variable importance.PREDICT_RASTER-A
          prediction raster will be generated for the area
          where the explanatory rasters intersect. Explanatory rasters must be
          provided for both the training area and the area to be predicted. The
          output of this option will be a prediction surface, model diagnostics
          in the messages window, and an optional table and chart of variable
          importance.
      in_features (Feature Layer):
          The feature class containing the variable_predict parameter value and,
          optionally, the explanatory training variables from fields.
      variable_predict {Field}:
          The variable from the in_features parameter value containing the
          values to be used to train the model. This field contains known
          (training) values of the variable that will be used to predict at
          unknown locations.
      treat_variable_as_categorical {Boolean}:
          CATEGORICAL-The variable_predict value is a categorical variable and
          classification will be performed.NUMERIC-The variable_predict value is
          continuous and regression will
          be performed. This is the default
      explanatory_variables {Value Table}:
          A list of fields representing the explanatory variables that help
          predict the value or category of the variable_predict value. Use the
          treat_variable_as_categorical parameter for any variables that
          represent classes or categories (such as land cover or presence or
          absence). Specify the variable as CATEGORICAL if it represents classes
          or categories such as land cover or presence or absence, and specify
          NUMERIC if it is continuous.
      distance_features {Feature Layer}:
          The explanatory training distance features. Explanatory variables will
          be automatically created by calculating a distance from the provided
          features to the in_features values. Distances will be calculated from
          each of the features in the in_features value to the nearest
          distance_features values. If the input distance_features values are
          polygons or lines, the distance attributes will be calculated as the
          distance between the closest segments of the pair of features.
      explanatory_rasters {Value Table}:
          The explanatory training variables extracted from rasters. Explanatory
          training variables will be automatically created by extracting raster
          cell values. For each feature in the in_features parameter, the value
          of the raster cell is extracted at that exact location. Bilinear
          raster resampling is used when extracting the raster value unless it
          is specified as categorical, in which case nearest neighbor assignment
          is used. Specify the raster as CATEGORICAL if it represents classes or
          categories such as land cover or presence or absence, and specify
          NUMERIC if it is continuous.
      features_to_predict {Feature Layer}:
          A feature class representing the locations where predictions will be
          made. This feature class must also contain any explanatory variables
          provided as fields that correspond to those used from the training
          data.
      explanatory_variable_matching {Value Table}:
          A list of the explanatory_variables values specified from the
          in_features parameter on the right and corresponding fields from the
          features_to_predict parameter on the left, for example,
          [["LandCover2000", "LandCover2010"], ["Income", "PerCapitaIncome"]].
      explanatory_distance_matching {Value Table}:
          A list of the distance_features values specified for the in_features
          parameter on the right and corresponding feature sets from the
          features_to_predict parameter on the
          left.explanatory_distance_features values that are more appropriate
          for the
          features_to_predict parameter can be provided if those used for
          training are in a different study area or time period.
      explanatory_rasters_matching {Value Table}:
          A list of the explanatory_rasters values specified for the in_features
          on the right and corresponding rasters from the features_to_predict
          parameter or output_raster parameter to be created on the left.The
          explanatory_rasters values that are more appropriate for the
          features_to_predict parameter can be provided if those used for
          training are in a different study area or time period.
      use_raster_values {Boolean}:
          Specifies how polygons will be treated when training the model if the
          in_features values are polygons with a categorical variable_predict
          value and only explanatory_rasters values have been provided.TRUE-The
          polygon will be divided into all of the raster cells with
          centroids falling within the polygon. The raster values at each
          centroid will be extracted and used to train the model. The model will
          no longer be trained on the polygon; it will be trained on the raster
          values extracted for each cell centroid. This is the
          default.FALSE-Each polygon will be assigned the average value of the
          underlying continuous rasters and the majority for underlying
          categorical rasters.
      number_of_trees {Long}:
          The number of trees that will be created in the Forest-based and
          Gradient Boosted models. The default is 100.If the model_type
          parameter value is FOREST-BASED, more trees will
          generally result in more accurate model predictions; however, the
          model will take longer to calculate. If the model_type parameter value
          is GRADIENT_BOOSTED, more trees may result in more accurate model
          predictions; however, they may also lead to overfitting the training
          data. To avoid overfitting the data, provide values for the
          maximum_depth, reg_lambda, gamma, and eta parameters.
      minimum_leaf_size {Long}:
          The minimum number of observations required to keep a leaf (that is,
          the terminal node on a tree without further splits). The default
          minimum for regression is 5 and the default for classification is 1.
          For very large data, increasing these numbers will decrease the run
          time of the tool.
      maximum_depth {Long}:
          The maximum number of splits that will be made down a tree. Using a
          large maximum depth, more splits will be created, which may increase
          the chances of overfitting the model. If the model_type parameter
          value is FOREST-BASED, the default is data driven and depends on the
          number of trees created and the number of variables included. If the
          model_type parameter value is GRADIENT_BOOSTED, the default is 6.
      sample_size {Long}:
          The percentage of the in_features values that will be used for each
          decision tree. The default is 100 percent of the data. Samples for
          each tree are taken randomly from two-thirds of the data
          specified.Each decision tree in the forest is created using a random
          sample or
          subset (approximately two-thirds) of the training data available.
          Using a lower percentage of the input data for each decision tree
          decreases the run time of the tool for very large datasets.
      random_variables {Long}:
          The number of explanatory variables that will be used to create each
          decision tree.Each decision tree in the forest is created using a
          random subset of
          the specified explanatory variables. Increasing the number of
          variables used in each decision tree will increase the chances of
          overfitting the model, particularly if there is one or more dominant
          variables. A common practice is to use the square root of the total
          number of explanatory variables (fields, distances, and rasters
          combined) if the variable_predict value is categorical or to divide
          the total number of explanatory variables (fields, distances, and
          rasters combined) by 3 if the variable_predict value is numeric.
      percentage_for_training {Double}:
          The percentage (between 10 percent and 50 percent) of the in_features
          values that will be reserved as the test dataset for validation. The
          model will be trained without this random subset of data, and the
          observed values for those features will be compared to the predicted
          value. The default is 10 percent.
      compensate_sparse_categories {Boolean}:
          Specifies whether each category in the training dataset, regardless of
          its frequency, will be represented in each tree. This parameter is
          available when the model_type parameter value is FOREST-
          BASED.TRUE-Each tree will include every category that is represented
          in the
          training dataset.FALSE-Each tree will be created based on a random
          sample of the
          categories in the training dataset. This is the default.
      number_validation_runs {Long}:
          The number of iterations of the tool.The distribution of R-squared
          values or accuracies of all the models
          can be displayed using the output_validation_table parameter. If the
          prediction_type parameter value is PREDICT_RASTER or PREDICT_FEATURES,
          the model that produced the median R-squared value or accuracy will be
          used to make predictions. Using the median value helps ensure
          stability of the predictions.
      calculate_uncertainty {Boolean}:
          Specifies whether prediction uncertainty will be calculated when
          training, predicting to features, or predicting to raster.This
          parameter is available when the model_type parameter value is
          FOREST-BASED.TRUE-A prediction uncertainty interval will be
          calculated.FALSE-
          Uncertainty will not be calculated. This is the default.
      model_type {String}:
          Specifies the method that will be used to create the model.FOREST-
          BASED-A model will be created using an adaptation of the random
          forest algorithm. The model will use the votes from hundreds of
          decisions trees. Each decision tree will be created from a randomly
          generated subset of the original data and original
          variables.GRADIENT_BOOSTED-A model will be created using the Extreme
          Gradient
          Boosting (XGBoost) algorithm. The model will create a sequence of
          hundreds of trees in which each subsequent tree corrects the errors of
          the previous trees.
      reg_lambda {Double}:
          A regularization term that reduces the model's sensitivity to
          individual features. Increasing this value will make the model more
          conservative and prevent overfitting the training data. If the value
          is 0, the model becomes the traditional Gradient Boosting model. The
          default is 1.This parameter is available when the model_type parameter
          value is
          GRADIENT_BOOSTED.
      gamma {Double}:
          A threshold for the minimum loss reduction needed to split
          trees.Potential splits are evaluated for their loss reduction. If the
          candidate split has a higher loss reduction than this threshold value,
          the partition will occur. Higher threshold values avoid overfitting
          and result in more conservative models with fewer partitions. The
          default is 0.This parameter is available when the model_type parameter
          value is
          GRADIENT_BOOSTED.
      eta {Double}:
          A value that reduces the contribution of each tree to the final
          prediction. The value should be greater than 0 and less than or equal
          to 1. A lower learning rate prevents overfitting the model; however,
          it may require longer computation times. The default is 0.3.This
          parameter is available when the model_type parameter value is
          GRADIENT_BOOSTED.
      max_bins {Long}:
          The number of bins that the training data will be divided into to
          search for the best splitting point. The value cannot be 1. The
          default is 0, which corresponds to the use of a greedy algorithm. A
          greedy algorithm will create a candidate split at every data point.
          Providing too few bins for searching is not recommended because it
          will lead to poor model prediction performance.This parameter is
          available when the model_type parameter value is
          GRADIENT_BOOSTED.
      optimize {Boolean}:
          Specifies whether an optimization method will be used to find the set
          of hyperparameters that achieve optimal model performance.TRUE-An
          optimization method will be used to find the set of
          hyperparameters.FALSE-An optimization method will not be used. This is
          the default.
      optimize_algorithm {String}:
          Specifies the optimization method that will be used to select and test
          search points to find the optimal set of hyperparameters. Search
          points are combinations of hyperparameters within the search space
          specified by the model_param_setting parameter. This option is
          available when the optimize parameter value is TRUE.RANDOM-A
          stratified random sampling algorithm will be used to select
          the search points within the search space. This is the
          default.RANDOM_ROBUST-A stratified random sampling algorithm will be
          used to
          select the search points. Each search will be run 10 times using a
          different random seed. The result of each search will be the median
          best run determined by the optimize_target parameter value. This
          option is available when the model_type parameter value is FOREST-
          BASED.GRID-Every search point within the search space will be
          selected.
      optimize_target {String}:
          Specifies the objective function or value that will be minimized or
          maximized to find the optimal set of hyperparameters. R2-The
          optimization method will maximize Rto find the optimal
          set of hyperparameters. This option is only available when the
          variable to predict is not categorical. This is the default when the
          variable to predict is not categorical. 2RMSE-The optimization
          method will minimize root mean square error to
          find the optimal set of hyperparameters. This option is only available
          when the variable to predict is not categorical.ACCURACY-The
          optimization method will maximize accuracy to find the
          optimal model. This option is only available when the variable to
          predict is categorical. This is the default when the variable to
          predict is categorical.MCC-The optimization method will maximize
          Matthews correlation
          coefficient to find the optimal set of hyperparameters. This option is
          only available when the variable to predict is
          categorical.F1-SCORE-The optimization method will maximize the
          F1-Score to find
          the optimal set of hyperparameters. This option is only available when
          the variable to predict is categorical.
      num_search {Long}:
          The number of search points within the search space specified by the
          model_param_setting parameter that will be tested. This parameter is
          available when the optimize_algorithm parameter value is RANDOM or
          RANDOM_ROBUST.
      model_param_setting {Value Table}:
          A list of hyperparameters and their search spaces. Customize the
          search space of each hyperparameter by providing a lower bound, upper
          bound, and interval. The lower bound and upper bound specify the range
          of possible values for the hyperparameter. The following is the
          range of valid values for each
          hyperparameter:        Number of Trees (number_of_trees)-An integer
          value greater than
          1.Maximum Tree Depth (maximum_depth)-An integer value greater than or
          equal to 0.Minimum Leaf Size (minimum_leaf_size)-An integer value
          greater than 1.Data Available per Tree (%) (sample_size)-An integer
          value greater
          than 0 and less than or equal to 100.Number of Randomly Sampled
          Variables (random_variables)-An integer
          value less than or equal to the number of explanatory variables. This
          includes the explanatory variables from fields, distance features, and
          rasters.Learning Rate (Eta) (eta)-A double value greater than 0 and
          less than
          or equal to 1.L2 Regularization (Lambda) (reg_lambda)-A double value
          greater than or
          equal to 0.Minimum Loss Reduction for Splits (Gamma) (gamma)-A double
          value
          greater than or equal to 0.Maximum Number of Bins for Searching Splits
          (max_bins)-An integer
          value greater than 1 or the value 0. A value of 0 means the model will
          create a candidate split at every data point.
      include_probabilities {Boolean}:
          For categorical variables to predict, specifies whether the
          probability of every category of the categorical variable or only the
          probability of the record's category will be predicted. For example,
          if a categorical variable has categories A, B, and C, and the first
          record has category B, use this parameter to specify whether the
          probability for categories A, B, and C will be predicted or only the
          probability of category B will be
          predicted.ALL_PROBABILITIES-Probabilities for all categories of the
          categorical
          variable will be predicted and included in the
          output.HIGHEST_PROBABILITY_ONLY-Only the probability of the category
          of the
          record will be predicted and included in the output. This is the
          default.

     OUTPUTS:
      output_features {Feature Class}:
          The output feature class containing the prediction results.
      output_raster {Raster Dataset}:
          The output raster containing the prediction results. The default cell
          size will be the maximum cell size of the raster inputs. To set a
          different cell size, use the Cell Size environment setting.
      output_trained_features {Feature Class}:
          The explanatory variables used for training (including sampled raster
          values and distance calculations), as well as the observed
          variable_predict field and accompanying predictions that will be used
          to further assess performance of the trained model.
      output_importance_table {Table}:
          The table that will contain information describing the importance of
          each explanatory variable (fields, distance features, and rasters)
          used to create the model.
      output_classification_table {Table}:
          A confusion matrix that summarizes the performance of the model
          created on the validation data. The matrix compares the model
          predicted categories for the validation data to the actual categories.
          This table can be used to calculate additional diagnostics that are
          not included in the output messages. This parameter is available when
          the variable_predict value is categorical and the
          treat_variable_as_categorical parameter value is CATEGORICAL.
      output_validation_table {Table}:
          A table that contains the Rfor each model if the
          variable_predict value is not categorical, or the accuracy of each
          model if the value is categorical. This table includes a bar chart of
          the distribution of accuracies or the Rvalues. This distribution can
          be used to assess the stability of the model. This parameter is
          available when the number_validation_runs value is greater than 2.
          22
      output_trained_model {File}:
          An output model file that will save the trained model, which can be
          used later for prediction.
      output_param_tuning_table {Table}:
          A table that contains the parameter settings and objective values for
          each optimization trial. The output includes a chart of all the trials
          and their objective values. This option is available when optimize is
          TRUE.

        """