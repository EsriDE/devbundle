# Generated documentation for module arcpy.ra


class FlowDirection(object):
    """
    Calculates the direction of flow from each cell to its downslope neighbor or neighbors using the D8, D-Infinity (DINF), or Multiple Flow Direction (MFD) method.
    """

    @property
    def description(self) -> str:
        return """

        FlowDirection_ra(inputSurfaceRaster, outputFlowDirectionName, {forceFlow}, {flowDirectionType}, {outputDropName})

        Calculates the direction of flow from each cell to its downslope
        neighbor or neighbors using the D8, D-Infinity (DINF), or Multiple
        Flow Direction (MFD) method.

     INPUTS:
      inputSurfaceRaster (Image Service / Raster Layer / String):
          The input raster representing a continuous surface.
      outputFlowDirectionName (String):
          The name of the output flow direction raster service.The default name
          is based on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      forceFlow {Boolean}:
          Keywords defining if NoData values in the input raster are allowed to
          nibble into the area defined by the mask raster.NORMAL-If the maximum
          drop on the inside of an edge cell is greater
          than zero, the flow direction will be determined as usual; otherwise,
          the flow direction will be toward the edge. Cells that should flow
          from the edge of the surface raster inward will do so. This is the
          default.FORCE-All cells at the edge of the surface raster will flow
          outward
          from the surface raster.
      flowDirectionType {String}:
          Specifies the type of flow method to use while computing flow
          directions.D8-Assign a flow direction based on the D8 flow method.
          This method
          assigns flow direction to the steepest downslope neighbor. This is the
          default.MFD-Assign a flow direction based on the MFD flow method. This
          method
          assigns multiple flow directions towards all downslope
          neighbors.DINF-Assign a flow direction based on the D-Infinity flow
          method using
          the steepest slope of a triangular facet.
      outputDropName {String}:
          The name of the output drop raster service.The default name is based
          on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.

        """