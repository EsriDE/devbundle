# Generated documentation for module arcpy.management


class ComputeFiducials(object):
    """
    Computes the fiducial coordinates in image and film space for each image in a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        ComputeFiducials_management(in_mosaic_dataset, out_fiducial_table, {where_clause}, {fiducial_templates}, {film_coordinate_system})

        Computes the fiducial coordinates in image and film space for each
        image in a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset created from scanned aerial photos using scanned
          raster type or frame camera raster type.
      where_clause {SQL Expression}:
          A query definition string that defines a subset of rasters for
          computing fiducials.
      fiducial_templates {Table View / File / String}:
          The fiducial template table that contains required fields for storing
          fiducial pictures and other properties.
      film_coordinate_system {String}:
          A keyword that defines the film coordinate system of the scanned
          aerial photograph. It is used in computing fiducial information and
          affine transformation construction.NO_CHANGE-Maintain the coordinate
          system of the mosaic dataset. Do not
          change the film coordinate system of the scanned aerial photograph.
          Maintain the coordinate system of the mosaic dataset.X_RIGHT_Y_UP-The
          origin of the scanned photo's coordinate system is
          the center, and positive X points right and positive Y points
          up.X_UP_Y_LEFT-The origin of the scanned photo's coordinate system is
          the
          center, and positive X points up and positive Y points
          left.X_LEFT_Y_DOWN-The origin of the scanned photo's coordinate system
          is
          the center, and positive X points left and positive Y points
          down.X_DOWN_Y_RIGHT-The origin of the scanned photo's coordinate
          system is
          the center, and positive X points down and positive Y points right.

     OUTPUTS:
      out_fiducial_table (Table):
          The output table that stores all the fiducial coordinate information
          in image and film space.

        """