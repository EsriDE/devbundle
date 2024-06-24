# Generated documentation for module arcpy.ga


class EBKRegressionPrediction(object):
    """
    EBK Regression Prediction is a geostatistical interpolation method that uses Empirical Bayesian Kriging with explanatory variable rasters that are known to affect the value of the data that you are interpolating. This approach combines kriging with regression analysis to make predictions that are more accurate than either regression or kriging can achieve on their own.
    """

    @property
    def description(self) -> str:
        return """

        EBKRegressionPrediction_ga(in_features, dependent_field, in_explanatory_rasters;in_explanatory_rasters..., out_ga_layer, {out_raster}, {out_diagnostic_feature_class}, {measurement_error_field}, {min_cumulative_variance}, {in_subset_features}, {transformation_type}, {semivariogram_model_type}, {max_local_points}, {overlap_factor}, {number_simulations}, {search_neighborhood})

        EBK Regression Prediction is a geostatistical interpolation method
        that uses Empirical Bayesian Kriging with explanatory variable rasters
        that are known to affect the value of the data that you are
        interpolating. This approach combines kriging with regression analysis
        to make predictions that are more accurate than either regression or
        kriging can achieve on their own.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the field that will be
          interpolated.
      dependent_field (Field):
          The field of thecontaining the values of the dependent
          variable. This is the field that will be interpolated. Input
          dependent variable features
      in_explanatory_rasters (Raster Layer / Mosaic Layer):
          Input rasters representing the explanatory variables that will be used
          to build the regression model. These rasters should represent
          variables that are known to influence the values of the dependent
          variable. For example, when interpolating temperature data, an
          elevation raster should be used as an explanatory variable because
          temperature is influenced by elevation. You can use up to 62
          explanatory rasters.
      measurement_error_field {Field}:
          A field that specifies the measurement error for each point in the
          dependent variable features. For each point, the value of this field
          should correspond to one standard deviation of the measured value of
          the point. Use this field if the measurement error values are not the
          same at each point.A common source of nonconstant measurement error is
          when the data is
          measured with different devices. One device might be more precise than
          another, which means that it will have a smaller measurement error.
          For example, one thermometer rounds to the nearest degree and another
          thermometer rounds to the nearest tenth of a degree. The variability
          of measurements is often provided by the manufacturer of the measuring
          device, or it may be known from empirical practice.Leave this
          parameter empty if there are no measurement error values or
          the measurement error values are unknown.
      min_cumulative_variance {Double}:
          Defines the minimum cumulative percent of variance from the principal
          components of the explanatory variable rasters. Before building the
          regression model, the principal components of the explanatory
          variables are calculated, and these principal components are used as
          explanatory variables in the regression. Each principal component
          captures a certain percent of the variance of the explanatory
          variables, and this parameter controls the minimum percent of variance
          that must be captured by the principal components of each local model.
          For example, if a value of 75 is provided, the software will use the
          minimum number of principal components that are necessary to capture
          at least 75 percent of the variance of the explanatory
          variables.Principal components are all mutually uncorrelated with each
          other, so
          using principal components solves the problem of multicollinearity
          (explanatory variables that are correlated with each other). Most of
          the information contained in all explanatory variables can frequently
          be captured in just a few principal components. By discarding the
          least useful principal components, the model calculation becomes more
          stable and efficient without significant loss of accuracy. To
          calculate principal components, there must be variability
          in the explanatory variables, so if any of yourcontain constant values
          within a subset, these constant rasters will not be used to compute
          principal components for that subset. If all explanatory variable
          rasters in a subset contain constant values, thewill report that zero
          principal components were used and that they captured zero percent of
          the variability. Input explanatory variable rastersOutput
          diagnostic feature class
      in_subset_features {Feature Layer}:
          Polygon features defining where the local models will be calculated.
          The points inside each polygon will be used for the local models. This
          parameter is useful when you know that the values of the dependent
          variable changes according to known regions. For example, these
          polygons may represent administrative health districts where health
          policy changes in different districts.You can also use the Generate
          Subset Polygons tool to create subset
          polygons. The polygons created by this tool will be non-overlapping
          and compact.
      transformation_type {String}:
          Type of transformation to be applied to the input data.NONE-Do not
          apply any transformation. This is the
          default.EMPIRICAL-Multiplicative Skewing transformation with Empirical
          base
          function.LOGEMPIRICAL-Multiplicative Skewing transformation with Log
          Empirical
          base function. All data values must be positive. If this option is
          chosen, all predictions will be positive.
      semivariogram_model_type {String}:
          The semivariogram model that will be used for the
          interpolation.EXPONENTIAL-Exponential semivariogramNUGGET-Nugget
          semivariogramWHITTLE-Whittle semivariogramK_BESSEL-K-Bessel
          semivariogram
      max_local_points {Long}:
          The input data will automatically be divided into subsets that
          do not have more than this number of points. Ifare supplied, the value
          of this parameter will be ignored. Subset polygon features
      overlap_factor {Double}:
          A factor representing the degree of overlap between local
          models (also called subsets). Each input point can fall into several
          subsets, and the overlap factor specifies the average number of
          subsets that each point will fall into. A high value of the overlap
          factor makes the output surface smoother, but it also increases
          processing time. Values must be between 1 and 5. Ifare supplied, the
          value of this parameter will be ignored. Subset polygon
          features
      number_simulations {Long}:
          The number of simulated semivariograms of each local model. Using more
          simulations will make the model calculations more stable, but the
          model will take longer to calculate.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output.
          Standard is the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandardCircular and
          SearchNeighborhoodSmoothCircular.Standard Circularradius-The length of
          the radius of the search circle.angle-The angle
          of rotation for the axis (circle) or semimajor axis
          (ellipse) of the moving window.nbrMax-The maximum number of neighbors
          that will be used to estimate
          the value at the unknown location.nbrMin-The minimum number of
          neighbors that will be used to estimate
          the value at the unknown location. sectorType-The geometry of
          the neighborhood.
          ONE_SECTOR-Single ellipse.FOUR_SECTORS-Ellipse divided into four
          sectors.FOUR_SECTORS_SHIFTED-Ellipse divided into four sectors and
          shifted 45
          degrees.EIGHT_SECTORS-Ellipse divided into eight sectors.Smooth
          Circularradius-The length of the radius of the search
          circle.smoothFactor-The
          Smooth Interpolation option creates an outer ellipse
          and an inner ellipse at a distance equal to the Major Semiaxis
          multiplied by the Smoothing factor. The points that fall outside the
          smallest ellipse but inside the largest ellipse are weighted using a
          sigmoidal function with a value between zero and one.

     OUTPUTS:
      out_ga_layer (Geostatistical Layer):
          The output geostatistical layer displaying the result of the
          interpolation.
      out_raster {Raster Dataset}:
          The output raster displaying the result of the interpolation.
          The default cell size will be the maximum of the cell sizes of the. To
          use a different cell size, use the cell size environmental setting.
          Input explanatory variable rasters
      out_diagnostic_feature_class {Feature Class}:
          Output polygon feature class that shows the regions of each local
          model and contains fields with diagnostic information for the local
          models. For each subset, a polygon will be created that surrounds the
          points in the subset so you can easily identify which points were used
          in each subset. For example, if there are 10 local models, there will
          be ten polygons in this output. The feature class will contain the
          following fields:Number of Principal Components (PrincComps)-The
          number of principal
          components that were used as explanatory variables. The value will
          always be less than or equal to the number of explanatory variable
          rasters. Percent of Variance (PercVar)-The percent of variance
          captured by the principal components. This value will be greater than
          or equal to the value specified in theparameter below. Minimum
          cumulative percent of varianceRoot Mean Square Error (RMSE)-The square
          root of the average squared
          cross-validation errors. The smaller this value, the better the model
          fits.Percent 90 Interval (Perc90)-The percent of data points that fall
          within a 90 percent cross-validation confidence interval. Ideally,
          this number should be close to 90. A value significantly smaller than
          90 indicates that standard errors are being underestimated. A value
          significantly larger than 90 indicates that standard errors are being
          overestimated.Percent 95 Interval (Perc95)-The percent of data points
          that fall
          within a 95 percent cross-validation confidence interval. Ideally,
          this number should be close to 95. A value significantly smaller than
          95 indicates that standard errors are being underestimated. A value
          significantly larger than 95 indicates that standard errors are being
          overestimated. Mean Absolute Error (MeanAbsErr)-The average of
          the absolute
          values of the cross-validation errors. This value should be as small
          as possible. It is similar to, but it is less influenced by extreme
          values. Root Mean Square ErrorMean Error (MeanError)-The
          average of the cross-validation errors.
          This value should be close to zero. A value significantly different
          than zero indicates that the predictions are biased.Continuous Ranked
          Probability Score (CRPS)-The continuous ranked
          probability score is a diagnostic that measures the deviation from the
          predictive cumulative distribution function to each observed data
          value. This value should be as small as possible. This diagnostic has
          advantages over cross-validation diagnostics because it compares the
          data to a full distribution rather than to single-point predictions.

        """