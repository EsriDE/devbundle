# Generated documentation for module arcpy.oi


class UpdateOrientedImageryDatasetProperties(object):
    """
    Updates or modifies oriented imagery dataset properties.
    """

    @property
    def description(self) -> str:
        return """

        UpdateOrientedImageryDatasetProperties_oi(in_oriented_imagery_dataset, {maximum_distance}, {coverage_percent}, {footprint_item}, {elevation_source}, {constant_elevation}, {dem}, {lod}, {raster_function}, {vertical_measurement_unit}, {time_interval_unit}, {oriented_imagery_type}, {camera_heading}, {camera_pitch}, {camera_roll}, {camera_height}, {hfov}, {vfov}, {near_distance}, {far_distance}, {image_rotation}, {orientation_accuracy}, {image_path_prefix}, {image_path_suffix}, {depth_image_path_prefix}, {depth_image_path_suffix}, {dem_path_prefix}, {dem_path_suffix})

        Updates or modifies oriented imagery dataset properties.

     INPUTS:
      in_oriented_imagery_dataset (Oriented Imagery Layer):
          The path and name of the oriented imagery dataset.
      maximum_distance {Double}:
          The maximum search distance that will be used when querying the
          dataset features. The maximum distance cannot be less than zero. The
          unit is meters.
      coverage_percent {Double}:
          A percentage that modifies the extent of the image's ground footprint.
          The ground footprint of each image is computed to search for images
          that contain the selected location, which is identified as a red cross
          on the map.A negative percentage value reduces the size of the ground
          footprint
          and a positive percentage value increases it. This parameter can be
          used to exclude or include points on the edge of an image. For
          example, a value of -30 will reduce the size of the footprint by 30
          percent and a value of 20 will increase it by 20 percent. Valid values
          range from -50 to 50.
      footprint_item {String}:
          The name of the footprint feature class. The feature class should be
          in the same geodatabase as the oriented imagery dataset.
      elevation_source {String}:
          Specifies the elevation source that will be used.DEM-The elevation
          source will be a digital elevation model that is a
          dynamic image service or a tile image service.CONSTANT_ELEVATION-The
          elevation source will be a constant ground
          elevation value for the entire dataset.NONE-The elevation source will
          be removed.
      constant_elevation {Double}:
          The constant ground elevation value for the entire dataset. The
          vertical_measurement_unit parameter value will be used as the unit for
          constant elevation.This parameter is enabled when the elevation_source
          parameter value is
          specified as CONSTANT_ELEVATION.
      dem {Image Service}:
          The URL that references the input digital elevation model. A dynamic
          image service or a tile image service can be used as the digital
          elevation model.This parameter is enabled when the elevation_source
          parameter value is
          specified as DEM.
      lod {String}:
          The scale defined in a tiling schema. The scale represents the zoom
          level value. Each successive level improves resolution and map scale
          by double when compared to the previous level.This parameter is
          enabled when the dem parameter value is a tile image
          service.
      raster_function {String}:
          The raster function processing template that will be applied to the
          image service.This parameter is enabled when the dem parameter value
          is a dynamic
          image service.
      vertical_measurement_unit {String}:
          Specifies the unit that will be used for all vertical
          measurements.METER-Meters will be used as the unit of
          measurement.FEET-Feet will be
          used as the unit of measurement.
      time_interval_unit {String}:
          Specifies the time measurement unit that will be used to filter
          images.MINUTES-Images will be filtered by minutes.HOURS-Images will
          be
          filtered by hours.DAYS-Images will be filtered by days.WEEKS-Images
          will be filtered by weeks.MONTHS-Images will be filtered by
          months.YEARS-Images will be filtered by years.
      oriented_imagery_type {String}:
          Specifies the type of images in the dataset.HORIZONTAL-Images in
          which the exposure is parallel to the ground and
          looking to the horizon are in the dataset.OBLIQUE-Images in which the
          exposure is at an angle to the ground,
          typically at about 45 degrees, so the sides of objects can be seen are
          in the dataset.NADIR-Images in which the exposure is perpendicular to
          the ground and
          looking straight down are in the dataset. Only the top of objects can
          be seen.360-Images taken using cameras that provide 360-degree
          spherical
          surround views or have been stitched together as 360-degree views from
          multiple cameras are in the dataset.INSPECTION-Close-up images of
          assets are in the dataset.NONE-The oriented imagery type will be
          removed from the dataset.
      camera_heading {Double}:
          The camera orientation of the first rotation around the z-axis of the
          camera. The value is in degrees. The heading values are measured in
          the positive clockwise direction in which north is defined as 0
          degrees. -999 is used when the orientation is unknown.
      camera_pitch {Double}:
          The camera orientation of the second rotation around the x-axis of the
          camera in the positive counterclockwise direction. The value is in
          degrees. The pitch is 0 degrees when the camera is facing straight
          down to the ground. The valid range of pitch is from 0 to 180 degrees,
          with 180 degrees for a camera facing straight up and 90 degrees for a
          camera facing the horizon.
      camera_roll {Double}:
          The camera orientation of the final rotation around the z-axis of the
          camera in the positive clockwise direction. The value is in degrees.
          Valid values range from -90 to 90.
      camera_height {Double}:
          The height of the camera above the ground when the imagery was
          captured. The unit is meters. Camera height is used to determine the
          visible extent of the image. Large values will result in a greater
          view extent. Values should not be less than 0.
      hfov {Double}:
          The camera's scope in the horizontal direction. The value is in
          degrees. Valid values range from 0 to 360.
      vfov {Double}:
          The camera's scope in the vertical direction. The value is in degrees.
          Valid values range from 0 to 180.
      near_distance {Double}:
          The nearest usable distance of the imagery from the camera position.
          The unit is meters.
      far_distance {Double}:
          The farthest usable distance of the imagery from the camera position.
          The unit is meters. Far distances should be greater than 0.
      image_rotation {Double}:
          The orientation of the camera in degrees relative to the scene when
          the image was captured. The rotation is added in addition to the
          camera roll. Valid values range from-360 to 360.
      orientation_accuracy {String}:
          The standard deviation in accuracy values separated by
          semicolons. The standard deviation values are added in the following
          order and format:        Camera location in XY direction in
          metersCamera Height in metersCamera
          Heading in degreesCamera Pitch in degreesCamera Roll in degreesNear
          distance in metersFar distance in metersElevation in metersFor
          example, if the GPS has a +/- 10 meters RMS in x,y-coordinates and
          +/- 20 meters in height, the orientation accuracy value is 10;20.
      image_path_prefix {String}:
          The prefix that will be used to build the image path in
          conjunction with theattribute. Image
      image_path_suffix {String}:
          The suffix that will be used to build the image path in
          conjunction with theattribute. Image
      depth_image_path_prefix {String}:
          The prefix that will be used to build the depth image path in
          conjunction with theattribute. Depth Image
      depth_image_path_suffix {String}:
          The suffix that will be used to build the depth image path in
          conjunction with theattribute. Depth Image
      dem_path_prefix {String}:
          The prefix that will be used to build the DEM path in
          conjunction with theURL in the attribute. Elevation Source
      dem_path_suffix {String}:
          The suffix that will be used to build the DEM path in
          conjunction with theURL in the attribute. Elevation Source

        """