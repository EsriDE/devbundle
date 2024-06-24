# Generated documentation for module arcpy.management


class SetMosaicDatasetProperties(object):
    """
    Defines the defaults for displaying a mosaic dataset and serving it as an image service.
    """

    @property
    def description(self) -> str:
        return """

        SetMosaicDatasetProperties_management(in_mosaic_dataset, {rows_maximum_imagesize}, {columns_maximum_imagesize}, {allowed_compressions;allowed_compressions...}, {default_compression_type}, {JPEG_quality}, {LERC_Tolerance}, {resampling_type}, {clip_to_footprints}, {footprints_may_contain_nodata}, {clip_to_boundary}, {color_correction}, {allowed_mensuration_capabilities;allowed_mensuration_capabilities...}, {default_mensuration_capabilities}, {allowed_mosaic_methods;allowed_mosaic_methods...}, {default_mosaic_method}, {order_field}, {order_base}, {sorting_order}, {mosaic_operator}, {blend_width}, {view_point_x}, {view_point_y}, {max_num_per_mosaic}, {cell_size_tolerance}, {cell_size}, {metadata_level}, {transmission_fields;transmission_fields...}, {use_time}, {start_time_field}, {end_time_field}, {time_format}, {geographic_transform;geographic_transform...}, {max_num_of_download_items}, {max_num_of_records_returned}, {data_source_type}, {minimum_pixel_contribution}, {processing_templates;processing_templates...}, {default_processing_template}, {time_interval}, {time_interval_units}, {product_definition}, {product_band_definitions;product_band_definitions...})

        Defines the defaults for displaying a mosaic dataset and serving it as
        an image service.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset with the properties that will be set.
      rows_maximum_imagesize {Long}:
          The maximum number of rows for the mosaicked image, generated by the
          mosaic dataset for each request. This can help control how much work
          the server has to do when clients view the imagery. A higher number
          will create a larger image but will increase the amount of time to
          process the mosaic dataset. If the value is too low, the image may not
          display.
      columns_maximum_imagesize {Long}:
          The maximum number of columns for the mosaicked image, generated by
          the mosaic dataset for each request. This can help control how much
          work the server has to do when clients view the imagery. A higher
          number will create a larger image but will increase the amount of time
          to process the mosaic dataset. If the value is too low, the image may
          not display.
      allowed_compressions {String}:
          Specifies the compression methods that will be used to transmit the
          mosaicked image from the computer to the display (or from the server
          to the client).None-No compression will be used.JPEG-Compression up
          to 8:1 will be
          used, which is suitable for
          backdrops.LZ77-Compression of approximately 2:1 will be used, which
          is suitable
          for analysis.LERC-Compression between 10:1 and 20:1 will be used,
          which is fast and
          suitable for serving raw imagery with high bit depth (12 bit to 32
          bit).
      default_compression_type {String}:
          Specifies the default compression type. The default
          compression must be in the list of values used for the
          allowed_compressions parameter or must be set in the mosaic
          dataset'sproperty. Allowed Compression MethodsNone-No
          compression will be used.JPEG-Compression up to 8:1 will be
          used, which is suitable for
          backdrops.LZ77-Compression of approximately 2:1 will be used, which
          is suitable
          for analysis.LERC-Compression between 10:1 and 20:1 will be used,
          which is fast and
          suitable for serving raw imagery with high bit depth (12 bit to 32
          bit).
      JPEG_quality {Long}:
          The compression quality when using JPEG. Compression quality ranges
          from 1 to 100. A higher number means better image quality but less
          compression.
      LERC_Tolerance {Double}:
          The maximum per pixel error when using LERC compression. This value is
          specified in the units of the mosaic dataset. For example, if the
          error is 10 centimeters and the mosaic dataset is in meters, enter
          0.1.
      resampling_type {String}:
          Specifies how pixel values will be calculated when the dataset is
          displayed at small scales. Choose an appropriate technique based on
          the type of data. NEAREST-The value of each pixel will be from
          the nearest
          corresponding pixel. This technique is suitable for discrete data,
          such as land cover. This is the fastest resampling technique.
          It minimizes the changes to
          pixel values since it uses the value from the nearest
          pixel.BILINEAR-The value of each pixel will be calculated by averaging
          the
          values of the surrounding four pixels (based on distance). This
          technique is suitable for continuous data.CUBIC-The value of each
          pixel will be calculated by fitting a smooth
          curve based on the surrounding 16 pixels. This technique produces the
          smoothest image but can create values outside of the range in the
          source data. It is suitable for continuous data.MAJORITY-The value of
          each pixel will be based on the most popular
          value in a 3 by 3 window. This technique is suitable for discrete
          data.
      clip_to_footprints {Boolean}:
          Specifies whether rasters will be clipped to the footprint. Often the
          raster dataset and its footprint have the same extent. If they differ,
          the raster dataset can be clipped to the footprint.NOT_CLIP-The
          rasters will not be clipped to the footprint. This is the
          default.CLIP-The rasters will be clipped to the footprint.
      footprints_may_contain_nodata {Boolean}:
          Specifies whether pixels with NoData values will be
          shown.FOOTPRINTS_MAY_CONTAIN_NODATA-Pixels with NoData values will be
          shown.
          This is the default.FOOTPRINTS_DO_NOT_CONTAIN_NODATA-Pixels with
          NoData values will not be
          shown. You may notice an improvement in performance; however, if the
          imagery does include NoData values, they will appear as holes in the
          mosaic dataset.
      clip_to_boundary {Boolean}:
          Specifies whether the mosaicked image will be clipped to the boundary.
          Often the mosaic dataset and its boundary have the same extent. If
          they differ, the mosaic dataset can be clipped to the boundary.CLIP-
          The mosaicked image will be clipped to the boundary. This is the
          default.NOT_CLIP-The mosaicked image will not be clipped to the
          boundary.
      color_correction {Boolean}:
          Specifies whether color correction will be used on the mosaic
          dataset.NOT_APPLY-Color correction will not be used. This is the
          default.APPLY-The color correction that has been set up for the mosaic
          dataset
          will be used.
      allowed_mensuration_capabilities {String}:
          Specifies the measurements that will be performed on the mosaic
          dataset. The ability to perform vertical measurements is dependent on
          the imagery and may require a DEM.None-No mensuration capabilities
          will be performed.Basic-Ground
          measurements such as distance, point, centroid, and area
          calculations will be performed.Base-Top Height-Measurements from the
          base to the top of features will
          be performed. Rational polynomial coefficients must be imbedded in the
          imagery.Base-Top Shadow Height-Measurements from the base of a feature
          to the
          top of its shadow will be performed. Sun azimuth and sun elevation
          information is required.Top-Top Shadow Height-Measurements from the
          top of a feature to the
          top of its shadow will be performed. Sun azimuth, sun elevation, and
          rational polynomial coefficients are required.3D-Measurements in 3D
          will be performed if a DEM is available.
      default_mensuration_capabilities {String}:
          Specifies the default mensuration capability for the mosaic
          dataset. The default mensuration value must be set in the list of
          values used for the allowed_mensuration_capabilities parameter or be
          set in the mosaic dataset'sproperty. Mensuration
          CapabilitiesNone-No mensuration capabilities will be performed.Basic-
          Ground
          measurements such as distance, point, centroid, and area
          calculations will be performed.Base-Top Height-Measurements from the
          base to the top of features will
          be performed. Rational polynomial coefficients must be imbedded in the
          imagery.Base-Top Shadow Height-Measurements from the base of a feature
          to the
          top of its shadow will be performed. Sun azimuth and sun elevation
          information is required.Top-Top Shadow Height-Measurements from the
          top of a feature to the
          top of its shadow will be performed. Sun azimuth, sun elevation, and
          rational polynomial coefficients are required.3D-Measurements in 3D
          will be performed if a DEM is available.
      allowed_mosaic_methods {String}:
          Specifies the rules for displaying overlapping imagery.
          None-Rasters will be ordered based on thefield in the mosaic
          dataset attribute table. ObjectIDCenter-Imagery that is
          closest to the center of the screen will be
          displayed.NorthWest-Imagery that is closest to the northwest corner of
          the
          mosaic dataset boundary will be displayed.LockRaster-Selected raster
          datasets will be displayed.ByAttribute-Imagery will be displayed and
          prioritized based on a field
          in the attribute table.Nadir-Rasters with viewing angles closest to
          zero will be displayed.Viewpoint-Imagery that is closest to a selected
          viewing angle will be
          displayed.Seamline-Transitions between images will be smoothed using
          seamlines.
      default_mosaic_method {String}:
          Specifies the default mosaic method that will be used for the
          mosaic dataset. The default mosaic method must be set in the list of
          values used for the allowed_mosaic_methods parameter or be set in the
          mosaic dataset'sproperty. Allowed Mosaic Methods
          None-Rasters will be ordered based on thefield in the mosaic
          dataset attribute table. ObjectIDCenter-Imagery that is
          closest to the center of the screen will be
          displayed.NorthWest-Imagery that is closest to the northwest corner of
          the
          mosaic dataset boundary will be displayed.LockRaster-Selected raster
          datasets will be displayed.ByAttribute-Imagery will be displayed and
          prioritized based on a field
          in the attribute table.Nadir-Rasters with viewing angles closest to
          zero will be displayed.Viewpoint-Imagery that is closest to a selected
          viewing angle will be
          displayed.Seamline-Transitions between images will be smoothed using
          seamlines.
      order_field {String}:
          The field that will be used when ordering rasters using the
          ByAttribute value of the default_mosaic_method parameter. The list of
          fields is defined as those in the attribute table that are of type
          metadata and are integer. This list can include, but is not limited
          to, the following:
          MinPSMaxPSLowPSHighPSCenterXCenterYZOrderShape_LengthShape_AreaIf the
          field is a numeric or date field, the order_base parameter must
          be set.This parameter is not needed if the ByAttribute value is not in
          the
          allowed_mosaic_methods list.
      order_base {String}:
          Sorts the rasters based on their difference from this value in the
          field selected in the order_field parameter        If a Date attribute
          is used, it must be in one of the
          following formats:        YYYY/MM/DD HH:mm:ss.sYYYY/MM/DD
          HH:mm:ssYYYY/MM/DD HH:mmYYYY/MM/DD
          HHYYYY/MM/DDYYYY/MMYYYYThis parameter is required only if the
          ByAttribute value is specified
          for the allowed_mosaic_methods parameter.
      sorting_order {Boolean}:
          Specifies whether the rasters will be sorted in an ascending or a
          descending order.ASCENDING-Rasters will be sorted in an ascending
          order. This is the
          default.DESCENDING-Rasters will be sorted in a descending order.This
          parameter is required only if the ByAttribute value is specified
          for the allowed_mosaic_methods parameter.
      mosaic_operator {String}:
          Specifies the rule that will be used for resolving overlapping
          pixels.FIRST-The first image in the attribute table will be
          displayed.LAST-The last image in the attribute table will be
          displayed.MIN-The lowest pixel values will be displayed.MAX-The
          highest pixel values will be displayed.MEAN-The arithmetic mean will
          be used to average overlapping pixels.BLEND-A distance weighted
          algorithm will be used to average
          overlapping pixels.SUM-All of the overlapping pixel values will be
          added together.
      blend_width {Long}:
          The number of pixels to which the BLEND value of the mosaic_operator
          parameter will be applied.
      view_point_x {Double}:
          A numeric value that will be used to horizontally shift the center of
          the image. The units are the same as the spatial reference system.This
          parameter is only applicable if the allowed_mosaic_methods
          parameter is set to Viewpoint.
      view_point_y {Double}:
          A numeric value that will be used to vertically shift the center of
          the image. The units are the same as the spatial reference system.This
          parameter is only applicable if the allowed_mosaic_methods
          parameter is set to Viewpoint.
      max_num_per_mosaic {Long}:
          The maximum number of raster datasets that will be displayed at a
          given time in a mosaic dataset.
      cell_size_tolerance {Double}:
          The maximum pixel size difference that is allowed before images are
          considered to have a different cell pixel.This allows images of
          similar spatial resolutions to be considered as
          having the same nominal resolution. For example, with a factor of 0.1,
          all images with cell sizes within 10 percent of each other will be
          grouped for tools and operations that use cell sizes.
      cell_size {Cell Size XY}:
          The cell size of the mosaic dataset using an existing raster dataset
          or its specified width (x) and height (y). If you specify the cell
          size, you can use a single value for a square cell size, or x and y
          values for a rectangular cell size.
      metadata_level {String}:
          Specifies the level of metadata that will be exposed from the server
          to a client when publishing the mosaic dataset.FULL-Metadata regarding
          the processing applied at the mosaic dataset
          level as well as metadata related to the individual raster datasets
          will be exposed.NONE-No metadata will be exposed to the
          client.BASIC-Metadata related to individual raster datasets, such as
          the
          number of columns and rows, cell size, and spatial reference
          information, will be exposed.
      transmission_fields {String}:
          The fields in the attribute table that clients can view. By
          default, the list includes the following:
          NameMinPSMaxPSLowPSHighPSTagGroupNameProductNameCenterXCenterYZOrderSh
          ape_LengthShape_Area
      use_time {Boolean}:
          Specifies whether the mosaic dataset will be time aware. If time is
          activated, the start and end fields and the time format must be
          specified.DISABLED-The mosaic dataset will not be time aware. This is
          the
          default.ENABLED-The mosaic dataset will be time aware. This allows the
          client
          to use the Time Slider.
      start_time_field {String}:
          The field in the attribute table that shows the start time.
      end_time_field {String}:
          The field in the attribute table that shows the end time.
      time_format {String}:
          Specifies the time format that will be used for the mosaic dataset for
          parameters such as start_time_field and end_time_field.YYYY-The time
          format will be year.YYYYMM-The time format will be year
          and month.YYYY/MM-The time format will be year and month.YYYY-MM-The
          time format will be year and month.YYYYMMDD-The time format will be
          year, month, and day.YYYY/MM/DD-The time format will be year, month,
          and day.YYYY-MM-DD-The time format will be year, month, and
          day.YYYYMMDDhhmmss-The time format will be year, month, day, hour,
          minute,
          and seconds.YYYY/MM/DD hh:mm:ss-The time format will be year, month,
          day, hour,
          minute, and seconds.YYYY-MM-DD hh:mm:ss-The time format will be year,
          month, day, hour,
          minute, and seconds.YYYYMMDDhhmmss.s-The time format will be year,
          month, day, hour,
          minute, seconds, and fraction of seconds.YYYY/MM/DD hh:mm:ss.s-The
          time format will be year, month, day, hour,
          minute, seconds, and fraction of seconds.YYYY-MM-DD hh:mm:ss.s-The
          time format will be year, month, day, hour,
          minute, seconds, and fraction of seconds.
      geographic_transform {String}:
          The geographic transformations that will be associated with the mosaic
          dataset.
      max_num_of_download_items {Long}:
          The maximum number of raster datasets that will be downloaded per
          request.
      max_num_of_records_returned {Long}:
          The maximum number of records that will be downloaded per request.
      data_source_type {String}:
          Specifies the type of imagery in the mosaic dataset.GENERIC-The mosaic
          dataset contains no specified data
          type.THEMATIC-The mosaic dataset contains thematic data with discrete
          values, such as land cover.PROCESSED-The mosaic dataset has been color
          adjusted.ELEVATION-The mosaic dataset contains elevation
          data.SCIENTIFIC-The mosaic dataset contains scientific
          data.VECTOR_UV-The mosaic dataset has two variables.VECTOR_MAGDIR-The
          mosaic dataset has magnitude and direction.
      minimum_pixel_contribution {Long}:
          The minimum number of pixels required for a mosaic dataset item to be
          considered significant enough to be used in the mosaic dataset.
          Because of overlapping imagery, an item may display only a small
          sliver of its overall image. Skipping these mosaic dataset items will
          improve performance of the mosaic dataset.
      processing_templates {rft.xml|rft.json|rft|xml|json}:
          The function chains that will be used to process a mosaic dataset or
          the mosaic dataset items on the fly. You can add, remove, or reorder
          the function chains.All the template names that are added must be
          unique.For information about working with function chains, see Raster
          function template.
      default_processing_template {String}:
          The default function chain. The default function chain will be applied
          when the mosaic dataset is accessed.
      time_interval {Double}:
          The duration of each time step interval. The time step interval
          defines the granularity of the temporal data. The unit of time is
          specified in the time_interval_units parameter.
      time_interval_units {String}:
          Specifies the measurement unit that will be used for the time
          interval.None-No time unit exists or it is unknown.Milliseconds-The
          time unit
          will be milliseconds.Seconds-The time unit will be seconds.Minutes-The
          time unit will be minutes.Hours-The time unit will be hours.Days-The
          time unit will be days.Weeks-The time unit will be weeks.Months-The
          time unit will be months.Years-The time unit will be years.Decades-The
          time unit will be decades.Centuries-The time unit will be centuries.
      product_definition {String}:
          Specifies a template that is either specific to the type of imagery
          you are working with or generic. The generic options include the
          standard supported raster sensor types as follows:NONE-No band
          ordering is specified for the mosaic dataset. This is the
          default.NATURAL_COLOR_RGB-A 3-band mosaic dataset, with red, green,
          and blue
          wavelength ranges will be created. This is designed for natural color
          imagery.NATURAL_COLOR_RGBI-A 4-band mosaic dataset, with red, green,
          blue, and
          near infrared wavelength ranges will be created.VECTOR_FIELD_UV-A
          mosaic dataset displaying two variables will be
          created.VECTOR_FIELD_MAGNITUDE_DIRECTION-A mosaic dataset displaying
          magnitude
          and direction will be created.FALSE_COLOR_IRG-A 3-band mosaic dataset,
          with near infrared, red, and
          green wavelength ranges will be created.BLACKSKY-A 3-band mosaic
          dataset using the BlackSky wavelength ranges
          will be createdDMCII_3BANDS-A 3-band mosaic dataset using the DMCii
          wavelength ranges
          will be created.DEIMOS2_4BANDS-A 4-band mosaic dataset using the
          Deimos-2 wavelength
          ranges will be created.DUBAISAT-2_4BANDS-A 4-band mosaic dataset using
          the DubaiSat-2
          wavelength ranges will be created.FORMOSAT-2_4BANDS-A 4-band mosaic
          dataset using the FORMOSAT-2
          wavelength ranges will be created.GEOEYE-1_4BANDS-A 4-band mosaic
          dataset using the GeoEye-1 wavelength
          ranges will be created.GF-1 PMS_4BANDS-A 4-band mosaic dataset using
          the Gaofen-1
          Panchromatic Multispectral Sensor wavelength ranges will be
          created.GF-1 WFV_4BANDS-A 4-band mosaic dataset using the Gaofen-1
          Wide Field
          of View Sensor wavelength ranges will be created.GF-2 PMS_4BANDS-A
          4-band mosaic dataset using the Gaofen-2
          Panchromatic Multispectral Sensor wavelength ranges will be
          created.GF-4 PMI_4BANDS-A 4-band mosaic dataset using the Gaofen-4
          panchromatic and multispectral wavelength ranges will be created.HJ
          1A/1B CCD_4BANDS-A 4-band mosaic dataset using the Huan Jing-1 CCD
          Multispectral or Hyperspectral Sensor wavelength ranges will be
          created.IKONOS_4BANDS-A 4-band mosaic dataset using the IKONOS
          wavelength
          ranges will be created.JILIN-1_3BANDS-A 3-band mosaic dataset using
          the Jilin-1 wavelength
          ranges will be created.KOMPSAT-2_4BANDS-A 4-band mosaic dataset using
          the KOMPSAT-2
          wavelength ranges will be created.KOMPSAT-3_4BANDS-A 4-band mosaic
          dataset using the KOMPSAT-3
          wavelength ranges will be created.LANDSAT_6BANDS-A 6-band mosaic
          dataset using the Landsat 5 and 7
          wavelength ranges from the TM and ETM+ sensors will be
          created.LANDSAT_8BANDS-An 8-band mosaic dataset using the Landsat 8
          wavelength
          ranges will be created.LANDSAT_9BANDS-An 8-band mosaic dataset using
          the Landsat 9 wavelength
          ranges will be created.LANDSAT_MSS_4BANDS-A 4-band mosaic dataset
          using the Landsat
          wavelength ranges from the MSS sensor will be created.PLANETSCOPE-A
          5-band mosaic dataset using the PlanetScope wavelength
          ranges will be created.PLEIADES-1_4BANDS-A 4-band mosaic dataset using
          the Pleiades 1
          wavelength ranges will be created.PLEIADES_NEO_6BANDS-A 6-band mosaic
          dataset using the Pleiades Neo
          wavelength ranges will be created.QUICKBIRD_4BANDS-A 4-band mosaic
          dataset using the QuickBird
          wavelength ranges will be created.RAPIDEYE_5BANDS-A 5-band mosaic
          dataset using the RapidEye wavelength
          ranges will be created.SENTINEL2_13BANDS-A 13-band mosaic dataset
          using the Sentinel 2 MSI
          wavelength ranges will be created.SKYSAT_4BANDS-A 4-band mosaic
          dataset using the SkySat-C MSI
          wavelength ranges will be created.SPOT-5_4BANDS-A 4-band mosaic
          dataset using the SPOT-5 wavelength
          ranges will be created.SPOT-6_4BANDS-A 4-band mosaic dataset using the
          SPOT-6 wavelength
          ranges will be created.SPOT-7_4BANDS-A 4-band mosaic dataset using the
          SPOT-7 wavelength
          ranges will be created.SUPERVIEW-1_4BANDS-A 4-band mosaic dataset
          using the SuperView-1
          wavelength ranges will be created.TH-01_4BANDS-A 4-band mosaic dataset
          using the Tian Hui-1 wavelength
          ranges will be created.WORLDVIEW-2_8BANDS-An 8-band mosaic dataset
          using the WorldView-2
          wavelength ranges will be created.WORLDVIEW-3_8BANDS-An 8-band mosaic
          dataset using the WorldView-3
          wavelength ranges will be created.WORLDVIEW-4_4BANDS-A 4-band mosaic
          dataset using the WorldView-4
          wavelength ranges will be created.VISION-1_4BANDS-A 4-band mosaic
          dataset using the Vision-1 wavelength
          ranges will be created.ZY1-02C PMS_3BANDS-A 3-band mosaic dataset
          using the ZiYuan-1
          panchromatic/multispectral wavelength ranges will be
          created.ZY3-CRESDA_4BANDS-A 4-band mosaic dataset using the ZiYuan-3
          CRESDA
          wavelength ranges will be created.ZY3-SASMAC_4BANDS-A 4-band mosaic
          dataset using the ZiYuan-3 SASMAC
          wavelength ranges will be created. CUSTOM-The number of bands
          and the average wavelength for
          each band are defined using theparameter (product_band_definitions in
          Python). Product Band Definitions
      product_band_definitions {Value Table}:
          The wavelength ranges, number of bands, and band order definitions.
          You can edit the product_definition values and add new bands using the
          CUSTOM product definition.

        """