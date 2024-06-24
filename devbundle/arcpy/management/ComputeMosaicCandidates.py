# Generated documentation for module arcpy.management


class ComputeMosaicCandidates(object):
    """
    Finds the image candidates in a mosaic dataset that best represent the mosaic area.
    """

    @property
    def description(self) -> str:
        return """

        ComputeMosaicCandidates_management(in_mosaic_dataset, {maximum_overlap}, {maximum_area_loss}, {maximum_obliqueness_angle})

        Finds the image candidates in a mosaic dataset that best represent the
        mosaic area.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset with densely overlapped images.
      maximum_overlap {Double}:
          The maximum amount of overlap between the mosaic dataset and the
          footprint of each image in the mosaic dataset. If the percentage of
          overlap is greater than this threshold, the image is excluded since it
          will have too much redundant information.The percentage is expressed
          as a decimal. For example, a maximum
          overlap of 60 percent is expressed as 0.6.
      maximum_area_loss {Double}:
          The maximum percentage of area that can be excluded by the candidate
          images. After the tool finds the best candidate images based on the
          maximum_overlap parameter value, it checks whether the maximum
          excluded area is below the threshold specified. If the excluded area
          is greater than the specified threshold, the tool will add candidate
          images to fill in some of the voids that were missing. These excluded
          areas will typically be along the border of the mosaic dataset.The
          percentage is expressed as a double. For example, a maximum
          excluded area of 5 percent is expressed as 0.05.
      maximum_obliqueness_angle {Double}:
          The maximum image obliqueness angle that will be used to filter
          images. Any image with an obliqueness angle larger than this value
          will not be used as a candidate. This parameter is measured in
          degrees. The default value is 15.

        """