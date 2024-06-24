# Generated documentation for module arcpy.management


class CreatePointSceneLayerPackage(object):
    """
    Creates a point scene layer package (.slpk) or scene layer content (.i3sREST) from a point feature layer.
    """

    @property
    def description(self) -> str:
        return """

        CreatePointSceneLayerPackage_management(in_dataset, {out_slpk}, {out_coor_system}, {transform_method;transform_method...}, {target_cloud_connection})

        Creates a point scene layer package (.slpk) or scene layer content
        (.i3sREST) from a point feature layer.

     INPUTS:
      in_dataset (Layer File / Feature Layer):
          The input point feature layer.
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
      target_cloud_connection {Folder}:
          The target cloud connection file (.acs) where the scene layer content
          (.i3sREST) will be output.

     OUTPUTS:
      out_slpk {File}:
          The output scene layer package (.slpk).

        """