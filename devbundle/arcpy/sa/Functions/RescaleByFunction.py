# Generated documentation for module arcpy.sa.Functions


class RescaleByFunction(object):
    """
    Rescales the input raster values by applying a selected transformation function and transforming the resulting values onto a specified continuous evaluation scale.
    """

    @property
    def description(self) -> str:
        return """

        RescaleByFunction_sa(in_raster, {transformation_function}, {from_scale}, {to_scale})

        Rescales the input raster values by applying a selected transformation
        function and transforming the resulting values onto a specified
        continuous evaluation scale.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to rescale.
      transformation_function {Transformation function}:
          Specifies the continuous function to transform the input raster.The
          transformation function classes are used to specify the type of
          transformation function. The types of transformation function
          classes are
          TfExponential, TfGaussian, TfLarge, TfLinear, TfLogarithm,
          TfLogisticDecay, TfLogisticGrowth, TfMSLarge, TfMSSmall, TfNear,
          TfPower, TfSmall, and TfSymmetricLinearWhich transformation function
          to use depends on which function best
          captures the interaction of the phenomenon's preference to the input
          values. To better understand how the lower and upper thresholds affect
          the output values, For more information on the parameters that control
          the thresholds, see The interaction of the lower and upper thresholds
          on the output values. The following are the forms of the
          transformation function
          classes:        TfExponential({shift}, {baseFactor}, {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfGaussian({midpoint}, {spread},
          {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfLarge({midpoint}, {spread}, {lowerThreshold},
          {valueBelowThreshold},
          {upperThreshold}, {valueAboveThreshold})TfLinear({minimum}, {maximum},
          {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfLogarithm({shift}, {factor}, {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfLogisticDecay({minimum}, {maximum},
          {yInterceptPercent},
          {lowerThreshold}, {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfLogisticGrowth({minimum}, {maximum},
          {yInterceptPercent},
          {lowerThreshold}, {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfMSLarge({meanMultiplier}, {STDMultiplier},
          {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfMSSmall({meanMultiplier}, {STDMultiplier},
          {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold},
          {valueAboveThreshold})TfNear({midpoint}, {spread}, {lowerThreshold},
          {valueBelowThreshold},
          {upperThreshold}, {valueAboveThreshold})TfPower({shift}, {exponent},
          {lowerThreshold}, {valueBelowThreshold},
          {upperThreshold}, {valueAboveThreshold})TfSmall({midpoint}, {spread},
          {lowerThreshold}, {valueBelowThreshold},
          {upperThreshold}, {valueAboveThreshold})TfSymmetricLinear({minimum},
          {maximum}, {lowerThreshold},
          {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})The
          default transformation function is TfMSSmall. The parameter
          defaults for the transformation functions
          include the following:        baseFactor (for TfExponential) is
          derived from the input
          raster.exponent (for TfPower) is derived from the input raster.factor
          (for TfLogarithm) is derived from the input raster.lowerThreshold (for
          all functions) is set to the Minimum of the input
          raster.maximum (for TfLinear, TfLogisticDecay, TfLogisticGrowth, and
          TfSymmetricLinear) is set to the Maximum of the input
          raster.meanMultiplier (for TfMSLarge and TfMSSmall) is 1.midpoint (for
          TfGaussian and TfNear) is set to the midpoint of the
          value range of the input raster.midpoint (for TfLarge and TfSmall) is
          set to the mean of the input
          raster.minimum (for TfLinear, TfLogisticDecay, TfLogisticGrowth, and
          TfSymmetricLinear) is set to the Minimum of the input raster.shift
          (for TfExponential, TfLogarithm, and TfPower) is derived from
          the input raster.spread (for TfGaussian and TfNear) is derived from
          the input raster.spread (for TfLarge and TfSmall) is 5.STDMultiplier
          (for TfMSLarge and TFMSSmall) is 1.upperThreshold (for all functions)
          is set to the Maximum of the input
          raster.valueAboveThreshold (for all functions) is set to the to_scale
          value.valueBelowThreshold (for all functions) is set to the
          value.yInterceptPercent (for TfLogisticDecay) is
          99.0000.yInterceptPercent (for TfLogisticGrowth) is 1.0000.
      from_scale {Double}:
          The starting value of the output evaluation scale.The from_scale value
          cannot be equal to the to_scale value. The
          from_scale can be lower or higher than the to_scale (for example, from
          1 to 10, or from 10 to 1).The value must be positive and it can be
          either an integer or double.The default is 1.
      to_scale {Double}:
          The ending value of the output evaluation scale.The to_scale value
          cannot be equal to the from_scale value. The
          to_scale can be lower or higher than the from_scale (for example, from
          1 to 10, or from 10 to 1).The value must be positive and it can be
          either an integer or double.The default is 10.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output rescaled raster.The output will be a floating-point raster
          with values ranging from
          (or within) the from_scale and the to_scale evaluation values.

        """