# Generated documentation for module arcpy.management


class CreatePointCloudSceneLayerPackage(object):
    """
    Creates a point cloud scene layer package (.slpk) or scene layer content (.i3sREST) in the cloud from LAS, zLAS, LAZ, or LAS dataset input.
    """

    @property
    def description(self) -> str:
        return """

        CreatePointCloudSceneLayerPackage_management(in_dataset, {out_slpk}, {out_coor_system}, {transform_method;transform_method...}, {attributes;attributes...}, {point_size_m}, {xy_max_error_m}, {z_max_error_m}, {in_coor_system}, {scene_layer_version}, {target_cloud_connection}, {out_name})

        Creates a point cloud scene layer package (.slpk) or scene layer
        content (.i3sREST) in the cloud from LAS, zLAS, LAZ, or LAS dataset
        input.

     INPUTS:
      in_dataset (Layer File / LAS Dataset Layer / Folder / File):
          The lidar data (LAS, zLAS, LAZ, or LAS dataset) that will be used to
          create a scene layer package. The lidar data can also be specified by
          selecting the parent folder that contains the files.
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
          The datum transformation method that will be used when the
          input layer's coordinate system uses a datum that differs from the
          output coordinate system. All transformations are bidirectional,
          regardless of the direction implied by their names. For example,
          NAD_1927_to_WGS_1984_3 will work correctly even if the datum
          conversion is from WGS 1984 to NAD 1927. ArcGIS coordinate
          system data is required for vertical datum
          transformations between ellipsoidal and gravity-related and two
          gravity-related datums.
      attributes {String}:
          Specifies the source data attributes that will be included in the
          scene layer package. These values will be accessible when the content
          is consumed in other viewers. Select attributes that are required for
          the desired rendering and filtering options (for example, intensity,
          returns, class codes, RGB). To reduce storage, exclude unneeded
          attributes.INTENSITY-The return strength of the laser pulse for each
          lidar point
          will be included.RGB-RGB imagery information collected for each lidar
          point will be
          included.FLAGS-Classification and scan direction flags will be
          included.CLASS_CODE-Classification code values will be
          included.RETURNS-Discrete return numbers from the lidar pulse will be
          includedUSER_DATA-A customizable attribute that can be any number in
          the range
          of 0 through 255 will be included.POINT_SRC_ID-For aerial lidar, this
          value typically identifies the
          flight path that collected a given lidar point, which will be
          included.GPS_TIME-The GPS time stamp at which the laser point was
          emitted from
          the aircraft will be included. The time is in GPS seconds of the week
          in which the time stamp is between 0 and 604800 and resets at midnight
          on a Sunday.SCAN_ANGLE-The angular direction of the laser scanner for
          a given
          lidar point will be included. The value range is from -90 through
          90.NEAR_INFRARED-Near infrared records collected for each lidar point
          will be included.
      point_size_m {Double}:
          The point size of the lidar data. For airborne lidar data, the default
          of 0 or a value close to the average point spacing is usually best.
          For terrestrial lidar data, the point size should match the desired
          point spacing for the areas of interest. Values are expressed in
          meters. The default of 0 will automatically determine the best value
          for the input dataset.
      xy_max_error_m {Double}:
          The maximum x,y error tolerated. A higher tolerance will result in
          better data compression and more efficient data transfer. Values are
          expressed in meters. The default is 0.001.
      z_max_error_m {Double}:
          The maximum z-error tolerated. A higher tolerance will result in
          better data compression and more efficient data transfer. Values are
          expressed in meters. The default is 0.001.
      in_coor_system {Coordinate System}:
          The coordinate system of the input .laz files. This parameter is only
          used for .laz files that do not contain spatial reference information
          in their header or have a .prj file in the same location.
      scene_layer_version {String}:
          The Indexed 3D Scene Layer (I3S) version of the resulting point cloud
          scene layer package. Specifying a version supports backward
          compatibility and allows scene layer packages to be shared with
          earlier versions of ArcGIS.1.X-The point cloud scene layer package
          will be supported in all
          ArcGIS clients.2.X-The point cloud scene layer package will be
          supported in ArcGIS
          Pro 2.1.2 or later and can be published to ArcGIS Online and ArcGIS
          10.6.1 or later. This is the default.
      target_cloud_connection {Folder}:
          The target cloud connection file (.acs) where the scene layer content
          (.i3sREST) will be output.
      out_name {String}:
          The output name of the scene layer content when output to a cloud
          store. This parameter is only available when a target_cloud_connection
          parameter value is specified.

     OUTPUTS:
      out_slpk {File}:
          The output scene layer package (.slpk).

        """