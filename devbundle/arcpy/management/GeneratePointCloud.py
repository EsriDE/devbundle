# Generated documentation for module arcpy.management


class GeneratePointCloud(object):
    """
    Generates 3D points from stereo pairs and outputs a point cloud as a set of LAS files.
    """

    @property
    def description(self) -> str:
        return """

        GeneratePointCloud_management(in_mosaic_dataset, matching_method, out_folder, out_base_name, {object_size}, {ground_spacing}, {minimum_pairs}, {minimum_area}, {minimum_adjustment_quality}, {maximum_diff_gsd}, {maximum_diff_OP})

        Generates 3D points from stereo pairs and outputs a point cloud as a
        set of LAS files.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset, which must have completed the block
          adjustment process and have a stereo model.To block adjust the mosaic
          dataset, use the Apply Block Adjustment
          tool. To build a stereo model on the mosaic dataset, use the Build
          Stereo Model tool.
      matching_method (String):
          Specifies the method that will be used to generate 3D
          points.ETM-Extended terrain matching, a feature-based stereo matching
          in
          which the Harris operator is used in detecting feature points, will be
          used as the matching method. Since fewer feature points are extracted,
          this method is fast and can be used for data with fewer terrain
          variations and less detail.SGM-Semi-Global Matching, which produces
          points that are denser and
          have more detailed terrain information, will be used as the matching
          method. It can be used for images of urban areas. This method is more
          computational intensive than ETM.MVM-Multi-view image matching, which
          is based on the SGM matching
          method followed by a fusion step in which the redundant depth
          estimations across a single stereo model are merged, will be used as
          the matching method. It produces dense 3D points and is
          computationally efficient. References:        Heiko
          Hirschmuller et al., "Memory
          Efficient Semi-Global Matching,"
          ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial
          Information Sciences, Volume 1-3, (2012): 371-376.Hirschmuller, H.
          "Stereo Processing by Semiglobal Matching and Mutual
          Information." Pattern Analysis and Machine Intelligence, (2008).
      object_size {Double}:
          A search radius within which surface objects, such as buildings or
          trees, will be identified. It is the linear size in map units.
      ground_spacing {Double}:
          The ground spacing, in meters, at which the 3D points will be
          generated.The default is five times the source image pixel size.
      minimum_pairs {Double}:
          The maximum number of image pairs that an image can contribute to
          generate 3D points. The default value is a minimum of 2 image pairs.If
          the image is involved in more image pairs than specified, those
          image pairs will not be considered when constructing the 3D points. In
          this case, the tool will order the pairs based on the various
          threshold parameters specified in the tool. The pairs with the highest
          scores will be used to generate the points.
      minimum_area {Double}:
          The minimum overlap threshold area that is acceptable, which is a
          percentage of overlap between a pair of images. Image pairs with
          overlap areas smaller than this threshold will receive a score of 0
          for this criteria and will descend in the ordered list. The range of
          values for the threshold is 0 to 1. The default threshold value is
          0.6, which is equal to 60 percent.
      minimum_adjustment_quality {Double}:
          The minimum adjustment quality that is acceptable. The threshold value
          will be compared to the adjustment quality value that is stored in the
          stereo model. Image pairs with an adjustment quality less than the
          specified threshold will receive a score of 0 for this criteria and
          will descend in the ordered list. The range of values for the
          threshold is 0 to 1. The default value is 0.2, which is equal to 20
          percent.
      maximum_diff_gsd {Double}:
          The maximum allowable threshold for the ground sample distance (GSD)
          between two images in a pair. The resolution ratio between the two
          images will be compared to the threshold value. Image pairs with a
          ground sample ratio greater than this threshold will receive a score
          of 0 for this criteria and will descend in the ordered list. The
          default threshold ratio is 2.
      maximum_diff_OP {Double}:
          The maximum threshold for the difference between the Omega values and
          Phi values for the two image pairs. The Omega values and Phi values
          for the image pairs are compared. Image pairs with an Omega or a Phi
          difference greater than this threshold will receive a score of 0 for
          this criteria and will descend in the ordered list. The default
          threshold difference for each comparison is 8.

     OUTPUTS:
      out_folder (Folder):
          The folder used to store the output LAS files, including cloud
          storage.If this tool is run multiple times with the same input
          parameters, the
          output may be slightly different due to random sampling.
      out_base_name (String):
          A string used as a prefix to formulate the output LAS file names. For
          example, if name is used as the base, the output files will be named
          name1.las, name2.las, and so on.

        """