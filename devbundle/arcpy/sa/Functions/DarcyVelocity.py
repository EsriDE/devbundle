# Generated documentation for module arcpy.sa.Functions


class DarcyVelocity(object):
    """
    Calculates the groundwater seepage velocity vector (direction and magnitude) for steady flow in an aquifer.
    """

    @property
    def description(self) -> str:
        return """

        DarcyVelocity_sa(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster)

        Calculates the groundwater seepage velocity vector (direction and
        magnitude) for steady flow in an aquifer.

     INPUTS:
      in_head_raster (Composite Geodataset):
          The input raster where each cell value represents the groundwater head
          elevation at that location.The head is typically an elevation above
          some datum, such as mean sea
          level.
      in_porosity_raster (Composite Geodataset):
          The input raster where each cell value represents the effective
          formation porosity at that location.
      in_thickness_raster (Composite Geodataset):
          The input raster where each cell value represents the saturated
          thickness at that location.The value for the thickness is interpreted
          from geological properties
          of the aquifer.
      in_transmissivity_raster (Composite Geodataset):
          The input raster where each cell value represents the formation
          transmissivity at that location.The transmissivity of an aquifer is
          defined as the hydraulic
          conductivity K times the saturated aquifer thickness b, as units of
          length squared over time. This property is generally estimated from
          field experimental data such as pumping tests. Tables 1 and 2 in How
          Darcy Flow and Darcy Velocity work list ranges of hydraulic
          conductivities for some generalized geologic materials.

     OUTPUTS:
      out_direction_raster (Raster Dataset):
          The output flow direction raster.Each cell value represents the
          direction of the seepage velocity
          vector (average linear velocity) at the center of the cell, calculated
          as the average value of the seepage velocity through the four faces of
          the cell.It is used with the output magnitude raster to describe the
          flow
          vector.
      out_magnitude_raster (Raster Dataset):
          The output flow direction raster.Each cell value represents the
          direction of the seepage velocity
          vector (average linear velocity) at the center of the cell, calculated
          as the average value of the seepage velocity through the four faces of
          the cell.It is used with the output magnitude raster to describe the
          flow
          vector.

        """