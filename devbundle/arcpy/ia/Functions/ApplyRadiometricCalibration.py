# Generated documentation for module arcpy.ia.Functions


class ApplyRadiometricCalibration(object):
    """
    Converts the input synthetic aperture radar (SAR) reflectivity into physical units of normalized backscatter by normalizing the reflectivity using a reference plane.
    """

    @property
    def description(self) -> str:
        return """

        ApplyRadiometricCalibration_ia(in_radar_data, {polarization_bands;polarization_bands...}, {calibration_type})

        Converts the input synthetic aperture radar (SAR) reflectivity into
        physical units of normalized backscatter by normalizing the
        reflectivity using a reference plane.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      polarization_bands {String}:
          The polarization bands that will be corrected.The first band is
          selected by default.
      calibration_type {String}:
          Specifies the type of calibration that will be applied.BETA_NOUGHT-The
          radar reflectivity will be calibrated to backscatter
          for a unit area on the slant range. This is the default.SIGMA_NOUGHT-
          The backscatter returned will be calibrated to the
          antenna from a unit area on the ground with the plane locally tangent
          to the ellipsoid. This is known as the radar cross section. Sigma
          nought values vary due to incidence angle, wavelength, polarization,
          terrain, and surface scattering properties.GAMMA_NOUGHT-The
          backscatter returned will be calibrated to the
          antenna from a unit area aligned with the plane perpendicular to the
          slant range. This normalizes gamma nought using the incidence angle
          relative to the ellipsoid. Gamma nought values vary due to wavelength,
          polarization, terrain, and surface scattering properties.

     OUTPUTS:
      out_radar_data (Raster Dataset):
          The calibrated radar data.

        """