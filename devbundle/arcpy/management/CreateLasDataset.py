# Generated documentation for module arcpy.management


class CreateLasDataset(object):
    """
    Creates a LAS dataset referencing one or more .las files and optional surface constraint features.
    """

    @property
    def description(self) -> str:
        return """

        CreateLasDataset_management(input;input..., out_las_dataset, {folder_recursion}, {in_surface_constraints;in_surface_constraints...}, {spatial_reference}, {compute_stats}, {relative_paths}, {create_las_prj}, {extent}, {boundary}, {add_only_contained_files})

        Creates a LAS dataset referencing one or more .las files and optional
        surface constraint features.

     INPUTS:
      input (LAS Dataset Layer / Folder / File):
          The .las files, LAS datasets, and folders containing .las files that
          will be referenced by the LAS dataset. This information can be
          supplied as a string containing all the input data or a list of
          strings containing specific data elements (for example, "lidar1.las;
          lidar2.las; folder1; folder2" or ["lidar1.las", "lidar2.las",
          "folder1", "folder2"]).
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
      spatial_reference {Coordinate System}:
          The spatial reference of the LAS dataset. If no spatial reference is
          explicitly assigned, the LAS dataset will use the coordinate system of
          the first input .las file. If the input files do not contain spatial
          reference information and the coordinate system is not set, the
          coordinate system of the LAS dataset will be listed as unknown.
      compute_stats {Boolean}:
          Specifies whether statistics for the .las files will be computed and a
          spatial index generated for the LAS dataset. The presence of
          statistics allows the LAS dataset layer's filtering and symbology
          options to only show LAS attribute values that exist in the .las
          files. A .lasx auxiliary file is created for each .las
          file.COMPUTE_STATS-Statistics will be
          computed.NO_COMPUTE_STATS-Statistics
          will not be computed. This is the default.
      relative_paths {Boolean}:
          Specifies whether lidar files and surface constraint features will be
          referenced by the LAS dataset through relative or absolute paths.
          Using relative paths may be convenient for cases in which the LAS
          dataset and its associated data will be relocated in the file system
          using the same relative location to one
          another.ABSOLUTE_PATHS-Absolute paths will be used for the data
          referenced by
          the LAS dataset. This is the default.RELATIVE_PATHS-Relative paths
          will be used for the data referenced by
          the LAS dataset.
      create_las_prj {String}:
          Specifies whether .prj files will be created for the .las files
          referenced by the LAS dataset.NO_FILES-No .prj files will be created.
          This is the
          default.FILES_MISSING_PROJECTION-Corresponding .prj files will be
          created for
          .las files with no spatial reference.ALL_FILES-Corresponding .prj
          files will be created for all .las files.
      extent {Extent}:
          The processing extent will be used to select a subset of .las files
          from the list of files and folders in the input parameter value. Any
          .las files that fall entirely outside of this extent will be excluded
          from the resulting LAS dataset. Additionally, .las files that fall
          partially outside the extent will be excluded if the
          add_only_contained_files parameter is set to INTERSECTED_FILES.
      boundary {Feature Layer}:
          The polygon features whose boundary will be used to select a subset of
          .las files from the list of files and folders in the input parameter.
          Any .las files that fall entirely outside of the polygon features will
          be excluded from the resulting LAS dataset. Additionally, .las files
          that fall partially outside the polygons will be excluded if the
          add_only_contained_files parameter is set to INTERSECTED_FILES.
      add_only_contained_files {Boolean}:
          Specifies whether the .las files that will be added to the LAS dataset
          must be fully or partially contained by either the processing extent,
          the processing boundary polygon, or the intersection of
          both.CONTAINED_FILES-All files that intersect the processing extent,
          processing boundary, or the intersection of both will be added to the
          LAS dataset. This is the default.INTERSECTED_FILES-Only files that are
          entirely contained by the
          processing extent, processing boundary, or the intersection of both
          will be added to the LAS dataset.

     OUTPUTS:
      out_las_dataset (LAS Dataset):
          The LAS dataset that will be created.

        """