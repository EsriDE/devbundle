# Generated documentation for module arcpy.sa.Functions


class TrainIsoClusterClassifier(object):
    """
    Generates an Esri classifier definition file (.ecd) using the Iso Cluster classification definition.
    """

    @property
    def description(self) -> str:
        return """

        TrainIsoClusterClassifier_sa(in_raster, max_classes, out_classifier_definition, {in_additional_raster}, {max_iterations}, {min_samples_per_cluster}, {skip_factor}, {used_attributes;used_attributes...}, {max_merge_per_iter}, {max_merge_distance})

        Generates an Esri classifier definition file (.ecd) using the Iso
        Cluster classification definition.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String):
          The raster dataset to classify.
      max_classes (Long):
          Maximum number of desired classes to group pixels or segments. This
          should be set to be greater than the number of classes in your
          legend.It is possible that you will get fewer classes than what you
          specified
          for this parameter. If you need more, increase this value and
          aggregate classes after the training process is complete.
      in_additional_raster {Mosaic Layer / Raster Layer / Image Service / String}:
          Ancillary raster datasets, such as a multispectral image or a DEM,
          will be incorporated to generate attributes and other required
          information for classification. This parameter is optional.
      max_iterations {Long}:
          The maximum number of iterations the clustering process will run.The
          recommended range is between 10 and 20 iterations. Increasing this
          value will linearly increase the processing time.
      min_samples_per_cluster {Long}:
          The minimum number of pixels or segments in a valid cluster or
          class.The default value of 20 is effective in creating statistically
          significant classes. You can increase this number for more larger
          clusters and less slivers; however, it may limit the overall number of
          classes that are created.
      skip_factor {Long}:
          Number of pixels to skip for a pixel image input. If a segmented image
          is an input, specify the number of segments to skip.
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
          rectangle. This parameter is only enabled if thekey property is
          set to
          true on the input raster. If the only input to the tool is a segmented
          image, the default attributes are COLOR, COUNT, COMPACTNESS, and
          RECTANGULARITY. If an in_additional_raster value is included as an
          input with a segmented image, MEAN and STD are also available
          attributes. Segmented
      max_merge_per_iter {Long}:
          The maximum number of cluster merges per iteration. Increasing the
          number of merges will reduce the number of classes that are created. A
          lower value will result in more classes.
      max_merge_distance {Double}:
          The maximum distance between cluster centers in feature space.
          Increasing the distance will allow more clusters to merge, resulting
          in fewer classes. A lower value will result in more classes. Values
          from 0 to 5 typically return the best results.

     OUTPUTS:
      out_classifier_definition (File):
          The output JSON format file that will contain attribute information,
          statistics, hyperplane vectors, and other information for the
          classifier. An .ecd file will be created.

        """