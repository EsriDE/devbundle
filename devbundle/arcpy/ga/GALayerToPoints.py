# Generated documentation for module arcpy.ga


class GALayerToPoints(object):
    """
    Exports a geostatistical layer to points. The tool can also be used to predict values at unmeasured locations or to validate predictions made at measured locations.
    """

    @property
    def description(self) -> str:
        return """

        GALayerToPoints_ga(in_geostat_layer, in_locations, {z_field}, out_feature_class, {append_all_fields}, {elevation_field}, {elevation_units})

        Exports a geostatistical layer to points. The tool can also be used to
        predict values at unmeasured locations or to validate predictions made
        at measured locations.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      in_locations (Feature Layer):
          Point locations where predictions or validations will be performed.
      z_field {Field}:
          If this field is left blank, predictions are made at the
          location points. If a field is selected, predictions are made at the
          location points, compared to theirvalues, and a validation analysis is
          performed. Z_value_field
      append_all_fields {Boolean}:
          Determines whether all fields will be copied from the input features
          to the output feature class.ALL-All fields from the input features
          will be copied to the output
          feature class. This is the default. FID_ONLY-Only the feature
          ID will be copied, and it will be
          namedon the output feature class. Source_ID
      elevation_field {Field}:
          The field containing the elevation of each input point. The parameter
          only applies to 3D geostatistical models. If the elevation values are
          stored as geometry attributes in Shape.Z, it is recommended to use
          that field. If the elevations are stored in an attribute field, the
          elevations must indicate distance from sea level. Positive values
          indicate distance above sea level, and negative values indicate
          distance below sea level.
      elevation_units {String}:
          The units of the elevation field. This parameter only applies to 3D
          geostatistical models. If Shape.Z is provided as the elevation field,
          the units will automatically match the Z-units of the vertical
          coordinate system.INCH-Elevations are in U.S. survey
          inches.FOOT-Elevations are in U.S.
          survey feet.YARD-Elevations are in U.S. survey
          yards.MILE_US-Elevations are in U.S. survey
          miles.NAUTICAL_MILE-Elevations are in U.S. survey nautical
          miles.MILLIMETER-Elevations are in millimeters.CENTIMETER-Elevations
          are in centimeters.DECIMETER-Elevations are in
          decimeters.METER-Elevations are in meters.KILOMETER-Elevations are in
          kilometers.INCH_INT-Elevations are in international
          inches.FOOT_INT-Elevations are in international
          feet.YARD_INT-Elevations are in international
          yards.MILE_INT-Elevations are in statute
          miles.NAUTICAL_MILE_INT-Elevations are in international nautical
          miles.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing either the predictions or the
          predictions and the validation results.The fields in this feature
          class can include the following fields
          (where applicable):         Source_ID (Source ID)-The object ID of the
          source feature in
          the. Input point observation locationsThe feature or object
          identifier of the input dataset that was used. Included
          (Included)-Indicates whether a prediction was
          calculated for this feature. The values in this field can be one of
          the following:         Yes-There are no problems making a prediction
          at this point.Not enough
          neighbors-There are not enough neighbors to make a
          prediction.Weight parameter is too small-The weight parameter is too
          small.Overfilling-Overflow of floating-point calculations.Problem with
          data transformation-The value to be transformed is
          outside of the supported range for the selected transformation (only
          in kriging).No explanatory rasters-The value cannot be calculated
          because one of
          the explanatory variables is not defined. The point could be outside
          the extent of at least one explanatory variable raster, or the point
          could be on top of a NoData cell in at least one of the explanatory
          variable rasters. This only applies to EBK Regression Prediction
          models.Predicted (Predicted)-The prediction value at this
          location.Error (Error)-The predicted value minus the value in the
          validation
          field.StdError (Standard Error)-The kriging standard error.Stdd_Error
          (Standardized Error)-The standardized prediction errors.
          Ideally, the standardized prediction errors are distributed
          normally.NormValue (Normal Value)-The normal distribution value
          (x-axis) that
          corresponds to the standardized prediction errors (y-axis) in the
          normal QQplot.CRPS (Continuous Ranked Probability Score)-The
          continuous ranked
          probability score is a diagnostic that measures the deviation from the
          predictive cumulative distribution function to each observed data
          value. This value should be as small as possible. This diagnostic has
          advantages over cross-validation diagnostics because it compares the
          data to a full distribution rather than to single-point predictions.
          This field is only created for Empirical Bayesian Kriging and EBK
          Regression Prediction models. Interval90 (Inside 90 Percent
          Interval)-Indicates whether or
          not the validation point is inside of a 90 percent confidence
          interval. This field is only created for Empirical Bayesian Kriging
          and EBK Regression Prediction models. If the model fits the data,
          approximately 90 percent of the features should be contained in a 90
          percent confidence interval. This field can contain the following
          values:         Yes-The validation point is inside the 90 percent
          confidence
          interval.No-The validation point is not inside the 90 percent
          confidence
          interval.Excluded-A prediction cannot be made at this location.
          Interval95 (Inside 95 Percent Interval)-Indicates whether or
          not the validation point is inside of a 95 percent confidence
          interval. This field is only created for Empirical Bayesian Kriging
          and EBK Regression Prediction models. If the model fits the data,
          approximately 95 percent of the features should be contained in a 95
          percent confidence interval. This field can contain the following
          values:         Yes-The validation point is inside the 95 percent
          confidence
          interval.No-The validation point is not inside the 95 percent
          confidence
          interval.Excluded-A prediction cannot be made at this location.QuanVal
          (Validation Quantile)-The quantile of the measured value at
          the feature with respect to the prediction distribution. This value
          can range from 0 to 1, and values close to 0 indicate that the
          measured value is on the far left tail of the distribution, and values
          close to 1 indicate that the measured value is on the right tail of
          the distribution. If many values are close to either extreme, this
          could indicate that the prediction distributions do not model the data
          well, and some of the interpolation parameters need to be altered.
          This field is only created for Empirical Bayesian Kriging and EBK
          Regression Prediction models.

        """