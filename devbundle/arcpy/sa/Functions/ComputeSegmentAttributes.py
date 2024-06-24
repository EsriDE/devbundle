# Generated documentation for module arcpy.sa.Functions


class ComputeSegmentAttributes(object):
    """
    Computes a set of attributes associated with the segmented image. The input raster can be a single-band or 3-band, 8-bit segmented image.
    """

    @property
    def description(self) -> str:
        return """

        ComputeSegmentAttributes_sa(in_segmented_raster, {in_additional_raster}, {used_attributes;used_attributes...})

        Computes a set of attributes associated with the segmented image. The
        input raster can be a single-band or 3-band, 8-bit segmented image.

     INPUTS:
      in_segmented_raster (Mosaic Layer / Raster Layer):
          The input segmented raster dataset, where all the pixels belonging to
          a segment have the same converged RGB color. Usually, it is an 8-bit,
          3-band RGB raster, but it can also be a 1-band grayscale raster.
      in_additional_raster {Mosaic Layer / Raster Layer}:
          Ancillary raster datasets, such as a multispectral image or a DEM,
          will be incorporated to generate attributes and other required
          information for the classifier. This raster is necessary when
          calculating attributes such as mean or standard deviation. This
          parameter is optional.
      used_attributes {String}:
          Specifies the attributes that will be included in the attribute table
          associated with the output raster.COLOR-The RGB color values will be
          derived from the input raster on a
          per-segment basis. This is also known as average chromaticity
          color.MEAN-The average digital number (DN) will be derived from the
          optional
          pixel image on a per-segment basis.STD-The standard deviation will be
          derived from the optional pixel
          image on a per-segment basis.COUNT-The number of pixels composing the
          segment, on a per-segment
          basis.COMPACTNESS-The degree to which a segment is compact or
          circular, on a
          per-segment basis. The values range from 0 to 1, in which 1 is a
          circle.RECTANGULARITY-The degree to which the segment is rectangular,
          on a
          per-segment basis. The values range from 0 to 1, in which 1 is a
          rectangle.If the only input into the tool is a segmented image, the
          default
          attributes are COLOR, COUNT, COMPACTNESS, and RECTANGULARITY. If an
          in_additional_raster is also included as an input along with a
          segmented image, then MEAN and STD are available as options.

     OUTPUTS:
      out_index_raster_dataset (Raster Dataset):
          The output segment index raster, where the attributes for each segment
          are recorded in the associated attribute table.

        """