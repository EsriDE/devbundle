# Generated documentation for module arcpy.management


class UpdateInteriorOrientation(object):
    """
    Refines the interior orientation for each image in the mosaic dataset by constructing an affine transformation from a fiducial table.
    """

    @property
    def description(self) -> str:
        return """

        UpdateInteriorOrientation_management(in_mosaic_dataset, {where_clause}, {fiducial_table}, {film_coordinate_system}, {update_footprints})

        Refines the interior orientation for each image in the mosaic dataset
        by constructing an affine transformation from a fiducial table.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that is created from scanned aerial photos using
          the scanned raster type or frame camera raster type.
      where_clause {SQL Expression}:
          A query definition string that defines a subset of rasters for
          computing fiducials.
      fiducial_table {Table View}:
          The fiducial table created using the Compute Fiducials tool.
      film_coordinate_system {String}:
          Defines the film coordinate system of the scanned aerial photograph.
          It is used in computing fiducial information and affine transformation
          construction.NO_CHANGE-Maintain the coordinate system of the mosaic
          dataset. Do not
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
      update_footprints {Boolean}:
          Generates or updates the footprints of the digital photos in the
          mosaic dataset.UPDATE-The footprints will be generated or
          updated.NO_UPDATE-The
          footprints will not be generated or updated. This is the
          default

        """