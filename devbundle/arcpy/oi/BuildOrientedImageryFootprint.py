# Generated documentation for module arcpy.oi


class BuildOrientedImageryFootprint(object):
    """
    Builds a footprint feature class for an oriented imagery dataset.
    """

    @property
    def description(self) -> str:
        return """

        BuildOrientedImageryFootprint_oi(in_oriented_imagery_dataset, out_dataset_path, out_dataset_name, footprint_option)

        Builds a footprint feature class for an oriented imagery dataset.

     INPUTS:
      in_oriented_imagery_dataset (Oriented Imagery Layer):
          The oriented imagery dataset for which the footprint will be computed.
      out_dataset_path (Workspace / Feature Dataset):
          The enterprise or file geodatabase where the output footprint feature
          class will be created.
      out_dataset_name (String):
          The name of the output footprint feature class.
      footprint_option (String):
          Specifies the method that will be used to create the
          footprint.PER_IMAGE-Polygon features will be created from each feature
          based on
          camera parameters. Use this option when there are only a few feature
          points and they are scattered over a large projected
          area.MERGE-Individual polygons will be computed and merged into a
          single
          polygon feature that is a more optimized footprint for the
          dataset.BUFFER-Each feature point will be buffered using the average
          far
          distance value of the oriented imagery dataset and merged to a single
          polygon feature. Use this option for street view imagery.EXTENT-A
          footprint will be created based on the extent of the oriented
          imagery dataset. Use this option when there are many camera points
          within a small area.

        """