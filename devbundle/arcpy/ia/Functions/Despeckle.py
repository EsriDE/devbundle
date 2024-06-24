# Generated documentation for module arcpy.ia.Functions


class Despeckle(object):
    """
    Corrects the input synthetic aperture radar (SAR) data for speckle, which is a result of coherent illumination that resembles a grainy or salt and pepper effect.
    """

    @property
    def description(self) -> str:
        return """

        Despeckle_ia(in_radar_data, {polarization_bands;polarization_bands...}, {filter_type}, {filter_size}, {noise_model}, {noise_variance}, {add_noise_mean}, {mult_noise_mean}, {number_of_looks}, {damp_factor})

        Corrects the input synthetic aperture radar (SAR) data for speckle,
        which is a result of coherent illumination that resembles a grainy or
        salt and pepper effect.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      polarization_bands {String}:
          The polarization bands that will be filtered.The first band is
          selected by default.
      filter_type {String}:
          Specifies the type of smoothing algorithm or filter that will be
          applied.LEE-A spatial filter will be applied to each pixel in an image
          to
          reduce the speckle noise. This option filters the data based on local
          statistics calculated within a square window. This filter is useful
          for smoothing speckled data that has an additive or multiplicative
          component.ENHANCED_LEE-A spatial filter that preserves the sharpness
          and detail
          of the image will be applied to reduce the speckle noise. This option
          is an enhanced version of the Lee filter. This filter is useful for
          reducing speckle while preserving texture information.REFINED_LEE-A
          spatial filter will be applied to selected pixels, based
          on local statistics, to reduce the speckle noise. This filter uses a
          nonsquare filter window to match the direction of edges. It is useful
          for reducing speckle while preserving edges. This is the
          default.FROST-An exponentially damped circularly symmetric filter that
          uses
          local statistics within individual filter windows will be applied to
          reduce the speckle noise. This does not affect image features at the
          edges. This filter is useful for reducing speckle while preserving
          edges.KUAN-A spatial filter will be applied to each pixel in an image
          to
          reduce the speckle noise. This filters the data based on local
          statistics of the centered pixel value that is calculated using the
          neighboring pixels. This filter is useful for reducing speckle while
          preserving edges.GAMMA_MAP-A Bayesian analysis and Gamma distribution
          filter will be
          applied to reduce the speckle noise. This filter is useful for
          reducing speckle while preserving edges.
      filter_size {String}:
          Specifies the size of the pixel window that will be used to filter
          noise.3x3-A 3-by-3 filter size will be used. This is the default.5x5-A
          5-by-5 filter size will be used.7x7-A 7-by-7 filter size will be
          used.9x9-A 9-by-9 filter size will be used.11x11-An 11-by-11 filter
          size will be used.This parameter is only valid when the filter_type
          parameter is set to
          LEE, ENHANCED_LEE, FROST, KUAN, or GAMMA_MAP.
      noise_model {String}:
          This parameter is only valid when the filter_type parameter is set to
          LEE.
      noise_variance {Double}:
          The noise variance of the radar image. The default is 0.25.This
          parameter is only valid when the filter_type parameter is set to
          LEE and the noise_model parameter is set to ADDITIVE_NOISE or
          ADDITIVE_AND_MULTIPLICATIVE_NOISE.
      add_noise_mean {Double}:
          The mean value of additive noise. A larger noise mean value will
          produce less smoothing, while a smaller value results in more
          smoothing. The default value is 0.This parameter is only valid when
          the filter_type parameter is set to
          LEE and the noise_model parameter is set to ADDITIVE_NOISE or
          ADDITIVE_AND_MULTIPLICATIVE_NOISE.
      mult_noise_mean {Double}:
          The mean value of multiplicative noise. A larger noise mean value will
          produce less smoothing, while a smaller value results in more
          smoothing. The default value is 1.This parameter is only valid when
          the filter_type parameter is set to
          LEE and the noise_model parameter is set to MULTIPLICATIVE_NOISE or
          ADDITIVE_AND_MULTIPLICATIVE_NOISE.
      number_of_looks {Long}:
          The number of looks value of the image, which controls image smoothing
          and estimates noise variance. A smaller value results in more
          smoothing, while a larger value retains more image features. The
          default value is 1.This parameter is only valid when the filter_type
          parameter is set to
          ENHANCED_LEE, KUAN, or GAMMA_MAP or when the filter_type parameter is
          set to LEE and the noise_model parameter is set to
          MULTIPLICATIVE_NOISE.
      damp_factor {Long}:
          The exponential damping level of smoothing that will be applied. A
          damping value greater than 1 will result in better edge preservation
          but less smoothing. Values less than 1 will result in more smoothing.
          A value of 0 will produce results similar to a low-pass filter. The
          default is 1.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The despeckled radar data.

        """