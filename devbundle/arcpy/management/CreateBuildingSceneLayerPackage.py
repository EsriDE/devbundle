# Generated documentation for module arcpy.management


class CreateBuildingSceneLayerPackage(object):
    """
    Creates a scene layer package (.slpk) or scene layer content (.i3sREST) from a building layer input.
    """

    @property
    def description(self) -> str:
        return """

        CreateBuildingSceneLayerPackage_management(in_dataset, {out_slpk}, {out_coor_system}, {transform_method;transform_method...}, {texture_optimization}, {target_cloud_connection})

        Creates a scene layer package (.slpk) or scene layer content
        (.i3sREST) from a building layer input.

     INPUTS:
      in_dataset (Layer File / Building Layer):
          The input building layer or layer file (.lyrx).
      out_coor_system {Spatial Reference}:
          The coordinate system of the output scene layer package. It
          can be any projected or custom coordinate system. Supported geographic
          coordinate systems include WGS84 and China Geodetic Coordinate System
          2000. WGS84 and EGM96 Geoid are the default horizontal and vertical
          coordinate systems, respectively. The coordinate system can be
          specified in any of the following ways:        Specify the path to a
          .prj file.Reference a dataset with the correct
          coordinate system.Use an arcpy.SpatialReference object.
      transform_method {String}:
          The datum transformation method that will be used when the input
          layer's coordinate system uses a datum that differs from the output
          coordinate system. All transformations are bidirectional, regardless
          of the direction implied by their names. For example,
          NAD_1927_to_WGS84_3 will work correctly even if the datum conversion
          is from WGS84 to NAD 1927.The ArcGIS coordinate system data is
          required for vertical datum
          transformations between ellipsoidal and gravity-related and two
          gravity-related datums.
      texture_optimization {String}:
          Specifies the textures that will be optimized according to the
          target platform where the scene layer package is used.
          Optimizations that include KTX2 may take significant time to process.
          For fastest results, use the DESKTOP or NONE options.ALL-All texture
          formats will be optimized including JPEG, DXT, and
          KTX2 for use in desktop, web, and mobile platforms.DESKTOP-Windows,
          Linux, and Mac supported textures will be optimized
          including JPEG and DXT for use in ArcGIS Pro clients on Windows and
          ArcGIS Maps SDKs desktop clients on Windows, Linux, and Mac. This is
          the default.MOBILE-Android and iOS supported textures will be
          optimized including
          JPEG and KTX2 for use in ArcGIS Maps SDKs mobile
          applications.NONE-JPEG textures will be optimized for use in desktop
          and web
          platforms.
      target_cloud_connection {Folder}:
          The target cloud connection file (.acs) where the scene layer content
          (.i3sREST) will be output.

     OUTPUTS:
      out_slpk {File}:
          The output scene layer package (.slpk).

        """