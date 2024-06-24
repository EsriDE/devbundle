# Generated documentation for module arcpy.management


class AddFilesToLasDataset(object):
    """
    Adds references for one or more LAS files and surface constraint features to a LAS dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddFilesToLasDataset_management(in_las_dataset, {in_files;in_files...}, {folder_recursion}, {in_surface_constraints;in_surface_constraints...})

        Adds references for one or more LAS files and surface constraint
        features to a LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed.
      in_files {LAS Dataset Layer / Folder / File}:
          Inputs that can include any combination of .las files, .zlas files,
          LAS datasets, and folders containing .las or .zlas data. When a LAS
          dataset is specified as input, all .las and .zlas files that have a
          valid path reference will be added to the input LAS dataset. In
          thepane, a folder can also be specified as an input by
          selecting the folder in File Explorer and dragging it onto the
          parameter's input box. Geoprocessing
      folder_recursion {Boolean}:
          Specifies whether lidar files residing in the subdirectories of an
          input folder will be added to the LAS dataset.NO_RECURSION-Only lidar
          files residing in an input folder will be
          added to the LAS dataset. This is the default.RECURSION-All lidar
          files residing in the subdirectories of an input
          folder will be added to the LAS dataset.
      in_surface_constraints {Value Table}:
          The features that will be referenced by the LAS dataset when
          generating a triangulated surface. Each feature must have the
          following properties defined:        in_feature_class-The feature to
          be referenced by the LAS
          dataset.height_field-Any numeric field in the feature's attribute
          table can be
          used to define the height source. If the feature's geometry contains
          z-values, it can be selected by specifying Shape.Z. If no height is
          necessary, specify the keyword <None> to create z-less features with
          elevation that will be interpolated from the surface.
          SF_type-The surface feature type that defines how the
          feature geometry will be incorporated into the triangulation for the
          surface. Options with hard or soft designation refer to whether the
          feature edges represent distinct breaks in slope or a gradual change.
          anchorpoints-Elevation points that will not be thinned away. This
          option is only available for single-point feature geometry.
          hardline or-Breaklines that enforce a height value.
          softline            hardclip or-Polygon dataset that defines the
          boundary of
          the LAS dataset. softclip            harderase or-Polygon
          dataset that defines holes in the LAS
          dataset. softerase            hardreplace or-Polygon
          dataset that defines areas of
          constant height. softreplace

        """