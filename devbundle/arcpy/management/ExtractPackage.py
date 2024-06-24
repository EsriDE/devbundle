# Generated documentation for module arcpy.management


class ExtractPackage(object):
    """
    Extracts the contents of a package to a specified folder. The output folder will be updated with the extracted contents of the input package.
    """

    @property
    def description(self) -> str:
        return """

        ExtractPackage_management(in_package, {output_folder}, {cache_package}, {storage_format_type}, {create_ready_to_serve_format}, {target_cloud_connection})

        Extracts the contents of a package to a specified folder. The output
        folder will be updated with the extracted contents of the input
        package.

     INPUTS:
      in_package (File):
          The input package that will be extracted.
      cache_package {Boolean}:
          Specifies whether a copy of the package will be cached to your
          profile.When extracting a package, the output is first extracted to
          your user
          profile and appended with a unique ID before a copy is made to the
          directory specified in the output_folder parameter. Downloading and
          extracting subsequent versions of the same package will only update
          this location. You do not need to manually create a cached version of
          the package in your user profile when using this parameter. This
          parameter is not enabled if the input package is a vector tile package
          (.vtpk) or a tile package (.tpk and .tpkx).CACHE-A copy of the
          package will be extracted and cached to your
          profile. This is the default.NO_CACHE-A copy of the package will only
          be extracted to the output
          parameter specified; it will not be cached.
      storage_format_type {String}:
          Specifies the storage format that will be used for the extracted
          cache. This parameter is applicable only when the input package is a
          vector tile package (.vtpk).COMPACT-The tiles will be grouped in
          bundle files using the Compact
          V2 storage format. This format provides better performance on network
          shares and cloud store directories. This is the default.EXPLODED-Each
          tile will be stored as an individual file.
      create_ready_to_serve_format {Boolean}:
          Specifies whether a ready-to-serve format for ArcGIS Enterprise will
          be created. This parameter is enabled only when the input package is a
          vector tile package (.vtpk) or a tile package
          (.tpkx).READY_TO_SERVE_CACHE_DATASET-A folder structure with an
          extracted
          cache that can be used to create a tile layer in ArcGIS Enterprise
          will be created. The file extension of the folder signifies the
          content it stores: .tiles (cache dataset) for tile layer packages or
          .vtiles (vector cache dataset) for vector tile
          packages.EXTRACTED_PACKAGE-A folder structure with extracted contents
          of the
          package will be created. This is the default.
      target_cloud_connection {Folder}:
          The target .acs file to which the package contents will be extracted.
          This parameter is enabled only when the input package is a scene layer
          package (.slpk), a vector tile package (.vtpk), or a tile package
          (.tpkx).

     OUTPUTS:
      output_folder {Folder}:
          The output folder that will contain the contents of the package.If the
          specified folder does not exist, a folder will be created.

        """