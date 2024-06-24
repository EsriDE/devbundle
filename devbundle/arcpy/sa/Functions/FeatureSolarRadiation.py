# Generated documentation for module arcpy.sa.Functions


class FeatureSolarRadiation(object):
    """
    Calculates the incoming solar insolation for input points or polygon features relative to the surface (ground) on Earth or the Moon.
    """

    @property
    def description(self) -> str:
        return """

        FeatureSolarRadiation_sa(in_surface_raster, in_features, unique_id_field, out_table, start_date_time, end_date_time, {time_zone}, {adjust_DST}, {use_time_interval}, {interval_unit}, {interval}, {feature_offset}, {feature_area}, {feature_slope}, {feature_aspect}, {neighborhood_distance}, {use_adaptive_neighborhood}, {diffuse_model_type}, {diffuse_proportion}, {transmittivity}, {analysis_target_device}, {out_join_layer}, {sunmap_grid_level})

        Calculates the incoming solar insolation for input points or polygon
        features relative to the surface (ground) on Earth or the Moon.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input elevation surface raster.
      in_features (Composite Geodataset):
          The input features (point or polygon) that represent a location or
          engineered surface to calculate the amount of solar radiation
          received.
      unique_id_field (Field):
          The field that contains the values that define each feature.It can be
          an integer or a string field of the input features.
      start_date_time (Date):
          The start date and time for the analysis.
      end_date_time (Date):
          The end date and time for the analysis.
      time_zone {String}:
          The time zone that will be used for the start and end time. The
          default is coordinated universal time (UTC).UTC-The time zone will be
          UTC.Dateline_Standard_Time-The time zone
          will be Dateline Standard Time
          (UTC-12:00).UTC-11-The time zone will be UTC-11
          (UTC-11:00).Aleutian_Standard_Time-The time zone will be Aleutian
          Standard Time
          (UTC-10:00).Hawaiian_Standard_Time-The time zone will be Hawaiian
          Standard Time
          (UTC-10:00).Marquesas_Standard_Time-The time zone will be Marquesas
          Standard Time
          (UTC-09:30).Alaskan_Standard_Time-The time zone will be Alaskan
          Standard Time
          (UTC-09:00).UTC-09-The time zone will be UTC-09
          (UTC-09:00).Pacific_Standard_Time_(Mexico)-The time zone will be
          Pacific Standard
          Time (Mexico) (UTC-08:00).UTC-08-The time zone will be UTC-08
          (UTC-08:00).Pacific_Standard_Time-The time zone will be Pacific
          Standard Time
          (UTC-08:00).US_Mountain_Standard_Time-The time zone will be US
          Mountain Standard
          Time (UTC-07:00).Mountain_Standard_Time_(Mexico)-The time zone will be
          Mountain
          Standard Time (Mexico) (UTC-07:00).Mountain_Standard_Time-The time
          zone will be Mountain Standard Time
          (UTC-07:00).Yukon_Standard_Time-The time zone will be Yukon Standard
          Time
          (UTC-07:00).Central_America_Standard_Time-The time zone will be
          Central America
          Standard Time (UTC-06:00).Central_Standard_Time-The time zone will be
          Central Standard Time
          (UTC-06:00).Easter_Island_Standard_Time-The time zone will be Easter
          Island
          Standard Time (UTC-06:00).Central_Standard_Time_(Mexico)-The time zone
          will be Central Standard
          Time (Mexico) (UTC-06:00).Canada_Central_Standard_Time-The time zone
          will be Canada Central
          Standard Time (UTC-06:00).SA_Pacific_Standard_Time-The time zone will
          be SA Pacific Standard
          Time (UTC-05:00).Eastern_Standard_Time_(Mexico)-The time zone will be
          Eastern Standard
          Time (Mexico) (UTC-05:00).Eastern_Standard_Time-The time zone will be
          Eastern Standard Time
          (UTC-05:00).Haiti_Standard_Time-The time zone will be Haiti Standard
          Time
          (UTC-05:00).Cuba_Standard_Time-The time zone will be Cuba Standard
          Time
          (UTC-05:00).US_Eastern_Standard_Time-The time zone will be US Eastern
          Standard
          Time (UTC-05:00).Turks_And_Caicos_Standard_Time-The time zone will be
          Turks And Caicos
          Standard Time (UTC-04:00).Paraguay_Standard_Time-The time zone will be
          Paraguay Standard Time
          (UTC-04:00).Atlantic_Standard_Time-The time zone will be Atlantic
          Standard Time
          (UTC-04:00).Venezuela_Standard_Time-The time zone will be Venezuela
          Standard Time
          (UTC-04:00).Central_Brazilian_Standard_Time-The time zone will be
          Central
          Brazilian Standard Time (UTC-04:00).SA_Western_Standard_Time-The time
          zone will be SA Western Standard
          Time (UTC-04:00).Pacific_SA_Standard_Time-The time zone will be
          Pacific SA Standard
          Time (UTC-04:00).Newfoundland_Standard_Time-The time zone will be
          Newfoundland Standard
          Time (UTC-03:30).Tocantins_Standard_Time-The time zone will be
          Tocantins Standard Time
          (UTC-03:00).E._South_America_Standard_Time-The time zone will be E.
          South America
          Standard Time (UTC-03:00).SA_Eastern_Standard_Time-The time zone will
          be SA Eastern Standard
          Time (UTC-03:00).Argentina_Standard_Time-The time zone will be
          Argentina Standard Time
          (UTC-03:00).Greenland_Standard_Time-The time zone will be Greenland
          Standard Time
          (UTC-03:00).Montevideo_Standard_Time-The time zone will be Montevideo
          Standard
          Time (UTC-03:00).Magallanes_Standard_Time-The time zone will be
          Magallanes Standard
          Time (UTC-03:00).Saint_Pierre_Standard_Time-The time zone will be
          Saint Pierre Standard
          Time (UTC-03:00).Bahia_Standard_Time-The time zone will be Bahia
          Standard Time
          (UTC-03:00).UTC-02-The time zone will be UTC-02 (UTC-02:00).Mid-
          Atlantic_Standard_Time-The time zone will be Mid-Atlantic Standard
          Time (UTC-02:00).Azores_Standard_Time-The time zone will be Azores
          Standard Time
          (UTC-01:00).Cape_Verde_Standard_Time-The time zone will be Cape Verde
          Standard
          Time (UTC-01:00).GMT_Standard_Time-The time zone will be GMT Standard
          Time (UTC+00:00).Greenwich_Standard_Time-The time zone will be
          Greenwich Standard Time
          (UTC+00:00).Sao_Tome_Standard_Time-The time zone will be Sao Tome
          Standard Time
          (UTC+00:00).Morocco_Standard_Time-The time zone will be Morocco
          Standard Time
          (UTC+00:00).W._Europe_Standard_Time-The time zone will be W. Europe
          Standard Time
          (UTC+01:00).Central_Europe_Standard_Time-The time zone will be Central
          Europe
          Standard Time (UTC+01:00).Romance_Standard_Time-The time zone will be
          Romance Standard Time
          (UTC+01:00).Central_European_Standard_Time-The time zone will be
          Central European
          Standard Time (UTC+01:00).W._Central_Africa_Standard_Time-The time
          zone will be W. Central
          Africa Standard Time (UTC+01:00).Jordan_Standard_Time-The time zone
          will be Jordan Standard Time
          (UTC+02:00).GTB_Standard_Time-The time zone will be GTB Standard Time
          (UTC+02:00).Middle_East_Standard_Time-The time zone will be Middle
          East Standard
          Time (UTC+02:00).Egypt_Standard_Time-The time zone will be Egypt
          Standard Time
          (UTC+02:00).E._Europe_Standard_Time-The time zone will be E. Europe
          Standard Time
          (UTC+02:00).Syria_Standard_Time-The time zone will be Syria Standard
          Time
          (UTC+02:00).West_Bank_Standard_Time-The time zone will be West Bank
          Standard Time
          (UTC+02:00).South_Africa_Standard_Time-The time zone will be South
          Africa Standard
          Time (UTC+02:00).FLE_Standard_Time-The time zone will be FLE Standard
          Time (UTC+02:00).Israel_Standard_Time-The time zone will be Israel
          Standard
          (UTC+02:00).South_Sudan_Standard_Time-The time zone will be South
          Sudan Standard
          Time (UTC+02:00).Kaliningrad_Standard_Time-The time zone will be
          Kaliningrad Standard
          Time (UTC+02:00).Sudan_Standard_Time-The time zone will be Sudan
          Standard Time
          (UTC+02:00).Libya_Standard_Time-The time zone will be Libya Standard
          Time
          (UTC+02:00).Namibia_Standard_Time-The time zone will be Namibia
          Standard Time
          (UTC+02:00).Arabic_Standard_Time-The time zone will be Arabic Standard
          Time
          (UTC+03:00).Turkey_Standard_Time-The time zone will be Turkey Standard
          Time
          (UTC+03:00).Arab_Standard_Time-The time zone will be Arab Standard
          Time
          (UTC+03:00).Belarus_Standard_Time-The time zone will be Belarus
          Standard Time
          (UTC+03:00).Russian_Standard_Time-The time zone will be Russian
          Standard Time
          (UTC+03:00).E._Africa_Standard_Time-The time zone will be E. Africa
          Standard Time
          (UTC+03:00).Volgograd_Standard_Time-The time zone will be Volgograd
          Standard Time
          (UTC+03:00).Iran_Standard_Time-The time zone will be Iran Standard
          Time
          (UTC+03:30).Arabian_Standard_Time-The time zone will be Arabian
          Standard Time
          (UTC+04:00).Astrakhan_Standard_Time-The time zone will be Astrakhan
          Standard Time
          (UTC+04:00).Azerbaijan_Standard_Time-The time zone will be Azerbaijan
          Standard
          Time (UTC+04:00).Russia_Time_Zone_3-The time zone will be Russia Time
          Zone 3
          (UTC+04:00).Mauritius_Standard_Time-The time zone will be Mauritius
          Standard Time
          (UTC+04:00).Saratov_Standard_Time-The time zone will be Saratov
          Standard Time
          (UTC+04:00).Georgian_Standard_Time-The time zone will be Georgian
          Standard Time
          (UTC+04:00).Caucasus_Standard_Time-The time zone will be Caucasus
          Standard Time
          (UTC+04:00).Afghanistan_Standard_Time-The time zone will be
          Afghanistan Standard
          Time (UTC+04:30).West_Asia_Standard_Time-The time zone will be West
          Asia Standard Time
          (UTC+05:00).Ekaterinburg_Standard_Time-The time zone will be
          Ekaterinburg Standard
          Time (UTC+05:00).Pakistan_Standard_Time-The time zone will be Pakistan
          Standard Time
          (UTC+05:00).Qyzylorda_Standard_Time-The time zone will be Qyzylorda
          Standard Time
          (UTC+05:00).India_Standard_Time-The time zone will be India Standard
          Time
          (UTC+05:30).Sri_Lanka_Standard_Time-The time zone will be Sri Lanka
          Standard Time
          (UTC+05:30).Nepal_Standard_Time-The time zone will be Nepal Standard
          Time
          (UTC+05:45).Central_Asia_Standard_Time-The time zone will be Central
          Asia Standard
          Time (UTC+06:00).Bangladesh_Standard_Time-The time zone will be
          Bangladesh Standard
          Time (UTC+06:00).Omsk_Standard_Time-The time zone will be Omsk
          Standard Time
          (UTC+06:00).Myanmar_Standard_Time-The time zone will be Myanmar
          Standard Time
          (UTC+06:30).SE_Asia_Standard_Time-The time zone will be SE Asia
          Standard Time
          (UTC+07:00).Altai_Standard_Time-The time zone will be Altai Standard
          Time
          (UTC+07:00).W._Mongolia_Standard_Time-The time zone will be W.
          Mongolia Standard
          Time (UTC+07:00).North_Asia_Standard_Time-The time zone will be North
          Asia Standard
          Time (UTC+07:00).N._Central_Asia_Standard_Time-The time zone will be
          N. Central Asia
          Standard Time (UTC+07:00).Tomsk_Standard_Time-The time zone will be
          Tomsk Standard Time
          (UTC+07:00).China_Standard_Time-The time zone will be China Standard
          Time
          (UTC+08:00).North_Asia_East_Standard_Time-The time zone will be North
          Asia East
          Standard Time (UTC+08:00).Singapore_Standard_Time-The time zone will
          be Singapore Standard Time
          (UTC+08:00).W._Australia_Standard_Time-The time zone will be W.
          Australia Standard
          Time (UTC+08:00).Taipei_Standard_Time-The time zone will be Taipei
          Standard Time
          (UTC+08:00).Ulaanbaatar_Standard_Time-The time zone will be
          Ulaanbaatar Standard
          Time (UTC+08:00).Aus_Central_W._Standard_Time-The time zone will be
          Aus Central W.
          Standard Time (UTC+08:45).Transbaikal_Standard_Time-The time zone will
          be Transbaikal Standard
          Time (UTC+09:00).Tokyo_Standard_Time-The time zone will be Tokyo
          Standard Time
          (UTC+09:00).North_Korea_Standard_Time-The time zone will be North
          Korea Standard
          Time (UTC+09:00).Korea_Standard_Time-The time zone will be Korea
          Standard Time
          (UTC+09:00).Yakutsk_Standard_Time-The time zone will be Yakutsk
          Standard Time
          (UTC+09:00).Cen._Australia_Standard_Time-The time zone will be Cen.
          Australia
          Standard Time (UTC+09:30).AUS_Central_Standard_Time-The time zone will
          be AUS Central Standard
          Time (UTC+09:30).E._Australia_Standard_Time-The time zone will be E.
          Australia Standard
          Time (UTC+10:00).AUS_Eastern_Standard_Time-The time zone will be AUS
          Eastern Standard
          Time (UTC+10:00).West_Pacific_Standard_Time-The time zone will be West
          Pacific Standard
          Time (UTC+10:00).Tasmania_Standard_Time-The time zone will be Tasmania
          Standard Time
          (UTC+10:00).Vladivostok_Standard_Time-The time zone will be
          Vladivostok Standard
          Time (UTC+10:00).Lord_Howe_Standard_Time-The time zone will be Lord
          Howe Standard Time
          (UTC+10:30).Bougainville_Standard_Time-The time zone will be
          Bougainville Standard
          Time (UTC+11:00).Russia_Time_Zone_10-The time zone will be Russia Time
          Zone 10
          (UTC+11:00).Magadan_Standard_Time-The time zone will be Magadan
          Standard Time
          (UTC+11:00).Norfolk_Standard_Time-The time zone will be Norfolk
          Standard Time
          (UTC+11:00).Sakhalin_Standard_Time-The time zone will be Sakhalin
          Standard Time
          (UTC+11:00).Central_Pacific_Standard_Time-The time zone will be
          Central Pacific
          Standard Time (UTC+11:00).Russia_Time_Zone_11-The time zone will be
          Russia Time Zone 11
          (UTC+11:00).New_Zealand_Standard_Time-The time zone will be New
          Zealand Standard
          Time (UTC+12:00).UTC+12-The time zone will be UTC+12
          (UTC+12:00).Fiji_Standard_Time-The time zone will be Fiji Standard
          Time
          (UTC+12:00).Kamchatka_Standard_Time-The time zone will be Kamchatka
          Standard Time
          (UTC+12:00).Chatham_Islands_Standard_Time-The time zone will be
          Chatham Islands
          Standard Time (UTC+12:45).UTC+13-The time zone will be UTC+13
          (UTC+13:00).Tonga_Standard_Time-The time zone will be Tonga Standard
          Time
          (UTC+13:00).Samoa_Standard_Time-The time zone will be Samoa Standard
          Time
          (UTC+13:00).Line_Islands_Standard_Time-The time zone will be Line
          Islands Standard
          Time (UTC+14:00).
      adjust_DST {Boolean}:
          Specifies whether the input time configuration will be adjusted for
          daylight saving time.This parameter is not applicable for analysis on
          the Moon.NOT_ADJUSTED_FOR_DST-The input time values will not be
          adjusted for
          daylight saving time. This is the default.ADJUSTED_FOR_DST-The input
          time values will be adjusted for daylight
          saving time.
      use_time_interval {Boolean}:
          Specifies whether a single total insolation value will be calculated
          for the entire time configuration or multiple radiation values will be
          calculated for the specified interval.NO_INTERVAL-A single radiation
          value will be calculated for the entire
          time configuration. This is default.INTERVAL-Multiple radiation values
          will be calculated for each time
          interval over the entire time configuration.
      interval_unit {String}:
          Specifies the time unit that will be used for calculating solar
          radiation values over the entire time configuration.This parameter is
          only supported when the use_time_interval parameter
          is set to INTERVAL.MINUTE-The interval unit will be minutes. This
          option is only
          available for Earth-based data.HOUR-The interval unit will be
          hours.DAY-The interval unit will be days. This is the defaultWEEK-The
          interval unit will be weeks.
      interval {Long}:
          The value of the duration or time between intervals.The default value
          is dependent on the interval unit specified. The
          default value for each of the available units are listed
          below.MINUTE-60HOUR-4DAY-14WEEK-2
      feature_offset {Double / Field}:
          A vertical distance that will be added to the raster surface for
          analysis. It must be a positive integer or floating-point value.You
          can select a field from the input features dataset, or you can
          provide a numerical value.For example, if the object is a panel,
          provide the height of the
          panel.If a value is provided for this parameter, that value will be
          used by
          all features. To specify different values for each individual feature,
          select a field from the input features dataset.The default value is 0.
      feature_area {Double / Field}:
          The area associated with the input features. It must be a positive
          integer or floating-point value.You can select a field from the input
          features dataset, or you can
          provide a numerical value.For example, if the object is a panel,
          provide the area of the panel.If a value is provided for this
          parameter, that value will be used by
          all features. To specify different values for each individual feature,
          select a field from the input features dataset.By default, the area is
          obtained from the input features. For point
          features, the default area is 0.
      feature_slope {Double / Field}:
          The relative slope or incline associated with the input features. It
          must be a positive integer or floating-point value.You can select a
          field from the input features dataset, or you can
          provide a numerical value.For example, if the object is a panel,
          provide the incline of the
          panel.If a value is provided for this parameter, that value will be
          used by
          all features. To specify different values for each individual feature,
          select a field from the input features dataset.Slope is expressed in
          degrees from 0 to 90. The default values for
          analysis are calculated from the underlying values of the input
          surface raster.
      feature_aspect {Double / Field}:
          The relative aspect or direction associated with the input features.
          It must be a positive integer or floating-point value.You can select a
          field from the input features dataset, or you can
          provide a numerical value.For example, if the object is a panel,
          provide the direction of the
          panel face.If a value is provided for this parameter, that value will
          be used by
          all features. To specify different values for each individual feature,
          select a field from the input features dataset.Aspect is expressed in
          degrees from 0 to 360. The default values for
          analysis area calculated from the underlying values of the input
          surface raster.
      neighborhood_distance {Linear Unit}:
          The distance from the target cell center for which the output
          insolation value will be calculated. It determines the size of the
          neighborhood.The default value is the input surface raster cell size,
          resulting in
          a 3 by 3 neighborhood.
      use_adaptive_neighborhood {Boolean}:
          Specifies whether neighborhood distance will vary with landscape
          changes (adaptive). The maximum distance is determined by the
          neighborhood distance. The minimum distance is the input raster cell
          size.FIXED_NEIGHBORHOOD-A single (fixed) neighborhood distance will be
          used
          at all locations. This is the default.ADAPTIVE_NEIGHBORHOOD-An
          adaptive neighborhood distance will be used
          at all locations.
      diffuse_model_type {String}:
          Specifies the type of diffuse radiation model that will be
          used.UNIFORM_SKY-The uniform diffuse model will be used. The incoming
          diffuse radiation is the same from all sky directions. This is the
          default.STANDARD_OVERCAST_SKY-The standard overcast diffuse model will
          be
          used. The incoming diffuse radiation flux varies with the zenith
          angle.
      diffuse_proportion {Double}:
          The proportion of global normal radiation flux that is diffuse. Values
          range from 0 to 1.Set this value according to atmospheric conditions.
          The default value
          is 0.3 for generally clear sky conditions.
      transmittivity {Double}:
          The fraction of radiation that passes through the atmosphere (averaged
          overall wavelengths). Values range from 0 (no transmission) to 1 (all
          transmission).The default is 0.5 for a generally clear sky.
      analysis_target_device {String}:
          Specifies the device that will be used to perform the
          calculation.GPU_THEN_CPU-If a compatible GPU is found, it will be used
          to perform
          the calculation. Otherwise, the CPU will be used. This is the
          default.CPU_ONLY-The calculation will only be performed on the
          CPU.GPU_ONLY-The calculation will only be performed on the GPU.
      sunmap_grid_level {Long}:
          The resolution that will be used to generate the H3 hexagonal grid
          cells used for internal calculations. A lower grid level value creates
          fewer, larger sun map areas and decreases tool run time. A higher grid
          level creates more smaller sun maps improving the accuracy of the
          result.Valid values of the sun map grid level for Earth range from 5
          to 7.
          For the Moon, the valid value range is from 4 to 6.By default, the
          grid level is determined by the input surface raster.
          When analyzing surface data on Earth, if the analysis cell size is
          less than or equal to 4 meters, the default grid level is 6. If the
          analysis cell size is greater than 4 meters, the default grid level is
          5. For analyzing surface data on the Moon, the default grid level is
          6.

     OUTPUTS:
      out_table (Table):
          The output table that will contain the summary of the amount of solar
          radiation received by the input featuresThe format of the table is
          determined by the output location and path.
          By default, the output will be a geodatabase table if in a geodatabase
          workspace, or a dBASE table if in a file workspace.
      out_join_layer {Feature Layer}:
          The output layer that will be created by joining the output table to
          the input feature class. This is an optional output.

        """