# Generated documentation for module arcpy.management


class ComputeCameraModel(object):
    """
    Estimates the exterior camera model and interior camera model from the EXIF header of the raw image and refines the camera models. The model is then applied to the mosaic dataset with an option to use a tool- generated, high-resolution digital surface model (DSM) to achieve better orthorectification.
    """

    @property
    def description(self) -> str:
        return """

        ComputeCameraModel_management(in_mosaic_dataset, {out_dsm}, {gps_accuracy}, {estimate}, {refine}, {apply_adjustment}, {maximum_residual}, {initial_tiepoint_resolution}, {out_control_points}, {out_solution_table}, {out_solution_point_table}, {out_flight_path}, {maximum_overlap}, {minimum_coverage}, {remove}, {in_control_points}, {options;options...})

        Estimates the exterior camera model and interior camera model from the
        EXIF header of the raw image and refines the camera models. The model
        is then applied to the mosaic dataset with an option to use a tool-
        generated, high-resolution digital surface model (DSM) to achieve
        better orthorectification.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The mosaic dataset on which the camera model will be built and
          calculated.
      gps_accuracy {String}:
          Specifies the accuracy level of the input images. The tool will search
          for images in the neighborhood to compute matching points and
          automatically apply an adjustment strategy based on the accuracy
          level.HIGH-The GPS accuracy is 0 to 10 meters, and the tool uses a
          maximum
          of 4 by 3 images.MEDIUM-The GPS accuracy is 10 to 20 meters, and the
          tool uses a
          maximum of 4 by 6 images.LOW-The GPS accuracy is 20 to 50 meters, and
          the tool uses a maximum
          of 4 by 12 images.VERY_LOW-The GPS accuracy is more than 50 meters,
          and the tool uses a
          maximum of 4 by 20 images.VERY_HIGH-Imagery was collected with a high-
          accuracy, differential
          GPS, such as RTK or PPK. This option will hold image locations fixed
          during block adjustment.
      estimate {Boolean}:
          Specifies whether the camera model will be estimated by computing the
          adjustment based on eight times the mosaic dataset's source
          resolution. Computing the adjustment at this level will be faster but
          less accurate.ESTIMATE-The camera model will be estimated. This is the
          default.NO_ESTIMATE-The camera model will not be estimated.
      refine {Boolean}:
          Specifies whether the camera model will be refined by computing the
          adjustment at the mosaic dataset resolution. Computing the adjustment
          at this level will provide the most accurate result.REFINE-The camera
          model will be refined by computing the adjustment at
          the source resolution. This is the default.NO_REFINE-The camera model
          will not be refined. This option will be
          faster, so it is a good option when the computation does not need to
          be performed at the source resolution.
      apply_adjustment {Boolean}:
          Specifies whether the calculated adjustment will be applied to the
          input mosaic dataset.APPLY-The calculated adjustment will be applied
          to the input mosaic
          dataset. Although not required, it is recommended that you specify
          this option. This is the default.NO_APPLY-The calculated adjustment
          will not be applied to the input
          mosaic dataset.
      maximum_residual {Double}:
          The maximum residual value allowed to keep a computed control point as
          a valid control point. The default is 5.
      initial_tiepoint_resolution {Double}:
          The resolution factor at which tie points will be generated when
          estimating the camera model. The default value is 8, which means eight
          times the source pixel resolution.For images with only minor
          differentiation of features, such as
          agriculture fields, a lower value such as 2 can be used.
      maximum_overlap {Double}:
          The percentage of overlap between two images to consider them
          duplicates.For example, if the value is 0.9, it means if an image is
          90 percent
          covered by another image, it will be considered a duplicate and
          removed.
      minimum_coverage {Double}:
          The percentage indicating the control point's coverage on an image. If
          the coverage is less than the minimum percentage, the image will be
          unresolved and removed. The default is 0.
      remove {Boolean}:
          Specifies whether images will be automatically removed if they are too
          far from the flight strip.NO_REMOVE-Images will not be removed. This
          is the
          default.REMOVE-Images that are too far away from the flight strip will
          be
          removed.
      in_control_points {Feature Class}:
          The tie point table that will be used to compute the camera model. If
          no tie point table is provided, the tool will compute the tie points
          and estimate the camera model.
      options {Value Table}:
          Additional options for the adjustment engine. The specifications of
          many of the options are supplied by the data provider. The
          options include the following:        CalibrateF-The
          sensor's focal length will be calibrated for use in the
          block adjustment. Assign a value of 1 for focal length calibration, or
          0 to not calibrate. The default is 1.CalibratePP-The principle point
          in the block adjustment will be
          calibrated. Assign a value of 1 for calibration, or 0 to not
          calibrate. The default is 1.CalibrateP-Radial distortion parameters in
          the block adjustment will
          be calibrated. Assign a value of 1 for calibration, or 0 to not
          calibrate. The default is 1.CalibrateK-Tangential distortion
          parameters in the block adjustment
          will be calibrated. Assign a value of 1 for calibration, or 0 to not
          calibrate. The default is 1. EstimateOPK-The Omega, Phi, and
          Kappa angles will be
          calibrated to define the rotation between the image coordinate system
          and the projected coordinate system. Assign a value of 0 to use
          orientation angles (roll, pitch, and yaw) from UAV metadata as
          attitude initials in the block adjustment. Use a value of 1 to
          estimate orientation angles, and use estimated orientation angles as
          attitude initials in the block adjustment. The default is 1.
          For most DJI and Skydio cameras, a value of 0 is
          recommended.APrioriAccuracyX-The accuracy of the x-coordinate provided
          by the
          metadata. The units must match PerspectiveX. This option is not
          recommended for most UAV data.APrioriAccuracyY-The accuracy of the
          y-coordinate provided by the
          metadata. The units must match PerspectiveY. This option is not
          recommended for most UAV data.APrioriAccuracyZ-The accuracy of the
          z-coordinate provided by the
          metadata. The units must match PerspectiveZ. This option is not
          recommended for most UAV data.APrioriAccuracyXY-The accuracy of the
          planar coordinate provided by
          the metadata. The units must match PerspectiveX. This option is not
          recommended for most UAV data.APrioriAccuracyXYZ-The accuracy of image
          location provided by the
          metadata. The units must match PerspectiveX. This option is not
          recommended for most UAV data.APrioriAccuracyOmega-The accuracy of the
          Omega angle provided by the
          airborne Position Orientation System (POS). The units are in decimal
          degrees.APrioriAccuracyPhi-The accuracy of the Phi angle provided by
          the
          airborne Position Orientation System (POS). The units are in decimal
          degrees.APrioriAccuracyOmegaPhi-The accuracy of the Omega or Phi angle
          provided by the airborne Position Orientation System (POS). The units
          are in decimal degrees.APrioriAccuracyKappa-The accuracy of the Kappa
          angle provided by the
          airborne Position Orientation System (POS). The units are in decimal
          degrees.ComputeImagePosteriorStd-The posterior standard deviation of
          image
          location and orientation after adjustment will be computed. Assign a
          value of 1 to compute, or 0 to not compute. The default is
          1.ComputeSolutionPointPosteriorStd-The posterior standard deviation of
          solution points after adjustment will be computed. Assign a value of 1
          to compute, or 0 to not compute. The default is 0.

     OUTPUTS:
      out_dsm {Raster Dataset}:
          A DSM raster dataset generated from the adjusted images in the mosaic
          dataset. If apply_adjustment is set to APPLY, this DSM will replace
          the DEM in the geometric function to achieve better
          orthorectification.
      out_control_points {Feature Class}:
          The optional control points feature class.
      out_solution_table {Table}:
          The optional adjustment solution table. The solution table contains
          the root mean square (RMS) of the adjustment error and solution
          matrix.
      out_solution_point_table {Feature Class}:
          The optional solution point feature class. The solution points are the
          final controls points used to generate the adjustment solution.
      out_flight_path {Feature Class}:
          The optional flight path line feature class.

        """