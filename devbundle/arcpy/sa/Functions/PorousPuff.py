# Generated documentation for module arcpy.sa.Functions


class PorousPuff(object):
    """
    Calculates the time-dependent, two-dimensional concentration distribution in mass per volume of a solute introduced instantaneously and at a discrete point into a vertically mixed aquifer.
    """

    @property
    def description(self) -> str:
        return """

        PorousPuff_sa(in_track_file, in_porosity_raster, in_thickness_raster, mass, {dispersion_time}, {longitudinal_dispersivity}, {dispersivity_ratio}, {retardation_factor}, {decay_coefficient})

        Calculates the time-dependent, two-dimensional concentration
        distribution in mass per volume of a solute introduced instantaneously
        and at a discrete point into a vertically mixed aquifer.

     INPUTS:
      in_track_file (File):
          The input particle track path file.This is an ASCII text file
          containing information about the position,
          the local velocity vector, and the cumulative length and time of
          travel along the path.This file is generated using the Particle Track
          tool.
      in_porosity_raster (Composite Geodataset):
          The input raster where each cell value represents the effective
          formation porosity at that location.
      in_thickness_raster (Composite Geodataset):
          The input raster where each cell value represents the saturated
          thickness at that location.The value for the thickness is interpreted
          from geological properties
          of the aquifer.
      mass (Double):
          A value for the amount of mass released instantaneously at the source
          point, in units of mass.
      dispersion_time {Double}:
          A value representing the time horizon for dispersion of the solute, in
          units of time.The time must be less than or equal to the maximum time
          in the track
          file. If the requested time exceeds the available time from the track
          file, the tool is aborted. The default time is the latest time
          (corresponding to the terminal point) in the track file.
      longitudinal_dispersivity {Double}:
          A value representing the dispersivity parallel to the flow
          direction.For details on how the default value is determined, and how
          it relates
          to the scale of the study, see the How Porous Puff works section in
          the documentation.
      dispersivity_ratio {Double}:
          A value representing the ratio of longitudinal dispersivity over
          transverse dispersivity.Transverse dispersivity is perpendicular to
          the flow direction in the
          same horizontal plane. The default value is three.
      retardation_factor {Double}:
          A dimensionless value representing the retardation of the solute in
          the aquifer.Retardation varies between one and infinity, with one
          corresponding to
          no retardation. The default value is one.
      decay_coefficient {Double}:
          Decay coefficient for solutes undergoing first-order exponential decay
          (for example, radionuclides) in units of inverse time.The default is
          zero, corresponding to no decay.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster of the concentration distribution.Each cell value
          represents the concentration at that location.

        """