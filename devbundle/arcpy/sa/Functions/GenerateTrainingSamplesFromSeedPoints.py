# Generated documentation for module arcpy.sa.Functions


class GenerateTrainingSamplesFromSeedPoints(object):
    """
    Generates training samples from seed points, such as accuracy assessment points or training sample points. A typical use case is generating training samples from an existing source, such as a thematic raster or a feature class.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTrainingSamplesFromSeedPoints_sa(in_class_data, in_seed_points, out_training_feature_class, {min_sample_area}, {max_sample_radius})

        Generates training samples from seed points, such as accuracy
        assessment points or training sample points. A typical use case is
        generating training samples from an existing source, such as a
        thematic raster or a feature class.

     INPUTS:
      in_class_data (Mosaic Layer / Raster Layer / Feature Layer / Image Service / String):
          The data source that labels the training samples.
      in_seed_points (Feature Layer / Raster Catalog Layer):
          A point shapefile or feature class to provide the centers of training
          sample polygons.
      min_sample_area {Double}:
          The minimum area needed for each training sample, in square meters.
          The minimum value must be greater than or equal to 0.
      max_sample_radius {Double}:
          The longest distance (in meters) from any point within the training
          sample to its center seed point. If set to 0, the output training
          sample will be points instead of polygons. The minimum value must be
          greater than or equal to 0.

     OUTPUTS:
      out_training_feature_class (Feature Class):
          The output training sample feature class in the format that can be
          used in training tools, including shapefiles. The output feature class
          can be either a polygon feature class or a point feature class.

        """