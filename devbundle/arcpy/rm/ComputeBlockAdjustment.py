# Generated documentation for module arcpy.rm


class ComputeBlockAdjustment(object):
    """
    Computes the adjustments to the mosaic dataset. This tool will create a solution table that can be used to apply the actual adjustments.
    """

    @property
    def description(self) -> str:
        return """

        ComputeBlockAdjustment_rm(in_mosaic_dataset, in_control_points, transformation_type, out_solution_table, {out_solution_point_table}, {maximum_residual_value}, {adjustment_options;adjustment_options...}, {location_accuracy}, {out_quality_table}, {DEM}, {elevation_accuracy})

        Computes the adjustments to the mosaic dataset. This tool will create
        a solution table that can be used to apply the actual adjustments.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset that will be adjusted.
      in_control_points (Feature Layer):
          The control point table that includes tie points and ground control
          points.This feature class is usually the output from the Compute Tie
          Points
          tool.
      transformation_type (String):
          Specifies the type of transformation that will be used when adjusting
          the mosaic dataset.POLYORDER0-A zero-order polynomial will be used in
          the block
          adjustment computation. This is commonly used when the data is in flat
          area.POLYORDER1-A first-order polynomial (affine) will be used in the
          block
          adjustment computation. This is the default. RPC-The rational
          polynomial coefficients (RPCs) will be used
          for the transformation. This is used for satellite imagery that
          contains RPC information in the metadata. This option requires
          the ArcGIS Desktop Advanced license. Frame-The Frame camera
          model will be used for the
          transformation. This is used for aerial imagery that contains the
          frame camera information in the metadata. This option requires
          the ArcGIS Desktop Advanced license.
      maximum_residual_value {Double}:
          A threshold that is used in block adjustment computation; points with
          residuals exceeding the threshold will not be used. This parameter
          applies when the transformation type is POLYORDER0, POLYORDER1, or
          Frame. If the transformation type is RPC, the proper threshold for
          eliminating invalid points will be automatically determined.When the
          transformation type is POLYORDER0 or POLYORDER1, the units
          for this parameter will be map units, and the default value will be
          2.When the transformation type is Frame, the units for this parameter
          will be pixels, and the default value will be 5.
      adjustment_options {Value Table}:
          Additional options that will be used to fine-tune the
          adjustment computation. To set an option in thepane,
          type the keyword and the
          corresponding value in the list box. Geoprocessing
          MinResidual-The minimum residual value, which is the lower
          threshold value, will be used. When the transformation type is
          POLYORDER0 or POLYORDER1, the units will be map units and the default
          minimum residual value will be 0. The minimum residual value
          and the maximum_residual_value parameter
          value are used in detecting and removing points that generate large
          errors from the block adjustment computation.
          MaxResidualFactor-The maximum residual factor will be used to
          generate the maximum (upper threshold) residual value if the
          maximum_residual-value parameter is not defined. In this case,
          MaxResidualFactor * RMS will be used to calculate the upper threshold
          value. The minimum residual value and the
          maximum_residual_factor parameter
          value are used in detecting and removing points that generate large
          errors from block adjustment computation. Additional options
          for the adjustment engine are listed below
          whenis specified for theparameter. The specifications of many of the
          options are supplied by the data provider. FrameTransformation
          Type        The options include the following:
          CalibrateF-Calibrate
          the sensor's focal length for use in the block
          adjustment. Assign a value of 1 for focal length calibration or 0 for
          no calibration. The default is 0.CalibratePP-Calibrate the principle
          point in the block adjustment.
          Assign a value of 1 for calibration or 0 for no calibration. The
          default is 0.CalibrateP-Calibrate for radial distortion parameters in
          the block
          adjustment. Assign a value of 1 for calibration or 0 for no
          calibration. The default is 0.CalibrateK-Calibrate for tangential
          distortion parameters in the block
          adjustment. Assign a value of 1 for calibration or 0 for no
          calibration. The default is 0. Calibration parameters, such as
          perspective data, are usually
          provided for most professional digital aerial cameras, such as
          UltraCam or DMC. The calibration options can be 0 if camera
          calibration parameters are prepared in the camera
          table.APrioriAccuracyX-Include the accuracy of the x-coordinate
          provided by
          the airborne Position Orientation System. The units must match
          PerspectiveX. If the value is set to 0, the x-coordinate of the image
          location is not adjusted in adjustment. This is not recommended for
          most UAV data.APrioriAccuracyY-Include the accuracy of the
          y-coordinate provided by
          the airborne Position Orientation System. The units must match
          PerspectiveY. If the value is set to 0, the y-coordinate of the image
          location is not adjusted in adjustment. This is not recommended for
          most UAV data.APrioriAccuracyZ-Include the accuracy of the
          z-coordinate provided by
          the airborne Position Orientation System. The units must match
          PerspectiveZ. If the value is set to 0, the z-coordinate of the image
          location is not adjusted in adjustment. This is not recommended for
          most UAV data.APrioriAccuracyXY-Include the accuracy of the planar
          coordinate
          provided by the metadata. The units must match PerspectiveX. If the
          value is set to 0, planar coordinates (x and y) of the image location
          are not adjusted in adjustment. This is not recommended for most UAV
          data.APrioriAccuracyXYZ-Include the accuracy of image location
          provided by
          the metadata. The units must match PerspectiveX. If the value is set
          to 0, the image location is not adjusted in adjustment. This is not
          recommended for most UAV data.APrioriAccuracyOmega-Include the
          accuracy of the Omega angle provided
          by the airborne Position Orientation System. The units are in decimal
          degrees.APrioriAccuracyPhi-Include the accuracy of the Phi angle
          provided by
          the airborne Position Orientation System. The units are in decimal
          degrees.APrioriAccuracyOmegaPhi-Include the accuracy of the Omega or
          Phi angle
          provided by the airborne Position Orientation System. The units are in
          decimal degrees.APrioriAccuracyKappa-Include the accuracy of the Kappa
          angle provided
          by the airborne Position Orientation System. The units are in decimal
          degrees.ComputeAntennaOffset-Compute the offset between GNSS antenna
          center
          and camera projection center in adjustment. Assign a value of 1 to
          compute or 0 for no computation. The default is 0.ComputeShift-Compute
          the GNSS signal shift in flights in bundle
          adjustment. Assign a value of 1 to compute or 0 for no computation.
          The default is 0.ComputeImagePosteriorStd-Compute the posterior
          standard deviation of
          image location and orientation after adjustment. Assign a value of 1
          to compute or 0 for no computation. The default is
          1.ComputeSolutionPointPosteriorStd-Compute the posterior standard
          deviation of solution points after adjustment. Assign a value of 1 to
          compute or 0 for no computation. The default is 0.rigCamera-Allow
          processing of a multiple camera rig in the block
          adjustment. Assign a value of 1 to use the rigCamera module or a value
          of 0 to not use the rigCamera module. If a value of 1 is assigned, the
          relationship of multiple cameras in the adjustment will be computed.
          The default is 0.
      location_accuracy {String}:
          Specifies the geometric accuracy level of the images.This parameter is
          only enabled if the transformation_type parameter is
          specified as RPC.HIGH-The accuracy will be 30 meters or
          less.MEDIUM-The accuracy will
          be between 31 meters and 100 meters.LOW-The accuracy will be more than
          100 meters.VERY_HIGH-The imagery was collected with a high-accuracy,
          differential
          GPS, such as RTK or PPK. This option will keep image locations fixed
          during block adjustment.If LOW is specified, the control points will
          first be improved by an
          initial triangulation; then they will be used in the block adjustment
          calculation. The medium and high accuracy options do not require
          additional estimation processing.
      DEM {Raster Dataset / Raster Layer / Mosaic Dataset / Mosaic Layer}:
          An input DEM from which elevations will be sampled as ground control
          points for refining the geometric accuracy of the image network in the
          adjustment.This parameter is only enabled when the transformation_type
          parameter
          is specified as Frame.
      elevation_accuracy {Double}:
          The elevation accuracy of the input DEM. The accuracy value will be
          used as a weight for the sampled ground control points in the
          adjustment.This parameter is only enabled when the transformation_type
          parameter
          is specified as Frame.

     OUTPUTS:
      out_solution_table (Table):
          The output solution table containing the adjustments.
      out_solution_point_table {Feature Class}:
          The output solution points table. This will be saved as a polygon
          feature class. This output can be quite large.
      out_quality_table {Table}:
          An output table used to store adjustment quality information.This
          parameter is only enabled if the transformation_type parameter is
          specified as RPC.

        """