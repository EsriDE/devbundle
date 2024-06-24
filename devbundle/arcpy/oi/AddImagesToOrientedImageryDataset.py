# Generated documentation for module arcpy.oi


class AddImagesToOrientedImageryDataset(object):
    """
    Adds images to an oriented imagery dataset from multiple input sources, including a file, folder, table, list of image paths, or a point feature layer.
    """

    @property
    def description(self) -> str:
        return """

        AddImagesToOrientedImageryDataset_oi(in_oriented_imagery_dataset, imagery_category, input_data;input_data..., {include_sub_folders}, {folder_filter}, {where_clause}, {include_all_fields})

        Adds images to an oriented imagery dataset from multiple input
        sources, including a file, folder, table, list of image paths, or a
        point feature layer.

     INPUTS:
      in_oriented_imagery_dataset (Oriented Imagery Layer):
          The path and name of the oriented imagery dataset where the images
          will be added.
      imagery_category (String):
          Specifies the type of input images that will be used and sets the
          default properties of the oriented imagery dataset. The default
          property will be used if the equivalent attribute is not found in the
          oriented imagery dataset attribute table.Horizontal-Images in which
          the exposure is parallel to the ground and
          looking to the horizon will be used.Oblique-Images in which the
          exposure is at an angle to the ground,
          typically at about 45 degrees so sides of objects can be seen will be
          used.Nadir-Images in which the exposure is perpendicular to the ground
          and
          looking straight down will be used. Only the top of the objects can be
          seen.360-Images taken using specialized cameras that provide
          360-degree
          spherical surround views or have been stitched together as 360-degree
          views from multiple cameras will be used.Inspection-Close-up imagery
          of assets (less than 5 meters from the
          camera) will be used.
      input_data (Folder / Oriented Imagery Layer / Table / Raster Layer / File):
          The path and name of the input data. The following are
          supported:        One or more images in JPEG format.A folder
          containing images. Only
          JPEG images will be added to the
          dataset from the folder.A .txt file containing JPEG image paths. Each
          image path must be on a
          separate line.A .csv file using the oriented imagery table schema.A
          feature layer using the oriented imagery attribute table schema.An
          oriented imagery layer.
      include_sub_folders {Boolean}:
          Specifies whether subfolders will be recursively
          explored.SUBFOLDERS-All subfolders will be recursively explored for
          data. This
          is the default.NOSUBFOLDERS-Only the top-level folder will be explored
          for data.
      folder_filter {String}:
          An expression that will be used to filter and add images in the input
          folder.For example, to add only images that contain a particular
          string, add
          percentage signs before and after the string value (%value%).
      where_clause {SQL Expression}:
          An SQL expression that will be used to select a subset of records. For
          more information about SQL syntax, see SQL reference for query
          expressions used in ArcGIS.
      include_all_fields {Boolean}:
          Specifies whether all fields from input table, apart from the required
          schema, will be added to the dataset's attribute
          table.NO_INCLUDE_ALL_FIELDS-Only oriented imagery schema-specific
          fields
          will be added to the dataset's attribute table. This is the
          default.INCLUDE_ALL_FIELDS-All fields in the input table will be added
          to the
          dataset's attribute table.

        """