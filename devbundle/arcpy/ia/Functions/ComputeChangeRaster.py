# Generated documentation for module arcpy.ia.Functions


class ComputeChangeRaster(object):
    """
    Calculates the absolute, relative, categorical, or spectral difference between two raster datasets.
    """

    @property
    def description(self) -> str:
        return """

        ComputeChangeRaster_ia(from_raster, to_raster, {compute_change_method}, {from_classes;from_classes...}, {to_classes;to_classes...}, {filter_method}, {define_transition_colors}, {from_classname_field}, {to_classname_field})

        Calculates the absolute, relative, categorical, or spectral difference
        between two raster datasets.

     INPUTS:
      from_raster (Raster Layer / Mosaic Layer / Raster Dataset / Mosaic Dataset / Image Service / String):
          The initial or earlier raster to be analyzed.
      to_raster (Raster Layer / Mosaic Layer / Raster Dataset / Mosaic Dataset / Image Service / String):
          The final or later raster to be analyzed. This is the raster that will
          be compared to the initial raster.
      compute_change_method {String}:
          Specifies the type of calculation that will be performed between the
          two rasters.DIFFERENCE-The mathematical difference, or subtraction,
          between the
          pixel values in the rasters will be calculated. This is the
          default.RELATIVE_DIFFERENCE-The difference in pixel values, accounting
          for the
          quantities of the values being compared, will be
          calculated.CATEGORICAL_DIFFERENCE-The difference between two
          categorical or
          thematic rasters will be calculated. The output will contain class
          transitions that occurred between the two
          rasters.SPECTRAL_EUCLIDEAN_DISTANCE-The Euclidean distance between the
          pixel
          values of two multiband rasters will be
          calculated.SPECTRAL_ANGLE_DIFFERENCE-The spectral angle between the
          pixel values
          of two multiband rasters will be calculated. The output is in
          radians.BAND_WITH_MOST_CHANGE-The band that accounts for the most
          change in
          each pixel between two multiband rasters will be calculated.
      from_classes {String}:
          The list of class names from the from_raster parameter that will be
          included in the computation. If no classes are provided, all classes
          will be included.This parameter is enabled when the
          compute_change_method parameter is
          set to CATEGORICAL_DIFFERENCE.
      to_classes {String}:
          The list of class names from the to_raster parameter that will be
          included in the computation. If no classes are provided, all classes
          will be included.This parameter is enabled when the
          compute_change_method parameter is
          set to CATEGORICAL_DIFFERENCE.
      filter_method {String}:
          Specifies the pixels that will be categorized in the output raster.
          This parameter is enabled when the compute_change_method parameter is
          set to CATEGORICAL_DIFFERENCE.CHANGED_PIXELS_ONLY-Only the pixels that
          changed categories will be
          categorized in the output. Pixels that did not change categories will
          be grouped in a class called Other.UNCHANGED_PIXELS_ONLY-Only the
          pixels that did not change categories
          will be categorized in the output. Pixels that changed categories will
          be grouped in a class called Other.ALL-All pixels will be categorized
          in the output. This is the default.
      define_transition_colors {String}:
          Specifies the color that will be used to symbolize the output classes.
          When a pixel changes from one class type to another, the output pixel
          color represents the initial class type, the final class type, or a
          blend of the two.This parameter is enabled when the
          compute_change_method parameter is
          set to CATEGORICAL_DIFFERENCE.AVERAGE-The color of the output class
          will be the average of the from
          (initial) and to (final) class colors. This is the
          default.FROM_COLOR-The color of the output class will match the color
          of the
          from (initial) class.TO_COLOR-The color of the output class will match
          the color of the to
          (final) class.
      from_classname_field {Field}:
          The field that will store class names in the from_raster
          parameter value. The tool automatically searches for thefield orfield
          to use. ClassNameClass_NameUse this parameter if the input does
          not contain these standard field
          names.
      to_classname_field {Field}:
          The field that will store class names in the to_raster
          parameter value. The tool will automatically search for thefield
          orfield to use. ClassNameClass_NameUse this parameter if the
          input does not contain these standard field
          names.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The output change raster dataset.

        """