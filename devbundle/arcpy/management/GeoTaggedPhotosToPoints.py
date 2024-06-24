# Generated documentation for module arcpy.management


class GeoTaggedPhotosToPoints(object):
    """
    Creates points from the x-, y-, and z-coordinates stored in the metadata of geotagged photo files (.jpg or .tif). You can add the photo files to the output features as geodatabase attachments.
    """

    @property
    def description(self) -> str:
        return """

        GeoTaggedPhotosToPoints_management(Input_Folder, Output_Feature_Class, {Invalid_Photos_Table}, {Include_Non_GeoTagged_Photos}, {Add_Photos_As_Attachments})

        Creates points from the x-, y-, and z-coordinates stored in the
        metadata of geotagged photo files (.jpg or .tif). You can add the
        photo files to the output features as geodatabase attachments.

     INPUTS:
      Input_Folder (Folder):
          The folder where photo files (.jpg or .tif) are located. This folder
          is scanned recursively for photo files; any photos in the base level
          of the folder, as well as in any subfolders, will be added to the
          output.
      Include_Non-GeoTagged_Photos {Boolean}:
          Specifies whether all photo files will be included in the output
          feature class or only those with valid coordinates.ALL_PHOTOS-All
          photos will be included as records in the output
          feature class. If a photo file does not have coordinate information,
          it will be included as a feature with null geometry. This is the
          default.ONLY_GEOTAGGED-Only photos with valid coordinate information
          will be
          included in the output feature class.
      Add_Photos_As_Attachments {Boolean}:
          Specifies whether the input photos will be added to the output
          features as geodatabase attachments.Adding attachments requires that
          the output feature class be in a
          version 10 or later geodatabase.ADD_ATTACHMENTS-Photos will be added
          to the output features as
          geodatabase attachments copied internally to the geodatabase. This is
          the default.NO_ATTACHMENTS-Photos will not be added to the output
          features as
          geodatabase attachments.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output point feature class.
      Invalid_Photos_Table {Table}:
          An output table that will list any photo files in the input folder
          with invalid Exif metadata or empty or invalid coordinates.If no value
          is specified, the table will not be created.

        """