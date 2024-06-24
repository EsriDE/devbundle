# Generated documentation for module arcpy.management


class ColorBalanceMosaicDataset(object):
    """
    Color balances a mosaic dataset so that the tiles appear seamless.
    """

    @property
    def description(self) -> str:
        return """

        ColorBalanceMosaicDataset_management(in_mosaic_dataset, {balancing_method}, {color_surface_type}, {target_raster}, {exclude_raster}, {stretch_type}, {gamma}, {block_field}, {in_DEM_raster}, {ZFactor}, {ZOffset}, {Geoid}, {solution_points}, {target_objectid}, {refine_estimation}, {reduce_shadow}, {reduce_cloud})

        Color balances a mosaic dataset so that the tiles appear seamless.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that will be color balanced.
      balancing_method {String}:
          Specifies the balancing method that will be used.DODGING-Each pixel's
          value will be changed toward a target color. With
          this method, you must also choose the type of target color surface,
          which affects the target color. Dodging tends to give the best result
          in most cases.GLOBAL_FIT-An optimal pixel value will be determined by
          globally
          adjusting the color difference in all overlap areas to the minimum.
          This method is suitable for a mosaic dataset in which each image has
          good overlap with each other.HISTOGRAM-Each pixel's value will be
          changed according to its
          relationship with a target histogram. The target histogram can be
          derived from all of the rasters, or you can specify a raster. This
          method works well when all of the rasters have a similar
          histogram.STANDARD_DEVIATION-Each of the pixel's values will be
          changed
          according to its relationship with the histogram of the target raster,
          within one standard deviation. The standard deviation can be
          calculated from all of the rasters in the mosaic dataset, or you can
          specify a target raster. This method works best when all of the
          rasters have normal distributions.
      color_surface_type {String}:
          Specifies how the target color of each pixel will be determined.This
          parameter is enabled when the balancing_method parameter is set
          to DODGING.SINGLE_COLOR-All the pixels will be altered toward a
          single color
          point-the average of all pixels. Use this option when there are only a
          small number of raster datasets and a few different types of ground
          objects. If there are too many raster datasets or too many types of
          ground surfaces, the output color may become blurred.COLOR_GRID-
          Pixels will be altered toward multiple target colors,
          which are distributed across the mosaic dataset. Use this option when
          you have a large number of raster datasets or areas with a large
          number of diverse ground objects.FIRST_ORDER-All pixels will be
          altered toward many points obtained
          from the two-dimensional polynomial slanted plane. This option tends
          to create a smoother color change and uses less storage in the
          auxiliary table, but it may take longer to process compared to the
          color grid surface.SECOND_ORDER-All input pixels will be altered
          toward a set of
          multiple points obtained from the two-dimensional polynomial parabolic
          surface. This option tends to create a smoother color change and uses
          less storage in the auxiliary table, but it may take longer to process
          compared to the color grid surface.THIRD_ORDER-All input pixels will
          be altered toward multiple points
          obtained from the cubic surface. This option tends to create a
          smoother color change and uses less storage in the auxiliary table,
          but it may take longer to process compared to the color grid surface.
      target_raster {Raster Dataset / Raster Layer / Internet Tiled Layer / Map Server Layer}:
          The raster that will be used to color balance the other images. The
          balance method and color surface type, if applicable, will be derived
          from this image.
      exclude_raster {Raster Layer}:
          A raster that identifies the locations that will be excluded.Create a
          mask using the Generate Exclude Area tool.
      stretch_type {String}:
          Specifies how the range of values will be stretched before color
          balancing.NONE-The original pixel values will be used. This is the
          default.ADAPTIVE-An adaptive prestretch will be applied before any
          processing
          takes place.MINIMUM_MAXIMUM-The values will be stretched between
          their minimum
          and maximum values.STANDARD_DEVIATION-The values will be stretched
          between the default
          number of standard deviations.
      gamma {Double}:
          A numeric value that will adjust the overall brightness of an image. A
          low value will minimize the contrast between moderate values by making
          them appear darker. Higher values will increase the contrast by making
          them appear brighter.
      block_field {String}:
          A field in the mosaic dataset's attribute table that will be used to
          identify items that will be considered one item when performing some
          calculations and operations.
      in_DEM_raster {Raster Dataset / Raster Layer / Mosaic Dataset / Mosaic Layer}:
          A DEM to help estimate the overlapped locations in the mosaic
          dataset.This parameter is enabled when the balancing_method parameter
          is set
          to GLOBAL_FIT.
      ZFactor {Double}:
          A conversion factor that adjusts the units of measure for the vertical
          (or elevation) units when they are different from the horizontal
          coordinate (x,y) units of the input surface DEM. It is the number of
          ground x,y units in one surface z-unit. If the vertical units are
          meters, set the parameter to 1. If the vertical units are feet, set
          the parameter to 0.3048. If any other vertical units are used, use
          this parameter to scale the units to meters.This parameter is enabled
          when the in_DEM_raster parameter is
          specified.
      ZOffset {Double}:
          A base value that will be added to the elevation value in the DEM.
          This can be used to offset elevation values that do not start at sea
          level.This parameter is enabled when the in_DEM_raster parameter is
          specified.
      Geoid {Boolean}:
          Specifies whether the geoid correction required by rational polynomial
          coefficients ( RPC) that reference ellipsoidal heights will be made.
          Most elevation datasets are referenced to sea level orthometric
          heights, so this correction is required in these cases to convert to
          ellipsoidal heights.This parameter is active when the in_DEM_raster
          parameter is
          specified.NONE-No geoid correction will be made. Use this option only
          if the DEM
          is already expressed in ellipsoidal heights. This is the
          default.GEOID-A geoid correction will be made to convert orthometric
          heights
          to ellipsoidal heights (based on EGM96 geoid).
      solution_points {Table View}:
          The solution points from block adjustment output to help accurately
          estimate the overlapped locations. This parameter is helpful when the
          image has less than 50 percent overlap with its neighbors. Using this
          parameter will increase the computation time, so for the ordinary
          mosaic dataset with good overlaps, you can leave this parameter
          unspecified.This parameter is enabled when the balancing_method
          parameter is set
          to GLOBAL_FIT.
      target_objectid {Long}:
          The target raster object ID that will be used to color balance the
          other images. The balance method and color surface type, if
          applicable, will be derived from this image.This parameter is enabled
          when the balancing_method parameter is set
          to GLOBAL_FIT.
      refine_estimation {Boolean}:
          Specifies whether the color balancing estimation for corresponding
          locations in the overlapped areas will be refined using image
          correlation.This parameter is helpful for the exact color difference
          correction
          but will increase the computation time. If you have a mosaic dataset
          composed of a large number of images, specify the NO_REFINE_ESTIMATION
          option to reduce the computation time.This parameter is enabled when
          the balancing_method parameter is set
          to GLOBAL_FIT.NO_REFINE_ESTIMATION-No refined estimation will be made.
          This is the
          default.REFINE_ESTIMATION-A refined estimation for color balance will
          be made
      reduce_shadow {Boolean}:
          Specifies whether the negative influence of shadows on the color
          balance output will be reduced.This parameter is enabled when the
          balancing_method parameter is set
          to GLOBAL_FIT.NO_REDUCE_SHADOW-The influence of shadows will not be
          reduced. This is
          the default.REDUCE_SHADOW-The influence of shadows will be reduced.
          Use this
          option when the mosaic dataset has a lot of shadows.
      reduce_cloud {Boolean}:
          Specifies whether the negative influence of clouds on the color
          balance output will be reduced.This parameter is active when the
          balancing_method parameter is set to
          DODGING or GLOBAL_FIT.NO_REDUCE_CLOUD-The influence of clouds will not
          be reduced. This is
          the default.REDUCE_CLOUD-The influence of clouds will be reduced.

        """