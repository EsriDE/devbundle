# Generated documentation for module arcpy.indoors


class ImportIndoorImages(object):
    """
    Imports 360-degree and panoramic images from an .e57 file to an Indoors workspace. The output of this tool can be added to floor-aware maps and scenes in ArcGIS Pro.
    """

    @property
    def description(self) -> str:
        return """

        ImportIndoorImages_indoors(in_data, in_level_features, target_image_folder, target_oriented_imagery, {in_coordinate_system}, {elevation_adjustment}, {horizontal_field_of_view}, {vertical_field_of_view})

        Imports 360-degree and panoramic images from an .e57 file to an
        Indoors workspace. The output of this tool can be added to floor-aware
        maps and scenes in ArcGIS Pro.

     INPUTS:
      in_data (File):
          The .e57 file containing the target oriented imagery file that will be
          imported.
      in_level_features (Feature Layer):
          The associated Levels layer from the ArcGIS Indoors Information Model
          that resides in the same workspace as the target images layer.
      target_image_folder (Folder):
          The existing folder where the imagery files will be written.
      target_oriented_imagery (Oriented Imagery Layer):
          The target oriented imagery dataset in the Indoors workspace that will
          be updated by the imported images.
      in_coordinate_system {Spatial Reference}:
          The spatial reference of the input image file. A coordinate system can
          be selected if none are specified in the input data file.
      elevation_adjustment {Linear Unit}:
          The value by which the z-values of imported images will be adjusted.
          If the imported images are reprojected, the adjustment will be applied
          after projection. The default value is 0 meters.A value of -300 feet
          reduces the z-value of imported images by 300
          feet.A value of 250 meters increases the z-value of imported images by
          250
          meters.
      horizontal_field_of_view {Double}:
          The effective width of the field of view of imported images, in
          degrees. Valid values range from 0 to 360. The default value is 360.
      vertical_field_of_view {Double}:
          The effective height of the field of view of imported images, in
          degrees. Valid values range from 0 to 180. The default value is 180.

        """