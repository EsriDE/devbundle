# Generated documentation for module arcpy.management


class CreateIntegratedMeshSceneLayerPackage(object):
    """
    Creates scene layer content (.slpk or .i3sREST) from OpenSceneGraph binary (OSGB) data.
    """

    @property
    def description(self) -> str:
        return """

        CreateIntegratedMeshSceneLayerPackage_management(in_dataset;in_dataset..., {out_slpk}, {anchor_point}, {file_suffix}, {out_coor_system}, {max_texture_size}, {texture_optimization}, {target_cloud_connection}, {out_name})

        Creates scene layer content (.slpk or .i3sREST) from OpenSceneGraph
        binary (OSGB) data.

     INPUTS:
      in_dataset (Folder / File):
          The OSGB format files, or folders containing OSGB format files, that
          will be imported into the integrated mesh scene layer package. This
          parameter allows a selection of multiple OSGB format files or a
          selection of multiple folders containing OSGB format files.
      anchor_point {File / Feature Layer}:
          The point feature or .3mx, .xml, or .wld3 file that will be used to
          position the center of the OSGB model. If there are multiple points in
          the feature class, only the first point will be used to georeference
          the data.
      file_suffix {String}:
          Specifies the files that will be processed for the input dataset.*-All
          binary files, regardless of their extension, will be processed
          to determine if they are in the OSGB format.osgb-Only files with the
          .osgb extension will be processed.
      out_coor_system {Spatial Reference}:
          The coordinate system of the output scene layer package. It
          can be any projected or custom coordinate system. Supported geographic
          coordinate systems include WGS84 and China Geodetic Coordinate System
          2000. WGS84 and EGM96 Geoid are the default horizontal and vertical
          coordinate systems, respectively. The coordinate system can be
          specified in any of the following ways:        Specify the path to a
          .prj file.Reference a dataset with the correct
          coordinate system.Use an arcpy.SpatialReference object.
      max_texture_size {Long}:
          The maximum texture size in pixels for each scene layer node.
      texture_optimization {String}:
          Specifies the textures that will be optimized according to the
          target platform where the scene layer package is used.
          Optimizations that include KTX2 may take significant time to process.
          For fastest results, use the Desktop or None options.All-All texture
          formats will be optimized including JPEG, DXT, and
          KTX2 for use in desktop, web, and mobile platforms.Desktop-Windows,
          Linux, and Mac supported textures will be optimized
          including JPEG and DXT for use in ArcGIS Pro clients on Windows and
          ArcGIS Maps SDKs desktop clients on Windows, Linux, and Mac. This is
          the default.Mobile-Android and iOS supported textures will be
          optimized including
          JPEG and KTX2 for use in Maps SDKs mobile applications.None-JPEG
          textures will be optimized for use in desktop and web
          platforms.
      target_cloud_connection {Folder}:
          The target cloud connection file (.acs) where the scene layer content
          (.i3sREST) will be output.
      out_name {String}:
          The output name of the scene layer content when output to a cloud
          store. This parameter is only available when the
          target_cloud_connection parameter value is specified.

     OUTPUTS:
      out_slpk {File}:
          The integrated mesh scene layer package that will be created.
          This parameter is required if theparameter value is not specified.
          Target Cloud Connection

        """