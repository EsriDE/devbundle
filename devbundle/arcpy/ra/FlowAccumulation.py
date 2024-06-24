# Generated documentation for module arcpy.ra


class FlowAccumulation(object):
    """
    Creates a raster of accumulated flow into each cell.
    """

    @property
    def description(self) -> str:
        return """

        FlowAccumulation_ra(inputFlowDirectionRaster, outputName, {inputWeightRaster}, {dataType}, {flowDirectionType})

        Creates a raster of accumulated flow into each cell.

     INPUTS:
      inputFlowDirectionRaster (Image Service / Raster Layer / String):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the D8, MFD, or DINF
          method. Use the flowDirectionType parameter to specify the method used
          when the flow direction raster was created.
      outputName (String):
          The name of the output flow accumulation raster service.The default
          name is based on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      inputWeightRaster {Image Service / Raster Layer / String}:
          An optional integer input raster for applying a weight to each cell.
      dataType {String}:
          The output accumulation raster can be integer, floating or double
          type.FLOAT-The output raster will be floating point type. This is the
          default.INTEGER-The output raster will be integer type.DOUBLE-The
          output raster will be double type.
      flowDirectionType {String}:
          Specifies the input flow direction raster type.D8-The input flow
          direction raster is of type D8. This is the
          default.MFD-The input flow direction raster is of type Multi Flow
          Direction
          (MFD).DINF-The input flow direction raster is of type D-Infinity
          (DINF).

        """