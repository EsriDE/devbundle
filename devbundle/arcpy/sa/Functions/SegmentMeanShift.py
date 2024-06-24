# Generated documentation for module arcpy.sa.Functions


class SegmentMeanShift(object):
    """
    Groups adjacent pixels that have similar spectral characteristics into segments.
    """

    @property
    def description(self) -> str:
        return """

        SegmentMeanShift_sa(in_raster, {spectral_detail}, {spatial_detail}, {min_segment_size}, {band_indexes}, {max_segment_size})

        Groups adjacent pixels that have similar spectral characteristics into
        segments.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer):
          The raster dataset to segment. This can be a multispectral or
          grayscale image.
      spectral_detail {Double}:
          The level of importance given to the spectral differences of features
          in the imagery.Valid values range from 1.0 to 20.0. A higher value is
          appropriate
          when there are features to classify separately that have similar
          spectral characteristics. Smaller values create spectrally smoother
          outputs. For example, with higher spectral detail in a forested scene,
          there will be greater discrimination between the tree species.
      spatial_detail {Long}:
          The level of importance given to the proximity between features in the
          imagery.Valid values range from 1.0 to 20. A higher value is
          appropriate for a
          scene in which the features of interest are small and clustered
          together. Smaller values create spatially smoother outputs. For
          example, in an urban scene, impervious surfaces can be classified
          using a smaller spatial detail, or buildings and roads can be
          classified as separate classes using a higher spatial detail.
      min_segment_size {Long}:
          The minimum size of a segment. Merge segments smaller than this size
          with their best fitting neighbor segment. This is related to the
          minimum mapping unit for your project.Units are in pixels.
      band_indexes {String}:
          The bands that will be used to segment the imagery, separated
          by a space. If no band indexes are specified, they are determined by
          the following criteria:        If the raster has only 3 bands, those 3
          bands are usedIf the raster
          has more than 3 bands, the tool assigns the red, green,
          and blue bands according to the raster's properties.If the red, green,
          and blue bands are not identified in the raster
          dataset's properties, bands 1, 2, and 3 are used.The band order will
          not change the result.Select bands that offer the most differentiation
          between the features
          of interest.
      max_segment_size {Long}:
          The maximum size of a segment. Segments that are larger than the
          specified size will be divided. Use this parameter to prevent
          artifacts in the output raster resulting from large segments.Units are
          in pixels.The default value is -1, meaning there is no limit on the
          segment
          size.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          Specify a name and extension for the output dataset.If the input was a
          multispectral image, the output will be an 8-bit
          RGB image. If the input was a grayscale image, the output will be an
          8-bit grayscale image.

        """