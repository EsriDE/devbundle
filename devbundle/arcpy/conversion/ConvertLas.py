# Generated documentation for module arcpy.conversion


class ConvertLas(object):
    """
    Converts .las, .zlas, and .laz files between different LAS compression methods, file versions, and point record formats.
    """

    @property
    def description(self) -> str:
        return """

        ConvertLas_conversion(in_las, target_folder, {file_version}, {point_format}, {compression}, {las_options;las_options...}, {out_las_dataset}, {define_coordinate_system}, {in_coordinate_system})

        Converts .las, .zlas, and .laz files between different LAS compression
        methods, file versions, and point record formats.

     INPUTS:
      in_las (Layer File / LAS Dataset Layer / Folder / File):
          The .las, .zlas, or .laz files that will be converted. Multiple files
          can be processed by specifying the folder containing the files or a
          LAS dataset.
      target_folder (Folder):
          The existing folder where the output files will be written.
      file_version {String}:
          Specifies the file version that will be used for the output
          files.SAME_AS_INPUT-The output file version will be the same as the
          input.
          This is the default.1.0-The base version for the LAS format that
          supported 256 class codes
          will be used.1.1-The output file version will be 1.1. Class codes were
          reduced to
          32, but support for classification flags was added.1.2-The output file
          version will be 1.2. Support for red-green-blue
          (RGB) color channels and GPS time was added.1.3-The output file
          version will be 1.3. Storage of lidar waveform
          data for point record formats that are not supported in the ArcGIS
          platform was added.1.4-The output file version will be 1.4. Support
          for coordinate
          system definition using Well Known Text (WKT) convention, 256 class
          codes, up to 15 discrete returns per pulse, higher precision scan
          angle, and overlap classification flag was added.
      point_format {String}:
          Specifies the point record format that will be used for the output
          files. The available options will vary based on the output LAS format
          file version.0-The base type for storing discrete LAS points that
          supports
          attributes such as lidar intensity, return values, scan angle, scan
          direction, and edge of flight line will be used.1-GPS time is added to
          the attributes supported in point format 0,
          which will be used.2-RGB values are added to the attributes supported
          in point format 0,
          which will be used.3-RGB values and GPS time are added to the
          attributes supported in
          point format 0, which will be used.6-The preferred base type for
          storing discrete LAS points in LAS file
          version 1.4 will be used.7-RGB values are added to the attributes
          supported in point format 6,
          which will be used.8-RGB and near-infrared values are added to the
          attributes supported
          in point format 6, which will be used.
      compression {String}:
          Specifies whether the output files will be stored in a compressed or
          uncompressed format.NO_COMPRESSION-Output files will be in the
          uncompressed LAS format
          (*.las). This format supports edits to classification codes and flags.
          This is the default.ZLAS-Output files will be compressed in the zLAS
          format (*.zlas). This
          format supports edits to classification codes and flags.LAZ-Output
          files will be compressed in the LAZ format
          (*.laz).EDITED_ZLAS_TO_NON_EDITED-Edited .zlas files will be converted
          to
          unedited .zlas files. Creating unedited *.zlas files preserves the
          classification edits while allowing the files to be usable in ArcGIS
          Pro 3.1 and earlier. When this option is used on a LAS dataset
          referencing any combination of .las files, edited .zlas files, and
          unedited .zlas files, only the edited .zlas files will be processed.
      las_options {String}:
          Specifies the modifications that will be made to the output files that
          will reduce their size and improve their performance in display and
          analysis.REARRANGE_POINTS-Points will be rearranged to improve display
          and
          analysis performance. Statistics will be automatically computed during
          this process. This is the default.REMOVE_VLR-Variable-length records
          that are added after the header as
          well as the points records of each file will be
          removed.REMOVE_EXTRA_BYTES-Extra bytes that may be present with each
          point
          from the input file will be removed.
      define_coordinate_system {String}:
          Specifies how the coordinate system of each input file will be
          defined.NO_FILES-The coordinate system of each input file will be
          defined by
          the information in its header. Any file that lacks spatial reference
          information will be treated as having an unknown coordinate system.
          This is the default.ALL_FILES-The coordinate system of each input file
          will be defined by
          the in_coordinate_system parameter.FILES_MISSING_PROJECTION-The
          coordinate system of any input file that
          does not have spatial reference information in its header will be
          defined by the in_coordinate_system parameter.
      in_coordinate_system {Coordinate System}:
          The coordinate system that will be used to define the spatial
          reference of some or all input files based on the
          define_coordinate_system parameter value.

     OUTPUTS:
      out_las_dataset {LAS Dataset}:
          The output LAS dataset referencing the newly created .las files.

        """