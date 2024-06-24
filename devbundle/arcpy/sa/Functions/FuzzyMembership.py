# Generated documentation for module arcpy.sa.Functions


class FuzzyMembership(object):
    """
    Transforms the input raster into a 0 to 1 scale, indicating the strength of a membership in a set, based on a specified fuzzification algorithm.
    """

    @property
    def description(self) -> str:
        return """

        FuzzyMembership_sa(in_raster, {fuzzy_function}, {hedge})

        Transforms the input raster  into a 0 to 1 scale, indicating the
        strength of a membership in a set, based on a specified fuzzification
        algorithm.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster whose values will be scaled from 0 to 1.It can be an
          integer or a floating-point raster.
      fuzzy_function {Fuzzy function}:
          Specifies the algorithm used in fuzzification of the input raster.The
          fuzzy classes are used to specify the type of membership. The
          types of membership classes are:        FuzzyGaussian,
          FuzzyLarge, FuzzyLinear, FuzzyMSLarge, FuzzyMSSmall,
          FuzzyNear, and FuzzySmall. The following are the forms of the
          membership classes:
          FuzzyGaussian({midpoint},{spread})FuzzyLarge({midpoint},{spread})Fuzzy
          Linear({minimum},{maximum})FuzzyMSLarge({meanMultiplier},{STDMultiplie
          r})FuzzyMSSmall({meanMultiplier},{STDMultiplier})FuzzyNear({midpoint},
          {spread})FuzzySmall({midpoint},{spread})
      hedge {String}:
          Defining a hedge increases or decreases the fuzzy membership values
          which modify the meaning of a fuzzy set. Hedges are useful to help in
          controlling the criteria or important attributes.NONE-No hedge is
          applied. This is the default.SOMEWHAT-Known as
          dilation, defined as the square root of the fuzzy
          membership function. This hedge increases the fuzzy membership
          functions.VERY-Also known as concentration, defined as the fuzzy
          membership
          function squared. This hedge decreases the fuzzy membership functions.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output will be a floating-point raster with values ranging from 0
          to 1.

        """