#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Addresses:
    """
    This class stores all accessible addresses from the Next devices
    """
    def __init__(self, offset):
        self.version_major = 10
        self.version_minor = 137

        self.deviceAddressDefault = offset + 1
        self.device_address_system = offset + 1
        self.device_address_battery = offset + 2
        self.device_address_acsource = offset + 7
        self.device_address_acflexload = offset + 9
        self.device_address_next3 = offset + 14
        self.device_address_next1 = offset + 29
        self.device_address_nextgateway = offset + 59
        self.device_address_powermeters = offset + 89
        self.device_address_last_valid_address = offset + self.device_address_powermeters + 5

        # Group System Modbus Address
        # Object EarthingScheme Modbus Address
        self.system_earthingscheme_start_address = 1200
        self.system_earthingscheme_earthingmodeselection = self.system_earthingscheme_start_address + 0                 # Property ID: 0, [-] (enum). Selection of the earthing mode.
        self.system_earthingscheme_disablecheck = self.system_earthingscheme_start_address + 2                          # Property ID: 1, [-] (bool). Disable the continuity and discontinuity check during on-grid and off-grid transition.
        self.system_earthingscheme_isearthingmaster = self.system_earthingscheme_start_address + 3                      # Property ID: 2, [-] (bool). True if this device is the earthing manager master.
        self.system_earthingscheme_relayisclosed = self.system_earthingscheme_start_address + 4                         # Property ID: 3, [-] (bool). True if the actual state of the earthing relay is closed.
        self.system_earthingscheme_earthingerrors = self.system_earthingscheme_start_address + 5                        # Property ID: 4, [-] (bitfield). Current earthing manager errors.
        self.system_earthingscheme_earthingwarnings = self.system_earthingscheme_start_address + 18                     # Property ID: 14, [-] (bitfield). Current earthing manager warnings.
        self.system_earthingscheme_discontinuitycheckokcnt = self.system_earthingscheme_start_address + 20              # Property ID: 15, [ms] (int). Total time where the discontinuity test has succeeded
        self.system_earthingscheme_discontinuitychecknokcnt = self.system_earthingscheme_start_address + 22             # Property ID: 16, [ms] (int). Total time where the discontinuity test has failed

        # Object EnergyPolicy Modbus Address
        self.system_energypolicy_start_address = 1800
        self.system_energypolicy_acsourcepriority = self.system_energypolicy_start_address + 0                          # Property ID: 0, [-] (enum). When several AC sources exists, the one that will be used is determined according to this setting.
        self.system_energypolicy_currentlyactiveacsourceindex = self.system_energypolicy_start_address + 2              # Property ID: 1, [-] (int). Currently active AC source index.

        # Object Installation Modbus Address
        self.system_installation_start_address = 2100
        self.system_installation_guid = self.system_installation_start_address + 3                                      # Property ID: 2, [-] (char[36]). The GUID of this installation.
        self.system_installation_datetimeinternetupdate = self.system_installation_start_address + 21                   # Property ID: 3, [-] (bool). Automatic date/time internet update. When available, internet date/time will be used to set installation date/time.
        self.system_installation_country = self.system_installation_start_address + 22                                  # Property ID: 4, [-] (int). Country of this installation.
        self.system_installation_timezone = self.system_installation_start_address + 24                                 # Property ID: 5, [-] (char[50]). Time zone of this installation (IANA ID).

        # Object AllDevices Modbus Address
        self.system_alldevices_start_address = 2400
        self.system_alldevices_buzzersenabled = self.system_alldevices_start_address + 3                                # Property ID: 2, [-] (bool). Indicates all buzzers state. If disabled, buzzers don't beep when the led panel central red light is blinking.
        self.system_alldevices_frontpanelbuttonsenabled = self.system_alldevices_start_address + 4                      # Property ID: 3, [-] (bool). Indicates all front panel buttons state. If disabled, pressing on the front panel buttons has no effect.
        self.system_alldevices_nbrofcmdentries = self.system_alldevices_start_address + 5                               # Property ID: 4, [-] (int). Total number of command inputs in the system.
        self.system_alldevices_nbrofrelevantdevices = self.system_alldevices_start_address + 7                          # Property ID: 5, [-] (uint). Number of power electronics devices.
        self.system_alldevices_nbrofnext3 = self.system_alldevices_start_address + 9                                    # Property ID: 6, [-] (uint). Current next3 devices.
        self.system_alldevices_next3status = self.system_alldevices_start_address + 11                                  # Property ID: 7, [-] (bitfield). Current Next3 status.
        self.system_alldevices_nbrofnext1 = self.system_alldevices_start_address + 13                                   # Property ID: 8, [-] (uint). Number of next1 devices.
        self.system_alldevices_next1status = self.system_alldevices_start_address + 15                                  # Property ID: 9, [-] (bitfield). Current Next1 status.

        # Object TriPhaseInverter Modbus Address
        self.system_triphaseinverter_start_address = 2700
        self.system_triphaseinverter_turnonallphases = self.system_triphaseinverter_start_address + 3                   # Property ID: 2, [-] (signal). Turn on all phases.
        self.system_triphaseinverter_turnoffallphases = self.system_triphaseinverter_start_address + 4                  # Property ID: 3, [-] (signal). Turn off all phases.
        self.system_triphaseinverter_onoffstateallphases = self.system_triphaseinverter_start_address + 5               # Property ID: 4, [-] (bool). Indicates all phases ON/OFF state.
        self.system_triphaseinverter_turnonl1 = self.system_triphaseinverter_start_address + 6                          # Property ID: 5, [-] (signal). Turn on phase L1. Note that \"Allow individual phase operation\" (id 56) must be true to enable L1 individually.
        self.system_triphaseinverter_turnoffl1 = self.system_triphaseinverter_start_address + 7                         # Property ID: 6, [-] (signal). Turn off phase L1.
        self.system_triphaseinverter_onoffstatel1 = self.system_triphaseinverter_start_address + 8                      # Property ID: 7, [-] (bool). Indicates phase L1 ON/OFF state.
        self.system_triphaseinverter_turnonl2 = self.system_triphaseinverter_start_address + 9                          # Property ID: 8, [-] (signal). Turn on phase L2. Note that \"Allow individual phase operation\" (id 56) must be true to enable L2 individually.
        self.system_triphaseinverter_turnoffl2 = self.system_triphaseinverter_start_address + 10                        # Property ID: 9, [-] (signal). Turn off phase L2.
        self.system_triphaseinverter_onoffstatel2 = self.system_triphaseinverter_start_address + 11                     # Property ID: 10, [-] (bool). Indicates phase L2 ON/OFF state.
        self.system_triphaseinverter_turnonl3 = self.system_triphaseinverter_start_address + 12                         # Property ID: 11, [-] (signal). Turn on phase L3. Note that \"Allow individual phase operation\" (id 56) must be true to enable L3 individually.
        self.system_triphaseinverter_turnoffl3 = self.system_triphaseinverter_start_address + 13                        # Property ID: 12, [-] (signal). Turn off phase L3.
        self.system_triphaseinverter_onoffstatel3 = self.system_triphaseinverter_start_address + 14                     # Property ID: 13, [-] (bool). Indicates phase L3 ON/OFF state.
        self.system_triphaseinverter_threephasesystem = self.system_triphaseinverter_start_address + 17                 # Property ID: 15, [-] (enum). 3-phase system configuration.
        self.system_triphaseinverter_linevoltage = self.system_triphaseinverter_start_address + 19                      # Property ID: 16, [V] (float). Nominal line voltage.
        self.system_triphaseinverter_phasevoltagel1 = self.system_triphaseinverter_start_address + 21                   # Property ID: 17, [V] (float). L1 nominal phase voltage (also used for AC input ports nominal voltage).
        self.system_triphaseinverter_phasevoltagel2 = self.system_triphaseinverter_start_address + 23                   # Property ID: 18, [V] (float). L2 nominal phase voltage (also used for AC input ports nominal voltage).
        self.system_triphaseinverter_phasevoltagel3 = self.system_triphaseinverter_start_address + 25                   # Property ID: 19, [V] (float). L3 nominal phase voltage (also used for AC input ports nominal voltage).
        self.system_triphaseinverter_relativeanglel2 = self.system_triphaseinverter_start_address + 27                  # Property ID: 20, [°] (float). L2 voltage phase angle relative to L1.
        self.system_triphaseinverter_relativeanglel3 = self.system_triphaseinverter_start_address + 29                  # Property ID: 21, [°] (float). L3 voltage phase angle relative to L1.
        self.system_triphaseinverter_nominalfrequency = self.system_triphaseinverter_start_address + 31                 # Property ID: 22, [Hz] (float). Nominal frequency.
        self.system_triphaseinverter_rocofmax = self.system_triphaseinverter_start_address + 33                         # Property ID: 23, [Hz/s] (float). Maximal rate of change of frequency.
        self.system_triphaseinverter_alternatefrequency = self.system_triphaseinverter_start_address + 84               # Property ID: 49, [Hz] (float). Alternate frequency. See property \"Cmd entry idx for alternate frequency\" (id 50) for more details.
        self.system_triphaseinverter_cmdentryidxforalternatefrequency = self.system_triphaseinverter_start_address + 86 # Property ID: 50, [-] (int). Index of the command input used to switch to the alternate frequency \"Alternate frequency\" (id 49) (a value of 0 disables remote operation).
        self.system_triphaseinverter_allowpowerproductiononacload = self.system_triphaseinverter_start_address + 88     # Property ID: 51, [-] (bool). Allows power production on ACLoad or FlexLoad ports (e.g. when solar inverter is connected on ACLoad/FlexLoad). If false, a backfeed power dectection causes an error.
        self.system_triphaseinverter_frequencyincreasetolimitacloadproducedpower = self.system_triphaseinverter_start_address + 89    # Property ID: 52, [Hz] (float). When power is produced on ACLoad or FlexLoad port (e.g. when solar inverter is connected on on ACLoad/FlexLoad) and this power can't be absorbed by the system, the frequency must be increased to limit this power.
        self.system_triphaseinverter_standbysensitivity = self.system_triphaseinverter_start_address + 93               # Property ID: 54, [-] (enum). Standby sensitivity.
        self.system_triphaseinverter_standbydetectionratio = self.system_triphaseinverter_start_address + 95            # Property ID: 55, [%] (float). Standby detection expressed in % of nominal power. A negative value disables the standby.
        self.system_triphaseinverter_allowindividualphaseoperation = self.system_triphaseinverter_start_address + 97    # Property ID: 56, [-] (bool). Allow individual phase operation even if another phase is halted or in error state.
        self.system_triphaseinverter_overloadthresholdstage1 = self.system_triphaseinverter_start_address + 98          # Property ID: 57, [%] (float). Voltage threshold stage 1 for overload detection.
        self.system_triphaseinverter_overloadoperatetimestage1 = self.system_triphaseinverter_start_address + 100       # Property ID: 58, [s] (float). Overload operate time stage 1.
        self.system_triphaseinverter_overloadthresholdstage2 = self.system_triphaseinverter_start_address + 102         # Property ID: 59, [%] (float). Voltage threshold stage 2 for overload detection.
        self.system_triphaseinverter_overloadoperatetimestage2 = self.system_triphaseinverter_start_address + 104       # Property ID: 60, [s] (float). Overload operate time stage 2.
        self.system_triphaseinverter_overloadrestartdelay = self.system_triphaseinverter_start_address + 106            # Property ID: 61, [s] (float). Delay before automatic restarting after an overload occurs.
        self.system_triphaseinverter_maxolnbduringobsperiod = self.system_triphaseinverter_start_address + 108          # Property ID: 62, [-] (int). Maximum number of overloads allowed during the defined observation period before stopping.
        self.system_triphaseinverter_overloadobservationperiod = self.system_triphaseinverter_start_address + 110       # Property ID: 63, [s] (int). Observation period for overloads detection.
        self.system_triphaseinverter_errorrestartdelay = self.system_triphaseinverter_start_address + 112               # Property ID: 64, [s] (float). Delay before automatic restarting after an error.
        self.system_triphaseinverter_maxerrorsnbduringobsperiod = self.system_triphaseinverter_start_address + 114      # Property ID: 65, [-] (int). Maximum number of errors allowed during the defined observation period before stopping.
        self.system_triphaseinverter_errorobservationperiod = self.system_triphaseinverter_start_address + 116          # Property ID: 66, [s] (int). Observation period for errors detection.
        self.system_triphaseinverter_insmstrength = self.system_triphaseinverter_start_address + 132                    # Property ID: 74, [-] (float). Strength of inertial smoothing feature (smoothing of transient current of genset, used to improve stability of genset during transients).
        self.system_triphaseinverter_status = self.system_triphaseinverter_start_address + 134                          # Property ID: 75, [-] (bitfield). Contains the current status of the 3-phase inverter. Several values are possible simultaneously.
        self.system_triphaseinverter_phaseexistance = self.system_triphaseinverter_start_address + 136                  # Property ID: 76, [-] (bitfield). Indicates which phase(s) is(are) used for inverters / AC-Loads.

        # Object InverterL1 Modbus Address
        self.system_inverterl1_start_address = 3000
        self.system_inverterl1_status = self.system_inverterl1_start_address + 0                                        # Property ID: 0, [-] (enum). Current status.
        self.system_inverterl1_warnings = self.system_inverterl1_start_address + 2                                      # Property ID: 1, [-] (bitfield). Current warnings.
        self.system_inverterl1_causeoferror = self.system_inverterl1_start_address + 4                                  # Property ID: 2, [-] (bitfield). Indicates the cause of error.

        # Object InverterL2 Modbus Address
        self.system_inverterl2_start_address = 3300
        self.system_inverterl2_status = self.system_inverterl2_start_address + 0                                        # Property ID: 0, [-] (enum). Current status.
        self.system_inverterl2_warnings = self.system_inverterl2_start_address + 2                                      # Property ID: 1, [-] (bitfield). Current warnings.
        self.system_inverterl2_causeoferror = self.system_inverterl2_start_address + 4                                  # Property ID: 2, [-] (bitfield). Indicates the cause of error.

        # Object InverterL3 Modbus Address
        self.system_inverterl3_start_address = 3600
        self.system_inverterl3_status = self.system_inverterl3_start_address + 0                                        # Property ID: 0, [-] (enum). Current status.
        self.system_inverterl3_warnings = self.system_inverterl3_start_address + 2                                      # Property ID: 1, [-] (bitfield). Current warnings.
        self.system_inverterl3_causeoferror = self.system_inverterl3_start_address + 4                                  # Property ID: 2, [-] (bitfield). Indicates the cause of error.

        # Object AcLoadTriPhaseMeasure Modbus Address
        self.system_acloadtriphasemeasure_start_address = 3900
        self.system_acloadtriphasemeasure_frequency = self.system_acloadtriphasemeasure_start_address + 0               # Property ID: 0, [Hz] (float). Frequency measured.
        self.system_acloadtriphasemeasure_linevoltagel1l2 = self.system_acloadtriphasemeasure_start_address + 2         # Property ID: 4, [V] (float). Line voltage L1-L2 measured.
        self.system_acloadtriphasemeasure_linevoltagel2l3 = self.system_acloadtriphasemeasure_start_address + 4         # Property ID: 8, [V] (float). Line voltage L2-L3 measured.
        self.system_acloadtriphasemeasure_linevoltagel3l1 = self.system_acloadtriphasemeasure_start_address + 6         # Property ID: 12, [V] (float). Line voltage L3-L1 measured.
        self.system_acloadtriphasemeasure_totalactivepower = self.system_acloadtriphasemeasure_start_address + 8        # Property ID: 16, [W] (float). Total active power measured.
        self.system_acloadtriphasemeasure_totalapparentpower = self.system_acloadtriphasemeasure_start_address + 10     # Property ID: 20, [VA] (float). Total apparent power measured.
        self.system_acloadtriphasemeasure_anglel2relativetol1 = self.system_acloadtriphasemeasure_start_address + 12    # Property ID: 24, [degree] (float). Angle L2 relative to L1 measured.
        self.system_acloadtriphasemeasure_anglel3relativetol1 = self.system_acloadtriphasemeasure_start_address + 14    # Property ID: 25, [degree] (float). Angle L3 relative to L1 measured.
        self.system_acloadtriphasemeasure_dayconsumedenergy = self.system_acloadtriphasemeasure_start_address + 16      # Property ID: 26, [Wh] (float). Consumed energy of the current day.
        self.system_acloadtriphasemeasure_previousdayconsumedenergy = self.system_acloadtriphasemeasure_start_address + 18    # Property ID: 27, [Wh] (float). Consumed energy of the previous day.
        self.system_acloadtriphasemeasure_resetableconsumedenergy = self.system_acloadtriphasemeasure_start_address + 20    # Property ID: 28, [Wh] (float64). Resetable consumed energy.
        self.system_acloadtriphasemeasure_totalconsumedenergy = self.system_acloadtriphasemeasure_start_address + 24    # Property ID: 29, [Wh] (float64). Total consumed energy.
        self.system_acloadtriphasemeasure_dayproducedenergy = self.system_acloadtriphasemeasure_start_address + 28      # Property ID: 30, [Wh] (float). Produced energy of the current day.
        self.system_acloadtriphasemeasure_previousdayproducedenergy = self.system_acloadtriphasemeasure_start_address + 30    # Property ID: 31, [Wh] (float). Produced energy of the previous day.
        self.system_acloadtriphasemeasure_resetableproducedenergy = self.system_acloadtriphasemeasure_start_address + 32    # Property ID: 32, [Wh] (float64). Resetable produced energy.
        self.system_acloadtriphasemeasure_totalproducedenergy = self.system_acloadtriphasemeasure_start_address + 36    # Property ID: 33, [Wh] (float64). Total produced energy.
        self.system_acloadtriphasemeasure_dayruntime = self.system_acloadtriphasemeasure_start_address + 40             # Property ID: 34, [h] (float). Day runtime measured.
        self.system_acloadtriphasemeasure_totalruntime = self.system_acloadtriphasemeasure_start_address + 42           # Property ID: 35, [h] (float). Total runtime measured.
        self.system_acloadtriphasemeasure_daypeakpower = self.system_acloadtriphasemeasure_start_address + 44           # Property ID: 36, [VA] (float). Peak power of the current day.
        self.system_acloadtriphasemeasure_previousdaypeakpower = self.system_acloadtriphasemeasure_start_address + 46   # Property ID: 37, [VA] (float). Peak power of the previous day.
        self.system_acloadtriphasemeasure_dayminactivepower = self.system_acloadtriphasemeasure_start_address + 48      # Property ID: 38, [W] (float). Minimum active power of the current day.
        self.system_acloadtriphasemeasure_previousdayminactivepower = self.system_acloadtriphasemeasure_start_address + 50    # Property ID: 39, [W] (float). Minimum active power of the previous day.
        self.system_acloadtriphasemeasure_daymaxactivepower = self.system_acloadtriphasemeasure_start_address + 52      # Property ID: 40, [W] (float). Maximum active power of the current day.
        self.system_acloadtriphasemeasure_previousdaymaxactivepower = self.system_acloadtriphasemeasure_start_address + 54    # Property ID: 41, [W] (float). Maximum active power of the previous day.
        self.system_acloadtriphasemeasure_producedactivepower = self.system_acloadtriphasemeasure_start_address + 56    # Property ID: 42, [W] (float). Produced active power measured.
        self.system_acloadtriphasemeasure_consumedactivepower = self.system_acloadtriphasemeasure_start_address + 58    # Property ID: 44, [W] (float). Consumed active power measured.

        # Object AcLoadL1Measure Modbus Address
        self.system_acloadl1measure_start_address = 4200
        self.system_acloadl1measure_phasevoltage = self.system_acloadl1measure_start_address + 0                        # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_acloadl1measure_current = self.system_acloadl1measure_start_address + 2                             # Property ID: 4, [A] (float). Current RMS measured.
        self.system_acloadl1measure_activepower = self.system_acloadl1measure_start_address + 4                         # Property ID: 8, [W] (float). Active power measured.
        self.system_acloadl1measure_reactivepower = self.system_acloadl1measure_start_address + 6                       # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_acloadl1measure_apparentpower = self.system_acloadl1measure_start_address + 8                       # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_acloadl1measure_cosphi = self.system_acloadl1measure_start_address + 10                             # Property ID: 20, [-] (float). Power factor measured.
        self.system_acloadl1measure_daypeakpower = self.system_acloadl1measure_start_address + 12                       # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_acloadl1measure_previousdaypeakpower = self.system_acloadl1measure_start_address + 14               # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_acloadl1measure_dayminactivepower = self.system_acloadl1measure_start_address + 16                  # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_acloadl1measure_previousdayminactivepower = self.system_acloadl1measure_start_address + 18          # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_acloadl1measure_daymaxactivepower = self.system_acloadl1measure_start_address + 20                  # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_acloadl1measure_previousdaymaxactivepower = self.system_acloadl1measure_start_address + 22          # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_acloadl1measure_dayconsumedenergy = self.system_acloadl1measure_start_address + 28                  # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_acloadl1measure_previousdayconsumedenergy = self.system_acloadl1measure_start_address + 30          # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_acloadl1measure_resetableconsumedenergy = self.system_acloadl1measure_start_address + 32            # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_acloadl1measure_totalconsumedenergy = self.system_acloadl1measure_start_address + 36                # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_acloadl1measure_dayproducedenergy = self.system_acloadl1measure_start_address + 40                  # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_acloadl1measure_previousdayproducedenergy = self.system_acloadl1measure_start_address + 42          # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_acloadl1measure_resetableproducedenergy = self.system_acloadl1measure_start_address + 44            # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_acloadl1measure_totalproducedenergy = self.system_acloadl1measure_start_address + 48                # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AcLoadL2Measure Modbus Address
        self.system_acloadl2measure_start_address = 4500
        self.system_acloadl2measure_phasevoltage = self.system_acloadl2measure_start_address + 0                        # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_acloadl2measure_current = self.system_acloadl2measure_start_address + 2                             # Property ID: 4, [A] (float). Current RMS measured.
        self.system_acloadl2measure_activepower = self.system_acloadl2measure_start_address + 4                         # Property ID: 8, [W] (float). Active power measured.
        self.system_acloadl2measure_reactivepower = self.system_acloadl2measure_start_address + 6                       # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_acloadl2measure_apparentpower = self.system_acloadl2measure_start_address + 8                       # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_acloadl2measure_cosphi = self.system_acloadl2measure_start_address + 10                             # Property ID: 20, [-] (float). Power factor measured.
        self.system_acloadl2measure_daypeakpower = self.system_acloadl2measure_start_address + 12                       # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_acloadl2measure_previousdaypeakpower = self.system_acloadl2measure_start_address + 14               # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_acloadl2measure_dayminactivepower = self.system_acloadl2measure_start_address + 16                  # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_acloadl2measure_previousdayminactivepower = self.system_acloadl2measure_start_address + 18          # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_acloadl2measure_daymaxactivepower = self.system_acloadl2measure_start_address + 20                  # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_acloadl2measure_previousdaymaxactivepower = self.system_acloadl2measure_start_address + 22          # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_acloadl2measure_dayconsumedenergy = self.system_acloadl2measure_start_address + 28                  # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_acloadl2measure_previousdayconsumedenergy = self.system_acloadl2measure_start_address + 30          # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_acloadl2measure_resetableconsumedenergy = self.system_acloadl2measure_start_address + 32            # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_acloadl2measure_totalconsumedenergy = self.system_acloadl2measure_start_address + 36                # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_acloadl2measure_dayproducedenergy = self.system_acloadl2measure_start_address + 40                  # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_acloadl2measure_previousdayproducedenergy = self.system_acloadl2measure_start_address + 42          # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_acloadl2measure_resetableproducedenergy = self.system_acloadl2measure_start_address + 44            # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_acloadl2measure_totalproducedenergy = self.system_acloadl2measure_start_address + 48                # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AcLoadL3Measure Modbus Address
        self.system_acloadl3measure_start_address = 4800
        self.system_acloadl3measure_phasevoltage = self.system_acloadl3measure_start_address + 0                        # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_acloadl3measure_current = self.system_acloadl3measure_start_address + 2                             # Property ID: 4, [A] (float). Current RMS measured.
        self.system_acloadl3measure_activepower = self.system_acloadl3measure_start_address + 4                         # Property ID: 8, [W] (float). Active power measured.
        self.system_acloadl3measure_reactivepower = self.system_acloadl3measure_start_address + 6                       # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_acloadl3measure_apparentpower = self.system_acloadl3measure_start_address + 8                       # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_acloadl3measure_cosphi = self.system_acloadl3measure_start_address + 10                             # Property ID: 20, [-] (float). Power factor measured.
        self.system_acloadl3measure_daypeakpower = self.system_acloadl3measure_start_address + 12                       # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_acloadl3measure_previousdaypeakpower = self.system_acloadl3measure_start_address + 14               # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_acloadl3measure_dayminactivepower = self.system_acloadl3measure_start_address + 16                  # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_acloadl3measure_previousdayminactivepower = self.system_acloadl3measure_start_address + 18          # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_acloadl3measure_daymaxactivepower = self.system_acloadl3measure_start_address + 20                  # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_acloadl3measure_previousdaymaxactivepower = self.system_acloadl3measure_start_address + 22          # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_acloadl3measure_dayconsumedenergy = self.system_acloadl3measure_start_address + 28                  # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_acloadl3measure_previousdayconsumedenergy = self.system_acloadl3measure_start_address + 30          # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_acloadl3measure_resetableconsumedenergy = self.system_acloadl3measure_start_address + 32            # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_acloadl3measure_totalconsumedenergy = self.system_acloadl3measure_start_address + 36                # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_acloadl3measure_dayproducedenergy = self.system_acloadl3measure_start_address + 40                  # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_acloadl3measure_previousdayproducedenergy = self.system_acloadl3measure_start_address + 42          # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_acloadl3measure_resetableproducedenergy = self.system_acloadl3measure_start_address + 44            # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_acloadl3measure_totalproducedenergy = self.system_acloadl3measure_start_address + 48                # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AcInvertersTriPhaseMeasure Modbus Address
        self.system_acinverterstriphasemeasure_start_address = 5100
        self.system_acinverterstriphasemeasure_frequency = self.system_acinverterstriphasemeasure_start_address + 0     # Property ID: 0, [Hz] (float). Frequency measured.
        self.system_acinverterstriphasemeasure_linevoltagel1l2 = self.system_acinverterstriphasemeasure_start_address + 2    # Property ID: 4, [V] (float). Line voltage L1-L2 measured.
        self.system_acinverterstriphasemeasure_linevoltagel2l3 = self.system_acinverterstriphasemeasure_start_address + 4    # Property ID: 8, [V] (float). Line voltage L2-L3 measured.
        self.system_acinverterstriphasemeasure_linevoltagel3l1 = self.system_acinverterstriphasemeasure_start_address + 6    # Property ID: 12, [V] (float). Line voltage L3-L1 measured.
        self.system_acinverterstriphasemeasure_totalactivepower = self.system_acinverterstriphasemeasure_start_address + 8    # Property ID: 16, [W] (float). Total active power measured.
        self.system_acinverterstriphasemeasure_totalapparentpower = self.system_acinverterstriphasemeasure_start_address + 10    # Property ID: 20, [VA] (float). Total apparent power measured.
        self.system_acinverterstriphasemeasure_anglel2relativetol1 = self.system_acinverterstriphasemeasure_start_address + 12    # Property ID: 24, [degree] (float). Angle L2 relative to L1 measured.
        self.system_acinverterstriphasemeasure_anglel3relativetol1 = self.system_acinverterstriphasemeasure_start_address + 14    # Property ID: 25, [degree] (float). Angle L3 relative to L1 measured.
        self.system_acinverterstriphasemeasure_dayconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 16    # Property ID: 26, [Wh] (float). Consumed energy of the current day.
        self.system_acinverterstriphasemeasure_previousdayconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 18    # Property ID: 27, [Wh] (float). Consumed energy of the previous day.
        self.system_acinverterstriphasemeasure_resetableconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 20    # Property ID: 28, [Wh] (float64). Resetable consumed energy.
        self.system_acinverterstriphasemeasure_totalconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 24    # Property ID: 29, [Wh] (float64). Total consumed energy.
        self.system_acinverterstriphasemeasure_dayproducedenergy = self.system_acinverterstriphasemeasure_start_address + 28    # Property ID: 30, [Wh] (float). Produced energy of the current day.
        self.system_acinverterstriphasemeasure_previousdayproducedenergy = self.system_acinverterstriphasemeasure_start_address + 30    # Property ID: 31, [Wh] (float). Produced energy of the previous day.
        self.system_acinverterstriphasemeasure_resetableproducedenergy = self.system_acinverterstriphasemeasure_start_address + 32    # Property ID: 32, [Wh] (float64). Resetable produced energy.
        self.system_acinverterstriphasemeasure_totalproducedenergy = self.system_acinverterstriphasemeasure_start_address + 36    # Property ID: 33, [Wh] (float64). Total produced energy.
        self.system_acinverterstriphasemeasure_dayruntime = self.system_acinverterstriphasemeasure_start_address + 40   # Property ID: 34, [h] (float). Day runtime measured.
        self.system_acinverterstriphasemeasure_totalruntime = self.system_acinverterstriphasemeasure_start_address + 42 # Property ID: 35, [h] (float). Total runtime measured.
        self.system_acinverterstriphasemeasure_daypeakpower = self.system_acinverterstriphasemeasure_start_address + 44 # Property ID: 36, [VA] (float). Peak power of the current day.
        self.system_acinverterstriphasemeasure_previousdaypeakpower = self.system_acinverterstriphasemeasure_start_address + 46    # Property ID: 37, [VA] (float). Peak power of the previous day.
        self.system_acinverterstriphasemeasure_dayminactivepower = self.system_acinverterstriphasemeasure_start_address + 48    # Property ID: 38, [W] (float). Minimum active power of the current day.
        self.system_acinverterstriphasemeasure_previousdayminactivepower = self.system_acinverterstriphasemeasure_start_address + 50    # Property ID: 39, [W] (float). Minimum active power of the previous day.
        self.system_acinverterstriphasemeasure_daymaxactivepower = self.system_acinverterstriphasemeasure_start_address + 52    # Property ID: 40, [W] (float). Maximum active power of the current day.
        self.system_acinverterstriphasemeasure_previousdaymaxactivepower = self.system_acinverterstriphasemeasure_start_address + 54    # Property ID: 41, [W] (float). Maximum active power of the previous day.
        self.system_acinverterstriphasemeasure_producedactivepower = self.system_acinverterstriphasemeasure_start_address + 56    # Property ID: 42, [W] (float). Produced active power measured.
        self.system_acinverterstriphasemeasure_consumedactivepower = self.system_acinverterstriphasemeasure_start_address + 58    # Property ID: 44, [W] (float). Consumed active power measured.

        # Object AcInvertersL1Measure Modbus Address
        self.system_acinvertersl1measure_start_address = 5400
        self.system_acinvertersl1measure_phasevoltage = self.system_acinvertersl1measure_start_address + 0              # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_acinvertersl1measure_current = self.system_acinvertersl1measure_start_address + 2                   # Property ID: 4, [A] (float). Current RMS measured.
        self.system_acinvertersl1measure_activepower = self.system_acinvertersl1measure_start_address + 4               # Property ID: 8, [W] (float). Active power measured.
        self.system_acinvertersl1measure_reactivepower = self.system_acinvertersl1measure_start_address + 6             # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_acinvertersl1measure_apparentpower = self.system_acinvertersl1measure_start_address + 8             # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_acinvertersl1measure_cosphi = self.system_acinvertersl1measure_start_address + 10                   # Property ID: 20, [-] (float). Power factor measured.
        self.system_acinvertersl1measure_daypeakpower = self.system_acinvertersl1measure_start_address + 12             # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_acinvertersl1measure_previousdaypeakpower = self.system_acinvertersl1measure_start_address + 14     # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_acinvertersl1measure_dayminactivepower = self.system_acinvertersl1measure_start_address + 16        # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_acinvertersl1measure_previousdayminactivepower = self.system_acinvertersl1measure_start_address + 18    # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_acinvertersl1measure_daymaxactivepower = self.system_acinvertersl1measure_start_address + 20        # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_acinvertersl1measure_previousdaymaxactivepower = self.system_acinvertersl1measure_start_address + 22    # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_acinvertersl1measure_dayconsumedenergy = self.system_acinvertersl1measure_start_address + 28        # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_acinvertersl1measure_previousdayconsumedenergy = self.system_acinvertersl1measure_start_address + 30    # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_acinvertersl1measure_resetableconsumedenergy = self.system_acinvertersl1measure_start_address + 32  # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_acinvertersl1measure_totalconsumedenergy = self.system_acinvertersl1measure_start_address + 36      # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_acinvertersl1measure_dayproducedenergy = self.system_acinvertersl1measure_start_address + 40        # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_acinvertersl1measure_previousdayproducedenergy = self.system_acinvertersl1measure_start_address + 42    # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_acinvertersl1measure_resetableproducedenergy = self.system_acinvertersl1measure_start_address + 44  # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_acinvertersl1measure_totalproducedenergy = self.system_acinvertersl1measure_start_address + 48      # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AcInvertersL2Measure Modbus Address
        self.system_acinvertersl2measure_start_address = 5700
        self.system_acinvertersl2measure_phasevoltage = self.system_acinvertersl2measure_start_address + 0              # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_acinvertersl2measure_current = self.system_acinvertersl2measure_start_address + 2                   # Property ID: 4, [A] (float). Current RMS measured.
        self.system_acinvertersl2measure_activepower = self.system_acinvertersl2measure_start_address + 4               # Property ID: 8, [W] (float). Active power measured.
        self.system_acinvertersl2measure_reactivepower = self.system_acinvertersl2measure_start_address + 6             # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_acinvertersl2measure_apparentpower = self.system_acinvertersl2measure_start_address + 8             # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_acinvertersl2measure_cosphi = self.system_acinvertersl2measure_start_address + 10                   # Property ID: 20, [-] (float). Power factor measured.
        self.system_acinvertersl2measure_daypeakpower = self.system_acinvertersl2measure_start_address + 12             # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_acinvertersl2measure_previousdaypeakpower = self.system_acinvertersl2measure_start_address + 14     # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_acinvertersl2measure_dayminactivepower = self.system_acinvertersl2measure_start_address + 16        # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_acinvertersl2measure_previousdayminactivepower = self.system_acinvertersl2measure_start_address + 18    # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_acinvertersl2measure_daymaxactivepower = self.system_acinvertersl2measure_start_address + 20        # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_acinvertersl2measure_previousdaymaxactivepower = self.system_acinvertersl2measure_start_address + 22    # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_acinvertersl2measure_dayconsumedenergy = self.system_acinvertersl2measure_start_address + 28        # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_acinvertersl2measure_previousdayconsumedenergy = self.system_acinvertersl2measure_start_address + 30    # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_acinvertersl2measure_resetableconsumedenergy = self.system_acinvertersl2measure_start_address + 32  # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_acinvertersl2measure_totalconsumedenergy = self.system_acinvertersl2measure_start_address + 36      # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_acinvertersl2measure_dayproducedenergy = self.system_acinvertersl2measure_start_address + 40        # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_acinvertersl2measure_previousdayproducedenergy = self.system_acinvertersl2measure_start_address + 42    # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_acinvertersl2measure_resetableproducedenergy = self.system_acinvertersl2measure_start_address + 44  # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_acinvertersl2measure_totalproducedenergy = self.system_acinvertersl2measure_start_address + 48      # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AcInvertersL3Measure Modbus Address
        self.system_acinvertersl3measure_start_address = 6000
        self.system_acinvertersl3measure_phasevoltage = self.system_acinvertersl3measure_start_address + 0              # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_acinvertersl3measure_current = self.system_acinvertersl3measure_start_address + 2                   # Property ID: 4, [A] (float). Current RMS measured.
        self.system_acinvertersl3measure_activepower = self.system_acinvertersl3measure_start_address + 4               # Property ID: 8, [W] (float). Active power measured.
        self.system_acinvertersl3measure_reactivepower = self.system_acinvertersl3measure_start_address + 6             # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_acinvertersl3measure_apparentpower = self.system_acinvertersl3measure_start_address + 8             # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_acinvertersl3measure_cosphi = self.system_acinvertersl3measure_start_address + 10                   # Property ID: 20, [-] (float). Power factor measured.
        self.system_acinvertersl3measure_daypeakpower = self.system_acinvertersl3measure_start_address + 12             # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_acinvertersl3measure_previousdaypeakpower = self.system_acinvertersl3measure_start_address + 14     # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_acinvertersl3measure_dayminactivepower = self.system_acinvertersl3measure_start_address + 16        # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_acinvertersl3measure_previousdayminactivepower = self.system_acinvertersl3measure_start_address + 18    # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_acinvertersl3measure_daymaxactivepower = self.system_acinvertersl3measure_start_address + 20        # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_acinvertersl3measure_previousdaymaxactivepower = self.system_acinvertersl3measure_start_address + 22    # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_acinvertersl3measure_dayconsumedenergy = self.system_acinvertersl3measure_start_address + 28        # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_acinvertersl3measure_previousdayconsumedenergy = self.system_acinvertersl3measure_start_address + 30    # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_acinvertersl3measure_resetableconsumedenergy = self.system_acinvertersl3measure_start_address + 32  # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_acinvertersl3measure_totalconsumedenergy = self.system_acinvertersl3measure_start_address + 36      # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_acinvertersl3measure_dayproducedenergy = self.system_acinvertersl3measure_start_address + 40        # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_acinvertersl3measure_previousdayproducedenergy = self.system_acinvertersl3measure_start_address + 42    # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_acinvertersl3measure_resetableproducedenergy = self.system_acinvertersl3measure_start_address + 44  # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_acinvertersl3measure_totalproducedenergy = self.system_acinvertersl3measure_start_address + 48      # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AllFlexLoadsTriPhaseAcMeasure Modbus Address
        self.system_allflexloadstriphaseacmeasure_start_address = 6300
        self.system_allflexloadstriphaseacmeasure_frequency = self.system_allflexloadstriphaseacmeasure_start_address + 0    # Property ID: 0, [Hz] (float). Frequency measured.
        self.system_allflexloadstriphaseacmeasure_linevoltagel1l2 = self.system_allflexloadstriphaseacmeasure_start_address + 2    # Property ID: 4, [V] (float). Line voltage L1-L2 measured.
        self.system_allflexloadstriphaseacmeasure_linevoltagel2l3 = self.system_allflexloadstriphaseacmeasure_start_address + 4    # Property ID: 8, [V] (float). Line voltage L2-L3 measured.
        self.system_allflexloadstriphaseacmeasure_linevoltagel3l1 = self.system_allflexloadstriphaseacmeasure_start_address + 6    # Property ID: 12, [V] (float). Line voltage L3-L1 measured.
        self.system_allflexloadstriphaseacmeasure_totalactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 8    # Property ID: 16, [W] (float). Total active power measured.
        self.system_allflexloadstriphaseacmeasure_totalapparentpower = self.system_allflexloadstriphaseacmeasure_start_address + 10    # Property ID: 20, [VA] (float). Total apparent power measured.
        self.system_allflexloadstriphaseacmeasure_anglel2relativetol1 = self.system_allflexloadstriphaseacmeasure_start_address + 12    # Property ID: 24, [degree] (float). Angle L2 relative to L1 measured.
        self.system_allflexloadstriphaseacmeasure_anglel3relativetol1 = self.system_allflexloadstriphaseacmeasure_start_address + 14    # Property ID: 25, [degree] (float). Angle L3 relative to L1 measured.
        self.system_allflexloadstriphaseacmeasure_dayconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 16    # Property ID: 26, [Wh] (float). Consumed energy of the current day.
        self.system_allflexloadstriphaseacmeasure_previousdayconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 18    # Property ID: 27, [Wh] (float). Consumed energy of the previous day.
        self.system_allflexloadstriphaseacmeasure_resetableconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 20    # Property ID: 28, [Wh] (float64). Resetable consumed energy.
        self.system_allflexloadstriphaseacmeasure_totalconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 24    # Property ID: 29, [Wh] (float64). Total consumed energy.
        self.system_allflexloadstriphaseacmeasure_dayproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 28    # Property ID: 30, [Wh] (float). Produced energy of the current day.
        self.system_allflexloadstriphaseacmeasure_previousdayproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 30    # Property ID: 31, [Wh] (float). Produced energy of the previous day.
        self.system_allflexloadstriphaseacmeasure_resetableproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 32    # Property ID: 32, [Wh] (float64). Resetable produced energy.
        self.system_allflexloadstriphaseacmeasure_totalproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 36    # Property ID: 33, [Wh] (float64). Total produced energy.
        self.system_allflexloadstriphaseacmeasure_dayruntime = self.system_allflexloadstriphaseacmeasure_start_address + 40    # Property ID: 34, [h] (float). Day runtime measured.
        self.system_allflexloadstriphaseacmeasure_totalruntime = self.system_allflexloadstriphaseacmeasure_start_address + 42    # Property ID: 35, [h] (float). Total runtime measured.
        self.system_allflexloadstriphaseacmeasure_daypeakpower = self.system_allflexloadstriphaseacmeasure_start_address + 44    # Property ID: 36, [VA] (float). Peak power of the current day.
        self.system_allflexloadstriphaseacmeasure_previousdaypeakpower = self.system_allflexloadstriphaseacmeasure_start_address + 46    # Property ID: 37, [VA] (float). Peak power of the previous day.
        self.system_allflexloadstriphaseacmeasure_dayminactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 48    # Property ID: 38, [W] (float). Minimum active power of the current day.
        self.system_allflexloadstriphaseacmeasure_previousdayminactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 50    # Property ID: 39, [W] (float). Minimum active power of the previous day.
        self.system_allflexloadstriphaseacmeasure_daymaxactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 52    # Property ID: 40, [W] (float). Maximum active power of the current day.
        self.system_allflexloadstriphaseacmeasure_previousdaymaxactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 54    # Property ID: 41, [W] (float). Maximum active power of the previous day.
        self.system_allflexloadstriphaseacmeasure_producedactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 56    # Property ID: 42, [W] (float). Produced active power measured.
        self.system_allflexloadstriphaseacmeasure_consumedactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 58    # Property ID: 44, [W] (float). Consumed active power measured.

        # Object AllFlexLoadsL1AcMeasure Modbus Address
        self.system_allflexloadsl1acmeasure_start_address = 6600
        self.system_allflexloadsl1acmeasure_phasevoltage = self.system_allflexloadsl1acmeasure_start_address + 0        # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_allflexloadsl1acmeasure_current = self.system_allflexloadsl1acmeasure_start_address + 2             # Property ID: 4, [A] (float). Current RMS measured.
        self.system_allflexloadsl1acmeasure_activepower = self.system_allflexloadsl1acmeasure_start_address + 4         # Property ID: 8, [W] (float). Active power measured.
        self.system_allflexloadsl1acmeasure_reactivepower = self.system_allflexloadsl1acmeasure_start_address + 6       # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_allflexloadsl1acmeasure_apparentpower = self.system_allflexloadsl1acmeasure_start_address + 8       # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_allflexloadsl1acmeasure_cosphi = self.system_allflexloadsl1acmeasure_start_address + 10             # Property ID: 20, [-] (float). Power factor measured.
        self.system_allflexloadsl1acmeasure_daypeakpower = self.system_allflexloadsl1acmeasure_start_address + 12       # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_allflexloadsl1acmeasure_previousdaypeakpower = self.system_allflexloadsl1acmeasure_start_address + 14    # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_allflexloadsl1acmeasure_dayminactivepower = self.system_allflexloadsl1acmeasure_start_address + 16  # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_allflexloadsl1acmeasure_previousdayminactivepower = self.system_allflexloadsl1acmeasure_start_address + 18    # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_allflexloadsl1acmeasure_daymaxactivepower = self.system_allflexloadsl1acmeasure_start_address + 20  # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_allflexloadsl1acmeasure_previousdaymaxactivepower = self.system_allflexloadsl1acmeasure_start_address + 22    # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_allflexloadsl1acmeasure_dayconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 28  # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_allflexloadsl1acmeasure_previousdayconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 30    # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_allflexloadsl1acmeasure_resetableconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 32    # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_allflexloadsl1acmeasure_totalconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 36    # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_allflexloadsl1acmeasure_dayproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 40  # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_allflexloadsl1acmeasure_previousdayproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 42    # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_allflexloadsl1acmeasure_resetableproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 44    # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_allflexloadsl1acmeasure_totalproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 48    # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AllFlexLoadsL2AcMeasure Modbus Address
        self.system_allflexloadsl2acmeasure_start_address = 6900
        self.system_allflexloadsl2acmeasure_phasevoltage = self.system_allflexloadsl2acmeasure_start_address + 0        # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_allflexloadsl2acmeasure_current = self.system_allflexloadsl2acmeasure_start_address + 2             # Property ID: 4, [A] (float). Current RMS measured.
        self.system_allflexloadsl2acmeasure_activepower = self.system_allflexloadsl2acmeasure_start_address + 4         # Property ID: 8, [W] (float). Active power measured.
        self.system_allflexloadsl2acmeasure_reactivepower = self.system_allflexloadsl2acmeasure_start_address + 6       # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_allflexloadsl2acmeasure_apparentpower = self.system_allflexloadsl2acmeasure_start_address + 8       # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_allflexloadsl2acmeasure_cosphi = self.system_allflexloadsl2acmeasure_start_address + 10             # Property ID: 20, [-] (float). Power factor measured.
        self.system_allflexloadsl2acmeasure_daypeakpower = self.system_allflexloadsl2acmeasure_start_address + 12       # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_allflexloadsl2acmeasure_previousdaypeakpower = self.system_allflexloadsl2acmeasure_start_address + 14    # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_allflexloadsl2acmeasure_dayminactivepower = self.system_allflexloadsl2acmeasure_start_address + 16  # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_allflexloadsl2acmeasure_previousdayminactivepower = self.system_allflexloadsl2acmeasure_start_address + 18    # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_allflexloadsl2acmeasure_daymaxactivepower = self.system_allflexloadsl2acmeasure_start_address + 20  # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_allflexloadsl2acmeasure_previousdaymaxactivepower = self.system_allflexloadsl2acmeasure_start_address + 22    # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_allflexloadsl2acmeasure_dayconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 28  # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_allflexloadsl2acmeasure_previousdayconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 30    # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_allflexloadsl2acmeasure_resetableconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 32    # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_allflexloadsl2acmeasure_totalconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 36    # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_allflexloadsl2acmeasure_dayproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 40  # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_allflexloadsl2acmeasure_previousdayproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 42    # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_allflexloadsl2acmeasure_resetableproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 44    # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_allflexloadsl2acmeasure_totalproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 48    # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object AllFlexLoadsL3AcMeasure Modbus Address
        self.system_allflexloadsl3acmeasure_start_address = 7200
        self.system_allflexloadsl3acmeasure_phasevoltage = self.system_allflexloadsl3acmeasure_start_address + 0        # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.system_allflexloadsl3acmeasure_current = self.system_allflexloadsl3acmeasure_start_address + 2             # Property ID: 4, [A] (float). Current RMS measured.
        self.system_allflexloadsl3acmeasure_activepower = self.system_allflexloadsl3acmeasure_start_address + 4         # Property ID: 8, [W] (float). Active power measured.
        self.system_allflexloadsl3acmeasure_reactivepower = self.system_allflexloadsl3acmeasure_start_address + 6       # Property ID: 12, [VAR] (float). Reactive power measured.
        self.system_allflexloadsl3acmeasure_apparentpower = self.system_allflexloadsl3acmeasure_start_address + 8       # Property ID: 16, [VA] (float). Apparent power measured.
        self.system_allflexloadsl3acmeasure_cosphi = self.system_allflexloadsl3acmeasure_start_address + 10             # Property ID: 20, [-] (float). Power factor measured.
        self.system_allflexloadsl3acmeasure_daypeakpower = self.system_allflexloadsl3acmeasure_start_address + 12       # Property ID: 24, [VA] (float). Peak power of the current day.
        self.system_allflexloadsl3acmeasure_previousdaypeakpower = self.system_allflexloadsl3acmeasure_start_address + 14    # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.system_allflexloadsl3acmeasure_dayminactivepower = self.system_allflexloadsl3acmeasure_start_address + 16  # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.system_allflexloadsl3acmeasure_previousdayminactivepower = self.system_allflexloadsl3acmeasure_start_address + 18    # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.system_allflexloadsl3acmeasure_daymaxactivepower = self.system_allflexloadsl3acmeasure_start_address + 20  # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.system_allflexloadsl3acmeasure_previousdaymaxactivepower = self.system_allflexloadsl3acmeasure_start_address + 22    # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.system_allflexloadsl3acmeasure_dayconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 28  # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.system_allflexloadsl3acmeasure_previousdayconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 30    # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.system_allflexloadsl3acmeasure_resetableconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 32    # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.system_allflexloadsl3acmeasure_totalconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 36    # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.system_allflexloadsl3acmeasure_dayproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 40  # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.system_allflexloadsl3acmeasure_previousdayproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 42    # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.system_allflexloadsl3acmeasure_resetableproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 44    # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.system_allflexloadsl3acmeasure_totalproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 48    # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object SolarCommonAll Modbus Address
        self.system_solarcommonall_start_address = 7500
        self.system_solarcommonall_turnon = self.system_solarcommonall_start_address + 0                                # Property ID: 0, [-] (signal). Turns on solar(s).
        self.system_solarcommonall_turnoff = self.system_solarcommonall_start_address + 1                               # Property ID: 1, [-] (signal). Turns off solar(s).
        self.system_solarcommonall_onoffstate = self.system_solarcommonall_start_address + 2                            # Property ID: 2, [-] (bool). Indicates solar(s) on/off state.
        self.system_solarcommonall_enabledepolarization = self.system_solarcommonall_start_address + 3                  # Property ID: 3, [-] (signal). Enables depolarization.
        self.system_solarcommonall_disabledepolarization = self.system_solarcommonall_start_address + 4                 # Property ID: 4, [-] (signal). Disables depolarization.
        self.system_solarcommonall_power = self.system_solarcommonall_start_address + 5                                 # Property ID: 5, [W] (float). Power produced.
        self.system_solarcommonall_previousdayenergy = self.system_solarcommonall_start_address + 7                     # Property ID: 8, [Wh] (float). Energy produced for the previous day.
        self.system_solarcommonall_powerlimit = self.system_solarcommonall_start_address + 9                            # Property ID: 9, [W] (uint). Solar(s) max power limit.
        self.system_solarcommonall_dayenergy = self.system_solarcommonall_start_address + 11                            # Property ID: 10, [Wh] (float). Energy produced for the current day.
        self.system_solarcommonall_resetableenergy = self.system_solarcommonall_start_address + 15                      # Property ID: 12, [Wh] (float64). Energy produced (can be reset).
        self.system_solarcommonall_totalenergy = self.system_solarcommonall_start_address + 19                          # Property ID: 13, [Wh] (float64). Total energy produced (whole life).

        # Object SolarGroupAll Modbus Address
        self.system_solargroupall_start_address = 7800
        self.system_solargroupall_nbr = self.system_solargroupall_start_address + 0                                     # Property ID: 0, [-] (uint). Number of converters.
        self.system_solargroupall_status = self.system_solargroupall_start_address + 2                                  # Property ID: 1, [-] (bitfield). Current status.
        self.system_solargroupall_vt40nbr = self.system_solargroupall_start_address + 4                                 # Property ID: 2, [-] (uint). Number of vt40.
        self.system_solargroupall_vt65nbr = self.system_solargroupall_start_address + 6                                 # Property ID: 3, [-] (uint). Number of vt65.
        self.system_solargroupall_vt80nbr = self.system_solargroupall_start_address + 8                                 # Property ID: 4, [-] (uint). Number of vt80.
        self.system_solargroupall_vs70nbr = self.system_solargroupall_start_address + 10                                # Property ID: 5, [-] (uint). Number of vs70.
        self.system_solargroupall_vs120nbr = self.system_solargroupall_start_address + 12                               # Property ID: 6, [-] (uint). Number of vs120.

        # Object SystemTotal Modbus Address
        self.system_systemtotal_start_address = 8100
        self.system_systemtotal_clearerrors = self.system_systemtotal_start_address + 0                                 # Property ID: 0, [-] (signal). Clear all errors for this installation. Note that battery charging recovery mode will be enabled if \"Charging recovery mode\" (id 90) was \"Disabled and activatable\" (value 1) before sending this signal.
        self.system_systemtotal_turnon = self.system_systemtotal_start_address + 1                                      # Property ID: 1, [-] (signal). Turns on all converters.
        self.system_systemtotal_turnoff = self.system_systemtotal_start_address + 2                                     # Property ID: 2, [-] (signal). Turns off all converters.
        self.system_systemtotal_onoffstate = self.system_systemtotal_start_address + 3                                  # Property ID: 3, [-] (bool). Indicates all converters on/off state.
        self.system_systemtotal_acsourcepower = self.system_systemtotal_start_address + 4                               # Property ID: 4, [W] (float). Power of the currently used AC source (AcSource or AcFlex used as FlexSource).
        self.system_systemtotal_acloadandflexloadtotalpower = self.system_systemtotal_start_address + 6                 # Property ID: 6, [W] (float). AC Loads and FlexLoads total power (consumed - produced).
        self.system_systemtotal_acloadandflexloadapparentpower = self.system_systemtotal_start_address + 8              # Property ID: 8, [VA] (float). AC Loads and FlexLoads apparent power.
        self.system_systemtotal_warnings = self.system_systemtotal_start_address + 10                                   # Property ID: 10, [-] (bitfield). Current warning(s).
        self.system_systemtotal_errorsrestarting = self.system_systemtotal_start_address + 12                           # Property ID: 11, [-] (bitfield). Current error(s) (the function keeps retrying).
        self.system_systemtotal_acsourcedayconsumedenergy = self.system_systemtotal_start_address + 14                  # Property ID: 12, [Wh] (float). Day consumed energy of all AC sources (AcSource and AcFlex used as FlexSource).
        self.system_systemtotal_acsourcedayproducedenergy = self.system_systemtotal_start_address + 16                  # Property ID: 13, [Wh] (float). Day produced energy of all AC sources (AcSource and AcFlex used as FlexSource).
        self.system_systemtotal_errorshalted = self.system_systemtotal_start_address + 18                               # Property ID: 14, [-] (bitfield). Current error(s) (the function is halted).
        self.system_systemtotal_errorsrestartingorhalted = self.system_systemtotal_start_address + 20                   # Property ID: 15, [-] (bitfield). Current error(s) (the function is either halted or restarting).
        self.system_systemtotal_cmdentryidxforemergencystop = self.system_systemtotal_start_address + 22                # Property ID: 16, [-] (int). Index of the command entry interface used for emergency stop. (0 value disable remote operation).
        self.system_systemtotal_acsourcenbr = self.system_systemtotal_start_address + 24                                # Property ID: 17, [-] (int). Number of AC sources used in the installation. How much and which used phases is shown in \"Phase existance\" (id 126)
        self.system_systemtotal_acloadandflexloaddaytotalenergy = self.system_systemtotal_start_address + 26            # Property ID: 18, [Wh] (float). AC Loads and FlexLoads day total energy (consumed - produced).
        self.system_systemtotal_acflexloadnbr = self.system_systemtotal_start_address + 28                              # Property ID: 19, [-] (int). Number of AC FlexLoads used in the installation. How much and which used phases is shown in \"Phase existance\" (id 0)
        self.system_systemtotal_status = self.system_systemtotal_start_address + 30                                     # Property ID: 20, [-] (enum). Current status.
        self.system_systemtotal_acloadandflexloadconsumedpower = self.system_systemtotal_start_address + 32             # Property ID: 21, [W] (float). AC Loads and FlexLoads consumed power.
        self.system_systemtotal_acloadandflexloadproducedpower = self.system_systemtotal_start_address + 34             # Property ID: 22, [W] (float). AC Loads and FlexLoads produced power.
        self.system_systemtotal_acloadandflexloaddayconsumedenergy = self.system_systemtotal_start_address + 36         # Property ID: 25, [Wh] (float). AC Loads and FlexLoads day consumed energy.
        self.system_systemtotal_acloadandflexloaddayproducedenergy = self.system_systemtotal_start_address + 38         # Property ID: 26, [Wh] (float). AC Loads and FlexLoads day produced energy.
        self.system_systemtotal_nbrofsmartmeters = self.system_systemtotal_start_address + 44                           # Property ID: 29, [-] (uint). Number of powermeters.

        # Object BatteryCommonAll Modbus Address
        self.system_batterycommonall_start_address = 8400
        self.system_batterycommonall_chargingpower = self.system_batterycommonall_start_address + 0                     # Property ID: 0, [W] (float). Charging power measured.
        self.system_batterycommonall_daychargingenergy = self.system_batterycommonall_start_address + 2                 # Property ID: 4, [Wh] (float). Day charging energy measured.
        self.system_batterycommonall_previousdaychargingenergy = self.system_batterycommonall_start_address + 4         # Property ID: 5, [Wh] (float). Previous day charging energy measured.
        self.system_batterycommonall_resetablechargingenergy = self.system_batterycommonall_start_address + 6           # Property ID: 6, [Wh] (float64). Resetable charging energy measured.
        self.system_batterycommonall_totalchargingenergy = self.system_batterycommonall_start_address + 10              # Property ID: 7, [Wh] (float64). Total charging energy measured.
        self.system_batterycommonall_daydischargingenergy = self.system_batterycommonall_start_address + 14             # Property ID: 8, [Wh] (float). Day discharging energy measured.
        self.system_batterycommonall_previousdaydischargingenergy = self.system_batterycommonall_start_address + 16     # Property ID: 9, [Wh] (float). Previous day discharging energy measured.
        self.system_batterycommonall_resetabledischargingenergy = self.system_batterycommonall_start_address + 18       # Property ID: 10, [Wh] (float64). Resetable discharging energy measured.
        self.system_batterycommonall_totaldischargingenergy = self.system_batterycommonall_start_address + 22           # Property ID: 11, [Wh] (float64). Total discharging energy measured.
        self.system_batterycommonall_socinpercent = self.system_batterycommonall_start_address + 26                     # Property ID: 12, [%] (float). State of charge measured.

        # Object BatteryGroupAll Modbus Address
        self.system_batterygroupall_start_address = 8700
        self.system_batterygroupall_nbr = self.system_batterygroupall_start_address + 0                                 # Property ID: 0, [-] (uint). Number of batteries.
        self.system_batterygroupall_status = self.system_batterygroupall_start_address + 2                              # Property ID: 1, [-] (bitfield). Current status.


        # Group Battery Modbus Address
        # Object BatteryCommon Modbus Address
        self.battery_batterycommon_start_address = 0
        self.battery_batterycommon_chargingpower = self.battery_batterycommon_start_address + 0                         # Property ID: 0, [W] (float). Charging power measured.
        self.battery_batterycommon_daychargingenergy = self.battery_batterycommon_start_address + 2                     # Property ID: 4, [Wh] (float). Day charging energy measured.
        self.battery_batterycommon_previousdaychargingenergy = self.battery_batterycommon_start_address + 4             # Property ID: 5, [Wh] (float). Previous day charging energy measured.
        self.battery_batterycommon_resetablechargingenergy = self.battery_batterycommon_start_address + 6               # Property ID: 6, [Wh] (float64). Resetable charging energy measured.
        self.battery_batterycommon_totalchargingenergy = self.battery_batterycommon_start_address + 10                  # Property ID: 7, [Wh] (float64). Total charging energy measured.
        self.battery_batterycommon_daydischargingenergy = self.battery_batterycommon_start_address + 14                 # Property ID: 8, [Wh] (float). Day discharging energy measured.
        self.battery_batterycommon_previousdaydischargingenergy = self.battery_batterycommon_start_address + 16         # Property ID: 9, [Wh] (float). Previous day discharging energy measured.
        self.battery_batterycommon_resetabledischargingenergy = self.battery_batterycommon_start_address + 18           # Property ID: 10, [Wh] (float64). Resetable discharging energy measured.
        self.battery_batterycommon_totaldischargingenergy = self.battery_batterycommon_start_address + 22               # Property ID: 11, [Wh] (float64). Total discharging energy measured.
        self.battery_batterycommon_socinpercent = self.battery_batterycommon_start_address + 26                         # Property ID: 12, [%] (float). State of charge measured.

        # Object Battery Modbus Address
        self.battery_battery_start_address = 300
        self.battery_battery_status = self.battery_battery_start_address + 0                                            # Property ID: 0, [-] (enum). Current status.
        self.battery_battery_errors = self.battery_battery_start_address + 2                                            # Property ID: 1, [-] (bitfield). Current errors.
        self.battery_battery_warnings = self.battery_battery_start_address + 4                                          # Property ID: 2, [-] (bitfield). Current warnings.
        self.battery_battery_targetchargingcurrentlowlimit = self.battery_battery_start_address + 6                     # Property ID: 3, [A] (float). Target charging current low limit sent to the power flow dispatcher.
        self.battery_battery_targetchargingcurrenthighlimit = self.battery_battery_start_address + 8                    # Property ID: 4, [A] (float). Target charging current high limit sent to the power flow dispatcher.
        self.battery_battery_chargingcurrentlowlimit = self.battery_battery_start_address + 10                          # Property ID: 5, [A] (float). Charging current low limit sent to the power flow dispatcher.
        self.battery_battery_chargingcurrenthighlimit = self.battery_battery_start_address + 12                         # Property ID: 6, [A] (float). Charging current high limit sent to the power flow dispatcher.
        self.battery_battery_targetvoltagemax = self.battery_battery_start_address + 14                                 # Property ID: 7, [V] (float). Target voltage used to clamp \"Charging current high limit\" (id 6) dynamically in function of the voltage error to avoid overshoot.
        self.battery_battery_targetvoltagemin = self.battery_battery_start_address + 16                                 # Property ID: 8, [V] (float). Target voltage used to clamp \"Charging current low limit\" (id 5) dynamically in function of the voltage error to avoid undershoot.
        self.battery_battery_voltage = self.battery_battery_start_address + 18                                          # Property ID: 9, [V] (float). Voltage measured.
        self.battery_battery_chargingcurrent = self.battery_battery_start_address + 20                                  # Property ID: 13, [A] (float). Charging current measured.
        self.battery_battery_nbrcycles = self.battery_battery_start_address + 22                                        # Property ID: 17, [-] (float64). Number of cycles since the battery was configured. Note that one cycle corresponds to 'Nominal capacity' electric charges injected into the battery.
        self.battery_battery_sohinpercent = self.battery_battery_start_address + 26                                     # Property ID: 18, [%] (float). State of health measured.
        self.battery_battery_temperatureavailable = self.battery_battery_start_address + 28                             # Property ID: 19, [-] (bool). True if at least one battery contributor has a temperature sensor connected with non communicating battery. Not used with communicating battery.  
        self.battery_battery_temperature = self.battery_battery_start_address + 29                                      # Property ID: 20, [°C] (float). Temperature measured.
        self.battery_battery_userdefinedlimitwithcommunicatingbatteryenabled = self.battery_battery_start_address + 31  # Property ID: 24, [-] (bool). Useful only with communicating batteries. With non communicating batteries, the value can't be changed and is maintained to true. If enabled, \"Discharging current limit\" (id 25) and \"Charging current limit\" (id 26) can be manually set. If disabled, the limits used are those received by the bms. Note that the limits set by the user are ignored if the limits received by the bms are lower.
        self.battery_battery_maxdischargingcurrentlimit = self.battery_battery_start_address + 32                       # Property ID: 25, [A] (float). Sets the discharging current limit.
        self.battery_battery_maxchargingcurrentlimit = self.battery_battery_start_address + 34                          # Property ID: 26, [A] (float). Sets the charging current limit.
        self.battery_battery_currentlimitsmargingfactor = self.battery_battery_start_address + 36                       # Property ID: 27, [-] (float). With non communicating batteries, this ratio is used to keep a marging between the operating range ('Discharging current limit' and 'Charging current limit') and the 'Overcurrent' threshold. With communicating batteries, this ratio is used to keep a marging between \"BMS max charging current\" (id 85) and \"BMS max discharging current\" (id 86) and the limits actually used by the power flow dispatcher.
        self.battery_battery_managementofenergy = self.battery_battery_start_address + 38                               # Property ID: 28, [-] (bitfield). Used to select conditions used for energy management.
        self.battery_battery_socslopeforlimits = self.battery_battery_start_address + 40                                # Property ID: 29, [A/%] (float). Value used to change linearly the \"Target charging current low limit\" (id 3) around \"SOC for backup\" (id 32) and the \"Target charging current high limit\" (id 4) around \"SOC for grid feeding\" (id 31) from chargingCurrentLimit to -dischargingCurrentLimit. Also used to change linearly the \"Charging current high limit\" (id 6) around \"SOC for end of charge\" (id 30) from 100% to 0%.
        self.battery_battery_socforendofchargeinpercent = self.battery_battery_start_address + 42                       # Property ID: 30, [%] (float). SOC over which the \"Charging current high limit\" (id 6) is set to 0 if \"SOC for end of charge\" (value 1) is activated. This prevents the SOC to increase further even if solar power is available. Note that it's recommended to keep a value of 100% for non communicating battery.
        self.battery_battery_socforgridfeedinginpercent = self.battery_battery_start_address + 44                       # Property ID: 31, [%] (float). SOC over which energy is taken from battery to be sourced into grid if \"SOC for grid feeding\" (value 2) is activated. Note that it's recommended to keep a value of 100% for non communicating battery.
        self.battery_battery_socforbackupinpercent = self.battery_battery_start_address + 46                            # Property ID: 32, [%] (float). SOC under which energy is taken from AC source to charge batteries if \"SOC for backup\" (value 4) is activated.
        self.battery_battery_adaptivesocforbackup = self.battery_battery_start_address + 48                             # Property ID: 33, [-] (bool). Used to increase each day \"Current SOC for backup\" (id 38) by the quantity set via \"Adaptive SOC for backup slope\" (id 34) if the SOC is less than \"SOC to increase adaptive SOC for backup\" (id 37). \"Current SOC for backup\" (id 38) is also increased by 15% if an undervoltage has been detected. \"Current SOC for backup\" (id 38) is reset to \"SOC for backup\" (id 32) if the SOC is greather than or equal to \"SOC to reset adaptive SOC for backup\" (id 36) for at least \"Time before reseting adaptive SOC for backup\" (id 35) seconds.
        self.battery_battery_adaptivesocforbackupslopeinpercentperday = self.battery_battery_start_address + 49         # Property ID: 34, [%/day] (uint). \"Current SOC for backup\" (id 38) is increased each day by this amount if the SOC is less than \"SOC to increase adaptive SOC for backup\" (id 37) and if \"Adaptive SOC for backup\" (id 33) is enabled.
        self.battery_battery_timebeforeresetingadaptivesocforbackup = self.battery_battery_start_address + 51           # Property ID: 35, [s] (uint). \"Current SOC for backup\" (id 38) is reset to \"SOC for backup\" (id 32) if the SOC is greather than or equal to \"SOC to reset adaptive SOC for backup\" (id 36) for at least this amount of time.
        self.battery_battery_socinpercenttoresetadaptivesocforbackup = self.battery_battery_start_address + 53          # Property ID: 36, [%] (float). \"Current SOC for backup\" (id 38) is reset to \"SOC for backup\" (id 32) if the SOC is greather than or equal to this value during \"Time before reseting adaptive SOC for backup\" (id 35).
        self.battery_battery_socinpercenttoincreaseadaptivesocforbackup = self.battery_battery_start_address + 55       # Property ID: 37, [%] (float). \"Current SOC for backup\" (id 38) is increased each day by the value of \"Adaptive SOC for backup slope\" (id 34) if the SOC is less than this value and if \"Adaptive SOC for backup\" (id 33) is enabled.
        self.battery_battery_currentsocforbackupinpercent = self.battery_battery_start_address + 57                     # Property ID: 38, [%] (float). Indicate the current value of the SOC for backup.
        self.battery_battery_voltageforgridfeeding = self.battery_battery_start_address + 59                            # Property ID: 39, [V] (float). Voltage over which energy is taken from battery to be sourced into grid if \"Voltage for grid feeding\" (value 8) is activated. Note that the battery may never reach a fully charged state if this feature is activated.
        self.battery_battery_voltageforbackup = self.battery_battery_start_address + 61                                 # Property ID: 40, [V] (float). Voltage under which energy is taken from an AC source to charge batteries if \"Voltage for backup\" (value 16) is activated.
        self.battery_battery_nominaltemperature = self.battery_battery_start_address + 63                               # Property ID: 41, [°C] (float). Battery nominal temperature.
        self.battery_battery_temperaturecoefficient = self.battery_battery_start_address + 65                           # Property ID: 42, [V/°C] (float). Sets the temperature coefficient used to correct the charging voltage level.
        self.battery_battery_forcedmode = self.battery_battery_start_address + 67                                       # Property ID: 43, [-] (bool). Use given values instead of automatic ones for target min/max voltages and charging current.
        self.battery_battery_forcedtargetvoltagemax = self.battery_battery_start_address + 68                           # Property ID: 44, [V] (float). Forced value for \"Target voltage max\" (id 7) when \"Forced mode\" (id 43).
        self.battery_battery_forcedtargetvoltagemin = self.battery_battery_start_address + 70                           # Property ID: 45, [V] (float). Forced value for \"Target voltage min\" (id 8) when \"Forced mode\" (id 43).
        self.battery_battery_forcedtargetchargingcurrent = self.battery_battery_start_address + 72                      # Property ID: 46, [A] (float). Forced value for \"Target charging current low limit\" (id 3) and \"Target charging current high limit\" (id 4) when \"Forced mode\" (id 43). Please enter a positive value to set a target charging current and a negative value to set a target discharging current.
        self.battery_battery_lowlimitlevel = self.battery_battery_start_address + 74                                    # Property ID: 47, [-] (uint). Low limit level sent to the power flow dispatcher.
        self.battery_battery_setpointslevel = self.battery_battery_start_address + 76                                   # Property ID: 48, [-] (uint). Setpoints level sent to the power flow dispatcher.
        self.battery_battery_cominterface = self.battery_battery_start_address + 83                                     # Property ID: 52, [-] (enum). Indicates if the battery is communicating or not and if yes, indicates which communication interface is used. This property must be changed only by the wizard and never by the user !
        self.battery_battery_nominalvoltage = self.battery_battery_start_address + 85                                   # Property ID: 53, [V] (float). Battery nominal voltage. This property must be changed only by the wizard and never by the user !
        self.battery_battery_nominalcapacity = self.battery_battery_start_address + 89                                  # Property ID: 55, [Ah] (float). Battery nominal capacity. This property must be changed only by the wizard and never by the user !
        self.battery_battery_canprotocol = self.battery_battery_start_address + 91                                      # Property ID: 56, [-] (enum). Indicates which CAN protocol is used. This property must be changed only by the wizard and never by the user !
        self.battery_battery_rs485protocol = self.battery_battery_start_address + 93                                    # Property ID: 57, [-] (enum). Indicates which RS485 protocol is used. This property must be changed only by the wizard and never by the user !
        self.battery_battery_manufacturername = self.battery_battery_start_address + 95                                 # Property ID: 58, [-] (enum). Battery brand. This property must be changed only by the wizard and never by the user !
        self.battery_battery_baudrate = self.battery_battery_start_address + 97                                         # Property ID: 59, [kbps] (uint). Communication baud rate. This property must be changed only by the wizard and never by the user !
        self.battery_battery_technology = self.battery_battery_start_address + 100                                      # Property ID: 61, [-] (enum). Battery technology. This property must be changed only by the wizard and never by the user !
        self.battery_battery_adaptivesocforbackupundervoltageincrement = self.battery_battery_start_address + 111       # Property ID: 67, [%] (uint). Used to try to recharge the battery when an undervoltage has been detected. \"Current SOC for backup\" (id 38) is set higher than the current SOC by a quantity set via this property. This function is disabled if \"Adaptive SOC for backup\" (id 33) is set to false or if this value is set to 0.
        self.battery_battery_periodicalchargeanddischarge = self.battery_battery_start_address + 113                    # Property ID: 72, [-] (bool). Used to perform periodic charges (for example in applications where the soc for grid feeding is set lower than 100%) and periodic discharges (for example in backup applications). To be able to use this function, \"SOC for grid feeding\" (value 2) must be activated in \"Conditions for energy management\" (id 28). Configuration is done via \"Delay before periodical charge\" (id 73), \"Delay before periodical discharge\" (id 98), \"Time before reseting periodical (dis)charge\" (id 74), \"Periodical charge SOC\" (id 95), \"Periodical discharge SOC\" (id 96) and \"Use AC source during periodical (dis)charge transitions\" (id 97). How it works: If the function is activated and if the SOC has not reached \"Periodical charge SOC\" (id 95) after \"Delay before periodical charge\" (id 73) seconds, \"Periodical charge SOC\" (id 95) is used instead of \"SOC for grid feeding\" (id 31). Periodic charge ends when the SOC equals \"Periodical charge SOC\" (id 95) for \"Time before reseting periodical (dis)charge\" (id 74) seconds. The working principle of the periodical discharge is the same but the properties used are \"Periodical discharge SOC\" (id 96) and \"Delay before periodical discharge\" (id 98). The use or not of AC source during the transition from the normal operation to the periodical charge or discharge is done via \"Use AC source during periodical (dis)charge transitions\" (id 97). Please refer to the manual for more informations.
        self.battery_battery_delaybeforeperiodicalcharge = self.battery_battery_start_address + 114                     # Property ID: 73, [s] (uint). See explanation of \"Periodical charge and discharge\" (id 72).
        self.battery_battery_timebeforeresetingperiodicalchargeordischarge = self.battery_battery_start_address + 116   # Property ID: 74, [s] (uint). See explanation of \"Periodical charge and discharge\" (id 72).
        self.battery_battery_socforendofdischargeinpercent = self.battery_battery_start_address + 118                   # Property ID: 75, [%] (float). SOC under which \"SOC < SOC for end of discharge\" (value 262144) is set if \"SOC for end of discharge\" (value 32) is activated. The error is reset if the SOC is greather than or equal to \"SOC for backup\" (id 32).
        self.battery_battery_cmdentryidx = self.battery_battery_start_address + 120                                     # Property ID: 77, [-] (int). Index of the command entry interface. (0 value disable remote operation).
        self.battery_battery_ignorebmsrecommendedcurrents = self.battery_battery_start_address + 122                    # Property ID: 84, [-] (bool). Used only with communicating batteries. If true, \"BMS recommended charging current\" (id 87) and \"BMS recommended discharging current\" (id 88) received by the BMS are ignored.
        self.battery_battery_bmsmaxchargingcurrent = self.battery_battery_start_address + 123                           # Property ID: 85, [A] (float). Always 0 with non communicating batteries. Max charging current received by the BMS.
        self.battery_battery_bmsmaxdischargingcurrent = self.battery_battery_start_address + 125                        # Property ID: 86, [A] (float). Always 0 with non communicating batteries. Max discharging current received by the BMS.
        self.battery_battery_bmsrecommendedchargingcurrent = self.battery_battery_start_address + 127                   # Property ID: 87, [A] (float). Always 0 with non communicating batteries. Recommended charging current received by the BMS. This property is ignored if \"Ignore BMS recommended currents\" (id 84) is set to true.
        self.battery_battery_bmsrecommendeddischargingcurrent = self.battery_battery_start_address + 129                # Property ID: 88, [A] (float). Always 0 with non communicating batteries. Recommended discharging current received by the BMS. This property is ignored if \"Ignore BMS recommended currents\" (id 84) is set to true.
        self.battery_battery_communicationlosstimeout = self.battery_battery_start_address + 131                        # Property ID: 89, [s] (uint). Useful only with communicating battery. Error : \"Communication lost\" (value 16384) is set if the elapsed time between two consecutives frames received is greather than or equal to this value.
        self.battery_battery_chargingrecoverymode = self.battery_battery_start_address + 133                            # Property ID: 90, [-] (enum). Indicates the charging recovery mode state.
        self.battery_battery_stopchargingrecoverymode = self.battery_battery_start_address + 135                        # Property ID: 91, [-] (signal). Stop charging recovery mode.
        self.battery_battery_currentsocforendofchargeinpercent = self.battery_battery_start_address + 137               # Property ID: 93, [%] (float). Indicate the current value of the SOC for end of charge.
        self.battery_battery_currentsocforgridfeedinginpercent = self.battery_battery_start_address + 139               # Property ID: 94, [%] (float). Indicate the current value of the SOC for grid feeding.
        self.battery_battery_periodicalchargesocinpercent = self.battery_battery_start_address + 141                    # Property ID: 95, [%] (float). See explanation of \"Periodical charge and discharge\" (id 72). Note that this value must be greather than \"SOC for grid feeding\" (id 31) to perform a periodical charge.
        self.battery_battery_periodicaldischargesocinpercent = self.battery_battery_start_address + 143                 # Property ID: 96, [%] (float). See explanation of \"Periodical charge and discharge\" (id 72). Note that this value must be lower than \"SOC for grid feeding\" (id 31) to perform a periodical discharge.
        self.battery_battery_useacsourceduringperiodicalchargeordischargetransitions = self.battery_battery_start_address + 145    # Property ID: 97, [-] (bitfield). Used to select if AC source is used during periodical charge and periodical discharge transitions.
        self.battery_battery_delaybeforeperiodicaldischarge = self.battery_battery_start_address + 147                  # Property ID: 98, [s] (uint). See explanation of \"Periodical charge and discharge\" (id 72).
        self.battery_battery_cmdentryfunction = self.battery_battery_start_address + 149                                # Property ID: 103, [-] (enum). Function associated with the command entry.
        self.battery_battery_valueusedwhencmdentryisactivated = self.battery_battery_start_address + 151                # Property ID: 104, [-] (float). Value used when command entry is activated. The unit depends on the associated function of the command entry and is indicated in the description of \"Command entry function\" (id 103).
        self.battery_battery_currentsocforendofdischargeinpercent = self.battery_battery_start_address + 153            # Property ID: 105, [%] (float). Indicate the current value of the SOC for end of discharge.
        self.battery_battery_batterycontributorsvoltagedifferenceforerror = self.battery_battery_start_address + 155    # Property ID: 106, [V] (float). Useful only if at least two devices are connected to the battery. Set the voltage level at which \"Abnormal measured voltage\" (value 524288) is raised. The error is set if the highest battery voltage measured by one device - the lowest battery voltage measured by another device is greather than this value for 5s. If a current is flowing, the level is automatically adapted to take into account the voltage drop on the cables.
        self.battery_battery_batterycontributorstemperaturedifferenceforwarning = self.battery_battery_start_address + 157    # Property ID: 107, [°C] (float). Useful only with non communicating battery and if at least two devices are measuring the battery temperature. Set the temperature level at which \"Abnormal measured temperature\" (value 65536) is raised. The warning is set if the highest battery temperature measured by one device - the lowest battery temperature measured by another device is greather than this value.
        self.battery_battery_ignorebmschargerequest = self.battery_battery_start_address + 159                          # Property ID: 108, [-] (bool). Used only with communicating batteries. If true, the charge request received by the BMS is ignored.
        self.battery_battery_highlimitlevel = self.battery_battery_start_address + 160                                  # Property ID: 109, [-] (uint). High limit level sent to the power flow dispatcher.

        # Object BatteryCycle Modbus Address
        self.battery_batterycycle_start_address = 600
        self.battery_batterycycle_requestfloating = self.battery_batterycycle_start_address + 0                         # Property ID: 0, [-] (signal). Forces the battery cycle to go in \"Floating phase\" (value 2).
        self.battery_batterycycle_requestreducedfloating = self.battery_batterycycle_start_address + 1                  # Property ID: 1, [-] (signal). Forces the battery cycle to go in \"Reduced floating phase\" (value 1). This signal has no effect if \"Reduced Floating\" (id 5) is not enabled.
        self.battery_batterycycle_requestabsorption = self.battery_batterycycle_start_address + 2                       # Property ID: 2, [-] (signal). Forces the battery cycle to go in \"Absorption phase\" (value 4). This signal has no effect if \"Absorption\" (id 12) is not enabled.
        self.battery_batterycycle_requestequalization = self.battery_batterycycle_start_address + 3                     # Property ID: 3, [-] (signal). Forces the battery cycle to go in \"Equalization phase\" (value 5). This signal has no effect if \"Equalization\" (id 22) is not enabled.
        self.battery_batterycycle_floatingvoltage = self.battery_batterycycle_start_address + 4                         # Property ID: 4, [V] (float). Battery target voltage in \"Floating phase\" (value 2).
        self.battery_batterycycle_reducedfloatingenabled = self.battery_batterycycle_start_address + 6                  # Property ID: 5, [-] (bool). Enables \"Reduced floating phase\" (value 1).
        self.battery_batterycycle_reducedfloatingvoltage = self.battery_batterycycle_start_address + 7                  # Property ID: 6, [V] (float). Battery target voltage in \"Reduced floating phase\" (value 1).
        self.battery_batterycycle_timeatfloatingvoltagebeforeenteringreducedfloating = self.battery_batterycycle_start_address + 9    # Property ID: 7, [s] (uint). Time spent in \"Floating phase\" (value 2) before going in \"Reduced floating phase\" (value 1). \"Reduced Floating\" (id 5) must be enabled for the transition to happen.
        self.battery_batterycycle_periodicalabsorptionenabled = self.battery_batterycycle_start_address + 11            # Property ID: 8, [-] (bool). Enables \"Periodical absorption phase\" (value 3). This property has no effect if \"Reduced Floating\" (id 5) is not enabled.
        self.battery_batterycycle_periodicalabsorptionvoltage = self.battery_batterycycle_start_address + 12            # Property ID: 9, [V] (float). Battery target voltage in \"Periodical absorption phase\" (value 3).
        self.battery_batterycycle_periodicalabsorptionmaxduration = self.battery_batterycycle_start_address + 14        # Property ID: 10, [s] (uint). Sets \"Periodical absorption phase\" (value 3) max duration. Note that the duration can be lower than this value if \"Absorption terminated by current\" (id 19) is enabled or the duration can be higher than this value if the voltage is not maintained at \"Periodical absorption voltage\" (id 9).
        self.battery_batterycycle_timeinreducedfloatingbeforeaskingperiodicalabsorption = self.battery_batterycycle_start_address + 16    # Property ID: 11, [s] (uint). Time spent in \"Reduced floating phase\" (value 1) before going in \"Periodical absorption phase\" (value 3). \"Periodical absorption\" (id 8) must be enabled for the transition to happen.
        self.battery_batterycycle_absorption = self.battery_batterycycle_start_address + 18                             # Property ID: 12, [-] (bool). Enables \"Absorption phase\" (value 4).
        self.battery_batterycycle_absorptionconditions = self.battery_batterycycle_start_address + 19                   # Property ID: 13, [-] (bitfield). Selects condition(s) to go in \"Absorption phase\" (value 4). These conditions have no effect if \"Absorption\" (id 12) is not enabled.
        self.battery_batterycycle_absorptionvoltage = self.battery_batterycycle_start_address + 21                      # Property ID: 14, [V] (float). Battery target voltage in \"Absorption phase\" (value 4).
        self.battery_batterycycle_amphourdischargedforaskingabsorption = self.battery_batterycycle_start_address + 23   # Property ID: 15, [Ah] (float). \"Absorption phase\" (value 4) is started if the amp hours discharged since last absorption or periodical absorption is above this value, \"Absorption triggered by Ahs\" (value 1) in \"Absorption conditions\" (id 13) is set and \"Absorption\" (id 12) is enabled.
        self.battery_batterycycle_voltageforaskingabsorption = self.battery_batterycycle_start_address + 25             # Property ID: 16, [V] (float). \"Absorption phase\" (value 4) is started if the voltage is lower than this value for a duration greater than \"Voltage duration before asking absorption\" (id 17), \"Absorption triggered by voltage\" (value 4) in \"Absorption conditions\" (id 13) is set and \"Absorption\" (id 12) is enabled.
        self.battery_batterycycle_voltagedurationbeforeaskingabsorption = self.battery_batterycycle_start_address + 27  # Property ID: 17, [s] (uint). \"Absorption phase\" (value 4) is started if the voltage is lower than \"Voltage for asking absorption\" (id 16) for a duration greater than this value, \"Absorption triggered by voltage\" (value 4) in \"Absorption conditions\" (id 13) is set and \"Absorption\" (id 12) is enabled.
        self.battery_batterycycle_absorptionmaxduration = self.battery_batterycycle_start_address + 29                  # Property ID: 18, [s] (uint). Sets \"Absorption phase\" (value 4) max duration. Note that the duration can be lower than this value if \"Absorption terminated by current\" (id 19) is enabled or the duration can be higher than this value if the voltage is not maintained at \"Absorption voltage\" (id 14).
        self.battery_batterycycle_absorptionterminatedbycurrent = self.battery_batterycycle_start_address + 31          # Property ID: 19, [-] (bool). Enables the function allowing to stop \"Absorption phase\" (value 4) or \"Periodical absorption phase\" (value 3) based on the battery charging current.
        self.battery_batterycycle_currenttoterminateabsorption = self.battery_batterycycle_start_address + 32           # Property ID: 20, [A] (float). \"Absorption phase\" (value 4) or \"Periodical absorption phase\" (value 3) are stopped if the \"Absorption terminated by current\" (id 19) is enabled and if the battery charging current is lower than this value at a battery voltage equal to \"Absorption voltage\" (id 14) in \"Absorption phase\" (value 4) or \"Periodical absorption voltage\" (id 9) in \"Periodical absorption phase\" (value 3). 
        self.battery_batterycycle_minimumwaitingtimebetweenabsorptions = self.battery_batterycycle_start_address + 34   # Property ID: 21, [s] (uint). \"Absorption phase\" (value 4) can't be automatically started if the time since the end of the previous absorption or periodical absorption is smaller than this value. Note that this minimum waiting time is ignored if a signal is sent via \"Request absorption\" (id 2).
        self.battery_batterycycle_equalization = self.battery_batterycycle_start_address + 36                           # Property ID: 22, [-] (bool). Enables \"Equalization phase\" (value 5).
        self.battery_batterycycle_equalizationconditions = self.battery_batterycycle_start_address + 37                 # Property ID: 23, [-] (bitfield). Selects condition(s) to go in \"Equalization phase\" (value 5). These conditions have no effect if \"Equalization\" (id 22) is not enabled.
        self.battery_batterycycle_equalizationvoltage = self.battery_batterycycle_start_address + 39                    # Property ID: 24, [V] (float). Battery target voltage in \"Equalization phase\" (value 5).
        self.battery_batterycycle_elapsedtimeforaskinganequalization = self.battery_batterycycle_start_address + 41     # Property ID: 25, [s] (uint). \"Equalization phase\" (value 5) is started if the time since the last equalization is above this value, \"Equalization triggered by period\" (value 1) in \"Equalization conditions\" (id 23) is set and \"Equalization\" (id 22) is enabled.
        self.battery_batterycycle_amphourdischargedforaskingequalization = self.battery_batterycycle_start_address + 43 # Property ID: 26, [Ah] (float). \"Equalization phase\" (value 5) is started if the amp hours discharged since the last equalization is above this value, \"Equalization triggered by Ahs\" (value 2) in \"Equalization conditions\" (id 23) is set and \"Equalization\" (id 22) is enabled.
        self.battery_batterycycle_equalizationduration = self.battery_batterycycle_start_address + 45                   # Property ID: 27, [s] (uint). Sets \"Equalization phase\" (value 5) duration. Note that the duration can be higher than this value if the voltage is not maintained at \"Equalization voltage\" (id 24).
        self.battery_batterycycle_equalizationafterabsorption = self.battery_batterycycle_start_address + 47            # Property ID: 28, [-] (bool). Sets if \"Equalization phase\" (value 5) must be done after \"Absorption phase\" (value 4).
        self.battery_batterycycle_equalizationmaxcurrentifequalizationafterabsorption = self.battery_batterycycle_start_address + 48    # Property ID: 29, [A] (float). Transition from \"Absorption phase\" (value 4) to \"Equalization phase\" (value 5) if the battery charging current is lower than this value at a battery voltage equal to \"Equalization voltage\" (id 24), \"Equalization after absorption\" (id 28) is set to true, at least one condition in \"Equalization conditions\" (id 23) is true and \"Equalization\" (id 22) is enabled.
        self.battery_batterycycle_phase = self.battery_batterycycle_start_address + 50                                  # Property ID: 30, [-] (enum). Actual phase.
        self.battery_batterycycle_timespentinactualphase = self.battery_batterycycle_start_address + 52                 # Property ID: 31, [s] (uint). Time spent in the actual phase. Note that the time is slow down if the battery voltage is lower than the target voltage in \"Absorption phase\" (value 4), \"Periodical absorption phase\" (value 3) or \"Equalization phase\" (value 5).
        self.battery_batterycycle_transition = self.battery_batterycycle_start_address + 54                             # Property ID: 32, [-] (enum). Used to indicate from which phase to which phase the battery cycle has jumped.
        self.battery_batterycycle_transitionreasons = self.battery_batterycycle_start_address + 56                      # Property ID: 33, [-] (bitfield). Used to indicate the reason(s) of the transition.
        self.battery_batterycycle_remainingtimebeforenextabsorptionallowed = self.battery_batterycycle_start_address + 58    # Property ID: 34, [s] (uint). Stores the remaining time before \"Absorption phase\" (value 4) can be triggered by the condition(s) in \"Absorption conditions\" (id 13). The value is infinite if \"Absorption\" (id 12) is disabled. Note that \"Absorption phase\" (value 4) can be manually requested via \"Request absorption\" (id 2) even if this time is not 0.
        self.battery_batterycycle_remainingamphourdischargedbeforeabsorptionistriggered = self.battery_batterycycle_start_address + 60    # Property ID: 35, [Ah] (float). Stores the remaining amp hours discharged before \"Absorption phase\" (value 4) is triggered. The value is infinite if \"Absorption\" (id 12) is disabled or \"Absorption triggered by Ahs\" (value 1) is not set.
        self.battery_batterycycle_remainingtimebeforeabsorptionistriggeredbylowsoc = self.battery_batterycycle_start_address + 62    # Property ID: 36, [s] (uint). Stores the remaining time before \"Absorption phase\" (value 4) is triggered by low SOC. The value is infinite if \"Absorption\" (id 12) is disabled, \"Absorption triggered by SOC\" (value 2) is not set or the SOC is greather than 80%.
        self.battery_batterycycle_remainingtimebeforeabsorptionistriggeredbyvoltage = self.battery_batterycycle_start_address + 64    # Property ID: 37, [s] (uint). Stores the remaining time before \"Absorption phase\" (value 4) is triggered by voltage. The value is infinite if \"Absorption\" (id 12) is disabled or \"Absorption triggered by voltage\" (value 4) is not set.
        self.battery_batterycycle_remainingtimebeforeequalizationistriggeredbytimeperiod = self.battery_batterycycle_start_address + 66    # Property ID: 38, [s] (uint). Stores the remaining time before \"Equalization phase\" (value 5) is triggered by time period. The value is infinite if \"Equalization\" (id 22) is disabled or \"Equalization triggered by period\" (value 1) is not set.
        self.battery_batterycycle_remainingamphourdischargedbeforeequalizationistriggered = self.battery_batterycycle_start_address + 68    # Property ID: 39, [Ah] (float). Stores the remaining amp hours discharged before \"Equalization phase\" (value 5) is triggered. The value is infinite if \"Equalization\" (id 22) is disabled or \"Equalization triggered by Ahs\" (value 2) is not set.
        self.battery_batterycycle_remainingtimebeforeequalizationistriggeredbylowsoc = self.battery_batterycycle_start_address + 70    # Property ID: 40, [s] (uint). Stores the remaining time before \"Equalization phase\" (value 5) is triggered by low SOC. The value is infinite if \"Equalization\" (id 22) is disabled, \"Equalization triggered by SOC\" (value 4) is not set or the SOC is greather than 80%.

        # Object BatteryProtection Modbus Address
        self.battery_batteryprotection_start_address = 900
        self.battery_batteryprotection_undervoltageatrest = self.battery_batteryprotection_start_address + 0            # Property ID: 0, [V] (float). If the battery voltage is below this value when no current is flowing, warning : \"Undervoltage\" (value 2) is raised and if the warning is maintained for more than \"Undervoltage delay before error\" (id 2) seconds, error : \"Undervoltage\" (value 2) is raised.
        self.battery_batteryprotection_undervoltageatcnomoverfive = self.battery_batteryprotection_start_address + 2    # Property ID: 1, [V] (float). If the battery voltage is below this value when C/5 amp is flowing, warning : \"Undervoltage\" (value 2) is raised and if the warning is maintained for more than \"Undervoltage delay before error\" (id 2) seconds, error : \"Undervoltage\" (value 2) is raised.
        self.battery_batteryprotection_durationinundervoltagebeforeerror = self.battery_batteryprotection_start_address + 4    # Property ID: 2, [s] (uint). Error : \"Undervoltage\" (value 2) is raised once the duration with warning : \"Undervoltage\" (value 2) reaches this value.
        self.battery_batteryprotection_timeperiodforresetingundervoltagecnt = self.battery_batteryprotection_start_address + 6    # Property ID: 3, [s] (uint). The \"Undervoltage cnt\" (id 20) is reset once the time since the first undervoltage occured is greather than this value and if automatic restart is not prohibited.
        self.battery_batteryprotection_undervoltagecntvalueforprohibitautorestart = self.battery_batteryprotection_start_address + 8    # Property ID: 4, [-] (uint). Automatic restart is prohibited if the \"Undervoltage cnt\" (id 20) reaches this value.
        self.battery_batteryprotection_timeperiodforresetingcriticalundervoltagecnt = self.battery_batteryprotection_start_address + 10    # Property ID: 5, [s] (uint). The \"Critical undervoltage cnt\" (id 21) is reset once the time since the first critical undervoltage occured is greather than this value and if automatic restart is not prohibited.
        self.battery_batteryprotection_criticalundervoltagecntvalueforprohibitautorestart = self.battery_batteryprotection_start_address + 12    # Property ID: 6, [-] (uint). Automatic restart is prohibited if the \"Critical undervoltage cnt\" (id 21) reaches this value.
        self.battery_batteryprotection_restartvoltageafterundervoltageoccured = self.battery_batteryprotection_start_address + 14    # Property ID: 7, [V] (float). If the battery voltage is above this value, warning : \"Undervoltage\" (value 2) is cleared and if an automatic restart is allowed, error : \"Undervoltage\" (value 2) is cleared. Automatic restart is allowed if \"Undervoltage cnt\" (id 20) is smaller than \"UV nbr for perm. stop\" (id 4) and \"Critical undervoltage cnt\" (id 21) is smaller than \"Critical UV nbr for perm. stop\" (id 6).
        self.battery_batteryprotection_bloenabled = self.battery_batteryprotection_start_address + 16                   # Property ID: 8, [-] (bool). Enables the BLO (Battery Lifetime Optimizer) algorithm.
        self.battery_batteryprotection_blovoltageincrement = self.battery_batteryprotection_start_address + 17          # Property ID: 9, [V] (float). At each shut down by undervoltage, the undervoltage threshold is inreased by this value.
        self.battery_batteryprotection_blomaxvoltage = self.battery_batteryprotection_start_address + 19                # Property ID: 10, [V] (float). The undervoltage threshold is increased at each shut down by undervoltage, but never higher than this value.
        self.battery_batteryprotection_bloresetvoltage = self.battery_batteryprotection_start_address + 21              # Property ID: 11, [V] (float). The battery undervoltage threshold returns to its original value if the battery voltage reaches this value.
        self.battery_batteryprotection_overvoltage = self.battery_batteryprotection_start_address + 23                  # Property ID: 12, [V] (float). If the battery voltage is above this value, warning : \"Overvoltage\" (value 1) is raised and if the warning is maintained for more than 5s, error : \"Overvoltage\" (value 1) is raised.
        self.battery_batteryprotection_hightempforwarning = self.battery_batteryprotection_start_address + 25           # Property ID: 13, [°C] (float). If the battery temperature is above this value, warnings : \"Charging overtemperature\" (value 16) and \"Discharging overtemperature\" (value 32) are raised and a current derating is applied.
        self.battery_batteryprotection_hightempforerror = self.battery_batteryprotection_start_address + 27             # Property ID: 14, [°C] (float). If the battery temperature is above this value, errors \"Charging overtemperature\" (value 16) and \"Discharging overtemperature\" (value 32) are raised and no current flow is allowed.
        self.battery_batteryprotection_lowtempforwarning = self.battery_batteryprotection_start_address + 29            # Property ID: 15, [°C] (float). If the battery temperature is below this value, warnings : \"Charging undertemperature\" (value 64) and \"Discharging undertemperature\" (value 128) are raised and a current derating is applied.
        self.battery_batteryprotection_lowtempforerror = self.battery_batteryprotection_start_address + 31              # Property ID: 16, [°C] (float). If the battery temperature is below this value, errors : \"Charging undertemperature\" (value 64) and \"Discharging undertemperature\" (value 128) are raised and no current flow is allowed.
        self.battery_batteryprotection_overcurrent = self.battery_batteryprotection_start_address + 33                  # Property ID: 17, [A] (float). If the battery charging/discharging current is above this value, warning : \"Charging overcurrent\" (value 4)/\"Discharging overcurrent\" (value 8) is raised and if the warning is maintained for more than 2s, error : \"Charging overcurrent\" (value 4)/\"Discharging overcurrent\" (value 8) is raised.
        self.battery_batteryprotection_undervoltageatrestwithblo = self.battery_batteryprotection_start_address + 35    # Property ID: 18, [V] (float). The undervoltage threshold when no current is flowing. Note that this value can be different from \"Undervoltage at rest\" (id 0) when the BLO is activated.
        self.battery_batteryprotection_undervoltageatcnomoverfivewithblo = self.battery_batteryprotection_start_address + 37    # Property ID: 19, [V] (float). The undervoltage threshold when C/5 amp is flowing. Note that this value can be different from \"Undervoltage at C/5\" (id 1) when the BLO is activated.
        self.battery_batteryprotection_undervoltagecnt = self.battery_batteryprotection_start_address + 39              # Property ID: 20, [-] (uint). Undervoltage counter value. The counter is reset if \"UV nbr for perm. stop\" (id 4) is not reached and if the time since the first undervoltage occured is greather than \"Time for clearing UV cnt\" (id 3).
        self.battery_batteryprotection_criticalundervoltagecnt = self.battery_batteryprotection_start_address + 41      # Property ID: 21, [-] (uint). Critical undervoltage counter value. The counter is reset if \"Critical UV nbr for perm. stop\" (id 6) is not reached and if the time since the first critical undervoltage occured is greather than \"Time for clearing critical UV cnt\" (id 5).
        self.battery_batteryprotection_overvoltagealgorithm = self.battery_batteryprotection_start_address + 43         # Property ID: 22, [-] (enum). Used to select the overvoltage algorithm. Note that regardless of the selected algorithm, the battery will enter a halted error state if more than 3 overvoltages occur within 24 hours.

        # Object SocEstimator Modbus Address
        self.battery_socestimator_start_address = 1200
        self.battery_socestimator_peukertfactor = self.battery_socestimator_start_address + 26                          # Property ID: 13, [-] (float). Used to take into account the fact that the capacity goes down when the discharge current increases.
        self.battery_socestimator_selfdischargecoefficient = self.battery_socestimator_start_address + 28               # Property ID: 14, [%Cnom/month] (float). A battery gets discharged over time even when no current is consumed. This property allows to take this phenomenon into account.
        self.battery_socestimator_endofchargesynchronization = self.battery_socestimator_start_address + 30             # Property ID: 15, [-] (bool). This property activates the function of synchronization at 100 % of SOC under certain conditions of end of charge. The synchronization occurs if the voltage is above \"End of charge voltage level\" (id 16) and if the current is below \"End of charge current level\" (id 17) and this during a period defined by \"Minimum time before end of charge\" (id 18).
        self.battery_socestimator_endofchargevoltagelevel = self.battery_socestimator_start_address + 31                # Property ID: 16, [V] (float). See explanation of \"End of charge synchronization\" (id 15).
        self.battery_socestimator_endofchargecurrentlevel = self.battery_socestimator_start_address + 33                # Property ID: 17, [A] (float). See explanation of \"End of charge synchronization\" (id 15).
        self.battery_socestimator_minimumtimebeforeendofcharge = self.battery_socestimator_start_address + 35           # Property ID: 18, [s] (uint). See explanation of \"End of charge synchronization\" (id 15).
        self.battery_socestimator_resetsocvalue = self.battery_socestimator_start_address + 37                          # Property ID: 19, [-] (signal). the SOC is reset to the value \"Desired SOC value\" (id 20) if this signal is sent. 
        self.battery_socestimator_desiredsocvalueinpercent = self.battery_socestimator_start_address + 38               # Property ID: 20, [%] (float). Value at which the SOC is reset if the signal \"Reset SOC\" (id 19) is sent.
        self.battery_socestimator_configuredassimplecounter = self.battery_socestimator_start_address + 40              # Property ID: 21, [-] (bool). If true, the algorithm works as a simple coulomb counter. Note that \"Self-discharge rate\" (id 14) and \"End of charge synchronization\" (id 15) can also be used in this mode.


        # Group AcSource Modbus Address
        # Object TriPhaseMeasure Modbus Address
        self.acsource_triphasemeasure_start_address = 0
        self.acsource_triphasemeasure_frequency = self.acsource_triphasemeasure_start_address + 0                       # Property ID: 0, [Hz] (float). Frequency measured.
        self.acsource_triphasemeasure_linevoltagel1l2 = self.acsource_triphasemeasure_start_address + 2                 # Property ID: 4, [V] (float). Line voltage L1-L2 measured.
        self.acsource_triphasemeasure_linevoltagel2l3 = self.acsource_triphasemeasure_start_address + 4                 # Property ID: 8, [V] (float). Line voltage L2-L3 measured.
        self.acsource_triphasemeasure_linevoltagel3l1 = self.acsource_triphasemeasure_start_address + 6                 # Property ID: 12, [V] (float). Line voltage L3-L1 measured.
        self.acsource_triphasemeasure_totalactivepower = self.acsource_triphasemeasure_start_address + 8                # Property ID: 16, [W] (float). Total active power measured.
        self.acsource_triphasemeasure_totalapparentpower = self.acsource_triphasemeasure_start_address + 10             # Property ID: 20, [VA] (float). Total apparent power measured.
        self.acsource_triphasemeasure_anglel2relativetol1 = self.acsource_triphasemeasure_start_address + 12            # Property ID: 24, [degree] (float). Angle L2 relative to L1 measured.
        self.acsource_triphasemeasure_anglel3relativetol1 = self.acsource_triphasemeasure_start_address + 14            # Property ID: 25, [degree] (float). Angle L3 relative to L1 measured.
        self.acsource_triphasemeasure_dayconsumedenergy = self.acsource_triphasemeasure_start_address + 16              # Property ID: 26, [Wh] (float). Consumed energy of the current day.
        self.acsource_triphasemeasure_previousdayconsumedenergy = self.acsource_triphasemeasure_start_address + 18      # Property ID: 27, [Wh] (float). Consumed energy of the previous day.
        self.acsource_triphasemeasure_resetableconsumedenergy = self.acsource_triphasemeasure_start_address + 20        # Property ID: 28, [Wh] (float64). Resetable consumed energy.
        self.acsource_triphasemeasure_totalconsumedenergy = self.acsource_triphasemeasure_start_address + 24            # Property ID: 29, [Wh] (float64). Total consumed energy.
        self.acsource_triphasemeasure_dayproducedenergy = self.acsource_triphasemeasure_start_address + 28              # Property ID: 30, [Wh] (float). Produced energy of the current day.
        self.acsource_triphasemeasure_previousdayproducedenergy = self.acsource_triphasemeasure_start_address + 30      # Property ID: 31, [Wh] (float). Produced energy of the previous day.
        self.acsource_triphasemeasure_resetableproducedenergy = self.acsource_triphasemeasure_start_address + 32        # Property ID: 32, [Wh] (float64). Resetable produced energy.
        self.acsource_triphasemeasure_totalproducedenergy = self.acsource_triphasemeasure_start_address + 36            # Property ID: 33, [Wh] (float64). Total produced energy.
        self.acsource_triphasemeasure_dayruntime = self.acsource_triphasemeasure_start_address + 40                     # Property ID: 34, [h] (float). Day runtime measured.
        self.acsource_triphasemeasure_totalruntime = self.acsource_triphasemeasure_start_address + 42                   # Property ID: 35, [h] (float). Total runtime measured.
        self.acsource_triphasemeasure_daypeakpower = self.acsource_triphasemeasure_start_address + 44                   # Property ID: 36, [VA] (float). Peak power of the current day.
        self.acsource_triphasemeasure_previousdaypeakpower = self.acsource_triphasemeasure_start_address + 46           # Property ID: 37, [VA] (float). Peak power of the previous day.
        self.acsource_triphasemeasure_dayminactivepower = self.acsource_triphasemeasure_start_address + 48              # Property ID: 38, [W] (float). Minimum active power of the current day.
        self.acsource_triphasemeasure_previousdayminactivepower = self.acsource_triphasemeasure_start_address + 50      # Property ID: 39, [W] (float). Minimum active power of the previous day.
        self.acsource_triphasemeasure_daymaxactivepower = self.acsource_triphasemeasure_start_address + 52              # Property ID: 40, [W] (float). Maximum active power of the current day.
        self.acsource_triphasemeasure_previousdaymaxactivepower = self.acsource_triphasemeasure_start_address + 54      # Property ID: 41, [W] (float). Maximum active power of the previous day.
        self.acsource_triphasemeasure_producedactivepower = self.acsource_triphasemeasure_start_address + 56            # Property ID: 42, [W] (float). Produced active power measured.
        self.acsource_triphasemeasure_consumedactivepower = self.acsource_triphasemeasure_start_address + 58            # Property ID: 44, [W] (float). Consumed active power measured.

        # Object L1Measure Modbus Address
        self.acsource_l1measure_start_address = 300
        self.acsource_l1measure_phasevoltage = self.acsource_l1measure_start_address + 0                                # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.acsource_l1measure_current = self.acsource_l1measure_start_address + 2                                     # Property ID: 4, [A] (float). Current RMS measured.
        self.acsource_l1measure_activepower = self.acsource_l1measure_start_address + 4                                 # Property ID: 8, [W] (float). Active power measured.
        self.acsource_l1measure_reactivepower = self.acsource_l1measure_start_address + 6                               # Property ID: 12, [VAR] (float). Reactive power measured.
        self.acsource_l1measure_apparentpower = self.acsource_l1measure_start_address + 8                               # Property ID: 16, [VA] (float). Apparent power measured.
        self.acsource_l1measure_cosphi = self.acsource_l1measure_start_address + 10                                     # Property ID: 20, [-] (float). Power factor measured.
        self.acsource_l1measure_daypeakpower = self.acsource_l1measure_start_address + 12                               # Property ID: 24, [VA] (float). Peak power of the current day.
        self.acsource_l1measure_previousdaypeakpower = self.acsource_l1measure_start_address + 14                       # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.acsource_l1measure_dayminactivepower = self.acsource_l1measure_start_address + 16                          # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.acsource_l1measure_previousdayminactivepower = self.acsource_l1measure_start_address + 18                  # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.acsource_l1measure_daymaxactivepower = self.acsource_l1measure_start_address + 20                          # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.acsource_l1measure_previousdaymaxactivepower = self.acsource_l1measure_start_address + 22                  # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.acsource_l1measure_dayconsumedenergy = self.acsource_l1measure_start_address + 28                          # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.acsource_l1measure_previousdayconsumedenergy = self.acsource_l1measure_start_address + 30                  # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.acsource_l1measure_resetableconsumedenergy = self.acsource_l1measure_start_address + 32                    # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.acsource_l1measure_totalconsumedenergy = self.acsource_l1measure_start_address + 36                        # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.acsource_l1measure_dayproducedenergy = self.acsource_l1measure_start_address + 40                          # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.acsource_l1measure_previousdayproducedenergy = self.acsource_l1measure_start_address + 42                  # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.acsource_l1measure_resetableproducedenergy = self.acsource_l1measure_start_address + 44                    # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.acsource_l1measure_totalproducedenergy = self.acsource_l1measure_start_address + 48                        # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object L2Measure Modbus Address
        self.acsource_l2measure_start_address = 600
        self.acsource_l2measure_phasevoltage = self.acsource_l2measure_start_address + 0                                # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.acsource_l2measure_current = self.acsource_l2measure_start_address + 2                                     # Property ID: 4, [A] (float). Current RMS measured.
        self.acsource_l2measure_activepower = self.acsource_l2measure_start_address + 4                                 # Property ID: 8, [W] (float). Active power measured.
        self.acsource_l2measure_reactivepower = self.acsource_l2measure_start_address + 6                               # Property ID: 12, [VAR] (float). Reactive power measured.
        self.acsource_l2measure_apparentpower = self.acsource_l2measure_start_address + 8                               # Property ID: 16, [VA] (float). Apparent power measured.
        self.acsource_l2measure_cosphi = self.acsource_l2measure_start_address + 10                                     # Property ID: 20, [-] (float). Power factor measured.
        self.acsource_l2measure_daypeakpower = self.acsource_l2measure_start_address + 12                               # Property ID: 24, [VA] (float). Peak power of the current day.
        self.acsource_l2measure_previousdaypeakpower = self.acsource_l2measure_start_address + 14                       # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.acsource_l2measure_dayminactivepower = self.acsource_l2measure_start_address + 16                          # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.acsource_l2measure_previousdayminactivepower = self.acsource_l2measure_start_address + 18                  # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.acsource_l2measure_daymaxactivepower = self.acsource_l2measure_start_address + 20                          # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.acsource_l2measure_previousdaymaxactivepower = self.acsource_l2measure_start_address + 22                  # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.acsource_l2measure_dayconsumedenergy = self.acsource_l2measure_start_address + 28                          # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.acsource_l2measure_previousdayconsumedenergy = self.acsource_l2measure_start_address + 30                  # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.acsource_l2measure_resetableconsumedenergy = self.acsource_l2measure_start_address + 32                    # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.acsource_l2measure_totalconsumedenergy = self.acsource_l2measure_start_address + 36                        # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.acsource_l2measure_dayproducedenergy = self.acsource_l2measure_start_address + 40                          # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.acsource_l2measure_previousdayproducedenergy = self.acsource_l2measure_start_address + 42                  # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.acsource_l2measure_resetableproducedenergy = self.acsource_l2measure_start_address + 44                    # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.acsource_l2measure_totalproducedenergy = self.acsource_l2measure_start_address + 48                        # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object L3Measure Modbus Address
        self.acsource_l3measure_start_address = 900
        self.acsource_l3measure_phasevoltage = self.acsource_l3measure_start_address + 0                                # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.acsource_l3measure_current = self.acsource_l3measure_start_address + 2                                     # Property ID: 4, [A] (float). Current RMS measured.
        self.acsource_l3measure_activepower = self.acsource_l3measure_start_address + 4                                 # Property ID: 8, [W] (float). Active power measured.
        self.acsource_l3measure_reactivepower = self.acsource_l3measure_start_address + 6                               # Property ID: 12, [VAR] (float). Reactive power measured.
        self.acsource_l3measure_apparentpower = self.acsource_l3measure_start_address + 8                               # Property ID: 16, [VA] (float). Apparent power measured.
        self.acsource_l3measure_cosphi = self.acsource_l3measure_start_address + 10                                     # Property ID: 20, [-] (float). Power factor measured.
        self.acsource_l3measure_daypeakpower = self.acsource_l3measure_start_address + 12                               # Property ID: 24, [VA] (float). Peak power of the current day.
        self.acsource_l3measure_previousdaypeakpower = self.acsource_l3measure_start_address + 14                       # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.acsource_l3measure_dayminactivepower = self.acsource_l3measure_start_address + 16                          # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.acsource_l3measure_previousdayminactivepower = self.acsource_l3measure_start_address + 18                  # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.acsource_l3measure_daymaxactivepower = self.acsource_l3measure_start_address + 20                          # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.acsource_l3measure_previousdaymaxactivepower = self.acsource_l3measure_start_address + 22                  # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.acsource_l3measure_dayconsumedenergy = self.acsource_l3measure_start_address + 28                          # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.acsource_l3measure_previousdayconsumedenergy = self.acsource_l3measure_start_address + 30                  # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.acsource_l3measure_resetableconsumedenergy = self.acsource_l3measure_start_address + 32                    # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.acsource_l3measure_totalconsumedenergy = self.acsource_l3measure_start_address + 36                        # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.acsource_l3measure_dayproducedenergy = self.acsource_l3measure_start_address + 40                          # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.acsource_l3measure_previousdayproducedenergy = self.acsource_l3measure_start_address + 42                  # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.acsource_l3measure_resetableproducedenergy = self.acsource_l3measure_start_address + 44                    # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.acsource_l3measure_totalproducedenergy = self.acsource_l3measure_start_address + 48                        # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object Source Modbus Address
        self.acsource_source_start_address = 1200
        self.acsource_source_type = self.acsource_source_start_address + 3                                              # Property ID: 2, [-] (enum). Type
        self.acsource_source_gridcode = self.acsource_source_start_address + 5                                          # Property ID: 3, [-] (enum). Grid code
        self.acsource_source_connectionallowed = self.acsource_source_start_address + 7                                 # Property ID: 4, [-] (bool). Used to allowed or not the connection to the source.
        self.acsource_source_gridfeedingallowed = self.acsource_source_start_address + 8                                # Property ID: 5, [-] (bool). Used to allowed or not the grid-feeding.
        self.acsource_source_ratedcurrent = self.acsource_source_start_address + 9                                      # Property ID: 6, [A] (float). Rated current (minimum value of circuit breaker nominal current and grid/genset nominal current).
        self.acsource_source_relativeangletolerance = self.acsource_source_start_address + 11                           # Property ID: 7, [°] (float). Tolerance of the relative angle inbetween phases
        self.acsource_source_allowindividualphaseconnection = self.acsource_source_start_address + 13                   # Property ID: 8, [-] (bool). Allow individual phase connection. If false, connect only when all phases meets required conditions.
        self.acsource_source_mindisconnetedtimebeforenewconnection = self.acsource_source_start_address + 14            # Property ID: 9, [s] (float). Minimum disconneted time before allowing a new connection.
        self.acsource_source_activateinertialsmoothing = self.acsource_source_start_address + 16                        # Property ID: 10, [-] (bool). Activate transient smoothing. When severe power consumption variations occur, this can cause severe voltage and frequency fluctuation of gensets. This feature help to reduce such fluctuations.
        self.acsource_source_compensateloaddccurrent = self.acsource_source_start_address + 17                          # Property ID: 11, [-] (bool). Compensation of the AcLoad d.c. current
        self.acsource_source_enablefastenvelopedetection = self.acsource_source_start_address + 20                      # Property ID: 13, [-] (bool). Enable fast loss detection based on a the comparisson of instantaneous voltage and a sinusoidal envelope.
        self.acsource_source_envelopetolerance = self.acsource_source_start_address + 21                                # Property ID: 14, [%] (float). Size of the envelope for the fast loss detection.
        self.acsource_source_antiislandingdetectionlevel = self.acsource_source_start_address + 24                      # Property ID: 16, [%] (float). Anti-islanding detection level used by the \"vector shift\" method.
        self.acsource_source_antiislandingfrequency = self.acsource_source_start_address + 26                           # Property ID: 17, [Hz] (float). Anti-islanding frequency used by the \"vector shift\" method.
        self.acsource_source_antiislandingperturbationamplitude = self.acsource_source_start_address + 28               # Property ID: 18, [%] (float). Anti-islanding perturbation amplitude used by the \"vector shift\" method.
        self.acsource_source_antiislandingminimalamplitude = self.acsource_source_start_address + 30                    # Property ID: 19, [%] (float). Anti-islanding minimal amplitude used by the \"vector shift\" method.
        self.acsource_source_overvoltagecurveu1 = self.acsource_source_start_address + 35                               # Property ID: 22, [%] (float). P1 voltage of OV curve. EN 50549-1 chapter 4.5.4. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_overvoltagecurvet1 = self.acsource_source_start_address + 37                               # Property ID: 23, [s] (float). P1 time of OV curve. EN 50549-1 chapter 4.5.4. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_overvoltagecurveu2 = self.acsource_source_start_address + 39                               # Property ID: 24, [%] (float). P2 voltage of OV curve. EN 50549-1 chapter 4.5.4. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_overvoltagecurvet2 = self.acsource_source_start_address + 41                               # Property ID: 25, [s] (float). P2 time of OV curve. EN 50549-1 chapter 4.5.4. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_overvoltagecurveu3 = self.acsource_source_start_address + 43                               # Property ID: 26, [%] (float). P3 voltage of OV curve. EN 50549-1 chapter 4.5.4. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_overvoltagecurvet3 = self.acsource_source_start_address + 45                               # Property ID: 27, [s] (float). P3 time of OV curve. EN 50549-1 chapter 4.5.4. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_maxvoltagefaultonset = self.acsource_source_start_address + 47                             # Property ID: 28, [%] (float). Maximum voltage for fault onset. EN 50549-1 chapter 4.5.4.
        self.acsource_source_maxpermanentvoltage = self.acsource_source_start_address + 49                              # Property ID: 29, [%] (float). Maximum permanent voltage. EN 50549-1 chapter 4.4.4.
        self.acsource_source_minpermanentvoltage = self.acsource_source_start_address + 51                              # Property ID: 30, [%] (float). Mininum permanent voltage. EN 50549-1 chapter 4.4.4.
        self.acsource_source_minvoltagefaultonset = self.acsource_source_start_address + 53                             # Property ID: 31, [%] (float). Minimum voltage for fault onset. EN 50549-1 chapter 4.5.3.2.
        self.acsource_source_undervoltagecurvet2 = self.acsource_source_start_address + 55                              # Property ID: 32, [s] (float). P2 time of UV curve. EN 50549-1 chapter 4.5.3.2. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_undervoltagecurveu1 = self.acsource_source_start_address + 57                              # Property ID: 33, [%] (float). P1 voltage of UV curve. EN 50549-1 chapter 4.5.3.2. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_undervoltagecurvet1 = self.acsource_source_start_address + 59                              # Property ID: 34, [s] (float). P1 time of UV curve. EN 50549-1 chapter 4.5.3.2. VDE-AR-N 4105 chapter 5.7.3.2.
        self.acsource_source_zerocurrentmodeenabled = self.acsource_source_start_address + 61                           # Property ID: 35, [-] (bool). Zero current mode. EN 50549-1 chapter 4.7.4.2.2. VDE-AR-N chapter 5.7.3.1.
        self.acsource_source_zerocurrentmodeovervoltagethreshold = self.acsource_source_start_address + 62              # Property ID: 36, [%] (float). Static voltage range overvoltage for zero current mode. EN 50549-1 chapter 4.7.4.2.2. Behaviour during fault (OVRT) acrrording to VDE AR N 4105 chapter 5.7.3.1.
        self.acsource_source_zerocurrentmodeundervoltagethreshold = self.acsource_source_start_address + 64             # Property ID: 37, [%] (float). Static voltage range undervoltage for zero current mode. EN 50549-1 chapter 4.7.4.2.2. Behaviour during fault (UVRT) acrrording to VDE AR N 4105 chapter 5.7.3.1.
        self.acsource_source_thresholdfrequencyforoverfrequency = self.acsource_source_start_address + 66               # Property ID: 38, [Hz] (float). Threshold frequency (relative to \"Nominal frequency\" (id 22)) of frequency-dependant active power during over-frequency situation. Use a huge value to disable the feature. EN 50549-1 chapter 4.6.1. VDE-AR-N 4105 chapter 5.7.4.2.3 figure15. AS/NZS 4777.2 section 4.5.3.3 (f ULCO, upper limit of the continous operation range for frequency).
        self.acsource_source_statismforoverfrequency = self.acsource_source_start_address + 68                          # Property ID: 39, [%] (float). Static value of frequency-dependant active power during over-frequency situation. EN 50549-1 chapter 4.6.1. VDE-AR-N 4105 chapter 5.7.4.2.3 figure15.
        self.acsource_source_intensionaldelayforoverfrequency = self.acsource_source_start_address + 70                 # Property ID: 40, [s] (float). Intentional delay before activation of the function of active power adjustmen at over-frequency. EN 50549-1 chapter 4.6.1.
        self.acsource_source_disablingthresholdfrequencyforoverfrequency = self.acsource_source_start_address + 72      # Property ID: 41, [Hz] (float). Disabling threshold frequency fstop (relative to \"Nominal frequency\" (id 22)) of frequency-dependant active power during over-frequency situation. Disabled if value is greather or equal than \"Threshold frequency for OF\" (id 38). EN 50549-1 chapter 4.6.1. AS/NZS 4777.2 section 4.5.3.1 (f ULCO - f hyst, frequency for returning to continous operation).
        self.acsource_source_disablingdelayforoverfrequency = self.acsource_source_start_address + 74                   # Property ID: 42, [s] (float). Disabling delay (tstop) of frequency-dependant active power during over-frequency situation. EN 50549-1 chapter 4.6.1. AS/NZS 4777.2 section 4.5.3.3.
        self.acsource_source_prefforoverfrequency = self.acsource_source_start_address + 76                             # Property ID: 43, [-] (enum). Power reference of frequency-dependant active power during over-frequency situation. EN 50549-1 chapter 4.6.1
        self.acsource_source_thresholdfrequencyforunderfrequency = self.acsource_source_start_address + 78              # Property ID: 44, [Hz] (float). Threshold frequency (relative to \"Nominal frequency\" (id 22)) of frequency-dependant active power during under-frequency situation.  Use a small value to disable the feature. EN 50549-1 chapter 4.6.2. VDE-AR-N 4105 chapter 5.7.4.2.3 figure15. AS/NZS 4777.2 section 4.5.3.2 (f LLCO, lower limit of the continous operation range for frequency).
        self.acsource_source_statismforunderfrequency = self.acsource_source_start_address + 80                         # Property ID: 45, [%] (float). Static value of frequency-dependant active power during under-frequency situation. EN 50549-1 chapter 4.6.2. VDE-AR-N 4105 chapter 5.7.4.2.3 figure15.
        self.acsource_source_intensionaldelayforunderfrequency = self.acsource_source_start_address + 82                # Property ID: 46, [s] (float). Intentional delay before activation of the function of active power adjustmen at under-frequency. EN 50549-1 chapter 4.6.2.
        self.acsource_source_prefforunderfrequency = self.acsource_source_start_address + 84                            # Property ID: 47, [-] (enum). Power reference of frequency-dependant active power during under-frequency situation. EN 50549-1 chapter 4.6.2
        self.acsource_source_overexcitedcosphicapacity = self.acsource_source_start_address + 86                        # Property ID: 48, [-] (float). Over-excited displacement factor minimal capacity. EN 50549-1 chapter 4.7.2.2. VDE-AR-N 4105 chapter 5.7.2.2.2 and 5.7.2.3. AS/NZS 4777.2 section 2.6
        self.acsource_source_underexcitedcosphicapacity = self.acsource_source_start_address + 88                       # Property ID: 49, [-] (float). Under-excited displacement factor minimal capacity. EN 50549-1 chapter 4.7.2.2. VDE-AR-N 4105 chapter 5.7.2.2.2. AS/NZS 4777.2 section 2.6
        self.acsource_source_reactivepowermethod = self.acsource_source_start_address + 90                              # Property ID: 50, [-] (enum). Reactive power method. EN 50549-1 chapter 4.7.2.3. VDE-AR-N 4105 chapter 5.7.2.4.
        self.acsource_source_reactivepowersetpoint = self.acsource_source_start_address + 92                            # Property ID: 51, [%] (float). Produced reactive power setpoint, percentage of rated active power. Negative value for a consummed reactive power. EN 50549-1 chapter 4.7.2.3.2. VDE-AR-N 4105 chapter 5.7.2.5
        self.acsource_source_cosphisetpoint = self.acsource_source_start_address + 94                                   # Property ID: 52, [-] (float). Displacement factor cos(φ) setpoint. EN-50549-1 chapter 4.7.2.3.2. VDE-AR-N 4105 chapter 5.7.2.4 Re:c)
        self.acsource_source_reactivepowerdirection = self.acsource_source_start_address + 96                           # Property ID: 53, [-] (enum). Reactive power direction (over-excited or under-excited) for displacement factor and reactive power setpoints. EN 50549-1 chapter 4.7.2.3.2. VDE-AR-N 4105 chapter 5.7.2.4 Re:c)
        self.acsource_source_reactivepowercurveq1 = self.acsource_source_start_address + 98                             # Property ID: 54, [%] (float). Point 1 ordinate, produced normalised reactive power of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a). AS/NZS 4777.2 section 3.3.2.3
        self.acsource_source_reactivepowercurveq2 = self.acsource_source_start_address + 100                            # Property ID: 55, [%] (float). Point 2 ordinate, produced normalised reactive power of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a). AS/NZS 4777.2 section 3.3.2.3
        self.acsource_source_reactivepowercurveq3 = self.acsource_source_start_address + 102                            # Property ID: 56, [%] (float). Point 3 ordinate, produced normalised reactive power of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a). AS/NZS 4777.2 section 3.3.2.3
        self.acsource_source_reactivepowercurveq4 = self.acsource_source_start_address + 104                            # Property ID: 57, [%] (float). Point 4 ordinate, produced normalised reactive power of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a). AS/NZS 4777.2 section 3.3.2.3
        self.acsource_source_reactivepowercurveu1 = self.acsource_source_start_address + 106                            # Property ID: 58, [%] (float). Point 1 abscissa, normalised voltage of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a)
        self.acsource_source_reactivepowercurveu2 = self.acsource_source_start_address + 108                            # Property ID: 59, [%] (float). Point 2 abscissa, normalised voltage of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a)
        self.acsource_source_reactivepowercurveu3 = self.acsource_source_start_address + 110                            # Property ID: 60, [%] (float). Point 3 abscissa, normalised voltage of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a)
        self.acsource_source_reactivepowercurveu4 = self.acsource_source_start_address + 112                            # Property ID: 61, [%] (float). Point 4 abscissa, normalised voltage of Q(U) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.4 Re: a)
        self.acsource_source_reactivepowercontroltimebehaviour = self.acsource_source_start_address + 114               # Property ID: 62, [s] (float). Time behaviour of reactive power control (3 Tau of PT-1). EN 50549-1 chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.5 figure10. AS/NZS 4777.2 section 3.3.2.1
        self.acsource_source_reactivepowercontrolcosphimin = self.acsource_source_start_address + 116                   # Property ID: 63, [-] (float). Minimum displacement factor in Q(U) mode. EN50549-1 chapter 4.7.2.3.3. VDE-AR-N 4105 chapter 5.7.2.5. AS/NZS 4777.2 section 2.6
        self.acsource_source_reactivepowercontrollockinactivepower = self.acsource_source_start_address + 118           # Property ID: 64, [%] (float). Lock-in active power in Q(U) mode, percentage of rated active power. EN 50549-1 chapter 4.7.2.3.3. VDE-AR-N 4108 chapter 5.7.2.5.
        self.acsource_source_reactivepowercontrollockoutactivepower = self.acsource_source_start_address + 120          # Property ID: 65, [%] (float). Lock-out active power in Q(U) mode, percentage of rated active power. EN 50549-1 chapter 4.7.2.3.3. VDE-AR-N 4108 chapter 5.7.2.5.
        self.acsource_source_reactivepowercurvecosphioverexcited1 = self.acsource_source_start_address + 122            # Property ID: 66, [-] (float). Point 1 ordinate, over-excited displacement factor of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvecosphioverexcited2 = self.acsource_source_start_address + 124            # Property ID: 67, [-] (float). Point 2 ordinate, over-excited displacement factor of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvecosphiunderexcited3 = self.acsource_source_start_address + 126           # Property ID: 68, [-] (float). Point 3 ordinate, under-excited displacement factor of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvecosphiunderexcited4 = self.acsource_source_start_address + 128           # Property ID: 69, [-] (float). Point 4 ordinate, under-excited displacement factor of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvep1 = self.acsource_source_start_address + 130                            # Property ID: 70, [%] (float). Point 1 abscissa, normalised produced active power of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvep2 = self.acsource_source_start_address + 132                            # Property ID: 71, [%] (float). Point 2 abscissa, normalised produced active power of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvep3 = self.acsource_source_start_address + 134                            # Property ID: 72, [%] (float). Point 3 abscissa, normalised produced active power of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_reactivepowercurvep4 = self.acsource_source_start_address + 136                            # Property ID: 73, [%] (float). Point 4 abscissa, normalised produced active power of cos(φ)=f(P) reactive power characteristic curve. EN 50549-1 figure 16, chapter 4.7.2.3.4. VDE-AR-N 4105 chapter 5.7.2.4 Re: b)
        self.acsource_source_overvoltagethresholdstage2 = self.acsource_source_start_address + 138                      # Property ID: 74, [%] (float). Overvoltage threshold stage 2 [59 >>] of overvoltage protection. EN 50549-1 chapter 4.9.3.3.
        self.acsource_source_overvoltageoperatetimestage2 = self.acsource_source_start_address + 140                    # Property ID: 75, [s] (float). Overvoltage operate time stage 2 [59 >>] of overvoltage protection. EN 50549-1 chapter 4.9.3.3.
        self.acsource_source_overvoltagethresholdstage1 = self.acsource_source_start_address + 142                      # Property ID: 76, [%] (float). Overvoltage threshold stage 1 [59 >] of overvoltage protection. EN 50549-1 chapter 4.9.3.3.
        self.acsource_source_overvoltageoperatetimestage1 = self.acsource_source_start_address + 144                    # Property ID: 77, [s] (float). Overvoltage operate time stage 1 [59 >] of overvoltage protection. EN 50549-1 chapter 4.9.3.3.
        self.acsource_source_overvoltagethreshold10minmean = self.acsource_source_start_address + 146                   # Property ID: 78, [%] (float). Overvoltage threshold 10 min mean protection. EN 50549-1 chapter 4.9.3.4.
        self.acsource_source_undervoltagethresholdstage1 = self.acsource_source_start_address + 148                     # Property ID: 79, [%] (float). Undervoltage threshold stage 1 [27 <] of undervoltage protection. EN 50549-1 chapter 4.9.3.2.
        self.acsource_source_undervoltageoperatetimestage1 = self.acsource_source_start_address + 150                   # Property ID: 80, [s] (float). Undervoltage operate time stage 1 [27 <] of undervoltage protection. EN 50549-1 chapter 4.9.3.2.
        self.acsource_source_undervoltagethresholdstage2 = self.acsource_source_start_address + 152                     # Property ID: 81, [%] (float). Undervoltage threshold stage 2 [27 <<] of undervoltage protection. EN 50549-1 chapter 4.9.3.2.
        self.acsource_source_undervoltageoperatetimestage2 = self.acsource_source_start_address + 154                   # Property ID: 82, [s] (float). Undervoltage operate time stage 12[27 <<] of undervoltage protection. EN 50549-1 chapter 4.9.3.2.
        self.acsource_source_overfrequencythresholdstage1 = self.acsource_source_start_address + 158                    # Property ID: 84, [Hz] (float). Overfrequency threshold (relative to \"Nominal frequency\" (id 22)) stage 1 [81 >] of overfrequency protection. EN 50549-1 chapter 4.9.3.6.
        self.acsource_source_overfrequencyoperatetimestage1 = self.acsource_source_start_address + 160                  # Property ID: 85, [s] (float). Overfrequency operate time stage 1 [81 >] of overfrequency protection. EN 50549-1 chapter 4.9.3.6.
        self.acsource_source_overfrequencythresholdstage2 = self.acsource_source_start_address + 162                    # Property ID: 86, [Hz] (float). Overfrequency threshold (relative to \"Nominal frequency\" (id 22)) stage 2 [81 >>] of overfrequency protection. EN 50549-1 chapter 4.9.3.6.
        self.acsource_source_overfrequencyoperatetimestage2 = self.acsource_source_start_address + 164                  # Property ID: 87, [s] (float). Overfrequency operate time stage 2 [81 >>] of overfrequency protection. EN 50549-1 chapter 4.9.3.6.
        self.acsource_source_underfrequencythresholdstage2 = self.acsource_source_start_address + 166                   # Property ID: 88, [Hz] (float). Underfrequency threshold (relative to \"Nominal frequency\" (id 22)) stage 2 [81 <<] of underfrequency protection. EN 50549-1 chapter 4.9.3.5.
        self.acsource_source_underfrequencyoperatetimestage2 = self.acsource_source_start_address + 168                 # Property ID: 89, [s] (float). Underfrequency operate time stage 2 [81 <<] of underfrequency protection. EN 50549-1 chapter 4.9.3.5.
        self.acsource_source_underfrequencythresholdstage1 = self.acsource_source_start_address + 170                   # Property ID: 90, [Hz] (float). Underfrequency threshold (relative to \"Nominal frequency\" (id 22)) stage 1 [81 <] of underfrequency protection. EN 50549-1 chapter 4.9.3.5.
        self.acsource_source_underfrequencyoperatetimestage1 = self.acsource_source_start_address + 172                 # Property ID: 91, [s] (float). Underfrequency operate time stage 1 [81 <] of underfrequency protection. EN 50549-1 chapter 4.9.3.5.
        self.acsource_source_cmdentryidxtoswitchtonarrowfrequencyband = self.acsource_source_start_address + 176        # Property ID: 93, [-] (int). Index of the command entry interface used to switching to the narrow frequency band. (0 value disable remote operation). EN 50549-1 chapter 4.9.5
        self.acsource_source_overfrequencythresholdnarrowband = self.acsource_source_start_address + 178                # Property ID: 94, [Hz] (float). Overfrequency threshold (relative to \"Nominal frequency\" (id 22))  for the narrow band of overfrequency protection. EN 50549-1 chapter 4.9.5.
        self.acsource_source_overfrequencyoperatetimenarrowband = self.acsource_source_start_address + 180              # Property ID: 95, [s] (float). Overfrequency operate time for the narrow band of overfrequency protection. EN 50549-1 chapter 4.9.5.
        self.acsource_source_underfrequencythresholdnarrowband = self.acsource_source_start_address + 182               # Property ID: 96, [Hz] (float). Underfrequency threshold (relative to \"Nominal frequency\" (id 22)) for the narrow band of underfrequency protection. EN 50549-1 chapter 4.9.5.
        self.acsource_source_underfrequencyoperatetimenarrowband = self.acsource_source_start_address + 184             # Property ID: 97, [s] (float). Underfrequency operate time  for the narrow band of underfrequency protection. EN 50549-1 chapter 4.9.5.
        self.acsource_source_uppervoltageforautoreconnection = self.acsource_source_start_address + 186                 # Property ID: 98, [%] (float). Upper voltage for automatic reconnection after tripping. EN 50549-1 chapter 4.10.2.
        self.acsource_source_lowervoltageforautoreconnection = self.acsource_source_start_address + 188                 # Property ID: 99, [%] (float). Lower voltage for automatic reconnection after tripping. EN 50549-1 chapter 4.10.2.
        self.acsource_source_upperfrequencyforautoreconnection = self.acsource_source_start_address + 190               # Property ID: 100, [Hz] (float). Upper frequency (relative to \"Nominal frequency\" (id 22)) for automatic reconnection after tripping. EN 50549-1 chapter 4.10.2.
        self.acsource_source_lowerfrequencyforautoreconnection = self.acsource_source_start_address + 192               # Property ID: 101, [Hz] (float). Lower frequency (relative to \"Nominal frequency\" (id 22)) for automatic reconnection after tripping. EN 50549-1 chapter 4.10.2.
        self.acsource_source_observationtimeforautoreconnection = self.acsource_source_start_address + 194              # Property ID: 102, [s] (float). Observation time for automatic reconnection after tripping. EN 50549-1 chapter 4.10.2.
        self.acsource_source_activepowerincreasegradientforautoreconnection = self.acsource_source_start_address + 196  # Property ID: 103, [%/min] (float). Active power increase gradient when automatic reconnection after tripping or at the end of an over/under frequency situation. EN 50549-1 chapter 4.10.2. AS/NZS 4777.2 section 4.5.3
        self.acsource_source_uppervoltageforstartgeneration = self.acsource_source_start_address + 198                  # Property ID: 104, [%] (float). Upper voltage for automatic reconnection after tripping. EN 50549-1 chapter 4.10.3.
        self.acsource_source_lowervoltageforstartgeneration = self.acsource_source_start_address + 200                  # Property ID: 105, [%] (float). Lower voltage for automatic reconnection after tripping. EN 50549-1 chapter 4.10.3.
        self.acsource_source_upperfrequencyforstartgeneration = self.acsource_source_start_address + 202                # Property ID: 106, [Hz] (float). Upper frequency (relative to \"Nominal frequency\" (id 22)) for automatic reconnection after tripping. EN 50549-1 chapter 4.10.3.
        self.acsource_source_lowerfrequencyforstartgeneration = self.acsource_source_start_address + 204                # Property ID: 107, [Hz] (float). Lower frequency (relative to \"Nominal frequency\" (id 22)) for automatic reconnection after tripping. EN 50549-1 chapter 4.10.3.
        self.acsource_source_observationtimeforstartgeneration = self.acsource_source_start_address + 206               # Property ID: 108, [s] (float). Observation time for connection. EN 50549-1 chapter 4.10.3.
        self.acsource_source_activepowerincreasegradientforstartgeneration = self.acsource_source_start_address + 208   # Property ID: 109, [%/min] (float). Active power increase gradient after connection. EN 50549-1 chapter 4.10.3.
        self.acsource_source_cmdentryidxtoallowtransfertripping = self.acsource_source_start_address + 210              # Property ID: 110, [-] (int). Index of the command entry interface used to allow transfer trip. DRED port index used for DRM0. (0 value disable remote operation). EN 50549-1 chapter 4.9.5. AS/NZS 4777.2 section 3.2.
        self.acsource_source_cmdentryidxforceasingproducedactivepower = self.acsource_source_start_address + 212        # Property ID: 111, [-] (int). Index of the command entry interface used for ceasing produced active power (0 value disable remote operation). EN 50549-1 chapter 4.11.1.
        self.acsource_source_cmdentryidxforreductionofproducedactivepoweronsetpoint = self.acsource_source_start_address + 214    # Property ID: 112, [-] (int). Index of the command entry interface used for reduction of produced active power (0 value disable remote operation). EN 50549-1 chapter 4.11.2.
        self.acsource_source_reductionofproducedactivepowersetpoint = self.acsource_source_start_address + 216          # Property ID: 113, [%] (float). Reduced produced active power in case of remote operation. EN 50549-1 chapter 4.11.2.
        self.acsource_source_reductionofproducedactivepowersetpointslope = self.acsource_source_start_address + 218     # Property ID: 114, [%/s] (float). Slope for the reduction of produced active power in case of remote operation. Slope limitation is disable if this value is set to 0. EN 50549-1 chapter 4.11.2.
        self.acsource_source_voltagetostartproducedactivepowerreduction = self.acsource_source_start_address + 220      # Property ID: 115, [%] (float). Voltage at which the the produced normalised active power start to be reduced. EN 50549-1 chapter 4.7.3. AS/NZS 4777.2 section 3.3.2.2
        self.acsource_source_voltageforreducedproducedactivepower = self.acsource_source_start_address + 222            # Property ID: 116, [%] (float). Voltage over which the produced normalised active power is reduced to \"Reduced produced active power\" (id 130). AS/NZS 4777.2 section 3.3.2.2
        self.acsource_source_activepowercurvetimeconstant = self.acsource_source_start_address + 224                    # Property ID: 117, [s] (float). Time constant of voltage-dependant active power curves P(U). TOR Erzeuger Typ A chapter 5.3.6. EN 50549-1 chapter 4.7.3. AS/NZS 4777.2 section 3.3.2.1
        self.acsource_source_activepowercurvepref = self.acsource_source_start_address + 226                            # Property ID: 118, [-] (enum). Power reference of voltage-dependant active power curves P(U). TOR Erzeuger Typ A chapter 5.3.6.
        self.acsource_source_usetriphasetargetactivepower = self.acsource_source_start_address + 229                    # Property ID: 120, [-] (bool). Use of \"Target active power per phase\" (id 121) instead of \"Target sourced active power\" (id 13).
        self.acsource_source_targetactivepowerperphase = self.acsource_source_start_address + 230                       # Property ID: 121, [W] (float). Target active power per phase. Positive when the AC source is generating active power and negative when the AC source is consumming active power.
        self.acsource_source_setpointslevel = self.acsource_source_start_address + 232                                  # Property ID: 122, [Level] (int). setpoints priority level
        self.acsource_source_phaseexistance = self.acsource_source_start_address + 240                                  # Property ID: 126, [-] (bitfield). Indicate which phase(s) is(are) used for this AcSource
        self.acsource_source_antiislanding = self.acsource_source_start_address + 242                                   # Property ID: 127, [-] (enum). Anti-islanding function activation and choice of the detection method.
        self.acsource_source_antiislandingrocofthreshold = self.acsource_source_start_address + 244                     # Property ID: 128, [Hz/s] (float). Anti-islanding RoCoF threshold used by the \"RoCoF tripping\" method.
        self.acsource_source_antiislandingrocofoperatetime = self.acsource_source_start_address + 246                   # Property ID: 129, [s] (float). Anti-islanding RoCoF operate time used by the \"RoCoF tripping\" method.
        self.acsource_source_reducedproducedactivepower = self.acsource_source_start_address + 248                      # Property ID: 130, [%] (float). Reduced produced normalised active power at voltages over \"Voltage for reduced produced P\" (id 116). EN 50549-1 chapter 4.7.3. AS/NZS 4777.2 section 3.3.2.2. Note that values < 0% correspond to inverting the power sign, i.e. switching to consumption. (CEI 0-21 chapter 8.5.3.1 / Bbis.7.1)
        self.acsource_source_reducedconsummedactivepower = self.acsource_source_start_address + 250                     # Property ID: 131, [%] (float). Reduced consummed normalised active power at voltage under \"Voltage for reduced consummed P\" (id 132). AS/NZS 4777.2 section 3.4.3. Note that values < 0% correspond to inverting the power sign, i.e. switching to prduction.
        self.acsource_source_voltageforreducedconsummedactivepower = self.acsource_source_start_address + 252           # Property ID: 132, [%] (float). Voltage under which the normalised consummed active power is reduced to \"Reduced consummed active power\" (id 131). AS/NZS 4777.2 section 3.4.3
        self.acsource_source_voltagetostartconsummedactivepowerreduction = self.acsource_source_start_address + 254     # Property ID: 133, [%] (float). Voltage at which the the consummed normalised active power start to be reduced. AS/NZS 4777.2 section 3.4.3
        self.acsource_source_transitionfrequencyforoverfrequency = self.acsource_source_start_address + 256             # Property ID: 134, [Hz] (float). Frequency (relative to \"Nominal frequency\" (id 22)) where power output level is zero of frequency-dependant active power during over-frequency situation. Use a huge value to disable the feature. AS/NZS 4777.2 section 4.5.3.3 (f transition).
        self.acsource_source_pminfrequencyforoverfrequency = self.acsource_source_start_address + 258                   # Property ID: 135, [Hz] (float). Frequency (relative to \"Nominal frequency\" (id 22)) where power input level is maximum of frequency-dependant active power during over-frequency situation. Use a huge value to disable the feature. AS/NZS 4777.2 section 4.5.3.3 (f Pmin).
        self.acsource_source_stopchfrequencyforunderfrequency = self.acsource_source_start_address + 260                # Property ID: 136, [Hz] (float). Frequency (relative to \"Nominal frequency\" (id 22)) where power output level is zero of frequency-dependant active power during under-frequency situation. Use a huge value to disable the feature. AS/NZS 4777.2 section 4.5.3.2 (f stop-ch).
        self.acsource_source_pmaxfrequencyforunderfrequency = self.acsource_source_start_address + 262                  # Property ID: 137, [Hz] (float). Frequency (relative to \"Nominal frequency\" (id 22)) where power output level is maximum of frequency-dependant active power during under-frequency situation. Use a huge value to disable the feature. AS/NZS 4777.2 section 4.5.3.2 (f Pmax).
        self.acsource_source_hystfrequencyforoverunderfrequency = self.acsource_source_start_address + 264              # Property ID: 138, [Hz] (float). Frequency hystereris for returning in continous operation after over/under-frequency situation. AS/NZS 4777.2 section 4.5.3.1 (f hyst).
        self.acsource_source_compensateharmonics = self.acsource_source_start_address + 266                             # Property ID: 139, [-] (bool). Compensation of the invreter current harmonics
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat10 = self.acsource_source_start_address + 267    # Property ID: 140, [-] (int). Index of the command entry interface used for reduction of produced active power at 10% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat20 = self.acsource_source_start_address + 269    # Property ID: 141, [-] (int). Index of the command entry interface used for reduction of produced active power at 20% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat30 = self.acsource_source_start_address + 271    # Property ID: 142, [-] (int). Index of the command entry interface used for reduction of produced active power at 30% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat40 = self.acsource_source_start_address + 273    # Property ID: 143, [-] (int). Index of the command entry interface used for reduction of produced active power at 40% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat50 = self.acsource_source_start_address + 275    # Property ID: 144, [-] (int). Index of the command entry interface used for reduction of produced active power at 50% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat60 = self.acsource_source_start_address + 277    # Property ID: 145, [-] (int). Index of the command entry interface used for reduction of produced active power at 60% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat70 = self.acsource_source_start_address + 279    # Property ID: 146, [-] (int). Index of the command entry interface used for reduction of produced active power at 70% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat80 = self.acsource_source_start_address + 281    # Property ID: 147, [-] (int). Index of the command entry interface used for reduction of produced active power at 80% percent of the rated power (0 value disable remote operation).
        self.acsource_source_cmdentryidxforreductionofproducedactivepowerat90 = self.acsource_source_start_address + 283    # Property ID: 148, [-] (int). Index of the command entry interface used for reduction of produced active power at 90% percent of the rated power (0 value disable remote operation).
        self.acsource_source_phasebalancing = self.acsource_source_start_address + 285                                  # Property ID: 149, [-] (enum). Method used to distribute the total required power to each phase.
        self.acsource_source_voltageandfrequencytolerance = self.acsource_source_start_address + 287                    # Property ID: 150, [-] (enum). Tolarance to voltage and frequency faults.
        self.acsource_source_synchrothreshold = self.acsource_source_start_address + 289                                # Property ID: 151, [V] (float). The voltage differance in between AC-Loads and AC-Source must be smaller than \"Synchro. threshold\" (id 151) during \"Synchro. duration\" (id 152) to allow the connection.
        self.acsource_source_synchroduration = self.acsource_source_start_address + 291                                 # Property ID: 152, [s] (float). The voltage differance in between AC-Loads and AC-Source must be smaller than \"Synchro. threshold\" (id 151) during \"Synchro. duration\" (id 152) to allow the connection.
        self.acsource_source_undervoltagecurveu2 = self.acsource_source_start_address + 293                             # Property ID: 153, [%] (float). UVRT voltage extension at \"Under-voltage curve T1\" (id 34). This modification of the UVRT curve corresponds to CEI 0-21 chapter 8.5.1(b) Fig. 29 (Uclear). To disable this extension set this value equal to \"Under-voltage curve U1\" (id 33).
        self.acsource_source_reactivepowercontrollockinvoltage = self.acsource_source_start_address + 295               # Property ID: 154, [%] (float). Normalised lock-in voltage of cos(φ) = f(P) control according to CEI 0-21 chapter E.2. This feature can be disabled by setting the value equal to \"React. pow. control lock-out volt.\" (id 155).
        self.acsource_source_reactivepowercontrollockoutvoltage = self.acsource_source_start_address + 297              # Property ID: 155, [%] (float). Normalised lock-out voltage of cos(φ) = f(P) control according to CEI 0-21 chapter E.2. This feature can be disabled by setting the value equal to \"React. pow. control lock-in volt.\" (id 154).
        self.acsource_source_clearingdelayforoverunderfrequency = self.acsource_source_start_address + 299              # Property ID: 156, [s] (float). Delay before returning into continous operation after over/under-frequency situation. AS/NZS 4777.2 section 4.5.3.2/4.5.3.3. CEI 0-21 chapter 8.5.3.4. Note that this is similar to tstop (EN 50549-1 Ch. 4.6.1 Fig. 10), but applied in over- and under-frequency conditions.
        self.acsource_source_selftestactivationsignal = self.acsource_source_start_address + 301                        # Property ID: 157, [-] (signal). Activation of the voltage and frequency interface protection self-test according to CEI 0-21 A.4.4. Note that this test can take several minutes and the AC source relays will open/close multiple times, as well as errors and warnings will be present. If the test is passed, the device reconnects automatically to the grid. The test can be interrupted by disconnecting the AC source manually (turn-off system total or disable \"Connection allowed\" (id 4)).
        self.acsource_source_selftestgradientvoltage = self.acsource_source_start_address + 302                         # Property ID: 158, [%/s] (float). Voltage gradient for the threshold variation of voltage protection functions during self-test (CEI 0-21 A.4.4).
        self.acsource_source_selftestgradientfrequency = self.acsource_source_start_address + 304                       # Property ID: 159, [mHz/s] (float). Frequency gradient for the threshold variation of frequency protection functions during self-test (CEI 0-21 A.4.4).
        self.acsource_source_selfteststatus = self.acsource_source_start_address + 306                                  # Property ID: 160, [-] (bitfield). Indicates the current state of the interface protection self-test. Note that a new test is only authorized when the AC Source is connected without errors/warnings.
        self.acsource_source_cmdentryidxforreductionofconsumedactivepoweronsetpoint = self.acsource_source_start_address + 308    # Property ID: 161, [-] (int). Index of the command entry interface used for reduction of consumed active power (0 value disable remote operation).
        self.acsource_source_reductionofconsumedactivepowersetpoint = self.acsource_source_start_address + 310          # Property ID: 162, [W] (float). Reduced consumed active power in case of remote operation. Unlike \"Reduction of produced P\" (id 113), which is expressed as a percentage of the nominal power of inverters connected to the phase (governed by grid connection standards), the reduction of consumed power is expressed in W (per phase).

        # Object L1Source Modbus Address
        self.acsource_l1source_start_address = 1800
        self.acsource_l1source_status = self.acsource_l1source_start_address + 0                                        # Property ID: 0, [-] (enum). Current status.
        self.acsource_l1source_unconnectedreasons = self.acsource_l1source_start_address + 2                            # Property ID: 1, [-] (bitfield). Reasons explaining why the source is not connected.
        self.acsource_l1source_warnings = self.acsource_l1source_start_address + 4                                      # Property ID: 2, [-] (bitfield). Current warnings.
        self.acsource_l1source_errors = self.acsource_l1source_start_address + 6                                        # Property ID: 3, [-] (bitfield). Current errors.
        self.acsource_l1source_causeofdisconnection = self.acsource_l1source_start_address + 8                          # Property ID: 4, [-] (bitfield). Causes of the source disconnection. Note that the value is initialized to 0 (no items checked in the list) until the first connection to the source.
        self.acsource_l1source_voltage10minmean = self.acsource_l1source_start_address + 12                             # Property ID: 6, [%] (float). Compute a 10min period moving average of the voltage.
        self.acsource_l1source_connectionallowed = self.acsource_l1source_start_address + 14                            # Property ID: 7, [-] (bool). Used to allowed or not the connection to the source.
        self.acsource_l1source_gridfeedingallowed = self.acsource_l1source_start_address + 15                           # Property ID: 8, [-] (bool). Used to allowed or not the grid-feeding.
        self.acsource_l1source_maxsourcedactivepower = self.acsource_l1source_start_address + 16                        # Property ID: 9, [W] (float). Max sourced active power sent to the power flow dispatcher.
        self.acsource_l1source_maxsinkedactivepower = self.acsource_l1source_start_address + 18                         # Property ID: 10, [W] (float). Max sinked active power sent to the power flow dispatcher.
        self.acsource_l1source_maxsourcedreactivepower = self.acsource_l1source_start_address + 20                      # Property ID: 11, [VA] (float). Max sourced reactive power sent to the power flow dispatcher.
        self.acsource_l1source_maxsinkedreactivepower = self.acsource_l1source_start_address + 22                       # Property ID: 12, [VA] (float). Max sinked reactive power sent to the power flow dispatcher.
        self.acsource_l1source_targetsourcedactivepower = self.acsource_l1source_start_address + 24                     # Property ID: 13, [W] (float). Target sourced active power sent to the power flow dispatcher.
        self.acsource_l1source_sinkedlimitlevel = self.acsource_l1source_start_address + 28                             # Property ID: 15, [-] (int). Sinked limit level sent to the power flow dispatcher.
        self.acsource_l1source_setpointslevel = self.acsource_l1source_start_address + 30                               # Property ID: 16, [-] (int). Setpoints level sent to the power flow dispatcher.
        self.acsource_l1source_selftestresultsfield = self.acsource_l1source_start_address + 32                         # Property ID: 17, [-] (char[99]). The displayed values show encoded results of the interface protection self-test in hexadecimal format (FFF = invalid value). For Decoding (C=Column,R=Row): (C1,R1):(C2,R1):(C3,R1):(C4,R1) : Measured voltages at tripping, RealValue = 125/4095*DisplayValue [%]. (C5,R1):(C6,R1):(C7,R1):(C8,R1) : Measured frequencies at tripping, RealValue = 10/4095*DisplayValue + NominalFreq - 5 [Hz]. (C1,R2):(C2,R2):(C3,R2):(C4,R2) : Absolute errors on voltage thresholds, RealValue = 5/4095*DisplayValue [%]. (C5,R2):(C6,R2):(C7,R2):(C8,R2) : Absolute errors on frequency thresholds, RealValue = 20/4095*DisplayValue [mHz]. All Row3 : Absolute errors on trip time, RealValue = 1000/4095*DisplayValue [ms]. Note the test order per column : C1=UnderVoltageStage1, C2=UnderVoltageStage2, C3=OverVoltageStage1, C4=OverVoltageStage2, C5=UnderFrequencyStage1, C6=UnderFrequencyStage2, C7=OverFrequencyStage1, C8=OverFrequencyStage2. For more details see user manual.
        self.acsource_l1source_sourcedlimitlevel = self.acsource_l1source_start_address + 84                            # Property ID: 19, [-] (int). Sourced limit level sent to the power flow dispatcher.
        self.acsource_l1source_deviceid = self.acsource_l1source_start_address + 86                                     # Property ID: 20, [-] (int). The ID of the device associated with this AC input.

        # Object L2Source Modbus Address
        self.acsource_l2source_start_address = 2100
        self.acsource_l2source_status = self.acsource_l2source_start_address + 0                                        # Property ID: 0, [-] (enum). Current status.
        self.acsource_l2source_unconnectedreasons = self.acsource_l2source_start_address + 2                            # Property ID: 1, [-] (bitfield). Reasons explaining why the source is not connected.
        self.acsource_l2source_warnings = self.acsource_l2source_start_address + 4                                      # Property ID: 2, [-] (bitfield). Current warnings.
        self.acsource_l2source_errors = self.acsource_l2source_start_address + 6                                        # Property ID: 3, [-] (bitfield). Current errors.
        self.acsource_l2source_causeofdisconnection = self.acsource_l2source_start_address + 8                          # Property ID: 4, [-] (bitfield). Causes of the source disconnection. Note that the value is initialized to 0 (no items checked in the list) until the first connection to the source.
        self.acsource_l2source_voltage10minmean = self.acsource_l2source_start_address + 12                             # Property ID: 6, [%] (float). Compute a 10min period moving average of the voltage.
        self.acsource_l2source_connectionallowed = self.acsource_l2source_start_address + 14                            # Property ID: 7, [-] (bool). Used to allowed or not the connection to the source.
        self.acsource_l2source_gridfeedingallowed = self.acsource_l2source_start_address + 15                           # Property ID: 8, [-] (bool). Used to allowed or not the grid-feeding.
        self.acsource_l2source_maxsourcedactivepower = self.acsource_l2source_start_address + 16                        # Property ID: 9, [W] (float). Max sourced active power sent to the power flow dispatcher.
        self.acsource_l2source_maxsinkedactivepower = self.acsource_l2source_start_address + 18                         # Property ID: 10, [W] (float). Max sinked active power sent to the power flow dispatcher.
        self.acsource_l2source_maxsourcedreactivepower = self.acsource_l2source_start_address + 20                      # Property ID: 11, [VA] (float). Max sourced reactive power sent to the power flow dispatcher.
        self.acsource_l2source_maxsinkedreactivepower = self.acsource_l2source_start_address + 22                       # Property ID: 12, [VA] (float). Max sinked reactive power sent to the power flow dispatcher.
        self.acsource_l2source_targetsourcedactivepower = self.acsource_l2source_start_address + 24                     # Property ID: 13, [W] (float). Target sourced active power sent to the power flow dispatcher.
        self.acsource_l2source_sinkedlimitlevel = self.acsource_l2source_start_address + 28                             # Property ID: 15, [-] (int). Sinked limit level sent to the power flow dispatcher.
        self.acsource_l2source_setpointslevel = self.acsource_l2source_start_address + 30                               # Property ID: 16, [-] (int). Setpoints level sent to the power flow dispatcher.
        self.acsource_l2source_selftestresultsfield = self.acsource_l2source_start_address + 32                         # Property ID: 17, [-] (char[99]). The displayed values show encoded results of the interface protection self-test in hexadecimal format (FFF = invalid value). For Decoding (C=Column,R=Row): (C1,R1):(C2,R1):(C3,R1):(C4,R1) : Measured voltages at tripping, RealValue = 125/4095*DisplayValue [%]. (C5,R1):(C6,R1):(C7,R1):(C8,R1) : Measured frequencies at tripping, RealValue = 10/4095*DisplayValue + NominalFreq - 5 [Hz]. (C1,R2):(C2,R2):(C3,R2):(C4,R2) : Absolute errors on voltage thresholds, RealValue = 5/4095*DisplayValue [%]. (C5,R2):(C6,R2):(C7,R2):(C8,R2) : Absolute errors on frequency thresholds, RealValue = 20/4095*DisplayValue [mHz]. All Row3 : Absolute errors on trip time, RealValue = 1000/4095*DisplayValue [ms]. Note the test order per column : C1=UnderVoltageStage1, C2=UnderVoltageStage2, C3=OverVoltageStage1, C4=OverVoltageStage2, C5=UnderFrequencyStage1, C6=UnderFrequencyStage2, C7=OverFrequencyStage1, C8=OverFrequencyStage2. For more details see user manual.
        self.acsource_l2source_sourcedlimitlevel = self.acsource_l2source_start_address + 84                            # Property ID: 19, [-] (int). Sourced limit level sent to the power flow dispatcher.
        self.acsource_l2source_deviceid = self.acsource_l2source_start_address + 86                                     # Property ID: 20, [-] (int). The ID of the device associated with this AC input.

        # Object L3Source Modbus Address
        self.acsource_l3source_start_address = 2400
        self.acsource_l3source_status = self.acsource_l3source_start_address + 0                                        # Property ID: 0, [-] (enum). Current status.
        self.acsource_l3source_unconnectedreasons = self.acsource_l3source_start_address + 2                            # Property ID: 1, [-] (bitfield). Reasons explaining why the source is not connected.
        self.acsource_l3source_warnings = self.acsource_l3source_start_address + 4                                      # Property ID: 2, [-] (bitfield). Current warnings.
        self.acsource_l3source_errors = self.acsource_l3source_start_address + 6                                        # Property ID: 3, [-] (bitfield). Current errors.
        self.acsource_l3source_causeofdisconnection = self.acsource_l3source_start_address + 8                          # Property ID: 4, [-] (bitfield). Causes of the source disconnection. Note that the value is initialized to 0 (no items checked in the list) until the first connection to the source.
        self.acsource_l3source_voltage10minmean = self.acsource_l3source_start_address + 12                             # Property ID: 6, [%] (float). Compute a 10min period moving average of the voltage.
        self.acsource_l3source_connectionallowed = self.acsource_l3source_start_address + 14                            # Property ID: 7, [-] (bool). Used to allowed or not the connection to the source.
        self.acsource_l3source_gridfeedingallowed = self.acsource_l3source_start_address + 15                           # Property ID: 8, [-] (bool). Used to allowed or not the grid-feeding.
        self.acsource_l3source_maxsourcedactivepower = self.acsource_l3source_start_address + 16                        # Property ID: 9, [W] (float). Max sourced active power sent to the power flow dispatcher.
        self.acsource_l3source_maxsinkedactivepower = self.acsource_l3source_start_address + 18                         # Property ID: 10, [W] (float). Max sinked active power sent to the power flow dispatcher.
        self.acsource_l3source_maxsourcedreactivepower = self.acsource_l3source_start_address + 20                      # Property ID: 11, [VA] (float). Max sourced reactive power sent to the power flow dispatcher.
        self.acsource_l3source_maxsinkedreactivepower = self.acsource_l3source_start_address + 22                       # Property ID: 12, [VA] (float). Max sinked reactive power sent to the power flow dispatcher.
        self.acsource_l3source_targetsourcedactivepower = self.acsource_l3source_start_address + 24                     # Property ID: 13, [W] (float). Target sourced active power sent to the power flow dispatcher.
        self.acsource_l3source_sinkedlimitlevel = self.acsource_l3source_start_address + 28                             # Property ID: 15, [-] (int). Sinked limit level sent to the power flow dispatcher.
        self.acsource_l3source_setpointslevel = self.acsource_l3source_start_address + 30                               # Property ID: 16, [-] (int). Setpoints level sent to the power flow dispatcher.
        self.acsource_l3source_selftestresultsfield = self.acsource_l3source_start_address + 32                         # Property ID: 17, [-] (char[99]). The displayed values show encoded results of the interface protection self-test in hexadecimal format (FFF = invalid value). For Decoding (C=Column,R=Row): (C1,R1):(C2,R1):(C3,R1):(C4,R1) : Measured voltages at tripping, RealValue = 125/4095*DisplayValue [%]. (C5,R1):(C6,R1):(C7,R1):(C8,R1) : Measured frequencies at tripping, RealValue = 10/4095*DisplayValue + NominalFreq - 5 [Hz]. (C1,R2):(C2,R2):(C3,R2):(C4,R2) : Absolute errors on voltage thresholds, RealValue = 5/4095*DisplayValue [%]. (C5,R2):(C6,R2):(C7,R2):(C8,R2) : Absolute errors on frequency thresholds, RealValue = 20/4095*DisplayValue [mHz]. All Row3 : Absolute errors on trip time, RealValue = 1000/4095*DisplayValue [ms]. Note the test order per column : C1=UnderVoltageStage1, C2=UnderVoltageStage2, C3=OverVoltageStage1, C4=OverVoltageStage2, C5=UnderFrequencyStage1, C6=UnderFrequencyStage2, C7=OverFrequencyStage1, C8=OverFrequencyStage2. For more details see user manual.
        self.acsource_l3source_sourcedlimitlevel = self.acsource_l3source_start_address + 84                            # Property ID: 19, [-] (int). Sourced limit level sent to the power flow dispatcher.
        self.acsource_l3source_deviceid = self.acsource_l3source_start_address + 86                                     # Property ID: 20, [-] (int). The ID of the device associated with this AC input.


        # Group AcFlexLoad Modbus Address
        # Object TriPhaseMeasure Modbus Address
        self.acflexload_triphasemeasure_start_address = 0
        self.acflexload_triphasemeasure_frequency = self.acflexload_triphasemeasure_start_address + 0                   # Property ID: 0, [Hz] (float). Frequency measured.
        self.acflexload_triphasemeasure_linevoltagel1l2 = self.acflexload_triphasemeasure_start_address + 2             # Property ID: 4, [V] (float). Line voltage L1-L2 measured.
        self.acflexload_triphasemeasure_linevoltagel2l3 = self.acflexload_triphasemeasure_start_address + 4             # Property ID: 8, [V] (float). Line voltage L2-L3 measured.
        self.acflexload_triphasemeasure_linevoltagel3l1 = self.acflexload_triphasemeasure_start_address + 6             # Property ID: 12, [V] (float). Line voltage L3-L1 measured.
        self.acflexload_triphasemeasure_totalactivepower = self.acflexload_triphasemeasure_start_address + 8            # Property ID: 16, [W] (float). Total active power measured.
        self.acflexload_triphasemeasure_totalapparentpower = self.acflexload_triphasemeasure_start_address + 10         # Property ID: 20, [VA] (float). Total apparent power measured.
        self.acflexload_triphasemeasure_anglel2relativetol1 = self.acflexload_triphasemeasure_start_address + 12        # Property ID: 24, [degree] (float). Angle L2 relative to L1 measured.
        self.acflexload_triphasemeasure_anglel3relativetol1 = self.acflexload_triphasemeasure_start_address + 14        # Property ID: 25, [degree] (float). Angle L3 relative to L1 measured.
        self.acflexload_triphasemeasure_dayconsumedenergy = self.acflexload_triphasemeasure_start_address + 16          # Property ID: 26, [Wh] (float). Consumed energy of the current day.
        self.acflexload_triphasemeasure_previousdayconsumedenergy = self.acflexload_triphasemeasure_start_address + 18  # Property ID: 27, [Wh] (float). Consumed energy of the previous day.
        self.acflexload_triphasemeasure_resetableconsumedenergy = self.acflexload_triphasemeasure_start_address + 20    # Property ID: 28, [Wh] (float64). Resetable consumed energy.
        self.acflexload_triphasemeasure_totalconsumedenergy = self.acflexload_triphasemeasure_start_address + 24        # Property ID: 29, [Wh] (float64). Total consumed energy.
        self.acflexload_triphasemeasure_dayproducedenergy = self.acflexload_triphasemeasure_start_address + 28          # Property ID: 30, [Wh] (float). Produced energy of the current day.
        self.acflexload_triphasemeasure_previousdayproducedenergy = self.acflexload_triphasemeasure_start_address + 30  # Property ID: 31, [Wh] (float). Produced energy of the previous day.
        self.acflexload_triphasemeasure_resetableproducedenergy = self.acflexload_triphasemeasure_start_address + 32    # Property ID: 32, [Wh] (float64). Resetable produced energy.
        self.acflexload_triphasemeasure_totalproducedenergy = self.acflexload_triphasemeasure_start_address + 36        # Property ID: 33, [Wh] (float64). Total produced energy.
        self.acflexload_triphasemeasure_dayruntime = self.acflexload_triphasemeasure_start_address + 40                 # Property ID: 34, [h] (float). Day runtime measured.
        self.acflexload_triphasemeasure_totalruntime = self.acflexload_triphasemeasure_start_address + 42               # Property ID: 35, [h] (float). Total runtime measured.
        self.acflexload_triphasemeasure_daypeakpower = self.acflexload_triphasemeasure_start_address + 44               # Property ID: 36, [VA] (float). Peak power of the current day.
        self.acflexload_triphasemeasure_previousdaypeakpower = self.acflexload_triphasemeasure_start_address + 46       # Property ID: 37, [VA] (float). Peak power of the previous day.
        self.acflexload_triphasemeasure_dayminactivepower = self.acflexload_triphasemeasure_start_address + 48          # Property ID: 38, [W] (float). Minimum active power of the current day.
        self.acflexload_triphasemeasure_previousdayminactivepower = self.acflexload_triphasemeasure_start_address + 50  # Property ID: 39, [W] (float). Minimum active power of the previous day.
        self.acflexload_triphasemeasure_daymaxactivepower = self.acflexload_triphasemeasure_start_address + 52          # Property ID: 40, [W] (float). Maximum active power of the current day.
        self.acflexload_triphasemeasure_previousdaymaxactivepower = self.acflexload_triphasemeasure_start_address + 54  # Property ID: 41, [W] (float). Maximum active power of the previous day.
        self.acflexload_triphasemeasure_producedactivepower = self.acflexload_triphasemeasure_start_address + 56        # Property ID: 42, [W] (float). Produced active power measured.
        self.acflexload_triphasemeasure_consumedactivepower = self.acflexload_triphasemeasure_start_address + 58        # Property ID: 44, [W] (float). Consumed active power measured.

        # Object L1Measure Modbus Address
        self.acflexload_l1measure_start_address = 300
        self.acflexload_l1measure_phasevoltage = self.acflexload_l1measure_start_address + 0                            # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.acflexload_l1measure_current = self.acflexload_l1measure_start_address + 2                                 # Property ID: 4, [A] (float). Current RMS measured.
        self.acflexload_l1measure_activepower = self.acflexload_l1measure_start_address + 4                             # Property ID: 8, [W] (float). Active power measured.
        self.acflexload_l1measure_reactivepower = self.acflexload_l1measure_start_address + 6                           # Property ID: 12, [VAR] (float). Reactive power measured.
        self.acflexload_l1measure_apparentpower = self.acflexload_l1measure_start_address + 8                           # Property ID: 16, [VA] (float). Apparent power measured.
        self.acflexload_l1measure_cosphi = self.acflexload_l1measure_start_address + 10                                 # Property ID: 20, [-] (float). Power factor measured.
        self.acflexload_l1measure_daypeakpower = self.acflexload_l1measure_start_address + 12                           # Property ID: 24, [VA] (float). Peak power of the current day.
        self.acflexload_l1measure_previousdaypeakpower = self.acflexload_l1measure_start_address + 14                   # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.acflexload_l1measure_dayminactivepower = self.acflexload_l1measure_start_address + 16                      # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.acflexload_l1measure_previousdayminactivepower = self.acflexload_l1measure_start_address + 18              # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.acflexload_l1measure_daymaxactivepower = self.acflexload_l1measure_start_address + 20                      # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.acflexload_l1measure_previousdaymaxactivepower = self.acflexload_l1measure_start_address + 22              # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.acflexload_l1measure_dayconsumedenergy = self.acflexload_l1measure_start_address + 28                      # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.acflexload_l1measure_previousdayconsumedenergy = self.acflexload_l1measure_start_address + 30              # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.acflexload_l1measure_resetableconsumedenergy = self.acflexload_l1measure_start_address + 32                # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.acflexload_l1measure_totalconsumedenergy = self.acflexload_l1measure_start_address + 36                    # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.acflexload_l1measure_dayproducedenergy = self.acflexload_l1measure_start_address + 40                      # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.acflexload_l1measure_previousdayproducedenergy = self.acflexload_l1measure_start_address + 42              # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.acflexload_l1measure_resetableproducedenergy = self.acflexload_l1measure_start_address + 44                # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.acflexload_l1measure_totalproducedenergy = self.acflexload_l1measure_start_address + 48                    # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object L2Measure Modbus Address
        self.acflexload_l2measure_start_address = 600
        self.acflexload_l2measure_phasevoltage = self.acflexload_l2measure_start_address + 0                            # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.acflexload_l2measure_current = self.acflexload_l2measure_start_address + 2                                 # Property ID: 4, [A] (float). Current RMS measured.
        self.acflexload_l2measure_activepower = self.acflexload_l2measure_start_address + 4                             # Property ID: 8, [W] (float). Active power measured.
        self.acflexload_l2measure_reactivepower = self.acflexload_l2measure_start_address + 6                           # Property ID: 12, [VAR] (float). Reactive power measured.
        self.acflexload_l2measure_apparentpower = self.acflexload_l2measure_start_address + 8                           # Property ID: 16, [VA] (float). Apparent power measured.
        self.acflexload_l2measure_cosphi = self.acflexload_l2measure_start_address + 10                                 # Property ID: 20, [-] (float). Power factor measured.
        self.acflexload_l2measure_daypeakpower = self.acflexload_l2measure_start_address + 12                           # Property ID: 24, [VA] (float). Peak power of the current day.
        self.acflexload_l2measure_previousdaypeakpower = self.acflexload_l2measure_start_address + 14                   # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.acflexload_l2measure_dayminactivepower = self.acflexload_l2measure_start_address + 16                      # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.acflexload_l2measure_previousdayminactivepower = self.acflexload_l2measure_start_address + 18              # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.acflexload_l2measure_daymaxactivepower = self.acflexload_l2measure_start_address + 20                      # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.acflexload_l2measure_previousdaymaxactivepower = self.acflexload_l2measure_start_address + 22              # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.acflexload_l2measure_dayconsumedenergy = self.acflexload_l2measure_start_address + 28                      # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.acflexload_l2measure_previousdayconsumedenergy = self.acflexload_l2measure_start_address + 30              # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.acflexload_l2measure_resetableconsumedenergy = self.acflexload_l2measure_start_address + 32                # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.acflexload_l2measure_totalconsumedenergy = self.acflexload_l2measure_start_address + 36                    # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.acflexload_l2measure_dayproducedenergy = self.acflexload_l2measure_start_address + 40                      # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.acflexload_l2measure_previousdayproducedenergy = self.acflexload_l2measure_start_address + 42              # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.acflexload_l2measure_resetableproducedenergy = self.acflexload_l2measure_start_address + 44                # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.acflexload_l2measure_totalproducedenergy = self.acflexload_l2measure_start_address + 48                    # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object L3Measure Modbus Address
        self.acflexload_l3measure_start_address = 900
        self.acflexload_l3measure_phasevoltage = self.acflexload_l3measure_start_address + 0                            # Property ID: 0, [V] (float). Phase voltage RMS measured.
        self.acflexload_l3measure_current = self.acflexload_l3measure_start_address + 2                                 # Property ID: 4, [A] (float). Current RMS measured.
        self.acflexload_l3measure_activepower = self.acflexload_l3measure_start_address + 4                             # Property ID: 8, [W] (float). Active power measured.
        self.acflexload_l3measure_reactivepower = self.acflexload_l3measure_start_address + 6                           # Property ID: 12, [VAR] (float). Reactive power measured.
        self.acflexload_l3measure_apparentpower = self.acflexload_l3measure_start_address + 8                           # Property ID: 16, [VA] (float). Apparent power measured.
        self.acflexload_l3measure_cosphi = self.acflexload_l3measure_start_address + 10                                 # Property ID: 20, [-] (float). Power factor measured.
        self.acflexload_l3measure_daypeakpower = self.acflexload_l3measure_start_address + 12                           # Property ID: 24, [VA] (float). Peak power of the current day.
        self.acflexload_l3measure_previousdaypeakpower = self.acflexload_l3measure_start_address + 14                   # Property ID: 25, [VA] (float). Peak power of the previous day.
        self.acflexload_l3measure_dayminactivepower = self.acflexload_l3measure_start_address + 16                      # Property ID: 26, [W] (float). Minimum active power of the current day.
        self.acflexload_l3measure_previousdayminactivepower = self.acflexload_l3measure_start_address + 18              # Property ID: 27, [W] (float). Minimum active power of the previous day.
        self.acflexload_l3measure_daymaxactivepower = self.acflexload_l3measure_start_address + 20                      # Property ID: 28, [W] (float). Maximum active power of the current day.
        self.acflexload_l3measure_previousdaymaxactivepower = self.acflexload_l3measure_start_address + 22              # Property ID: 29, [W] (float). Maximum active power of the previous day.
        self.acflexload_l3measure_dayconsumedenergy = self.acflexload_l3measure_start_address + 28                      # Property ID: 32, [Wh] (float). Consumed energy of the current day.
        self.acflexload_l3measure_previousdayconsumedenergy = self.acflexload_l3measure_start_address + 30              # Property ID: 33, [Wh] (float). Consumed energy of the previous day.
        self.acflexload_l3measure_resetableconsumedenergy = self.acflexload_l3measure_start_address + 32                # Property ID: 34, [Wh] (float64). Resetable consumed energy.
        self.acflexload_l3measure_totalconsumedenergy = self.acflexload_l3measure_start_address + 36                    # Property ID: 35, [Wh] (float64). Total consumed energy.
        self.acflexload_l3measure_dayproducedenergy = self.acflexload_l3measure_start_address + 40                      # Property ID: 36, [Wh] (float). Produced energy of the current day.
        self.acflexload_l3measure_previousdayproducedenergy = self.acflexload_l3measure_start_address + 42              # Property ID: 37, [Wh] (float). Produced energy of the previous day.
        self.acflexload_l3measure_resetableproducedenergy = self.acflexload_l3measure_start_address + 44                # Property ID: 38, [Wh] (float64). Resetable produced energy.
        self.acflexload_l3measure_totalproducedenergy = self.acflexload_l3measure_start_address + 48                    # Property ID: 39, [Wh] (float64). Total produced energy.

        # Object L1FlexLoadContrRelay Modbus Address
        self.acflexload_l1flexloadcontrrelay_start_address = 1200
        self.acflexload_l1flexloadcontrrelay_isconnected = self.acflexload_l1flexloadcontrrelay_start_address + 0       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.acflexload_l1flexloadcontrrelay_currentrelayposition = self.acflexload_l1flexloadcontrrelay_start_address + 1    # Property ID: 1, [-] (enum). Current position.
        self.acflexload_l1flexloadcontrrelay_errors = self.acflexload_l1flexloadcontrrelay_start_address + 3            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.acflexload_l1flexloadcontrrelay_operatingmodeselect = self.acflexload_l1flexloadcontrrelay_start_address + 7    # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.acflexload_l1flexloadcontrrelay_automodeselect = self.acflexload_l1flexloadcontrrelay_start_address + 9    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.acflexload_l1flexloadcontrrelay_safestateselect = self.acflexload_l1flexloadcontrrelay_start_address + 11  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.acflexload_l1flexloadcontrrelay_presetbatvoltactvth = self.acflexload_l1flexloadcontrrelay_start_address + 13    # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.acflexload_l1flexloadcontrrelay_presetbatvoltdeactvth = self.acflexload_l1flexloadcontrrelay_start_address + 15    # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.acflexload_l1flexloadcontrrelay_presetbatsocactth = self.acflexload_l1flexloadcontrrelay_start_address + 17    # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.acflexload_l1flexloadcontrrelay_presetbatsocdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 19    # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.acflexload_l1flexloadcontrrelay_presetbattempactth = self.acflexload_l1flexloadcontrrelay_start_address + 21    # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.acflexload_l1flexloadcontrrelay_presetbattempdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 23    # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.acflexload_l1flexloadcontrrelay_presetbatstateselect = self.acflexload_l1flexloadcontrrelay_start_address + 25    # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.acflexload_l1flexloadcontrrelay_presetpacselect = self.acflexload_l1flexloadcontrrelay_start_address + 27  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.acflexload_l1flexloadcontrrelay_presetpacpowactth = self.acflexload_l1flexloadcontrrelay_start_address + 29    # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.acflexload_l1flexloadcontrrelay_presetpacpowdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 31    # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.acflexload_l1flexloadcontrrelay_presetsolarexcessongridpowactth = self.acflexload_l1flexloadcontrrelay_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.acflexload_l1flexloadcontrrelay_presetsolarexcessongridpowdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 35    # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.acflexload_l1flexloadcontrrelay_presetcmdentryidx = self.acflexload_l1flexloadcontrrelay_start_address + 41    # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.acflexload_l1flexloadcontrrelay_preseterrorwarningselect = self.acflexload_l1flexloadcontrrelay_start_address + 43    # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.acflexload_l1flexloadcontrrelay_presetonsourceselect = self.acflexload_l1flexloadcontrrelay_start_address + 45    # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.acflexload_l1flexloadcontrrelay_presetaccouplingblankingtime = self.acflexload_l1flexloadcontrrelay_start_address + 47    # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.acflexload_l1flexloadcontrrelay_isvirtualrelay = self.acflexload_l1flexloadcontrrelay_start_address + 49   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.acflexload_l1flexloadcontrrelay_presetadvancedlogicscombination = self.acflexload_l1flexloadcontrrelay_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.acflexload_l1flexloadcontrrelay_presetsolarpoweractth = self.acflexload_l1flexloadcontrrelay_start_address + 54    # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.acflexload_l1flexloadcontrrelay_presetsolarpowerdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 56    # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.acflexload_l1flexloadcontrrelay_presetbatbatidx = self.acflexload_l1flexloadcontrrelay_start_address + 58  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object L2FlexLoadContrRelay Modbus Address
        self.acflexload_l2flexloadcontrrelay_start_address = 1500
        self.acflexload_l2flexloadcontrrelay_isconnected = self.acflexload_l2flexloadcontrrelay_start_address + 0       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.acflexload_l2flexloadcontrrelay_currentrelayposition = self.acflexload_l2flexloadcontrrelay_start_address + 1    # Property ID: 1, [-] (enum). Current position.
        self.acflexload_l2flexloadcontrrelay_errors = self.acflexload_l2flexloadcontrrelay_start_address + 3            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.acflexload_l2flexloadcontrrelay_operatingmodeselect = self.acflexload_l2flexloadcontrrelay_start_address + 7    # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.acflexload_l2flexloadcontrrelay_automodeselect = self.acflexload_l2flexloadcontrrelay_start_address + 9    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.acflexload_l2flexloadcontrrelay_safestateselect = self.acflexload_l2flexloadcontrrelay_start_address + 11  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.acflexload_l2flexloadcontrrelay_presetbatvoltactvth = self.acflexload_l2flexloadcontrrelay_start_address + 13    # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.acflexload_l2flexloadcontrrelay_presetbatvoltdeactvth = self.acflexload_l2flexloadcontrrelay_start_address + 15    # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.acflexload_l2flexloadcontrrelay_presetbatsocactth = self.acflexload_l2flexloadcontrrelay_start_address + 17    # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.acflexload_l2flexloadcontrrelay_presetbatsocdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 19    # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.acflexload_l2flexloadcontrrelay_presetbattempactth = self.acflexload_l2flexloadcontrrelay_start_address + 21    # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.acflexload_l2flexloadcontrrelay_presetbattempdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 23    # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.acflexload_l2flexloadcontrrelay_presetbatstateselect = self.acflexload_l2flexloadcontrrelay_start_address + 25    # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.acflexload_l2flexloadcontrrelay_presetpacselect = self.acflexload_l2flexloadcontrrelay_start_address + 27  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.acflexload_l2flexloadcontrrelay_presetpacpowactth = self.acflexload_l2flexloadcontrrelay_start_address + 29    # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.acflexload_l2flexloadcontrrelay_presetpacpowdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 31    # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.acflexload_l2flexloadcontrrelay_presetsolarexcessongridpowactth = self.acflexload_l2flexloadcontrrelay_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.acflexload_l2flexloadcontrrelay_presetsolarexcessongridpowdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 35    # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.acflexload_l2flexloadcontrrelay_presetcmdentryidx = self.acflexload_l2flexloadcontrrelay_start_address + 41    # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.acflexload_l2flexloadcontrrelay_preseterrorwarningselect = self.acflexload_l2flexloadcontrrelay_start_address + 43    # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.acflexload_l2flexloadcontrrelay_presetonsourceselect = self.acflexload_l2flexloadcontrrelay_start_address + 45    # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.acflexload_l2flexloadcontrrelay_presetaccouplingblankingtime = self.acflexload_l2flexloadcontrrelay_start_address + 47    # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.acflexload_l2flexloadcontrrelay_isvirtualrelay = self.acflexload_l2flexloadcontrrelay_start_address + 49   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.acflexload_l2flexloadcontrrelay_presetadvancedlogicscombination = self.acflexload_l2flexloadcontrrelay_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.acflexload_l2flexloadcontrrelay_presetsolarpoweractth = self.acflexload_l2flexloadcontrrelay_start_address + 54    # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.acflexload_l2flexloadcontrrelay_presetsolarpowerdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 56    # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.acflexload_l2flexloadcontrrelay_presetbatbatidx = self.acflexload_l2flexloadcontrrelay_start_address + 58  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object L3FlexLoadContrRelay Modbus Address
        self.acflexload_l3flexloadcontrrelay_start_address = 1800
        self.acflexload_l3flexloadcontrrelay_isconnected = self.acflexload_l3flexloadcontrrelay_start_address + 0       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.acflexload_l3flexloadcontrrelay_currentrelayposition = self.acflexload_l3flexloadcontrrelay_start_address + 1    # Property ID: 1, [-] (enum). Current position.
        self.acflexload_l3flexloadcontrrelay_errors = self.acflexload_l3flexloadcontrrelay_start_address + 3            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.acflexload_l3flexloadcontrrelay_operatingmodeselect = self.acflexload_l3flexloadcontrrelay_start_address + 7    # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.acflexload_l3flexloadcontrrelay_automodeselect = self.acflexload_l3flexloadcontrrelay_start_address + 9    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.acflexload_l3flexloadcontrrelay_safestateselect = self.acflexload_l3flexloadcontrrelay_start_address + 11  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.acflexload_l3flexloadcontrrelay_presetbatvoltactvth = self.acflexload_l3flexloadcontrrelay_start_address + 13    # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.acflexload_l3flexloadcontrrelay_presetbatvoltdeactvth = self.acflexload_l3flexloadcontrrelay_start_address + 15    # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.acflexload_l3flexloadcontrrelay_presetbatsocactth = self.acflexload_l3flexloadcontrrelay_start_address + 17    # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.acflexload_l3flexloadcontrrelay_presetbatsocdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 19    # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.acflexload_l3flexloadcontrrelay_presetbattempactth = self.acflexload_l3flexloadcontrrelay_start_address + 21    # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.acflexload_l3flexloadcontrrelay_presetbattempdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 23    # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.acflexload_l3flexloadcontrrelay_presetbatstateselect = self.acflexload_l3flexloadcontrrelay_start_address + 25    # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.acflexload_l3flexloadcontrrelay_presetpacselect = self.acflexload_l3flexloadcontrrelay_start_address + 27  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.acflexload_l3flexloadcontrrelay_presetpacpowactth = self.acflexload_l3flexloadcontrrelay_start_address + 29    # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.acflexload_l3flexloadcontrrelay_presetpacpowdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 31    # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.acflexload_l3flexloadcontrrelay_presetsolarexcessongridpowactth = self.acflexload_l3flexloadcontrrelay_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.acflexload_l3flexloadcontrrelay_presetsolarexcessongridpowdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 35    # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.acflexload_l3flexloadcontrrelay_presetcmdentryidx = self.acflexload_l3flexloadcontrrelay_start_address + 41    # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.acflexload_l3flexloadcontrrelay_preseterrorwarningselect = self.acflexload_l3flexloadcontrrelay_start_address + 43    # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.acflexload_l3flexloadcontrrelay_presetonsourceselect = self.acflexload_l3flexloadcontrrelay_start_address + 45    # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.acflexload_l3flexloadcontrrelay_presetaccouplingblankingtime = self.acflexload_l3flexloadcontrrelay_start_address + 47    # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.acflexload_l3flexloadcontrrelay_isvirtualrelay = self.acflexload_l3flexloadcontrrelay_start_address + 49   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.acflexload_l3flexloadcontrrelay_presetadvancedlogicscombination = self.acflexload_l3flexloadcontrrelay_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.acflexload_l3flexloadcontrrelay_presetsolarpoweractth = self.acflexload_l3flexloadcontrrelay_start_address + 54    # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.acflexload_l3flexloadcontrrelay_presetsolarpowerdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 56    # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.acflexload_l3flexloadcontrrelay_presetbatbatidx = self.acflexload_l3flexloadcontrrelay_start_address + 58  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object L1FlexLoadTimeCtrl Modbus Address
        self.acflexload_l1flexloadtimectrl_start_address = 2100
        self.acflexload_l1flexloadtimectrl_timecontrolledmodeselect = self.acflexload_l1flexloadtimectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.acflexload_l1flexloadtimectrl_actmindelay = self.acflexload_l1flexloadtimectrl_start_address + 2           # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.acflexload_l1flexloadtimectrl_deactmindelay = self.acflexload_l1flexloadtimectrl_start_address + 4         # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.acflexload_l1flexloadtimectrl_actmintime = self.acflexload_l1flexloadtimectrl_start_address + 6            # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.acflexload_l1flexloadtimectrl_deactmintime = self.acflexload_l1flexloadtimectrl_start_address + 8          # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.acflexload_l1flexloadtimectrl_actmaxtime = self.acflexload_l1flexloadtimectrl_start_address + 10           # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.acflexload_l1flexloadtimectrl_acthourallow1 = self.acflexload_l1flexloadtimectrl_start_address + 12        # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.acflexload_l1flexloadtimectrl_acthourallow2 = self.acflexload_l1flexloadtimectrl_start_address + 14        # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.acflexload_l1flexloadtimectrl_actweekdaysallow = self.acflexload_l1flexloadtimectrl_start_address + 16     # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.acflexload_l1flexloadtimectrl_startingdate = self.acflexload_l1flexloadtimectrl_start_address + 18         # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.acflexload_l1flexloadtimectrl_startingtimesec = self.acflexload_l1flexloadtimectrl_start_address + 20      # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.acflexload_l1flexloadtimectrl_endingtimesec = self.acflexload_l1flexloadtimectrl_start_address + 22        # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.acflexload_l1flexloadtimectrl_selectedweekday = self.acflexload_l1flexloadtimectrl_start_address + 24      # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.acflexload_l1flexloadtimectrl_recurrenceweeks = self.acflexload_l1flexloadtimectrl_start_address + 26      # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.acflexload_l1flexloadtimectrl_rangeofrecurrenceselect = self.acflexload_l1flexloadtimectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.acflexload_l1flexloadtimectrl_endingdate = self.acflexload_l1flexloadtimectrl_start_address + 30           # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.acflexload_l1flexloadtimectrl_nbrofoccurrences = self.acflexload_l1flexloadtimectrl_start_address + 32     # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.acflexload_l1flexloadtimectrl_resettimecontrolled = self.acflexload_l1flexloadtimectrl_start_address + 34  # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object L2FlexLoadTimeCtrl Modbus Address
        self.acflexload_l2flexloadtimectrl_start_address = 2400
        self.acflexload_l2flexloadtimectrl_timecontrolledmodeselect = self.acflexload_l2flexloadtimectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.acflexload_l2flexloadtimectrl_actmindelay = self.acflexload_l2flexloadtimectrl_start_address + 2           # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.acflexload_l2flexloadtimectrl_deactmindelay = self.acflexload_l2flexloadtimectrl_start_address + 4         # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.acflexload_l2flexloadtimectrl_actmintime = self.acflexload_l2flexloadtimectrl_start_address + 6            # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.acflexload_l2flexloadtimectrl_deactmintime = self.acflexload_l2flexloadtimectrl_start_address + 8          # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.acflexload_l2flexloadtimectrl_actmaxtime = self.acflexload_l2flexloadtimectrl_start_address + 10           # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.acflexload_l2flexloadtimectrl_acthourallow1 = self.acflexload_l2flexloadtimectrl_start_address + 12        # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.acflexload_l2flexloadtimectrl_acthourallow2 = self.acflexload_l2flexloadtimectrl_start_address + 14        # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.acflexload_l2flexloadtimectrl_actweekdaysallow = self.acflexload_l2flexloadtimectrl_start_address + 16     # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.acflexload_l2flexloadtimectrl_startingdate = self.acflexload_l2flexloadtimectrl_start_address + 18         # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.acflexload_l2flexloadtimectrl_startingtimesec = self.acflexload_l2flexloadtimectrl_start_address + 20      # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.acflexload_l2flexloadtimectrl_endingtimesec = self.acflexload_l2flexloadtimectrl_start_address + 22        # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.acflexload_l2flexloadtimectrl_selectedweekday = self.acflexload_l2flexloadtimectrl_start_address + 24      # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.acflexload_l2flexloadtimectrl_recurrenceweeks = self.acflexload_l2flexloadtimectrl_start_address + 26      # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.acflexload_l2flexloadtimectrl_rangeofrecurrenceselect = self.acflexload_l2flexloadtimectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.acflexload_l2flexloadtimectrl_endingdate = self.acflexload_l2flexloadtimectrl_start_address + 30           # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.acflexload_l2flexloadtimectrl_nbrofoccurrences = self.acflexload_l2flexloadtimectrl_start_address + 32     # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.acflexload_l2flexloadtimectrl_resettimecontrolled = self.acflexload_l2flexloadtimectrl_start_address + 34  # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object L3FlexLoadTimeCtrl Modbus Address
        self.acflexload_l3flexloadtimectrl_start_address = 2700
        self.acflexload_l3flexloadtimectrl_timecontrolledmodeselect = self.acflexload_l3flexloadtimectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.acflexload_l3flexloadtimectrl_actmindelay = self.acflexload_l3flexloadtimectrl_start_address + 2           # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.acflexload_l3flexloadtimectrl_deactmindelay = self.acflexload_l3flexloadtimectrl_start_address + 4         # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.acflexload_l3flexloadtimectrl_actmintime = self.acflexload_l3flexloadtimectrl_start_address + 6            # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.acflexload_l3flexloadtimectrl_deactmintime = self.acflexload_l3flexloadtimectrl_start_address + 8          # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.acflexload_l3flexloadtimectrl_actmaxtime = self.acflexload_l3flexloadtimectrl_start_address + 10           # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.acflexload_l3flexloadtimectrl_acthourallow1 = self.acflexload_l3flexloadtimectrl_start_address + 12        # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.acflexload_l3flexloadtimectrl_acthourallow2 = self.acflexload_l3flexloadtimectrl_start_address + 14        # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.acflexload_l3flexloadtimectrl_actweekdaysallow = self.acflexload_l3flexloadtimectrl_start_address + 16     # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.acflexload_l3flexloadtimectrl_startingdate = self.acflexload_l3flexloadtimectrl_start_address + 18         # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.acflexload_l3flexloadtimectrl_startingtimesec = self.acflexload_l3flexloadtimectrl_start_address + 20      # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.acflexload_l3flexloadtimectrl_endingtimesec = self.acflexload_l3flexloadtimectrl_start_address + 22        # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.acflexload_l3flexloadtimectrl_selectedweekday = self.acflexload_l3flexloadtimectrl_start_address + 24      # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.acflexload_l3flexloadtimectrl_recurrenceweeks = self.acflexload_l3flexloadtimectrl_start_address + 26      # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.acflexload_l3flexloadtimectrl_rangeofrecurrenceselect = self.acflexload_l3flexloadtimectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.acflexload_l3flexloadtimectrl_endingdate = self.acflexload_l3flexloadtimectrl_start_address + 30           # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.acflexload_l3flexloadtimectrl_nbrofoccurrences = self.acflexload_l3flexloadtimectrl_start_address + 32     # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.acflexload_l3flexloadtimectrl_resettimecontrolled = self.acflexload_l3flexloadtimectrl_start_address + 34  # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object FlexLoad Modbus Address
        self.acflexload_flexload_start_address = 3000
        self.acflexload_flexload_phaseexistance = self.acflexload_flexload_start_address + 0                            # Property ID: 0, [-] (bitfield). Indicate which phase(s) is(are) used for this AcFlexLoad
        self.acflexload_flexload_allowindividualphaseoperation = self.acflexload_flexload_start_address + 2             # Property ID: 1, [-] (bool). Allow individual phase operation. Otherwise, all phases operates synchonously.

        # Object L1FlexLoad Modbus Address
        self.acflexload_l1flexload_start_address = 3300
        self.acflexload_l1flexload_status = self.acflexload_l1flexload_start_address + 0                                # Property ID: 0, [-] (enum). Current status.
        self.acflexload_l1flexload_errors = self.acflexload_l1flexload_start_address + 2                                # Property ID: 1, [-] (bitfield). Current errors.
        self.acflexload_l1flexload_warnings = self.acflexload_l1flexload_start_address + 4                              # Property ID: 2, [-] (bitfield). Current warnings.
        self.acflexload_l1flexload_deviceid = self.acflexload_l1flexload_start_address + 6                              # Property ID: 3, [-] (int). The ID of the device associated with this FlexLoad port.

        # Object L2FlexLoad Modbus Address
        self.acflexload_l2flexload_start_address = 3600
        self.acflexload_l2flexload_status = self.acflexload_l2flexload_start_address + 0                                # Property ID: 0, [-] (enum). Current status.
        self.acflexload_l2flexload_errors = self.acflexload_l2flexload_start_address + 2                                # Property ID: 1, [-] (bitfield). Current errors.
        self.acflexload_l2flexload_warnings = self.acflexload_l2flexload_start_address + 4                              # Property ID: 2, [-] (bitfield). Current warnings.
        self.acflexload_l2flexload_deviceid = self.acflexload_l2flexload_start_address + 6                              # Property ID: 3, [-] (int). The ID of the device associated with this FlexLoad port.

        # Object L3FlexLoad Modbus Address
        self.acflexload_l3flexload_start_address = 3900
        self.acflexload_l3flexload_status = self.acflexload_l3flexload_start_address + 0                                # Property ID: 0, [-] (enum). Current status.
        self.acflexload_l3flexload_errors = self.acflexload_l3flexload_start_address + 2                                # Property ID: 1, [-] (bitfield). Current errors.
        self.acflexload_l3flexload_warnings = self.acflexload_l3flexload_start_address + 4                              # Property ID: 2, [-] (bitfield). Current warnings.
        self.acflexload_l3flexload_deviceid = self.acflexload_l3flexload_start_address + 6                              # Property ID: 3, [-] (int). The ID of the device associated with this FlexLoad port.


        # Group Next3 Modbus Address
        # Object IdCardConverter Modbus Address
        self.next3_idcardconverter_start_address = 0
        self.next3_idcardconverter_serialnumber = self.next3_idcardconverter_start_address + 4                          # Property ID: 2, [-] (char[15]). Serial Number of this Studer Innotec device. 
        self.next3_idcardconverter_softwarepackageversion = self.next3_idcardconverter_start_address + 14               # Property ID: 4, [-] (uint). Software package version in this format : MAJOR.MIDDLE.MINOR.PATCH, encoded as follows from MSB to LSB : MAJOR (8 bits), MIDDLE (8bits), MINOR (12 bits), PATCH (4 bits).
        self.next3_idcardconverter_softwarerevisionsha1 = self.next3_idcardconverter_start_address + 18                 # Property ID: 6, [-] (char[7]). SHA-1 of the software project commit
        self.next3_idcardconverter_objectmodelversion = self.next3_idcardconverter_start_address + 30                   # Property ID: 8, [-] (uint). Version of the currently used ObjectModel in this format : MAJOR.MINOR, encoded as follows from MSB to LSB : MAJOR (16 bits), MINOR (16 bits).

        # Object IdCardTransfer Modbus Address
        self.next3_idcardtransfer_start_address = 300
        self.next3_idcardtransfer_serialnumber = self.next3_idcardtransfer_start_address + 4                            # Property ID: 2, [-] (char[15]). Serial Number of this Studer Innotec device. 
        self.next3_idcardtransfer_softwarepackageversion = self.next3_idcardtransfer_start_address + 14                 # Property ID: 4, [-] (uint). Software package version in this format : MAJOR.MIDDLE.MINOR.PATCH, encoded as follows from MSB to LSB : MAJOR (8 bits), MIDDLE (8bits), MINOR (12 bits), PATCH (4 bits).
        self.next3_idcardtransfer_softwarerevisionsha1 = self.next3_idcardtransfer_start_address + 18                   # Property ID: 6, [-] (char[7]). SHA-1 of the software project commit
        self.next3_idcardtransfer_objectmodelversion = self.next3_idcardtransfer_start_address + 30                     # Property ID: 8, [-] (uint). Version of the currently used ObjectModel in this format : MAJOR.MINOR, encoded as follows from MSB to LSB : MAJOR (16 bits), MINOR (16 bits).

        # Object BaseAppConverter Modbus Address
        self.next3_baseappconverter_start_address = 600
        self.next3_baseappconverter_warnings = self.next3_baseappconverter_start_address + 5                            # Property ID: 5, [-] (bitfield). Current warnings.
        self.next3_baseappconverter_restoreallnvmvalues = self.next3_baseappconverter_start_address + 15                # Property ID: 10, [-] (signal). Restore the original value (from Non-Volatile Memory) for all properties that were changed with WriteInRAM.

        # Object BaseAppTransfer Modbus Address
        self.next3_baseapptransfer_start_address = 900
        self.next3_baseapptransfer_warnings = self.next3_baseapptransfer_start_address + 5                              # Property ID: 5, [-] (bitfield). Current warnings.
        self.next3_baseapptransfer_restoreallnvmvalues = self.next3_baseapptransfer_start_address + 15                  # Property ID: 10, [-] (signal). Restore the original value (from Non-Volatile Memory) for all properties that were changed with WriteInRAM.

        # Object CanNodeConverter Modbus Address
        self.next3_cannodeconverter_start_address = 1800
        self.next3_cannodeconverter_status = self.next3_cannodeconverter_start_address + 2                              # Property ID: 1, [-] (enum). Stores the node status.
        self.next3_cannodeconverter_txerrorcounter = self.next3_cannodeconverter_start_address + 4                      # Property ID: 2, [-] (int). Counter of the TX errors.
        self.next3_cannodeconverter_rxerrorcounter = self.next3_cannodeconverter_start_address + 6                      # Property ID: 3, [-] (int). Counter of the RX errors.
        self.next3_cannodeconverter_busterminationset = self.next3_cannodeconverter_start_address + 8                   # Property ID: 4, [-] (bool). Bus termination status for this node.

        # Object CanNodeTransfer Modbus Address
        self.next3_cannodetransfer_start_address = 2100
        self.next3_cannodetransfer_status = self.next3_cannodetransfer_start_address + 2                                # Property ID: 1, [-] (enum). Stores the node status.
        self.next3_cannodetransfer_txerrorcounter = self.next3_cannodetransfer_start_address + 4                        # Property ID: 2, [-] (int). Counter of the TX errors.
        self.next3_cannodetransfer_rxerrorcounter = self.next3_cannodetransfer_start_address + 6                        # Property ID: 3, [-] (int). Counter of the RX errors.
        self.next3_cannodetransfer_busterminationset = self.next3_cannodetransfer_start_address + 8                     # Property ID: 4, [-] (bool). Bus termination status for this node.

        # Object Device Modbus Address
        self.next3_device_start_address = 4200
        self.next3_device_blinkingstate = self.next3_device_start_address + 0                                           # Property ID: 0, [-] (bool). If set, the device LEDs will blink.
        self.next3_device_deviceid = self.next3_device_start_address + 1                                                # Property ID: 1, [-] (int). System-wide ID of the device in topology.
        self.next3_device_batteryid = self.next3_device_start_address + 3                                               # Property ID: 2, [-] (int). System-wide ID of the battery in topology.
        self.next3_device_totalfunctioningtimesec = self.next3_device_start_address + 5                                 # Property ID: 3, [s] (uint). Total functioning time in this device's life.

        # Object Next3Converter Modbus Address
        self.next3_next3converter_start_address = 5100
        self.next3_next3converter_status = self.next3_next3converter_start_address + 0                                  # Property ID: 0, [-] (enum). Current status.
        self.next3_next3converter_errors = self.next3_next3converter_start_address + 2                                  # Property ID: 1, [-] (bitfield). Current errors.
        self.next3_next3converter_fan1speed = self.next3_next3converter_start_address + 4                               # Property ID: 2, [RPM] (float). Revolution speed of fan 1 measured.
        self.next3_next3converter_fan2speed = self.next3_next3converter_start_address + 6                               # Property ID: 3, [RPM] (float). Revolution speed of fan 2 measured.
        self.next3_next3converter_fan3speed = self.next3_next3converter_start_address + 8                               # Property ID: 4, [RPM] (float). Revolution speed of fan 3 measured.
        self.next3_next3converter_fan4speed = self.next3_next3converter_start_address + 10                              # Property ID: 5, [RPM] (float). Revolution speed of fan 4 measured.
        self.next3_next3converter_fan5speed = self.next3_next3converter_start_address + 12                              # Property ID: 6, [RPM] (float). Revolution speed of fan 5 measured.
        self.next3_next3converter_externalpowersupplycurrent = self.next3_next3converter_start_address + 14             # Property ID: 7, [A] (float). External power supply current measured.
        self.next3_next3converter_powersupplyvoltage = self.next3_next3converter_start_address + 16                     # Property ID: 8, [V] (float). Power supply voltage measured.
        self.next3_next3converter_warningnoisedadcchannels = self.next3_next3converter_start_address + 56               # Property ID: 28, [-] (bitfield). Channels for which the noise exceeds \"ADC noise warning threshold\" (id 32).
        self.next3_next3converter_errornoisedadcchannels = self.next3_next3converter_start_address + 58                 # Property ID: 29, [-] (bitfield). Channels for which the noise exceeds \"ADC noise error threshold\" (id 33).
        self.next3_next3converter_selectedadcchannel = self.next3_next3converter_start_address + 60                     # Property ID: 30, [-] (enum). Choose which ADC channel is showed by \"Noise of the selected ADC channel\" (id 31)
        self.next3_next3converter_selectedadcchannelnoise = self.next3_next3converter_start_address + 62                # Property ID: 31, [‰] (float). Noise of the ADC channel choosed by \"ADC channel selection\" (id 30).

        # Object SolarCommonDevice Modbus Address
        self.next3_solarcommondevice_start_address = 5700
        self.next3_solarcommondevice_turnon = self.next3_solarcommondevice_start_address + 0                            # Property ID: 0, [-] (signal). Turns on solar(s).
        self.next3_solarcommondevice_turnoff = self.next3_solarcommondevice_start_address + 1                           # Property ID: 1, [-] (signal). Turns off solar(s).
        self.next3_solarcommondevice_onoffstate = self.next3_solarcommondevice_start_address + 2                        # Property ID: 2, [-] (bool). Indicates solar(s) on/off state.
        self.next3_solarcommondevice_enabledepolarization = self.next3_solarcommondevice_start_address + 3              # Property ID: 3, [-] (signal). Enables depolarization.
        self.next3_solarcommondevice_disabledepolarization = self.next3_solarcommondevice_start_address + 4             # Property ID: 4, [-] (signal). Disables depolarization.
        self.next3_solarcommondevice_power = self.next3_solarcommondevice_start_address + 5                             # Property ID: 5, [W] (float). Power produced.
        self.next3_solarcommondevice_previousdayenergy = self.next3_solarcommondevice_start_address + 7                 # Property ID: 8, [Wh] (float). Energy produced for the previous day.
        self.next3_solarcommondevice_powerlimit = self.next3_solarcommondevice_start_address + 9                        # Property ID: 9, [W] (uint). Solar(s) max power limit.
        self.next3_solarcommondevice_dayenergy = self.next3_solarcommondevice_start_address + 11                        # Property ID: 10, [Wh] (float). Energy produced for the current day.
        self.next3_solarcommondevice_resetableenergy = self.next3_solarcommondevice_start_address + 15                  # Property ID: 12, [Wh] (float64). Energy produced (can be reset).
        self.next3_solarcommondevice_totalenergy = self.next3_solarcommondevice_start_address + 19                      # Property ID: 13, [Wh] (float64). Total energy produced (whole life).

        # Object SolarCommon1 Modbus Address
        self.next3_solarcommon1_start_address = 6000
        self.next3_solarcommon1_turnon = self.next3_solarcommon1_start_address + 0                                      # Property ID: 0, [-] (signal). Turns on solar(s).
        self.next3_solarcommon1_turnoff = self.next3_solarcommon1_start_address + 1                                     # Property ID: 1, [-] (signal). Turns off solar(s).
        self.next3_solarcommon1_onoffstate = self.next3_solarcommon1_start_address + 2                                  # Property ID: 2, [-] (bool). Indicates solar(s) on/off state.
        self.next3_solarcommon1_enabledepolarization = self.next3_solarcommon1_start_address + 3                        # Property ID: 3, [-] (signal). Enables depolarization.
        self.next3_solarcommon1_disabledepolarization = self.next3_solarcommon1_start_address + 4                       # Property ID: 4, [-] (signal). Disables depolarization.
        self.next3_solarcommon1_power = self.next3_solarcommon1_start_address + 5                                       # Property ID: 5, [W] (float). Power produced.
        self.next3_solarcommon1_previousdayenergy = self.next3_solarcommon1_start_address + 7                           # Property ID: 8, [Wh] (float). Energy produced for the previous day.
        self.next3_solarcommon1_powerlimit = self.next3_solarcommon1_start_address + 9                                  # Property ID: 9, [W] (uint). Solar(s) max power limit.
        self.next3_solarcommon1_dayenergy = self.next3_solarcommon1_start_address + 11                                  # Property ID: 10, [Wh] (float). Energy produced for the current day.
        self.next3_solarcommon1_resetableenergy = self.next3_solarcommon1_start_address + 15                            # Property ID: 12, [Wh] (float64). Energy produced (can be reset).
        self.next3_solarcommon1_totalenergy = self.next3_solarcommon1_start_address + 19                                # Property ID: 13, [Wh] (float64). Total energy produced (whole life).

        # Object SolarCommon2 Modbus Address
        self.next3_solarcommon2_start_address = 6300
        self.next3_solarcommon2_turnon = self.next3_solarcommon2_start_address + 0                                      # Property ID: 0, [-] (signal). Turns on solar(s).
        self.next3_solarcommon2_turnoff = self.next3_solarcommon2_start_address + 1                                     # Property ID: 1, [-] (signal). Turns off solar(s).
        self.next3_solarcommon2_onoffstate = self.next3_solarcommon2_start_address + 2                                  # Property ID: 2, [-] (bool). Indicates solar(s) on/off state.
        self.next3_solarcommon2_enabledepolarization = self.next3_solarcommon2_start_address + 3                        # Property ID: 3, [-] (signal). Enables depolarization.
        self.next3_solarcommon2_disabledepolarization = self.next3_solarcommon2_start_address + 4                       # Property ID: 4, [-] (signal). Disables depolarization.
        self.next3_solarcommon2_power = self.next3_solarcommon2_start_address + 5                                       # Property ID: 5, [W] (float). Power produced.
        self.next3_solarcommon2_previousdayenergy = self.next3_solarcommon2_start_address + 7                           # Property ID: 8, [Wh] (float). Energy produced for the previous day.
        self.next3_solarcommon2_powerlimit = self.next3_solarcommon2_start_address + 9                                  # Property ID: 9, [W] (uint). Solar(s) max power limit.
        self.next3_solarcommon2_dayenergy = self.next3_solarcommon2_start_address + 11                                  # Property ID: 10, [Wh] (float). Energy produced for the current day.
        self.next3_solarcommon2_resetableenergy = self.next3_solarcommon2_start_address + 15                            # Property ID: 12, [Wh] (float64). Energy produced (can be reset).
        self.next3_solarcommon2_totalenergy = self.next3_solarcommon2_start_address + 19                                # Property ID: 13, [Wh] (float64). Total energy produced (whole life).

        # Object SolarGroupDevice Modbus Address
        self.next3_solargroupdevice_start_address = 6600
        self.next3_solargroupdevice_nbr = self.next3_solargroupdevice_start_address + 0                                 # Property ID: 0, [-] (uint). Number of converters.
        self.next3_solargroupdevice_status = self.next3_solargroupdevice_start_address + 2                              # Property ID: 1, [-] (bitfield). Current status.
        self.next3_solargroupdevice_vt40nbr = self.next3_solargroupdevice_start_address + 4                             # Property ID: 2, [-] (uint). Number of vt40.
        self.next3_solargroupdevice_vt65nbr = self.next3_solargroupdevice_start_address + 6                             # Property ID: 3, [-] (uint). Number of vt65.
        self.next3_solargroupdevice_vt80nbr = self.next3_solargroupdevice_start_address + 8                             # Property ID: 4, [-] (uint). Number of vt80.
        self.next3_solargroupdevice_vs70nbr = self.next3_solargroupdevice_start_address + 10                            # Property ID: 5, [-] (uint). Number of vs70.
        self.next3_solargroupdevice_vs120nbr = self.next3_solargroupdevice_start_address + 12                           # Property ID: 6, [-] (uint). Number of vs120.

        # Object Solar1 Modbus Address
        self.next3_solar1_start_address = 6900
        self.next3_solar1_voltage = self.next3_solar1_start_address + 0                                                 # Property ID: 0, [V] (float). Voltage measured.
        self.next3_solar1_current = self.next3_solar1_start_address + 2                                                 # Property ID: 3, [A] (float). Current measured.
        self.next3_solar1_daysunshine = self.next3_solar1_start_address + 4                                             # Property ID: 6, [s] (uint). Sun radiation for the current day.
        self.next3_solar1_previousdaysunshine = self.next3_solar1_start_address + 6                                     # Property ID: 7, [s] (uint). Sun radiation for the previous day.
        self.next3_solar1_status = self.next3_solar1_start_address + 8                                                  # Property ID: 8, [-] (enum). Current status.
        self.next3_solar1_causeoferror = self.next3_solar1_start_address + 10                                           # Property ID: 9, [-] (bitfield). Memorizes why the converter entered \"Error halted\" (value 6) or \"Error restarting\" (value 7) state. The bitfield is cleared once the converter leaved one of these states.
        self.next3_solar1_errors = self.next3_solar1_start_address + 12                                                 # Property ID: 10, [-] (bitfield). Current errors.
        self.next3_solar1_warnings = self.next3_solar1_start_address + 14                                               # Property ID: 11, [-] (bitfield). Current warnings.
        self.next3_solar1_depolarizationstate = self.next3_solar1_start_address + 16                                    # Property ID: 12, [-] (enum). Indicates the depolarization state.
        self.next3_solar1_limitationstate = self.next3_solar1_start_address + 18                                        # Property ID: 13, [-] (enum). Indicates if there is a limitation and the reason of the limitation.
        self.next3_solar1_usercurrentlimit = self.next3_solar1_start_address + 20                                       # Property ID: 14, [A] (float). Set the current limit.
        self.next3_solar1_userpowerlimit = self.next3_solar1_start_address + 22                                         # Property ID: 15, [W] (float). Set the power limit.

        # Object Solar2 Modbus Address
        self.next3_solar2_start_address = 7200
        self.next3_solar2_voltage = self.next3_solar2_start_address + 0                                                 # Property ID: 0, [V] (float). Voltage measured.
        self.next3_solar2_current = self.next3_solar2_start_address + 2                                                 # Property ID: 3, [A] (float). Current measured.
        self.next3_solar2_daysunshine = self.next3_solar2_start_address + 4                                             # Property ID: 6, [s] (uint). Sun radiation for the current day.
        self.next3_solar2_previousdaysunshine = self.next3_solar2_start_address + 6                                     # Property ID: 7, [s] (uint). Sun radiation for the previous day.
        self.next3_solar2_status = self.next3_solar2_start_address + 8                                                  # Property ID: 8, [-] (enum). Current status.
        self.next3_solar2_causeoferror = self.next3_solar2_start_address + 10                                           # Property ID: 9, [-] (bitfield). Memorizes why the converter entered \"Error halted\" (value 6) or \"Error restarting\" (value 7) state. The bitfield is cleared once the converter leaved one of these states.
        self.next3_solar2_errors = self.next3_solar2_start_address + 12                                                 # Property ID: 10, [-] (bitfield). Current errors.
        self.next3_solar2_warnings = self.next3_solar2_start_address + 14                                               # Property ID: 11, [-] (bitfield). Current warnings.
        self.next3_solar2_depolarizationstate = self.next3_solar2_start_address + 16                                    # Property ID: 12, [-] (enum). Indicates the depolarization state.
        self.next3_solar2_limitationstate = self.next3_solar2_start_address + 18                                        # Property ID: 13, [-] (enum). Indicates if there is a limitation and the reason of the limitation.
        self.next3_solar2_usercurrentlimit = self.next3_solar2_start_address + 20                                       # Property ID: 14, [A] (float). Set the current limit.
        self.next3_solar2_userpowerlimit = self.next3_solar2_start_address + 22                                         # Property ID: 15, [W] (float). Set the power limit.

        # Object AlgoMppt1 Modbus Address
        self.next3_algomppt1_start_address = 7500
        self.next3_algomppt1_algoselected = self.next3_algomppt1_start_address + 0                                      # Property ID: 0, [-] (enum). Used to select the MPPT algorithm.
        self.next3_algomppt1_fvvoltagesetpoint = self.next3_algomppt1_start_address + 2                                 # Property ID: 1, [V] (float). Converter voltage setpoint applied when \"Algorithm\" (id 0) is set to \"Fixed voltage\" (value 1).
        self.next3_algomppt1_lsfcheckforglobalmpp = self.next3_algomppt1_start_address + 4                              # Property ID: 2, [-] (bool). Enables periodical check for global maximum power point to avoid power reduction due to partial shading. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Least square fit\" (value 0).
        self.next3_algomppt1_lsftimeperiodforglobalmppcheck = self.next3_algomppt1_start_address + 5                    # Property ID: 3, [s] (uint). Sets the period for global maximum power point check. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Least square fit\" (value 0).
        self.next3_algomppt1_focvrvoltageratio = self.next3_algomppt1_start_address + 7                                 # Property ID: 4, [-] (float). Ratio voltage setpoint/open-circuit voltage. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Fixed open-circuit voltage ratio\" (value 2).
        self.next3_algomppt1_focvrtimeperiodforvoccheck = self.next3_algomppt1_start_address + 9                        # Property ID: 5, [s] (uint). Sets the period for measuring open-circuit voltage. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Fixed open-circuit voltage ratio\" (value 2).

        # Object AlgoMppt2 Modbus Address
        self.next3_algomppt2_start_address = 7800
        self.next3_algomppt2_algoselected = self.next3_algomppt2_start_address + 0                                      # Property ID: 0, [-] (enum). Used to select the MPPT algorithm.
        self.next3_algomppt2_fvvoltagesetpoint = self.next3_algomppt2_start_address + 2                                 # Property ID: 1, [V] (float). Converter voltage setpoint applied when \"Algorithm\" (id 0) is set to \"Fixed voltage\" (value 1).
        self.next3_algomppt2_lsfcheckforglobalmpp = self.next3_algomppt2_start_address + 4                              # Property ID: 2, [-] (bool). Enables periodical check for global maximum power point to avoid power reduction due to partial shading. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Least square fit\" (value 0).
        self.next3_algomppt2_lsftimeperiodforglobalmppcheck = self.next3_algomppt2_start_address + 5                    # Property ID: 3, [s] (uint). Sets the period for global maximum power point check. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Least square fit\" (value 0).
        self.next3_algomppt2_focvrvoltageratio = self.next3_algomppt2_start_address + 7                                 # Property ID: 4, [-] (float). Ratio voltage setpoint/open-circuit voltage. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Fixed open-circuit voltage ratio\" (value 2).
        self.next3_algomppt2_focvrtimeperiodforvoccheck = self.next3_algomppt2_start_address + 9                        # Property ID: 5, [s] (uint). Sets the period for measuring open-circuit voltage. Note that this property is used only when \"Algorithm\" (id 0) is set to \"Fixed open-circuit voltage ratio\" (value 2).

        # Object RelayAux1 Modbus Address
        self.next3_relayaux1_start_address = 8100
        self.next3_relayaux1_isconnected = self.next3_relayaux1_start_address + 0                                       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next3_relayaux1_currentrelayposition = self.next3_relayaux1_start_address + 1                              # Property ID: 1, [-] (enum). Current position.
        self.next3_relayaux1_errors = self.next3_relayaux1_start_address + 3                                            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next3_relayaux1_operatingmodeselect = self.next3_relayaux1_start_address + 7                               # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next3_relayaux1_automodeselect = self.next3_relayaux1_start_address + 9                                    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next3_relayaux1_safestateselect = self.next3_relayaux1_start_address + 11                                  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next3_relayaux1_presetbatvoltactvth = self.next3_relayaux1_start_address + 13                              # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next3_relayaux1_presetbatvoltdeactvth = self.next3_relayaux1_start_address + 15                            # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next3_relayaux1_presetbatsocactth = self.next3_relayaux1_start_address + 17                                # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next3_relayaux1_presetbatsocdeactth = self.next3_relayaux1_start_address + 19                              # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next3_relayaux1_presetbattempactth = self.next3_relayaux1_start_address + 21                               # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next3_relayaux1_presetbattempdeactth = self.next3_relayaux1_start_address + 23                             # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next3_relayaux1_presetbatstateselect = self.next3_relayaux1_start_address + 25                             # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next3_relayaux1_presetpacselect = self.next3_relayaux1_start_address + 27                                  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next3_relayaux1_presetpacpowactth = self.next3_relayaux1_start_address + 29                                # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next3_relayaux1_presetpacpowdeactth = self.next3_relayaux1_start_address + 31                              # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next3_relayaux1_presetsolarexcessongridpowactth = self.next3_relayaux1_start_address + 33                  # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next3_relayaux1_presetsolarexcessongridpowdeactth = self.next3_relayaux1_start_address + 35                # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next3_relayaux1_presetcmdentryidx = self.next3_relayaux1_start_address + 41                                # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next3_relayaux1_preseterrorwarningselect = self.next3_relayaux1_start_address + 43                         # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next3_relayaux1_presetonsourceselect = self.next3_relayaux1_start_address + 45                             # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next3_relayaux1_presetaccouplingblankingtime = self.next3_relayaux1_start_address + 47                     # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next3_relayaux1_isvirtualrelay = self.next3_relayaux1_start_address + 49                                   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next3_relayaux1_presetadvancedlogicscombination = self.next3_relayaux1_start_address + 50                  # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next3_relayaux1_presetsolarpoweractth = self.next3_relayaux1_start_address + 54                            # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next3_relayaux1_presetsolarpowerdeactth = self.next3_relayaux1_start_address + 56                          # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next3_relayaux1_presetbatbatidx = self.next3_relayaux1_start_address + 58                                  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object RelayAux2 Modbus Address
        self.next3_relayaux2_start_address = 8400
        self.next3_relayaux2_isconnected = self.next3_relayaux2_start_address + 0                                       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next3_relayaux2_currentrelayposition = self.next3_relayaux2_start_address + 1                              # Property ID: 1, [-] (enum). Current position.
        self.next3_relayaux2_errors = self.next3_relayaux2_start_address + 3                                            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next3_relayaux2_operatingmodeselect = self.next3_relayaux2_start_address + 7                               # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next3_relayaux2_automodeselect = self.next3_relayaux2_start_address + 9                                    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next3_relayaux2_safestateselect = self.next3_relayaux2_start_address + 11                                  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next3_relayaux2_presetbatvoltactvth = self.next3_relayaux2_start_address + 13                              # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next3_relayaux2_presetbatvoltdeactvth = self.next3_relayaux2_start_address + 15                            # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next3_relayaux2_presetbatsocactth = self.next3_relayaux2_start_address + 17                                # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next3_relayaux2_presetbatsocdeactth = self.next3_relayaux2_start_address + 19                              # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next3_relayaux2_presetbattempactth = self.next3_relayaux2_start_address + 21                               # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next3_relayaux2_presetbattempdeactth = self.next3_relayaux2_start_address + 23                             # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next3_relayaux2_presetbatstateselect = self.next3_relayaux2_start_address + 25                             # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next3_relayaux2_presetpacselect = self.next3_relayaux2_start_address + 27                                  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next3_relayaux2_presetpacpowactth = self.next3_relayaux2_start_address + 29                                # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next3_relayaux2_presetpacpowdeactth = self.next3_relayaux2_start_address + 31                              # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next3_relayaux2_presetsolarexcessongridpowactth = self.next3_relayaux2_start_address + 33                  # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next3_relayaux2_presetsolarexcessongridpowdeactth = self.next3_relayaux2_start_address + 35                # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next3_relayaux2_presetcmdentryidx = self.next3_relayaux2_start_address + 41                                # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next3_relayaux2_preseterrorwarningselect = self.next3_relayaux2_start_address + 43                         # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next3_relayaux2_presetonsourceselect = self.next3_relayaux2_start_address + 45                             # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next3_relayaux2_presetaccouplingblankingtime = self.next3_relayaux2_start_address + 47                     # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next3_relayaux2_isvirtualrelay = self.next3_relayaux2_start_address + 49                                   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next3_relayaux2_presetadvancedlogicscombination = self.next3_relayaux2_start_address + 50                  # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next3_relayaux2_presetsolarpoweractth = self.next3_relayaux2_start_address + 54                            # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next3_relayaux2_presetsolarpowerdeactth = self.next3_relayaux2_start_address + 56                          # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next3_relayaux2_presetbatbatidx = self.next3_relayaux2_start_address + 58                                  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object RelayAux1TimeCtrl Modbus Address
        self.next3_relayaux1timectrl_start_address = 8700
        self.next3_relayaux1timectrl_timecontrolledmodeselect = self.next3_relayaux1timectrl_start_address + 0          # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next3_relayaux1timectrl_actmindelay = self.next3_relayaux1timectrl_start_address + 2                       # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next3_relayaux1timectrl_deactmindelay = self.next3_relayaux1timectrl_start_address + 4                     # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next3_relayaux1timectrl_actmintime = self.next3_relayaux1timectrl_start_address + 6                        # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next3_relayaux1timectrl_deactmintime = self.next3_relayaux1timectrl_start_address + 8                      # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next3_relayaux1timectrl_actmaxtime = self.next3_relayaux1timectrl_start_address + 10                       # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next3_relayaux1timectrl_acthourallow1 = self.next3_relayaux1timectrl_start_address + 12                    # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next3_relayaux1timectrl_acthourallow2 = self.next3_relayaux1timectrl_start_address + 14                    # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next3_relayaux1timectrl_actweekdaysallow = self.next3_relayaux1timectrl_start_address + 16                 # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_relayaux1timectrl_startingdate = self.next3_relayaux1timectrl_start_address + 18                     # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next3_relayaux1timectrl_startingtimesec = self.next3_relayaux1timectrl_start_address + 20                  # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next3_relayaux1timectrl_endingtimesec = self.next3_relayaux1timectrl_start_address + 22                    # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next3_relayaux1timectrl_selectedweekday = self.next3_relayaux1timectrl_start_address + 24                  # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_relayaux1timectrl_recurrenceweeks = self.next3_relayaux1timectrl_start_address + 26                  # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next3_relayaux1timectrl_rangeofrecurrenceselect = self.next3_relayaux1timectrl_start_address + 28          # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next3_relayaux1timectrl_endingdate = self.next3_relayaux1timectrl_start_address + 30                       # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next3_relayaux1timectrl_nbrofoccurrences = self.next3_relayaux1timectrl_start_address + 32                 # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next3_relayaux1timectrl_resettimecontrolled = self.next3_relayaux1timectrl_start_address + 34              # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object RelayAux2TimeCtrl Modbus Address
        self.next3_relayaux2timectrl_start_address = 9000
        self.next3_relayaux2timectrl_timecontrolledmodeselect = self.next3_relayaux2timectrl_start_address + 0          # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next3_relayaux2timectrl_actmindelay = self.next3_relayaux2timectrl_start_address + 2                       # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next3_relayaux2timectrl_deactmindelay = self.next3_relayaux2timectrl_start_address + 4                     # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next3_relayaux2timectrl_actmintime = self.next3_relayaux2timectrl_start_address + 6                        # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next3_relayaux2timectrl_deactmintime = self.next3_relayaux2timectrl_start_address + 8                      # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next3_relayaux2timectrl_actmaxtime = self.next3_relayaux2timectrl_start_address + 10                       # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next3_relayaux2timectrl_acthourallow1 = self.next3_relayaux2timectrl_start_address + 12                    # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next3_relayaux2timectrl_acthourallow2 = self.next3_relayaux2timectrl_start_address + 14                    # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next3_relayaux2timectrl_actweekdaysallow = self.next3_relayaux2timectrl_start_address + 16                 # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_relayaux2timectrl_startingdate = self.next3_relayaux2timectrl_start_address + 18                     # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next3_relayaux2timectrl_startingtimesec = self.next3_relayaux2timectrl_start_address + 20                  # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next3_relayaux2timectrl_endingtimesec = self.next3_relayaux2timectrl_start_address + 22                    # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next3_relayaux2timectrl_selectedweekday = self.next3_relayaux2timectrl_start_address + 24                  # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_relayaux2timectrl_recurrenceweeks = self.next3_relayaux2timectrl_start_address + 26                  # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next3_relayaux2timectrl_rangeofrecurrenceselect = self.next3_relayaux2timectrl_start_address + 28          # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next3_relayaux2timectrl_endingdate = self.next3_relayaux2timectrl_start_address + 30                       # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next3_relayaux2timectrl_nbrofoccurrences = self.next3_relayaux2timectrl_start_address + 32                 # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next3_relayaux2timectrl_resettimecontrolled = self.next3_relayaux2timectrl_start_address + 34              # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object CmdEntry1 Modbus Address
        self.next3_cmdentry1_start_address = 9300
        self.next3_cmdentry1_currentstate = self.next3_cmdentry1_start_address + 2                                      # Property ID: 2, [-] (bool). Current command entry state.
        self.next3_cmdentry1_cmdinsysidx = self.next3_cmdentry1_start_address + 3                                       # Property ID: 3, [-] (int). Index in the system of this command entry.
        self.next3_cmdentry1_configuration = self.next3_cmdentry1_start_address + 5                                     # Property ID: 4, [-] (enum). Configuration of this command entry.
        self.next3_cmdentry1_mirroredinternalauxrelayidx = self.next3_cmdentry1_start_address + 7                       # Property ID: 5, [-] (int). Index of the internal aux relay mirorred by this command entry, if configuration is set to \"Active when internal aux relay connected\" (value 32). 0 corresponds to the first internal aux relay, 1 to the second and so on.
        self.next3_cmdentry1_availableconfigurations = self.next3_cmdentry1_start_address + 9                           # Property ID: 6, [-] (bitfield). Available configurations of this command entry.
        self.next3_cmdentry1_analogvalue = self.next3_cmdentry1_start_address + 11                                      # Property ID: 7, [-] (float). Current command entry analog value. 0 when the measured analog voltage is 0V. 1 when the measured analog voltage is \"Max analog voltage\" (id 8). Always 1 if analog mode is not available or \"Cmd entry configuration\" (id 4) is not set to \"Analog mode\" (value 128).
        self.next3_cmdentry1_maxanalogvoltage = self.next3_cmdentry1_start_address + 13                                 # Property ID: 8, [V] (float). Maximum voltage value of the power supply used. \"Current analog value\" (id 7) is 1 when the measured analog voltage is greater than or equal to this value.

        # Object CmdEntry2 Modbus Address
        self.next3_cmdentry2_start_address = 9600
        self.next3_cmdentry2_currentstate = self.next3_cmdentry2_start_address + 2                                      # Property ID: 2, [-] (bool). Current command entry state.
        self.next3_cmdentry2_cmdinsysidx = self.next3_cmdentry2_start_address + 3                                       # Property ID: 3, [-] (int). Index in the system of this command entry.
        self.next3_cmdentry2_configuration = self.next3_cmdentry2_start_address + 5                                     # Property ID: 4, [-] (enum). Configuration of this command entry.
        self.next3_cmdentry2_mirroredinternalauxrelayidx = self.next3_cmdentry2_start_address + 7                       # Property ID: 5, [-] (int). Index of the internal aux relay mirorred by this command entry, if configuration is set to \"Active when internal aux relay connected\" (value 32). 0 corresponds to the first internal aux relay, 1 to the second and so on.
        self.next3_cmdentry2_availableconfigurations = self.next3_cmdentry2_start_address + 9                           # Property ID: 6, [-] (bitfield). Available configurations of this command entry.
        self.next3_cmdentry2_analogvalue = self.next3_cmdentry2_start_address + 11                                      # Property ID: 7, [-] (float). Current command entry analog value. 0 when the measured analog voltage is 0V. 1 when the measured analog voltage is \"Max analog voltage\" (id 8). Always 1 if analog mode is not available or \"Cmd entry configuration\" (id 4) is not set to \"Analog mode\" (value 128).
        self.next3_cmdentry2_maxanalogvoltage = self.next3_cmdentry2_start_address + 13                                 # Property ID: 8, [V] (float). Maximum voltage value of the power supply used. \"Current analog value\" (id 7) is 1 when the measured analog voltage is greater than or equal to this value.

        # Object BatteryContributor Modbus Address
        self.next3_batterycontributor_start_address = 9900
        self.next3_batterycontributor_chargingcurrent = self.next3_batterycontributor_start_address + 0                 # Property ID: 0, [A] (float). Charging current measured.
        self.next3_batterycontributor_temperaturesensorstate = self.next3_batterycontributor_start_address + 2          # Property ID: 1, [-] (enum). Indicates the temperature sensor state.
        self.next3_batterycontributor_temperature = self.next3_batterycontributor_start_address + 4                     # Property ID: 2, [°C] (float). Temperature measured.
        self.next3_batterycontributor_voltage = self.next3_batterycontributor_start_address + 10                        # Property ID: 5, [V] (float). Voltage measured.

        # Object Rs485iCommunicationBus Modbus Address
        self.next3_rs485icommunicationbus_start_address = 10200
        self.next3_rs485icommunicationbus_isterminationset = self.next3_rs485icommunicationbus_start_address + 2        # Property ID: 1, [-] (bool). Bus termination status for this communication bus.
        self.next3_rs485icommunicationbus_baudrate = self.next3_rs485icommunicationbus_start_address + 3                # Property ID: 2, [-] (enum). Connection baudrate.
        self.next3_rs485icommunicationbus_parity = self.next3_rs485icommunicationbus_start_address + 5                  # Property ID: 3, [-] (enum). Parity type to be used.
        self.next3_rs485icommunicationbus_stopbits = self.next3_rs485icommunicationbus_start_address + 7                # Property ID: 4, [-] (enum). Number of stop bits per transmitted character.
        self.next3_rs485icommunicationbus_databits = self.next3_rs485icommunicationbus_start_address + 9                # Property ID: 5, [-] (enum). Number of data bits per transmitted character.

        # Object CaniCommunicationBus Modbus Address
        self.next3_canicommunicationbus_start_address = 10500
        self.next3_canicommunicationbus_isterminationset = self.next3_canicommunicationbus_start_address + 2            # Property ID: 1, [-] (bool). Bus termination status for this communication bus.
        self.next3_canicommunicationbus_baudrate = self.next3_canicommunicationbus_start_address + 3                    # Property ID: 2, [-] (enum). Connection baudrate.
        self.next3_canicommunicationbus_parity = self.next3_canicommunicationbus_start_address + 5                      # Property ID: 3, [-] (enum). Parity type to be used.
        self.next3_canicommunicationbus_stopbits = self.next3_canicommunicationbus_start_address + 7                    # Property ID: 4, [-] (enum). Number of stop bits per transmitted character.
        self.next3_canicommunicationbus_databits = self.next3_canicommunicationbus_start_address + 9                    # Property ID: 5, [-] (enum). Number of data bits per transmitted character.

        # Object VirtualRelayAux3 Modbus Address
        self.next3_virtualrelayaux3_start_address = 10800
        self.next3_virtualrelayaux3_isconnected = self.next3_virtualrelayaux3_start_address + 0                         # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next3_virtualrelayaux3_currentrelayposition = self.next3_virtualrelayaux3_start_address + 1                # Property ID: 1, [-] (enum). Current position.
        self.next3_virtualrelayaux3_errors = self.next3_virtualrelayaux3_start_address + 3                              # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next3_virtualrelayaux3_operatingmodeselect = self.next3_virtualrelayaux3_start_address + 7                 # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next3_virtualrelayaux3_automodeselect = self.next3_virtualrelayaux3_start_address + 9                      # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next3_virtualrelayaux3_safestateselect = self.next3_virtualrelayaux3_start_address + 11                    # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next3_virtualrelayaux3_presetbatvoltactvth = self.next3_virtualrelayaux3_start_address + 13                # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next3_virtualrelayaux3_presetbatvoltdeactvth = self.next3_virtualrelayaux3_start_address + 15              # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next3_virtualrelayaux3_presetbatsocactth = self.next3_virtualrelayaux3_start_address + 17                  # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next3_virtualrelayaux3_presetbatsocdeactth = self.next3_virtualrelayaux3_start_address + 19                # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next3_virtualrelayaux3_presetbattempactth = self.next3_virtualrelayaux3_start_address + 21                 # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next3_virtualrelayaux3_presetbattempdeactth = self.next3_virtualrelayaux3_start_address + 23               # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next3_virtualrelayaux3_presetbatstateselect = self.next3_virtualrelayaux3_start_address + 25               # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next3_virtualrelayaux3_presetpacselect = self.next3_virtualrelayaux3_start_address + 27                    # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next3_virtualrelayaux3_presetpacpowactth = self.next3_virtualrelayaux3_start_address + 29                  # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next3_virtualrelayaux3_presetpacpowdeactth = self.next3_virtualrelayaux3_start_address + 31                # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next3_virtualrelayaux3_presetsolarexcessongridpowactth = self.next3_virtualrelayaux3_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next3_virtualrelayaux3_presetsolarexcessongridpowdeactth = self.next3_virtualrelayaux3_start_address + 35  # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next3_virtualrelayaux3_presetcmdentryidx = self.next3_virtualrelayaux3_start_address + 41                  # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next3_virtualrelayaux3_preseterrorwarningselect = self.next3_virtualrelayaux3_start_address + 43           # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next3_virtualrelayaux3_presetonsourceselect = self.next3_virtualrelayaux3_start_address + 45               # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next3_virtualrelayaux3_presetaccouplingblankingtime = self.next3_virtualrelayaux3_start_address + 47       # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next3_virtualrelayaux3_isvirtualrelay = self.next3_virtualrelayaux3_start_address + 49                     # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next3_virtualrelayaux3_presetadvancedlogicscombination = self.next3_virtualrelayaux3_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next3_virtualrelayaux3_presetsolarpoweractth = self.next3_virtualrelayaux3_start_address + 54              # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next3_virtualrelayaux3_presetsolarpowerdeactth = self.next3_virtualrelayaux3_start_address + 56            # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next3_virtualrelayaux3_presetbatbatidx = self.next3_virtualrelayaux3_start_address + 58                    # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object VirtualRelayAux4 Modbus Address
        self.next3_virtualrelayaux4_start_address = 11100
        self.next3_virtualrelayaux4_isconnected = self.next3_virtualrelayaux4_start_address + 0                         # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next3_virtualrelayaux4_currentrelayposition = self.next3_virtualrelayaux4_start_address + 1                # Property ID: 1, [-] (enum). Current position.
        self.next3_virtualrelayaux4_errors = self.next3_virtualrelayaux4_start_address + 3                              # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next3_virtualrelayaux4_operatingmodeselect = self.next3_virtualrelayaux4_start_address + 7                 # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next3_virtualrelayaux4_automodeselect = self.next3_virtualrelayaux4_start_address + 9                      # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next3_virtualrelayaux4_safestateselect = self.next3_virtualrelayaux4_start_address + 11                    # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next3_virtualrelayaux4_presetbatvoltactvth = self.next3_virtualrelayaux4_start_address + 13                # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next3_virtualrelayaux4_presetbatvoltdeactvth = self.next3_virtualrelayaux4_start_address + 15              # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next3_virtualrelayaux4_presetbatsocactth = self.next3_virtualrelayaux4_start_address + 17                  # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next3_virtualrelayaux4_presetbatsocdeactth = self.next3_virtualrelayaux4_start_address + 19                # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next3_virtualrelayaux4_presetbattempactth = self.next3_virtualrelayaux4_start_address + 21                 # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next3_virtualrelayaux4_presetbattempdeactth = self.next3_virtualrelayaux4_start_address + 23               # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next3_virtualrelayaux4_presetbatstateselect = self.next3_virtualrelayaux4_start_address + 25               # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next3_virtualrelayaux4_presetpacselect = self.next3_virtualrelayaux4_start_address + 27                    # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next3_virtualrelayaux4_presetpacpowactth = self.next3_virtualrelayaux4_start_address + 29                  # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next3_virtualrelayaux4_presetpacpowdeactth = self.next3_virtualrelayaux4_start_address + 31                # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next3_virtualrelayaux4_presetsolarexcessongridpowactth = self.next3_virtualrelayaux4_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next3_virtualrelayaux4_presetsolarexcessongridpowdeactth = self.next3_virtualrelayaux4_start_address + 35  # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next3_virtualrelayaux4_presetcmdentryidx = self.next3_virtualrelayaux4_start_address + 41                  # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next3_virtualrelayaux4_preseterrorwarningselect = self.next3_virtualrelayaux4_start_address + 43           # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next3_virtualrelayaux4_presetonsourceselect = self.next3_virtualrelayaux4_start_address + 45               # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next3_virtualrelayaux4_presetaccouplingblankingtime = self.next3_virtualrelayaux4_start_address + 47       # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next3_virtualrelayaux4_isvirtualrelay = self.next3_virtualrelayaux4_start_address + 49                     # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next3_virtualrelayaux4_presetadvancedlogicscombination = self.next3_virtualrelayaux4_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next3_virtualrelayaux4_presetsolarpoweractth = self.next3_virtualrelayaux4_start_address + 54              # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next3_virtualrelayaux4_presetsolarpowerdeactth = self.next3_virtualrelayaux4_start_address + 56            # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next3_virtualrelayaux4_presetbatbatidx = self.next3_virtualrelayaux4_start_address + 58                    # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object VirtualRelayAux3TimeCtrl Modbus Address
        self.next3_virtualrelayaux3timectrl_start_address = 11400
        self.next3_virtualrelayaux3timectrl_timecontrolledmodeselect = self.next3_virtualrelayaux3timectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next3_virtualrelayaux3timectrl_actmindelay = self.next3_virtualrelayaux3timectrl_start_address + 2         # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next3_virtualrelayaux3timectrl_deactmindelay = self.next3_virtualrelayaux3timectrl_start_address + 4       # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next3_virtualrelayaux3timectrl_actmintime = self.next3_virtualrelayaux3timectrl_start_address + 6          # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next3_virtualrelayaux3timectrl_deactmintime = self.next3_virtualrelayaux3timectrl_start_address + 8        # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next3_virtualrelayaux3timectrl_actmaxtime = self.next3_virtualrelayaux3timectrl_start_address + 10         # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next3_virtualrelayaux3timectrl_acthourallow1 = self.next3_virtualrelayaux3timectrl_start_address + 12      # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next3_virtualrelayaux3timectrl_acthourallow2 = self.next3_virtualrelayaux3timectrl_start_address + 14      # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next3_virtualrelayaux3timectrl_actweekdaysallow = self.next3_virtualrelayaux3timectrl_start_address + 16   # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_virtualrelayaux3timectrl_startingdate = self.next3_virtualrelayaux3timectrl_start_address + 18       # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next3_virtualrelayaux3timectrl_startingtimesec = self.next3_virtualrelayaux3timectrl_start_address + 20    # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next3_virtualrelayaux3timectrl_endingtimesec = self.next3_virtualrelayaux3timectrl_start_address + 22      # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next3_virtualrelayaux3timectrl_selectedweekday = self.next3_virtualrelayaux3timectrl_start_address + 24    # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_virtualrelayaux3timectrl_recurrenceweeks = self.next3_virtualrelayaux3timectrl_start_address + 26    # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next3_virtualrelayaux3timectrl_rangeofrecurrenceselect = self.next3_virtualrelayaux3timectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next3_virtualrelayaux3timectrl_endingdate = self.next3_virtualrelayaux3timectrl_start_address + 30         # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next3_virtualrelayaux3timectrl_nbrofoccurrences = self.next3_virtualrelayaux3timectrl_start_address + 32   # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next3_virtualrelayaux3timectrl_resettimecontrolled = self.next3_virtualrelayaux3timectrl_start_address + 34    # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object VirtualRelayAux4TimeCtrl Modbus Address
        self.next3_virtualrelayaux4timectrl_start_address = 11700
        self.next3_virtualrelayaux4timectrl_timecontrolledmodeselect = self.next3_virtualrelayaux4timectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next3_virtualrelayaux4timectrl_actmindelay = self.next3_virtualrelayaux4timectrl_start_address + 2         # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next3_virtualrelayaux4timectrl_deactmindelay = self.next3_virtualrelayaux4timectrl_start_address + 4       # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next3_virtualrelayaux4timectrl_actmintime = self.next3_virtualrelayaux4timectrl_start_address + 6          # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next3_virtualrelayaux4timectrl_deactmintime = self.next3_virtualrelayaux4timectrl_start_address + 8        # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next3_virtualrelayaux4timectrl_actmaxtime = self.next3_virtualrelayaux4timectrl_start_address + 10         # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next3_virtualrelayaux4timectrl_acthourallow1 = self.next3_virtualrelayaux4timectrl_start_address + 12      # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next3_virtualrelayaux4timectrl_acthourallow2 = self.next3_virtualrelayaux4timectrl_start_address + 14      # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next3_virtualrelayaux4timectrl_actweekdaysallow = self.next3_virtualrelayaux4timectrl_start_address + 16   # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_virtualrelayaux4timectrl_startingdate = self.next3_virtualrelayaux4timectrl_start_address + 18       # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next3_virtualrelayaux4timectrl_startingtimesec = self.next3_virtualrelayaux4timectrl_start_address + 20    # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next3_virtualrelayaux4timectrl_endingtimesec = self.next3_virtualrelayaux4timectrl_start_address + 22      # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next3_virtualrelayaux4timectrl_selectedweekday = self.next3_virtualrelayaux4timectrl_start_address + 24    # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next3_virtualrelayaux4timectrl_recurrenceweeks = self.next3_virtualrelayaux4timectrl_start_address + 26    # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next3_virtualrelayaux4timectrl_rangeofrecurrenceselect = self.next3_virtualrelayaux4timectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next3_virtualrelayaux4timectrl_endingdate = self.next3_virtualrelayaux4timectrl_start_address + 30         # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next3_virtualrelayaux4timectrl_nbrofoccurrences = self.next3_virtualrelayaux4timectrl_start_address + 32   # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next3_virtualrelayaux4timectrl_resettimecontrolled = self.next3_virtualrelayaux4timectrl_start_address + 34    # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object BatteryContributorExtSolarChargers Modbus Address
        self.next3_batterycontributorextsolarchargers_start_address = 12000
        self.next3_batterycontributorextsolarchargers_chargingcurrent = self.next3_batterycontributorextsolarchargers_start_address + 0    # Property ID: 0, [A] (float). Charging current measured.
        self.next3_batterycontributorextsolarchargers_temperaturesensorstate = self.next3_batterycontributorextsolarchargers_start_address + 2    # Property ID: 1, [-] (enum). Indicates the temperature sensor state.
        self.next3_batterycontributorextsolarchargers_temperature = self.next3_batterycontributorextsolarchargers_start_address + 4    # Property ID: 2, [°C] (float). Temperature measured.
        self.next3_batterycontributorextsolarchargers_voltage = self.next3_batterycontributorextsolarchargers_start_address + 10    # Property ID: 5, [V] (float). Voltage measured.

        # Object SolarCommonExtSolarChargers Modbus Address
        self.next3_solarcommonextsolarchargers_start_address = 12300
        self.next3_solarcommonextsolarchargers_turnon = self.next3_solarcommonextsolarchargers_start_address + 0        # Property ID: 0, [-] (signal). Turns on solar(s).
        self.next3_solarcommonextsolarchargers_turnoff = self.next3_solarcommonextsolarchargers_start_address + 1       # Property ID: 1, [-] (signal). Turns off solar(s).
        self.next3_solarcommonextsolarchargers_onoffstate = self.next3_solarcommonextsolarchargers_start_address + 2    # Property ID: 2, [-] (bool). Indicates solar(s) on/off state.
        self.next3_solarcommonextsolarchargers_enabledepolarization = self.next3_solarcommonextsolarchargers_start_address + 3    # Property ID: 3, [-] (signal). Enables depolarization.
        self.next3_solarcommonextsolarchargers_disabledepolarization = self.next3_solarcommonextsolarchargers_start_address + 4    # Property ID: 4, [-] (signal). Disables depolarization.
        self.next3_solarcommonextsolarchargers_power = self.next3_solarcommonextsolarchargers_start_address + 5         # Property ID: 5, [W] (float). Power produced.
        self.next3_solarcommonextsolarchargers_previousdayenergy = self.next3_solarcommonextsolarchargers_start_address + 7    # Property ID: 8, [Wh] (float). Energy produced for the previous day.
        self.next3_solarcommonextsolarchargers_powerlimit = self.next3_solarcommonextsolarchargers_start_address + 9    # Property ID: 9, [W] (uint). Solar(s) max power limit.
        self.next3_solarcommonextsolarchargers_dayenergy = self.next3_solarcommonextsolarchargers_start_address + 11    # Property ID: 10, [Wh] (float). Energy produced for the current day.
        self.next3_solarcommonextsolarchargers_resetableenergy = self.next3_solarcommonextsolarchargers_start_address + 15    # Property ID: 12, [Wh] (float64). Energy produced (can be reset).
        self.next3_solarcommonextsolarchargers_totalenergy = self.next3_solarcommonextsolarchargers_start_address + 19  # Property ID: 13, [Wh] (float64). Total energy produced (whole life).

        # Object SolarGroupExtSolarChargers Modbus Address
        self.next3_solargroupextsolarchargers_start_address = 12600
        self.next3_solargroupextsolarchargers_nbr = self.next3_solargroupextsolarchargers_start_address + 0             # Property ID: 0, [-] (uint). Number of converters.
        self.next3_solargroupextsolarchargers_status = self.next3_solargroupextsolarchargers_start_address + 2          # Property ID: 1, [-] (bitfield). Current status.
        self.next3_solargroupextsolarchargers_vt40nbr = self.next3_solargroupextsolarchargers_start_address + 4         # Property ID: 2, [-] (uint). Number of vt40.
        self.next3_solargroupextsolarchargers_vt65nbr = self.next3_solargroupextsolarchargers_start_address + 6         # Property ID: 3, [-] (uint). Number of vt65.
        self.next3_solargroupextsolarchargers_vt80nbr = self.next3_solargroupextsolarchargers_start_address + 8         # Property ID: 4, [-] (uint). Number of vt80.
        self.next3_solargroupextsolarchargers_vs70nbr = self.next3_solargroupextsolarchargers_start_address + 10        # Property ID: 5, [-] (uint). Number of vs70.
        self.next3_solargroupextsolarchargers_vs120nbr = self.next3_solargroupextsolarchargers_start_address + 12       # Property ID: 6, [-] (uint). Number of vs120.


        # Group Next1 Modbus Address
        # Object IdCard Modbus Address
        self.next1_idcard_start_address = 0
        self.next1_idcard_serialnumber = self.next1_idcard_start_address + 4                                            # Property ID: 2, [-] (char[15]). Serial Number of this Studer Innotec device. 
        self.next1_idcard_softwarepackageversion = self.next1_idcard_start_address + 14                                 # Property ID: 4, [-] (uint). Software package version in this format : MAJOR.MIDDLE.MINOR.PATCH, encoded as follows from MSB to LSB : MAJOR (8 bits), MIDDLE (8bits), MINOR (12 bits), PATCH (4 bits).
        self.next1_idcard_softwarerevisionsha1 = self.next1_idcard_start_address + 18                                   # Property ID: 6, [-] (char[7]). SHA-1 of the software project commit
        self.next1_idcard_objectmodelversion = self.next1_idcard_start_address + 30                                     # Property ID: 8, [-] (uint). Version of the currently used ObjectModel in this format : MAJOR.MINOR, encoded as follows from MSB to LSB : MAJOR (16 bits), MINOR (16 bits).

        # Object BaseApp Modbus Address
        self.next1_baseapp_start_address = 300
        self.next1_baseapp_warnings = self.next1_baseapp_start_address + 5                                              # Property ID: 5, [-] (bitfield). Current warnings.
        self.next1_baseapp_restoreallnvmvalues = self.next1_baseapp_start_address + 15                                  # Property ID: 10, [-] (signal). Restore the original value (from Non-Volatile Memory) for all properties that were changed with WriteInRAM.

        # Object CanNode Modbus Address
        self.next1_cannode_start_address = 900
        self.next1_cannode_status = self.next1_cannode_start_address + 2                                                # Property ID: 1, [-] (enum). Stores the node status.
        self.next1_cannode_txerrorcounter = self.next1_cannode_start_address + 4                                        # Property ID: 2, [-] (int). Counter of the TX errors.
        self.next1_cannode_rxerrorcounter = self.next1_cannode_start_address + 6                                        # Property ID: 3, [-] (int). Counter of the RX errors.
        self.next1_cannode_busterminationset = self.next1_cannode_start_address + 8                                     # Property ID: 4, [-] (bool). Bus termination status for this node.

        # Object Device Modbus Address
        self.next1_device_start_address = 1800
        self.next1_device_blinkingstate = self.next1_device_start_address + 0                                           # Property ID: 0, [-] (bool). If set, the device LEDs will blink.
        self.next1_device_deviceid = self.next1_device_start_address + 1                                                # Property ID: 1, [-] (int). System-wide ID of the device in topology.
        self.next1_device_batteryid = self.next1_device_start_address + 3                                               # Property ID: 2, [-] (int). System-wide ID of the battery in topology.
        self.next1_device_totalfunctioningtimesec = self.next1_device_start_address + 5                                 # Property ID: 3, [s] (uint). Total functioning time in this device's life.

        # Object Next1 Modbus Address
        self.next1_next1_start_address = 2700
        self.next1_next1_status = self.next1_next1_start_address + 0                                                    # Property ID: 0, [-] (enum). Current status.
        self.next1_next1_errors = self.next1_next1_start_address + 2                                                    # Property ID: 1, [-] (bitfield). Current errors.
        self.next1_next1_temptransfo = self.next1_next1_start_address + 18                                              # Property ID: 9, [°C] (float). Temperature of the transformer.
        self.next1_next1_tempinductor = self.next1_next1_start_address + 20                                             # Property ID: 10, [°C] (float). Temperature of the inductor.
        self.next1_next1_tempinternal = self.next1_next1_start_address + 22                                             # Property ID: 11, [°C] (float). Temperature of the internal air.
        self.next1_next1_temppowerbridgea = self.next1_next1_start_address + 24                                         # Property ID: 12, [°C] (float). Temperature power bridge A measured.
        self.next1_next1_temppowerbridgeb = self.next1_next1_start_address + 26                                         # Property ID: 13, [°C] (float). Temperature power bridge B measured.
        self.next1_next1_temppowerbridgec = self.next1_next1_start_address + 28                                         # Property ID: 14, [°C] (float). Temperature power bridge C measured.
        self.next1_next1_fan1speed = self.next1_next1_start_address + 32                                                # Property ID: 16, [RPM] (float). Revolution speed of fan 1 measured.
        self.next1_next1_fan2speed = self.next1_next1_start_address + 34                                                # Property ID: 17, [RPM] (float). Revolution speed of fan 2 measured.
        self.next1_next1_externalpowersupplycurrent = self.next1_next1_start_address + 42                               # Property ID: 21, [A] (float). External power supply current measured.
        self.next1_next1_tempmaxacboard = self.next1_next1_start_address + 44                                           # Property ID: 22, [°C] (float). Maximal temperature measured on AC board.
        self.next1_next1_tempmcu = self.next1_next1_start_address + 46                                                  # Property ID: 23, [°C] (float). Temperature of MCU.
        self.next1_next1_powerlimitationcause = self.next1_next1_start_address + 48                                     # Property ID: 25, [-] (enum). Describes the origin of the power limitation.
        self.next1_next1_temp1 = self.next1_next1_start_address + 50                                                    # Property ID: 26, [°C] (float). Temperature 1.
        self.next1_next1_temp2 = self.next1_next1_start_address + 52                                                    # Property ID: 27, [°C] (float). Temperature 2.
        self.next1_next1_temp3 = self.next1_next1_start_address + 54                                                    # Property ID: 28, [°C] (float). Temperature 3.
        self.next1_next1_temp4 = self.next1_next1_start_address + 56                                                    # Property ID: 29, [°C] (float). Temperature 4.
        self.next1_next1_temp5 = self.next1_next1_start_address + 58                                                    # Property ID: 30, [°C] (float). Temperature 5.

        # Object RelayAux1 Modbus Address
        self.next1_relayaux1_start_address = 3000
        self.next1_relayaux1_isconnected = self.next1_relayaux1_start_address + 0                                       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next1_relayaux1_currentrelayposition = self.next1_relayaux1_start_address + 1                              # Property ID: 1, [-] (enum). Current position.
        self.next1_relayaux1_errors = self.next1_relayaux1_start_address + 3                                            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next1_relayaux1_operatingmodeselect = self.next1_relayaux1_start_address + 7                               # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next1_relayaux1_automodeselect = self.next1_relayaux1_start_address + 9                                    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next1_relayaux1_safestateselect = self.next1_relayaux1_start_address + 11                                  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next1_relayaux1_presetbatvoltactvth = self.next1_relayaux1_start_address + 13                              # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next1_relayaux1_presetbatvoltdeactvth = self.next1_relayaux1_start_address + 15                            # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next1_relayaux1_presetbatsocactth = self.next1_relayaux1_start_address + 17                                # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next1_relayaux1_presetbatsocdeactth = self.next1_relayaux1_start_address + 19                              # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next1_relayaux1_presetbattempactth = self.next1_relayaux1_start_address + 21                               # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next1_relayaux1_presetbattempdeactth = self.next1_relayaux1_start_address + 23                             # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next1_relayaux1_presetbatstateselect = self.next1_relayaux1_start_address + 25                             # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next1_relayaux1_presetpacselect = self.next1_relayaux1_start_address + 27                                  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next1_relayaux1_presetpacpowactth = self.next1_relayaux1_start_address + 29                                # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next1_relayaux1_presetpacpowdeactth = self.next1_relayaux1_start_address + 31                              # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next1_relayaux1_presetsolarexcessongridpowactth = self.next1_relayaux1_start_address + 33                  # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next1_relayaux1_presetsolarexcessongridpowdeactth = self.next1_relayaux1_start_address + 35                # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next1_relayaux1_presetcmdentryidx = self.next1_relayaux1_start_address + 41                                # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next1_relayaux1_preseterrorwarningselect = self.next1_relayaux1_start_address + 43                         # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next1_relayaux1_presetonsourceselect = self.next1_relayaux1_start_address + 45                             # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next1_relayaux1_presetaccouplingblankingtime = self.next1_relayaux1_start_address + 47                     # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next1_relayaux1_isvirtualrelay = self.next1_relayaux1_start_address + 49                                   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next1_relayaux1_presetadvancedlogicscombination = self.next1_relayaux1_start_address + 50                  # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next1_relayaux1_presetsolarpoweractth = self.next1_relayaux1_start_address + 54                            # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next1_relayaux1_presetsolarpowerdeactth = self.next1_relayaux1_start_address + 56                          # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next1_relayaux1_presetbatbatidx = self.next1_relayaux1_start_address + 58                                  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object RelayAux2 Modbus Address
        self.next1_relayaux2_start_address = 3300
        self.next1_relayaux2_isconnected = self.next1_relayaux2_start_address + 0                                       # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next1_relayaux2_currentrelayposition = self.next1_relayaux2_start_address + 1                              # Property ID: 1, [-] (enum). Current position.
        self.next1_relayaux2_errors = self.next1_relayaux2_start_address + 3                                            # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next1_relayaux2_operatingmodeselect = self.next1_relayaux2_start_address + 7                               # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next1_relayaux2_automodeselect = self.next1_relayaux2_start_address + 9                                    # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next1_relayaux2_safestateselect = self.next1_relayaux2_start_address + 11                                  # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next1_relayaux2_presetbatvoltactvth = self.next1_relayaux2_start_address + 13                              # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next1_relayaux2_presetbatvoltdeactvth = self.next1_relayaux2_start_address + 15                            # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next1_relayaux2_presetbatsocactth = self.next1_relayaux2_start_address + 17                                # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next1_relayaux2_presetbatsocdeactth = self.next1_relayaux2_start_address + 19                              # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next1_relayaux2_presetbattempactth = self.next1_relayaux2_start_address + 21                               # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next1_relayaux2_presetbattempdeactth = self.next1_relayaux2_start_address + 23                             # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next1_relayaux2_presetbatstateselect = self.next1_relayaux2_start_address + 25                             # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next1_relayaux2_presetpacselect = self.next1_relayaux2_start_address + 27                                  # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next1_relayaux2_presetpacpowactth = self.next1_relayaux2_start_address + 29                                # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next1_relayaux2_presetpacpowdeactth = self.next1_relayaux2_start_address + 31                              # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next1_relayaux2_presetsolarexcessongridpowactth = self.next1_relayaux2_start_address + 33                  # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next1_relayaux2_presetsolarexcessongridpowdeactth = self.next1_relayaux2_start_address + 35                # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next1_relayaux2_presetcmdentryidx = self.next1_relayaux2_start_address + 41                                # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next1_relayaux2_preseterrorwarningselect = self.next1_relayaux2_start_address + 43                         # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next1_relayaux2_presetonsourceselect = self.next1_relayaux2_start_address + 45                             # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next1_relayaux2_presetaccouplingblankingtime = self.next1_relayaux2_start_address + 47                     # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next1_relayaux2_isvirtualrelay = self.next1_relayaux2_start_address + 49                                   # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next1_relayaux2_presetadvancedlogicscombination = self.next1_relayaux2_start_address + 50                  # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next1_relayaux2_presetsolarpoweractth = self.next1_relayaux2_start_address + 54                            # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next1_relayaux2_presetsolarpowerdeactth = self.next1_relayaux2_start_address + 56                          # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next1_relayaux2_presetbatbatidx = self.next1_relayaux2_start_address + 58                                  # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object RelayAux1TimeCtrl Modbus Address
        self.next1_relayaux1timectrl_start_address = 3600
        self.next1_relayaux1timectrl_timecontrolledmodeselect = self.next1_relayaux1timectrl_start_address + 0          # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next1_relayaux1timectrl_actmindelay = self.next1_relayaux1timectrl_start_address + 2                       # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next1_relayaux1timectrl_deactmindelay = self.next1_relayaux1timectrl_start_address + 4                     # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next1_relayaux1timectrl_actmintime = self.next1_relayaux1timectrl_start_address + 6                        # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next1_relayaux1timectrl_deactmintime = self.next1_relayaux1timectrl_start_address + 8                      # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next1_relayaux1timectrl_actmaxtime = self.next1_relayaux1timectrl_start_address + 10                       # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next1_relayaux1timectrl_acthourallow1 = self.next1_relayaux1timectrl_start_address + 12                    # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next1_relayaux1timectrl_acthourallow2 = self.next1_relayaux1timectrl_start_address + 14                    # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next1_relayaux1timectrl_actweekdaysallow = self.next1_relayaux1timectrl_start_address + 16                 # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_relayaux1timectrl_startingdate = self.next1_relayaux1timectrl_start_address + 18                     # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next1_relayaux1timectrl_startingtimesec = self.next1_relayaux1timectrl_start_address + 20                  # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next1_relayaux1timectrl_endingtimesec = self.next1_relayaux1timectrl_start_address + 22                    # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next1_relayaux1timectrl_selectedweekday = self.next1_relayaux1timectrl_start_address + 24                  # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_relayaux1timectrl_recurrenceweeks = self.next1_relayaux1timectrl_start_address + 26                  # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next1_relayaux1timectrl_rangeofrecurrenceselect = self.next1_relayaux1timectrl_start_address + 28          # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next1_relayaux1timectrl_endingdate = self.next1_relayaux1timectrl_start_address + 30                       # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next1_relayaux1timectrl_nbrofoccurrences = self.next1_relayaux1timectrl_start_address + 32                 # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next1_relayaux1timectrl_resettimecontrolled = self.next1_relayaux1timectrl_start_address + 34              # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object RelayAux2TimeCtrl Modbus Address
        self.next1_relayaux2timectrl_start_address = 3900
        self.next1_relayaux2timectrl_timecontrolledmodeselect = self.next1_relayaux2timectrl_start_address + 0          # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next1_relayaux2timectrl_actmindelay = self.next1_relayaux2timectrl_start_address + 2                       # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next1_relayaux2timectrl_deactmindelay = self.next1_relayaux2timectrl_start_address + 4                     # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next1_relayaux2timectrl_actmintime = self.next1_relayaux2timectrl_start_address + 6                        # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next1_relayaux2timectrl_deactmintime = self.next1_relayaux2timectrl_start_address + 8                      # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next1_relayaux2timectrl_actmaxtime = self.next1_relayaux2timectrl_start_address + 10                       # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next1_relayaux2timectrl_acthourallow1 = self.next1_relayaux2timectrl_start_address + 12                    # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next1_relayaux2timectrl_acthourallow2 = self.next1_relayaux2timectrl_start_address + 14                    # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next1_relayaux2timectrl_actweekdaysallow = self.next1_relayaux2timectrl_start_address + 16                 # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_relayaux2timectrl_startingdate = self.next1_relayaux2timectrl_start_address + 18                     # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next1_relayaux2timectrl_startingtimesec = self.next1_relayaux2timectrl_start_address + 20                  # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next1_relayaux2timectrl_endingtimesec = self.next1_relayaux2timectrl_start_address + 22                    # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next1_relayaux2timectrl_selectedweekday = self.next1_relayaux2timectrl_start_address + 24                  # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_relayaux2timectrl_recurrenceweeks = self.next1_relayaux2timectrl_start_address + 26                  # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next1_relayaux2timectrl_rangeofrecurrenceselect = self.next1_relayaux2timectrl_start_address + 28          # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next1_relayaux2timectrl_endingdate = self.next1_relayaux2timectrl_start_address + 30                       # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next1_relayaux2timectrl_nbrofoccurrences = self.next1_relayaux2timectrl_start_address + 32                 # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next1_relayaux2timectrl_resettimecontrolled = self.next1_relayaux2timectrl_start_address + 34              # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object CmdEntry1 Modbus Address
        self.next1_cmdentry1_start_address = 4200
        self.next1_cmdentry1_currentstate = self.next1_cmdentry1_start_address + 2                                      # Property ID: 2, [-] (bool). Current command entry state.
        self.next1_cmdentry1_cmdinsysidx = self.next1_cmdentry1_start_address + 3                                       # Property ID: 3, [-] (int). Index in the system of this command entry.
        self.next1_cmdentry1_configuration = self.next1_cmdentry1_start_address + 5                                     # Property ID: 4, [-] (enum). Configuration of this command entry.
        self.next1_cmdentry1_mirroredinternalauxrelayidx = self.next1_cmdentry1_start_address + 7                       # Property ID: 5, [-] (int). Index of the internal aux relay mirorred by this command entry, if configuration is set to \"Active when internal aux relay connected\" (value 32). 0 corresponds to the first internal aux relay, 1 to the second and so on.
        self.next1_cmdentry1_availableconfigurations = self.next1_cmdentry1_start_address + 9                           # Property ID: 6, [-] (bitfield). Available configurations of this command entry.
        self.next1_cmdentry1_analogvalue = self.next1_cmdentry1_start_address + 11                                      # Property ID: 7, [-] (float). Current command entry analog value. 0 when the measured analog voltage is 0V. 1 when the measured analog voltage is \"Max analog voltage\" (id 8). Always 1 if analog mode is not available or \"Cmd entry configuration\" (id 4) is not set to \"Analog mode\" (value 128).
        self.next1_cmdentry1_maxanalogvoltage = self.next1_cmdentry1_start_address + 13                                 # Property ID: 8, [V] (float). Maximum voltage value of the power supply used. \"Current analog value\" (id 7) is 1 when the measured analog voltage is greater than or equal to this value.

        # Object CmdEntry2 Modbus Address
        self.next1_cmdentry2_start_address = 4500
        self.next1_cmdentry2_currentstate = self.next1_cmdentry2_start_address + 2                                      # Property ID: 2, [-] (bool). Current command entry state.
        self.next1_cmdentry2_cmdinsysidx = self.next1_cmdentry2_start_address + 3                                       # Property ID: 3, [-] (int). Index in the system of this command entry.
        self.next1_cmdentry2_configuration = self.next1_cmdentry2_start_address + 5                                     # Property ID: 4, [-] (enum). Configuration of this command entry.
        self.next1_cmdentry2_mirroredinternalauxrelayidx = self.next1_cmdentry2_start_address + 7                       # Property ID: 5, [-] (int). Index of the internal aux relay mirorred by this command entry, if configuration is set to \"Active when internal aux relay connected\" (value 32). 0 corresponds to the first internal aux relay, 1 to the second and so on.
        self.next1_cmdentry2_availableconfigurations = self.next1_cmdentry2_start_address + 9                           # Property ID: 6, [-] (bitfield). Available configurations of this command entry.
        self.next1_cmdentry2_analogvalue = self.next1_cmdentry2_start_address + 11                                      # Property ID: 7, [-] (float). Current command entry analog value. 0 when the measured analog voltage is 0V. 1 when the measured analog voltage is \"Max analog voltage\" (id 8). Always 1 if analog mode is not available or \"Cmd entry configuration\" (id 4) is not set to \"Analog mode\" (value 128).
        self.next1_cmdentry2_maxanalogvoltage = self.next1_cmdentry2_start_address + 13                                 # Property ID: 8, [V] (float). Maximum voltage value of the power supply used. \"Current analog value\" (id 7) is 1 when the measured analog voltage is greater than or equal to this value.

        # Object BatteryContributor Modbus Address
        self.next1_batterycontributor_start_address = 4800
        self.next1_batterycontributor_chargingcurrent = self.next1_batterycontributor_start_address + 0                 # Property ID: 0, [A] (float). Charging current measured.
        self.next1_batterycontributor_temperaturesensorstate = self.next1_batterycontributor_start_address + 2          # Property ID: 1, [-] (enum). Indicates the temperature sensor state.
        self.next1_batterycontributor_temperature = self.next1_batterycontributor_start_address + 4                     # Property ID: 2, [°C] (float). Temperature measured.
        self.next1_batterycontributor_voltage = self.next1_batterycontributor_start_address + 10                        # Property ID: 5, [V] (float). Voltage measured.

        # Object Rs485iCommunicationBus Modbus Address
        self.next1_rs485icommunicationbus_start_address = 5100
        self.next1_rs485icommunicationbus_isterminationset = self.next1_rs485icommunicationbus_start_address + 2        # Property ID: 1, [-] (bool). Bus termination status for this communication bus.
        self.next1_rs485icommunicationbus_baudrate = self.next1_rs485icommunicationbus_start_address + 3                # Property ID: 2, [-] (enum). Connection baudrate.
        self.next1_rs485icommunicationbus_parity = self.next1_rs485icommunicationbus_start_address + 5                  # Property ID: 3, [-] (enum). Parity type to be used.
        self.next1_rs485icommunicationbus_stopbits = self.next1_rs485icommunicationbus_start_address + 7                # Property ID: 4, [-] (enum). Number of stop bits per transmitted character.
        self.next1_rs485icommunicationbus_databits = self.next1_rs485icommunicationbus_start_address + 9                # Property ID: 5, [-] (enum). Number of data bits per transmitted character.

        # Object CaniCommunicationBus Modbus Address
        self.next1_canicommunicationbus_start_address = 5400
        self.next1_canicommunicationbus_isterminationset = self.next1_canicommunicationbus_start_address + 2            # Property ID: 1, [-] (bool). Bus termination status for this communication bus.
        self.next1_canicommunicationbus_baudrate = self.next1_canicommunicationbus_start_address + 3                    # Property ID: 2, [-] (enum). Connection baudrate.
        self.next1_canicommunicationbus_parity = self.next1_canicommunicationbus_start_address + 5                      # Property ID: 3, [-] (enum). Parity type to be used.
        self.next1_canicommunicationbus_stopbits = self.next1_canicommunicationbus_start_address + 7                    # Property ID: 4, [-] (enum). Number of stop bits per transmitted character.
        self.next1_canicommunicationbus_databits = self.next1_canicommunicationbus_start_address + 9                    # Property ID: 5, [-] (enum). Number of data bits per transmitted character.

        # Object VirtualRelayAux3 Modbus Address
        self.next1_virtualrelayaux3_start_address = 5700
        self.next1_virtualrelayaux3_isconnected = self.next1_virtualrelayaux3_start_address + 0                         # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next1_virtualrelayaux3_currentrelayposition = self.next1_virtualrelayaux3_start_address + 1                # Property ID: 1, [-] (enum). Current position.
        self.next1_virtualrelayaux3_errors = self.next1_virtualrelayaux3_start_address + 3                              # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next1_virtualrelayaux3_operatingmodeselect = self.next1_virtualrelayaux3_start_address + 7                 # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next1_virtualrelayaux3_automodeselect = self.next1_virtualrelayaux3_start_address + 9                      # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next1_virtualrelayaux3_safestateselect = self.next1_virtualrelayaux3_start_address + 11                    # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next1_virtualrelayaux3_presetbatvoltactvth = self.next1_virtualrelayaux3_start_address + 13                # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next1_virtualrelayaux3_presetbatvoltdeactvth = self.next1_virtualrelayaux3_start_address + 15              # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next1_virtualrelayaux3_presetbatsocactth = self.next1_virtualrelayaux3_start_address + 17                  # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next1_virtualrelayaux3_presetbatsocdeactth = self.next1_virtualrelayaux3_start_address + 19                # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next1_virtualrelayaux3_presetbattempactth = self.next1_virtualrelayaux3_start_address + 21                 # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next1_virtualrelayaux3_presetbattempdeactth = self.next1_virtualrelayaux3_start_address + 23               # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next1_virtualrelayaux3_presetbatstateselect = self.next1_virtualrelayaux3_start_address + 25               # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next1_virtualrelayaux3_presetpacselect = self.next1_virtualrelayaux3_start_address + 27                    # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next1_virtualrelayaux3_presetpacpowactth = self.next1_virtualrelayaux3_start_address + 29                  # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next1_virtualrelayaux3_presetpacpowdeactth = self.next1_virtualrelayaux3_start_address + 31                # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next1_virtualrelayaux3_presetsolarexcessongridpowactth = self.next1_virtualrelayaux3_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next1_virtualrelayaux3_presetsolarexcessongridpowdeactth = self.next1_virtualrelayaux3_start_address + 35  # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next1_virtualrelayaux3_presetcmdentryidx = self.next1_virtualrelayaux3_start_address + 41                  # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next1_virtualrelayaux3_preseterrorwarningselect = self.next1_virtualrelayaux3_start_address + 43           # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next1_virtualrelayaux3_presetonsourceselect = self.next1_virtualrelayaux3_start_address + 45               # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next1_virtualrelayaux3_presetaccouplingblankingtime = self.next1_virtualrelayaux3_start_address + 47       # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next1_virtualrelayaux3_isvirtualrelay = self.next1_virtualrelayaux3_start_address + 49                     # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next1_virtualrelayaux3_presetadvancedlogicscombination = self.next1_virtualrelayaux3_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next1_virtualrelayaux3_presetsolarpoweractth = self.next1_virtualrelayaux3_start_address + 54              # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next1_virtualrelayaux3_presetsolarpowerdeactth = self.next1_virtualrelayaux3_start_address + 56            # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next1_virtualrelayaux3_presetbatbatidx = self.next1_virtualrelayaux3_start_address + 58                    # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object VirtualRelayAux4 Modbus Address
        self.next1_virtualrelayaux4_start_address = 6000
        self.next1_virtualrelayaux4_isconnected = self.next1_virtualrelayaux4_start_address + 0                         # Property ID: 0, [-] (bool). Shows the relay current state.
        self.next1_virtualrelayaux4_currentrelayposition = self.next1_virtualrelayaux4_start_address + 1                # Property ID: 1, [-] (enum). Current position.
        self.next1_virtualrelayaux4_errors = self.next1_virtualrelayaux4_start_address + 3                              # Property ID: 2, [-] (enum). Relay aux list of errors.
        self.next1_virtualrelayaux4_operatingmodeselect = self.next1_virtualrelayaux4_start_address + 7                 # Property ID: 4, [-] (enum). Selection of controlled relay operating mode.
        self.next1_virtualrelayaux4_automodeselect = self.next1_virtualrelayaux4_start_address + 9                      # Property ID: 5, [-] (enum). Selection of the automatic configuration.
        self.next1_virtualrelayaux4_safestateselect = self.next1_virtualrelayaux4_start_address + 11                    # Property ID: 6, [-] (enum). Selection of the controlled relay safe state position in case of problem or undetermined condition.
        self.next1_virtualrelayaux4_presetbatvoltactvth = self.next1_virtualrelayaux4_start_address + 13                # Property ID: 7, [V] (float). Pre-set battery voltage activation threshold voltage.
        self.next1_virtualrelayaux4_presetbatvoltdeactvth = self.next1_virtualrelayaux4_start_address + 15              # Property ID: 8, [V] (float). Pre-set battery voltage deactivation threshold voltage.
        self.next1_virtualrelayaux4_presetbatsocactth = self.next1_virtualrelayaux4_start_address + 17                  # Property ID: 9, [%] (uint). Pre-set battery SOC activation threshold SOC.
        self.next1_virtualrelayaux4_presetbatsocdeactth = self.next1_virtualrelayaux4_start_address + 19                # Property ID: 10, [%] (uint). Pre-set battery SOC deactivation threshold SOC.
        self.next1_virtualrelayaux4_presetbattempactth = self.next1_virtualrelayaux4_start_address + 21                 # Property ID: 11, [°C] (uint). Pre-set battery temperature activation threshold temperature.
        self.next1_virtualrelayaux4_presetbattempdeactth = self.next1_virtualrelayaux4_start_address + 23               # Property ID: 12, [°C] (uint). Pre-set battery temperature deactivation threshold temperature.
        self.next1_virtualrelayaux4_presetbatstateselect = self.next1_virtualrelayaux4_start_address + 25               # Property ID: 13, [-] (bitfield). Pre-set battery charging state selection of the triggering states. Multiple choice possible.
        self.next1_virtualrelayaux4_presetpacselect = self.next1_virtualrelayaux4_start_address + 27                    # Property ID: 14, [-] (enum). Pre-set power AC selection of the source/load active power for comparison.
        self.next1_virtualrelayaux4_presetpacpowactth = self.next1_virtualrelayaux4_start_address + 29                  # Property ID: 15, [W] (float). Pre-set power AC activation threshold power.
        self.next1_virtualrelayaux4_presetpacpowdeactth = self.next1_virtualrelayaux4_start_address + 31                # Property ID: 16, [W] (float). Pre-set power AC deactivation threshold power.
        self.next1_virtualrelayaux4_presetsolarexcessongridpowactth = self.next1_virtualrelayaux4_start_address + 33    # Property ID: 17, [W] (float). Pre-set solar excess on-grid activation threshold power.
        self.next1_virtualrelayaux4_presetsolarexcessongridpowdeactth = self.next1_virtualrelayaux4_start_address + 35  # Property ID: 18, [W] (float). Pre-set solar excess on-grid deactivation threshold power.
        self.next1_virtualrelayaux4_presetcmdentryidx = self.next1_virtualrelayaux4_start_address + 41                  # Property ID: 21, [-] (uint). Index of the command entry interface used to control the relay.
        self.next1_virtualrelayaux4_preseterrorwarningselect = self.next1_virtualrelayaux4_start_address + 43           # Property ID: 22, [-] (bitfield). Pre-set errors and warnings selection of the triggering signal.
        self.next1_virtualrelayaux4_presetonsourceselect = self.next1_virtualrelayaux4_start_address + 45               # Property ID: 23, [-] (enum). Pre-set on source selection.
        self.next1_virtualrelayaux4_presetaccouplingblankingtime = self.next1_virtualrelayaux4_start_address + 47       # Property ID: 24, [s.] (uint). Pre-set AC-coupling time during which the relay remains open during on-grid to off-grid transition.
        self.next1_virtualrelayaux4_isvirtualrelay = self.next1_virtualrelayaux4_start_address + 49                     # Property ID: 25, [-] (bool). Shows if the relay is a virtual relay.
        self.next1_virtualrelayaux4_presetadvancedlogicscombination = self.next1_virtualrelayaux4_start_address + 50    # Property ID: 26, [-] (uint). Pre-set advanced logics, combination function (see advanced documentation).
        self.next1_virtualrelayaux4_presetsolarpoweractth = self.next1_virtualrelayaux4_start_address + 54              # Property ID: 28, [W] (float). Pre-set solar power activation threshold.
        self.next1_virtualrelayaux4_presetsolarpowerdeactth = self.next1_virtualrelayaux4_start_address + 56            # Property ID: 29, [W] (float). Pre-set solar power deactivation threshold power.
        self.next1_virtualrelayaux4_presetbatbatidx = self.next1_virtualrelayaux4_start_address + 58                    # Property ID: 30, [-] (enum). Index of the battery from which the values for the pre-set battery must be read.

        # Object VirtualRelayAux3TimeCtrl Modbus Address
        self.next1_virtualrelayaux3timectrl_start_address = 6300
        self.next1_virtualrelayaux3timectrl_timecontrolledmodeselect = self.next1_virtualrelayaux3timectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next1_virtualrelayaux3timectrl_actmindelay = self.next1_virtualrelayaux3timectrl_start_address + 2         # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next1_virtualrelayaux3timectrl_deactmindelay = self.next1_virtualrelayaux3timectrl_start_address + 4       # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next1_virtualrelayaux3timectrl_actmintime = self.next1_virtualrelayaux3timectrl_start_address + 6          # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next1_virtualrelayaux3timectrl_deactmintime = self.next1_virtualrelayaux3timectrl_start_address + 8        # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next1_virtualrelayaux3timectrl_actmaxtime = self.next1_virtualrelayaux3timectrl_start_address + 10         # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next1_virtualrelayaux3timectrl_acthourallow1 = self.next1_virtualrelayaux3timectrl_start_address + 12      # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next1_virtualrelayaux3timectrl_acthourallow2 = self.next1_virtualrelayaux3timectrl_start_address + 14      # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next1_virtualrelayaux3timectrl_actweekdaysallow = self.next1_virtualrelayaux3timectrl_start_address + 16   # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_virtualrelayaux3timectrl_startingdate = self.next1_virtualrelayaux3timectrl_start_address + 18       # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next1_virtualrelayaux3timectrl_startingtimesec = self.next1_virtualrelayaux3timectrl_start_address + 20    # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next1_virtualrelayaux3timectrl_endingtimesec = self.next1_virtualrelayaux3timectrl_start_address + 22      # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next1_virtualrelayaux3timectrl_selectedweekday = self.next1_virtualrelayaux3timectrl_start_address + 24    # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_virtualrelayaux3timectrl_recurrenceweeks = self.next1_virtualrelayaux3timectrl_start_address + 26    # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next1_virtualrelayaux3timectrl_rangeofrecurrenceselect = self.next1_virtualrelayaux3timectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next1_virtualrelayaux3timectrl_endingdate = self.next1_virtualrelayaux3timectrl_start_address + 30         # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next1_virtualrelayaux3timectrl_nbrofoccurrences = self.next1_virtualrelayaux3timectrl_start_address + 32   # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next1_virtualrelayaux3timectrl_resettimecontrolled = self.next1_virtualrelayaux3timectrl_start_address + 34    # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object VirtualRelayAux4TimeCtrl Modbus Address
        self.next1_virtualrelayaux4timectrl_start_address = 6600
        self.next1_virtualrelayaux4timectrl_timecontrolledmodeselect = self.next1_virtualrelayaux4timectrl_start_address + 0    # Property ID: 0, [-] (enum). Time Controlled object working mode.
        self.next1_virtualrelayaux4timectrl_actmindelay = self.next1_virtualrelayaux4timectrl_start_address + 2         # Property ID: 1, [s] (uint). Temporal restriction: Minimum delay before activation. The signal must be high during all this period.
        self.next1_virtualrelayaux4timectrl_deactmindelay = self.next1_virtualrelayaux4timectrl_start_address + 4       # Property ID: 2, [s] (uint). Temporal restriction: Minimum delay before deactivation. The signal must be low during all this period.
        self.next1_virtualrelayaux4timectrl_actmintime = self.next1_virtualrelayaux4timectrl_start_address + 6          # Property ID: 3, [s] (uint). Temporal restriction: Output signal minimum activation time.
        self.next1_virtualrelayaux4timectrl_deactmintime = self.next1_virtualrelayaux4timectrl_start_address + 8        # Property ID: 4, [s] (uint). Temporal restriction: Output signal minimum deactivation time.
        self.next1_virtualrelayaux4timectrl_actmaxtime = self.next1_virtualrelayaux4timectrl_start_address + 10         # Property ID: 5, [s] (int). Temporal restriction: Output signal maximum activation time.
        self.next1_virtualrelayaux4timectrl_acthourallow1 = self.next1_virtualrelayaux4timectrl_start_address + 12      # Property ID: 6, [s] (uint). Temporal restriction: Daily time range hour 1. Given in seconds from midnight.
        self.next1_virtualrelayaux4timectrl_acthourallow2 = self.next1_virtualrelayaux4timectrl_start_address + 14      # Property ID: 7, [s] (uint). Temporal restriction: Daily time range hour 2. Given in seconds from midnight.
        self.next1_virtualrelayaux4timectrl_actweekdaysallow = self.next1_virtualrelayaux4timectrl_start_address + 16   # Property ID: 8, [-] (bitfield). Temporal restriction: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_virtualrelayaux4timectrl_startingdate = self.next1_virtualrelayaux4timectrl_start_address + 18       # Property ID: 9, [days] (uint). Schedule time: Starting date. Given in days since 01.01.1970.
        self.next1_virtualrelayaux4timectrl_startingtimesec = self.next1_virtualrelayaux4timectrl_start_address + 20    # Property ID: 10, [s] (uint). Schedule time: Activation starting hour. Given in seconds from midnight.
        self.next1_virtualrelayaux4timectrl_endingtimesec = self.next1_virtualrelayaux4timectrl_start_address + 22      # Property ID: 11, [s] (uint). Schedule time: Activation ending hour. Given in seconds from midnight.
        self.next1_virtualrelayaux4timectrl_selectedweekday = self.next1_virtualrelayaux4timectrl_start_address + 24    # Property ID: 12, [-] (bitfield). Schedule time: Allowed week days. Given in a binary format such as each bits represents a day: (MSB) M T W T F S S (LSB).
        self.next1_virtualrelayaux4timectrl_recurrenceweeks = self.next1_virtualrelayaux4timectrl_start_address + 26    # Property ID: 13, [-] (uint). Schedule time: Activation weeks recurrences.
        self.next1_virtualrelayaux4timectrl_rangeofrecurrenceselect = self.next1_virtualrelayaux4timectrl_start_address + 28    # Property ID: 14, [-] (enum). Schedule time: Selection of recurrence before deactivation.
        self.next1_virtualrelayaux4timectrl_endingdate = self.next1_virtualrelayaux4timectrl_start_address + 30         # Property ID: 15, [days] (uint). Schedule time: Activations ending date. Given in days since 01.01.1970.
        self.next1_virtualrelayaux4timectrl_nbrofoccurrences = self.next1_virtualrelayaux4timectrl_start_address + 32   # Property ID: 16, [-] (uint). Schedule time: Number of occurrences.
        self.next1_virtualrelayaux4timectrl_resettimecontrolled = self.next1_virtualrelayaux4timectrl_start_address + 34    # Property ID: 17, [-] (signal). Reset all time controlled counters. For exampe the occurences counts.

        # Object CmdEntry3 Modbus Address
        self.next1_cmdentry3_start_address = 6900
        self.next1_cmdentry3_currentstate = self.next1_cmdentry3_start_address + 2                                      # Property ID: 2, [-] (bool). Current command entry state.
        self.next1_cmdentry3_cmdinsysidx = self.next1_cmdentry3_start_address + 3                                       # Property ID: 3, [-] (int). Index in the system of this command entry.
        self.next1_cmdentry3_configuration = self.next1_cmdentry3_start_address + 5                                     # Property ID: 4, [-] (enum). Configuration of this command entry.
        self.next1_cmdentry3_mirroredinternalauxrelayidx = self.next1_cmdentry3_start_address + 7                       # Property ID: 5, [-] (int). Index of the internal aux relay mirorred by this command entry, if configuration is set to \"Active when internal aux relay connected\" (value 32). 0 corresponds to the first internal aux relay, 1 to the second and so on.
        self.next1_cmdentry3_availableconfigurations = self.next1_cmdentry3_start_address + 9                           # Property ID: 6, [-] (bitfield). Available configurations of this command entry.
        self.next1_cmdentry3_analogvalue = self.next1_cmdentry3_start_address + 11                                      # Property ID: 7, [-] (float). Current command entry analog value. 0 when the measured analog voltage is 0V. 1 when the measured analog voltage is \"Max analog voltage\" (id 8). Always 1 if analog mode is not available or \"Cmd entry configuration\" (id 4) is not set to \"Analog mode\" (value 128).
        self.next1_cmdentry3_maxanalogvoltage = self.next1_cmdentry3_start_address + 13                                 # Property ID: 8, [V] (float). Maximum voltage value of the power supply used. \"Current analog value\" (id 7) is 1 when the measured analog voltage is greater than or equal to this value.

        # Object CmdEntry4 Modbus Address
        self.next1_cmdentry4_start_address = 7200
        self.next1_cmdentry4_currentstate = self.next1_cmdentry4_start_address + 2                                      # Property ID: 2, [-] (bool). Current command entry state.
        self.next1_cmdentry4_cmdinsysidx = self.next1_cmdentry4_start_address + 3                                       # Property ID: 3, [-] (int). Index in the system of this command entry.
        self.next1_cmdentry4_configuration = self.next1_cmdentry4_start_address + 5                                     # Property ID: 4, [-] (enum). Configuration of this command entry.
        self.next1_cmdentry4_mirroredinternalauxrelayidx = self.next1_cmdentry4_start_address + 7                       # Property ID: 5, [-] (int). Index of the internal aux relay mirorred by this command entry, if configuration is set to \"Active when internal aux relay connected\" (value 32). 0 corresponds to the first internal aux relay, 1 to the second and so on.
        self.next1_cmdentry4_availableconfigurations = self.next1_cmdentry4_start_address + 9                           # Property ID: 6, [-] (bitfield). Available configurations of this command entry.
        self.next1_cmdentry4_analogvalue = self.next1_cmdentry4_start_address + 11                                      # Property ID: 7, [-] (float). Current command entry analog value. 0 when the measured analog voltage is 0V. 1 when the measured analog voltage is \"Max analog voltage\" (id 8). Always 1 if analog mode is not available or \"Cmd entry configuration\" (id 4) is not set to \"Analog mode\" (value 128).
        self.next1_cmdentry4_maxanalogvoltage = self.next1_cmdentry4_start_address + 13                                 # Property ID: 8, [V] (float). Maximum voltage value of the power supply used. \"Current analog value\" (id 7) is 1 when the measured analog voltage is greater than or equal to this value.

        # Object BatteryContributorExtSolarChargers Modbus Address
        self.next1_batterycontributorextsolarchargers_start_address = 7500
        self.next1_batterycontributorextsolarchargers_chargingcurrent = self.next1_batterycontributorextsolarchargers_start_address + 0    # Property ID: 0, [A] (float). Charging current measured.
        self.next1_batterycontributorextsolarchargers_temperaturesensorstate = self.next1_batterycontributorextsolarchargers_start_address + 2    # Property ID: 1, [-] (enum). Indicates the temperature sensor state.
        self.next1_batterycontributorextsolarchargers_temperature = self.next1_batterycontributorextsolarchargers_start_address + 4    # Property ID: 2, [°C] (float). Temperature measured.
        self.next1_batterycontributorextsolarchargers_voltage = self.next1_batterycontributorextsolarchargers_start_address + 10    # Property ID: 5, [V] (float). Voltage measured.

        # Object SolarCommonExtSolarChargers Modbus Address
        self.next1_solarcommonextsolarchargers_start_address = 7800
        self.next1_solarcommonextsolarchargers_turnon = self.next1_solarcommonextsolarchargers_start_address + 0        # Property ID: 0, [-] (signal). Turns on solar(s).
        self.next1_solarcommonextsolarchargers_turnoff = self.next1_solarcommonextsolarchargers_start_address + 1       # Property ID: 1, [-] (signal). Turns off solar(s).
        self.next1_solarcommonextsolarchargers_onoffstate = self.next1_solarcommonextsolarchargers_start_address + 2    # Property ID: 2, [-] (bool). Indicates solar(s) on/off state.
        self.next1_solarcommonextsolarchargers_enabledepolarization = self.next1_solarcommonextsolarchargers_start_address + 3    # Property ID: 3, [-] (signal). Enables depolarization.
        self.next1_solarcommonextsolarchargers_disabledepolarization = self.next1_solarcommonextsolarchargers_start_address + 4    # Property ID: 4, [-] (signal). Disables depolarization.
        self.next1_solarcommonextsolarchargers_power = self.next1_solarcommonextsolarchargers_start_address + 5         # Property ID: 5, [W] (float). Power produced.
        self.next1_solarcommonextsolarchargers_previousdayenergy = self.next1_solarcommonextsolarchargers_start_address + 7    # Property ID: 8, [Wh] (float). Energy produced for the previous day.
        self.next1_solarcommonextsolarchargers_powerlimit = self.next1_solarcommonextsolarchargers_start_address + 9    # Property ID: 9, [W] (uint). Solar(s) max power limit.
        self.next1_solarcommonextsolarchargers_dayenergy = self.next1_solarcommonextsolarchargers_start_address + 11    # Property ID: 10, [Wh] (float). Energy produced for the current day.
        self.next1_solarcommonextsolarchargers_resetableenergy = self.next1_solarcommonextsolarchargers_start_address + 15    # Property ID: 12, [Wh] (float64). Energy produced (can be reset).
        self.next1_solarcommonextsolarchargers_totalenergy = self.next1_solarcommonextsolarchargers_start_address + 19  # Property ID: 13, [Wh] (float64). Total energy produced (whole life).

        # Object SolarGroupExtSolarChargers Modbus Address
        self.next1_solargroupextsolarchargers_start_address = 8100
        self.next1_solargroupextsolarchargers_nbr = self.next1_solargroupextsolarchargers_start_address + 0             # Property ID: 0, [-] (uint). Number of converters.
        self.next1_solargroupextsolarchargers_status = self.next1_solargroupextsolarchargers_start_address + 2          # Property ID: 1, [-] (bitfield). Current status.
        self.next1_solargroupextsolarchargers_vt40nbr = self.next1_solargroupextsolarchargers_start_address + 4         # Property ID: 2, [-] (uint). Number of vt40.
        self.next1_solargroupextsolarchargers_vt65nbr = self.next1_solargroupextsolarchargers_start_address + 6         # Property ID: 3, [-] (uint). Number of vt65.
        self.next1_solargroupextsolarchargers_vt80nbr = self.next1_solargroupextsolarchargers_start_address + 8         # Property ID: 4, [-] (uint). Number of vt80.
        self.next1_solargroupextsolarchargers_vs70nbr = self.next1_solargroupextsolarchargers_start_address + 10        # Property ID: 5, [-] (uint). Number of vs70.
        self.next1_solargroupextsolarchargers_vs120nbr = self.next1_solargroupextsolarchargers_start_address + 12       # Property ID: 6, [-] (uint). Number of vs120.


        # Group NextGateway Modbus Address
        # Object IdCard Modbus Address
        self.nextgateway_idcard_start_address = 0
        self.nextgateway_idcard_serialnumber = self.nextgateway_idcard_start_address + 4                                # Property ID: 2, [-] (char[15]). Serial Number of this Studer Innotec device. 
        self.nextgateway_idcard_softwarepackageversion = self.nextgateway_idcard_start_address + 14                     # Property ID: 4, [-] (uint). Software package version in this format : MAJOR.MIDDLE.MINOR.PATCH, encoded as follows from MSB to LSB : MAJOR (8 bits), MIDDLE (8bits), MINOR (12 bits), PATCH (4 bits).
        self.nextgateway_idcard_softwarerevisionsha1 = self.nextgateway_idcard_start_address + 18                       # Property ID: 6, [-] (char[7]). SHA-1 of the software project commit
        self.nextgateway_idcard_objectmodelversion = self.nextgateway_idcard_start_address + 30                         # Property ID: 8, [-] (uint). Version of the currently used ObjectModel in this format : MAJOR.MINOR, encoded as follows from MSB to LSB : MAJOR (16 bits), MINOR (16 bits).

        # Object BaseApplication Modbus Address
        self.nextgateway_baseapplication_start_address = 300
        self.nextgateway_baseapplication_warnings = self.nextgateway_baseapplication_start_address + 5                  # Property ID: 5, [-] (bitfield). Current warnings.
        self.nextgateway_baseapplication_restoreallnvmvalues = self.nextgateway_baseapplication_start_address + 15      # Property ID: 10, [-] (signal). Restore the original value (from Non-Volatile Memory) for all properties that were changed with WriteInRAM.

        # Object CanNode Modbus Address
        self.nextgateway_cannode_start_address = 600
        self.nextgateway_cannode_status = self.nextgateway_cannode_start_address + 2                                    # Property ID: 1, [-] (enum). Stores the node status.
        self.nextgateway_cannode_txerrorcounter = self.nextgateway_cannode_start_address + 4                            # Property ID: 2, [-] (int). Counter of the TX errors.
        self.nextgateway_cannode_rxerrorcounter = self.nextgateway_cannode_start_address + 6                            # Property ID: 3, [-] (int). Counter of the RX errors.
        self.nextgateway_cannode_busterminationset = self.nextgateway_cannode_start_address + 8                         # Property ID: 4, [-] (bool). Bus termination status for this node.

        # Object Device Modbus Address
        self.nextgateway_device_start_address = 900
        self.nextgateway_device_blinkingstate = self.nextgateway_device_start_address + 0                               # Property ID: 0, [-] (bool). If set, the device LEDs will blink.
        self.nextgateway_device_deviceid = self.nextgateway_device_start_address + 1                                    # Property ID: 1, [-] (int). System-wide ID of the device in topology.
        self.nextgateway_device_batteryid = self.nextgateway_device_start_address + 3                                   # Property ID: 2, [-] (int). System-wide ID of the battery in topology.
        self.nextgateway_device_totalfunctioningtimesec = self.nextgateway_device_start_address + 5                     # Property ID: 3, [s] (uint). Total functioning time in this device's life.

        # Object GatewayModule Modbus Address
        self.nextgateway_gatewaymodule_start_address = 1200
        self.nextgateway_gatewaymodule_errors = self.nextgateway_gatewaymodule_start_address + 0                        # Property ID: 0, [-] (bitfield). Current errors.
        self.nextgateway_gatewaymodule_warnings = self.nextgateway_gatewaymodule_start_address + 2                      # Property ID: 1, [-] (bitfield). Current warnings.
        self.nextgateway_gatewaymodule_emmctotalsizekib = self.nextgateway_gatewaymodule_start_address + 6              # Property ID: 3, [KiB] (uint). Total size of eMMC main area.
        self.nextgateway_gatewaymodule_usbmountedpartitionsnumber = self.nextgateway_gatewaymodule_start_address + 10   # Property ID: 5, [-] (uint). Number of mounted USB partitions.
        self.nextgateway_gatewaymodule_cputemperature = self.nextgateway_gatewaymodule_start_address + 16               # Property ID: 7, [°C] (float). The current temperature of the CPU chip.
        self.nextgateway_gatewaymodule_internetstatus = self.nextgateway_gatewaymodule_start_address + 20               # Property ID: 10, [-] (enum). The internet connection status.
        self.nextgateway_gatewaymodule_saveconfigfile = self.nextgateway_gatewaymodule_start_address + 22               # Property ID: 11, [-] (signal). Signal used to save the config file on the gateway and the USB drive.
        self.nextgateway_gatewaymodule_firstwizarddone = self.nextgateway_gatewaymodule_start_address + 23              # Property ID: 12, [-] (bool). Flag indicating that the first wizard configuration is done.

        # Object HmiDisplay Modbus Address
        self.nextgateway_hmidisplay_start_address = 1500
        self.nextgateway_hmidisplay_brightness = self.nextgateway_hmidisplay_start_address + 0                          # Property ID: 0, [/20] (int). Display brightness.
        self.nextgateway_hmidisplay_sleepdelaysec = self.nextgateway_hmidisplay_start_address + 2                       # Property ID: 1, [s.] (int). Sleep delay in seconds.
        self.nextgateway_hmidisplay_unlockcode = self.nextgateway_hmidisplay_start_address + 4                          # Property ID: 2, [-] (char[7]). Unlock code to be entered when exiting sleep mode. Used only if \"Use slider for unlocking after sleep\" option is disabled.
        self.nextgateway_hmidisplay_unlockmechanism = self.nextgateway_hmidisplay_start_address + 8                     # Property ID: 3, [-] (enum). Unlock mechanism used when exiting sleep mode.
        self.nextgateway_hmidisplay_totaldisplayontimesec = self.nextgateway_hmidisplay_start_address + 14              # Property ID: 6, [s.] (uint). Total time this display was turned ON.

        # Object Rs485iCommunicationBus Modbus Address
        self.nextgateway_rs485icommunicationbus_start_address = 1800
        self.nextgateway_rs485icommunicationbus_isterminationset = self.nextgateway_rs485icommunicationbus_start_address + 2    # Property ID: 1, [-] (bool). Bus termination status for this communication bus.
        self.nextgateway_rs485icommunicationbus_baudrate = self.nextgateway_rs485icommunicationbus_start_address + 3    # Property ID: 2, [-] (enum). Connection baudrate.
        self.nextgateway_rs485icommunicationbus_parity = self.nextgateway_rs485icommunicationbus_start_address + 5      # Property ID: 3, [-] (enum). Parity type to be used.
        self.nextgateway_rs485icommunicationbus_stopbits = self.nextgateway_rs485icommunicationbus_start_address + 7    # Property ID: 4, [-] (enum). Number of stop bits per transmitted character.
        self.nextgateway_rs485icommunicationbus_databits = self.nextgateway_rs485icommunicationbus_start_address + 9    # Property ID: 5, [-] (enum). Number of data bits per transmitted character.

        # Object CaniCommunicationBus Modbus Address
        self.nextgateway_canicommunicationbus_start_address = 2100
        self.nextgateway_canicommunicationbus_isterminationset = self.nextgateway_canicommunicationbus_start_address + 2    # Property ID: 1, [-] (bool). Bus termination status for this communication bus.
        self.nextgateway_canicommunicationbus_baudrate = self.nextgateway_canicommunicationbus_start_address + 3        # Property ID: 2, [-] (enum). Connection baudrate.
        self.nextgateway_canicommunicationbus_parity = self.nextgateway_canicommunicationbus_start_address + 5          # Property ID: 3, [-] (enum). Parity type to be used.
        self.nextgateway_canicommunicationbus_stopbits = self.nextgateway_canicommunicationbus_start_address + 7        # Property ID: 4, [-] (enum). Number of stop bits per transmitted character.
        self.nextgateway_canicommunicationbus_databits = self.nextgateway_canicommunicationbus_start_address + 9        # Property ID: 5, [-] (enum). Number of data bits per transmitted character.

        # Object MemoryPartitionEmmcRootfs Modbus Address
        self.nextgateway_memorypartitionemmcrootfs_start_address = 2400
        self.nextgateway_memorypartitionemmcrootfs_media = self.nextgateway_memorypartitionemmcrootfs_start_address + 0 # Property ID: 0, [-] (enum). Media on which this partition is located.
        self.nextgateway_memorypartitionemmcrootfs_filesystem = self.nextgateway_memorypartitionemmcrootfs_start_address + 2    # Property ID: 1, [-] (enum). File system of this partition.
        self.nextgateway_memorypartitionemmcrootfs_totalsizekib = self.nextgateway_memorypartitionemmcrootfs_start_address + 4    # Property ID: 2, [KiB] (uint). Total size of this partition.
        self.nextgateway_memorypartitionemmcrootfs_usedsizekib = self.nextgateway_memorypartitionemmcrootfs_start_address + 6    # Property ID: 3, [KiB] (uint). Used size of this partition.

        # Object MemoryPartitionEmmcConfig Modbus Address
        self.nextgateway_memorypartitionemmcconfig_start_address = 2700
        self.nextgateway_memorypartitionemmcconfig_media = self.nextgateway_memorypartitionemmcconfig_start_address + 0 # Property ID: 0, [-] (enum). Media on which this partition is located.
        self.nextgateway_memorypartitionemmcconfig_filesystem = self.nextgateway_memorypartitionemmcconfig_start_address + 2    # Property ID: 1, [-] (enum). File system of this partition.
        self.nextgateway_memorypartitionemmcconfig_totalsizekib = self.nextgateway_memorypartitionemmcconfig_start_address + 4    # Property ID: 2, [KiB] (uint). Total size of this partition.
        self.nextgateway_memorypartitionemmcconfig_usedsizekib = self.nextgateway_memorypartitionemmcconfig_start_address + 6    # Property ID: 3, [KiB] (uint). Used size of this partition.

        # Object MemoryPartitionEmmcData Modbus Address
        self.nextgateway_memorypartitionemmcdata_start_address = 3000
        self.nextgateway_memorypartitionemmcdata_media = self.nextgateway_memorypartitionemmcdata_start_address + 0     # Property ID: 0, [-] (enum). Media on which this partition is located.
        self.nextgateway_memorypartitionemmcdata_filesystem = self.nextgateway_memorypartitionemmcdata_start_address + 2    # Property ID: 1, [-] (enum). File system of this partition.
        self.nextgateway_memorypartitionemmcdata_totalsizekib = self.nextgateway_memorypartitionemmcdata_start_address + 4    # Property ID: 2, [KiB] (uint). Total size of this partition.
        self.nextgateway_memorypartitionemmcdata_usedsizekib = self.nextgateway_memorypartitionemmcdata_start_address + 6    # Property ID: 3, [KiB] (uint). Used size of this partition.

        # Object MemoryPartitionUsb1 Modbus Address
        self.nextgateway_memorypartitionusb1_start_address = 3300
        self.nextgateway_memorypartitionusb1_media = self.nextgateway_memorypartitionusb1_start_address + 0             # Property ID: 0, [-] (enum). Media on which this partition is located.
        self.nextgateway_memorypartitionusb1_filesystem = self.nextgateway_memorypartitionusb1_start_address + 2        # Property ID: 1, [-] (enum). File system of this partition.
        self.nextgateway_memorypartitionusb1_totalsizekib = self.nextgateway_memorypartitionusb1_start_address + 4      # Property ID: 2, [KiB] (uint). Total size of this partition.
        self.nextgateway_memorypartitionusb1_usedsizekib = self.nextgateway_memorypartitionusb1_start_address + 6       # Property ID: 3, [KiB] (uint). Used size of this partition.

        # Object MemoryPartitionUsb2 Modbus Address
        self.nextgateway_memorypartitionusb2_start_address = 3600
        self.nextgateway_memorypartitionusb2_media = self.nextgateway_memorypartitionusb2_start_address + 0             # Property ID: 0, [-] (enum). Media on which this partition is located.
        self.nextgateway_memorypartitionusb2_filesystem = self.nextgateway_memorypartitionusb2_start_address + 2        # Property ID: 1, [-] (enum). File system of this partition.
        self.nextgateway_memorypartitionusb2_totalsizekib = self.nextgateway_memorypartitionusb2_start_address + 4      # Property ID: 2, [KiB] (uint). Total size of this partition.
        self.nextgateway_memorypartitionusb2_usedsizekib = self.nextgateway_memorypartitionusb2_start_address + 6       # Property ID: 3, [KiB] (uint). Used size of this partition.

        # Object MemoryPartitionUsb3 Modbus Address
        self.nextgateway_memorypartitionusb3_start_address = 3900
        self.nextgateway_memorypartitionusb3_media = self.nextgateway_memorypartitionusb3_start_address + 0             # Property ID: 0, [-] (enum). Media on which this partition is located.
        self.nextgateway_memorypartitionusb3_filesystem = self.nextgateway_memorypartitionusb3_start_address + 2        # Property ID: 1, [-] (enum). File system of this partition.
        self.nextgateway_memorypartitionusb3_totalsizekib = self.nextgateway_memorypartitionusb3_start_address + 4      # Property ID: 2, [KiB] (uint). Total size of this partition.
        self.nextgateway_memorypartitionusb3_usedsizekib = self.nextgateway_memorypartitionusb3_start_address + 6       # Property ID: 3, [KiB] (uint). Used size of this partition.

        # Object Modbus Modbus Address
        self.nextgateway_modbus_start_address = 4200
        self.nextgateway_modbus_baseaddress = self.nextgateway_modbus_start_address + 0                                 # Property ID: 0, [-] (uint). Base address for first object group instance.
        self.nextgateway_modbus_modbustcpport = self.nextgateway_modbus_start_address + 2                               # Property ID: 1, [-] (uint). The TCP port number.
        self.nextgateway_modbus_modbustcpserverstatus = self.nextgateway_modbus_start_address + 14                      # Property ID: 3, [-] (enum). The current status of the connection to the Modbus TCP server
        self.nextgateway_modbus_modbusrtuserverstatus = self.nextgateway_modbus_start_address + 16                      # Property ID: 4, [-] (enum). The current status of the connection to the Modbus RTU server
        self.nextgateway_modbus_mode = self.nextgateway_modbus_start_address + 18                                       # Property ID: 5, [-] (enum). The current modbus server selected.
        self.nextgateway_modbus_writepersistent = self.nextgateway_modbus_start_address + 20                            # Property ID: 6, [-] (bool). Force writing persistently using Modbus.
        self.nextgateway_modbus_smartmeteremulatoraddress = self.nextgateway_modbus_start_address + 21                  # Property ID: 7, [-] (int). Address for powermeter emulator. If this address is positive and valid, a request to this address will emulate access to a powermeter on AC input 1.
        self.nextgateway_modbus_emulatorbatterysoc = self.nextgateway_modbus_start_address + 23                         # Property ID: 8, [%] (float). In powermeter emulator, battery state-of-charge above which the battery charging power is displayed as available (injected) power.
        self.nextgateway_modbus_emulatorbatterychargeconsign = self.nextgateway_modbus_start_address + 25               # Property ID: 9, [W] (float). In powermeter emulator, battery charging power consign for system battery when SoC is above \"Emulator battery priority limit SoC\" (id 8).

        # Object ModbusUserLevel Modbus Address
        self.nextgateway_modbususerlevel_start_address = 4500
        self.nextgateway_modbususerlevel_userlevel = self.nextgateway_modbususerlevel_start_address + 0                 # Property ID: 0, [-] (uint). Current user level.
        self.nextgateway_modbususerlevel_userlevelcodeinput = self.nextgateway_modbususerlevel_start_address + 2        # Property ID: 1, [-] (char[7]). Please enter here the user level code for changing the user level.

        # Object TermsAndConditions Modbus Address
        self.nextgateway_termsandconditions_start_address = 4800
        self.nextgateway_termsandconditions_acceptedversion = self.nextgateway_termsandconditions_start_address + 0     # Property ID: 0, [-] (char[12]). Version of the Terms and Conditions that have been accepted by the user.
        self.nextgateway_termsandconditions_acceptationdatetime = self.nextgateway_termsandconditions_start_address + 6 # Property ID: 1, [-] (uint). Date and time of the customers acceptation of the Terms and Conditions.
        self.nextgateway_termsandconditions_acceptationextent = self.nextgateway_termsandconditions_start_address + 8   # Property ID: 2, [-] (bitfield). Extent of the customer acceptation to the Terms and Conditions.
        self.nextgateway_termsandconditions_acceptationorigin = self.nextgateway_termsandconditions_start_address + 10  # Property ID: 3, [-] (uint64). Origin of acceptation.

        # Object NetworkInterfaceEthernet Modbus Address
        self.nextgateway_networkinterfaceethernet_start_address = 5100
        self.nextgateway_networkinterfaceethernet_interfacestatus = self.nextgateway_networkinterfaceethernet_start_address + 2    # Property ID: 1, [-] (enum). Current status of the interface.
        self.nextgateway_networkinterfaceethernet_interfacename = self.nextgateway_networkinterfaceethernet_start_address + 4    # Property ID: 2, [-] (char[20]). The internal name of this interface.
        self.nextgateway_networkinterfaceethernet_hardwareaddress = self.nextgateway_networkinterfaceethernet_start_address + 14    # Property ID: 3, [-] (char[20]). The hardware (MAC) address of this interface.
        self.nextgateway_networkinterfaceethernet_ipaddressv4 = self.nextgateway_networkinterfaceethernet_start_address + 24    # Property ID: 4, [-] (char[20]). The current IP (v4) address of this interface.
        self.nextgateway_networkinterfaceethernet_netmaskv4 = self.nextgateway_networkinterfaceethernet_start_address + 34    # Property ID: 5, [-] (char[20]). The net mask of this interface.
        self.nextgateway_networkinterfaceethernet_broadcastv4 = self.nextgateway_networkinterfaceethernet_start_address + 44    # Property ID: 6, [-] (char[20]). The broadcast address of this interface.
        self.nextgateway_networkinterfaceethernet_interfacemode = self.nextgateway_networkinterfaceethernet_start_address + 54    # Property ID: 7, [-] (enum). The current interface mode selected (WLAN only).
        self.nextgateway_networkinterfaceethernet_forcedisable = self.nextgateway_networkinterfaceethernet_start_address + 56    # Property ID: 8, [-] (bool). Force the interface to be disabled.
        self.nextgateway_networkinterfaceethernet_wishedipaddressv4 = self.nextgateway_networkinterfaceethernet_start_address + 57    # Property ID: 9, [-] (char[20]). The wished IP (v4) address of this interface.
        self.nextgateway_networkinterfaceethernet_wishednetmaskv4 = self.nextgateway_networkinterfaceethernet_start_address + 67    # Property ID: 10, [-] (char[20]). The wished net mask of this interface.
        self.nextgateway_networkinterfaceethernet_wishedgatewayv4 = self.nextgateway_networkinterfaceethernet_start_address + 77    # Property ID: 11, [-] (char[20]). The wished network gateway IP (v4) address of this interface.
        self.nextgateway_networkinterfaceethernet_dnsipaddressv4 = self.nextgateway_networkinterfaceethernet_start_address + 87    # Property ID: 12, [-] (char[20]). The DNS server IP (v4) address of this interface.
        self.nextgateway_networkinterfaceethernet_enablestaticip = self.nextgateway_networkinterfaceethernet_start_address + 97    # Property ID: 13, [-] (bool). Enable the static IP wished by the user.

        # Object NetworkInterfaceWifi Modbus Address
        self.nextgateway_networkinterfacewifi_start_address = 5400
        self.nextgateway_networkinterfacewifi_interfacestatus = self.nextgateway_networkinterfacewifi_start_address + 2 # Property ID: 1, [-] (enum). Current status of the interface.
        self.nextgateway_networkinterfacewifi_interfacename = self.nextgateway_networkinterfacewifi_start_address + 4   # Property ID: 2, [-] (char[20]). The internal name of this interface.
        self.nextgateway_networkinterfacewifi_hardwareaddress = self.nextgateway_networkinterfacewifi_start_address + 14    # Property ID: 3, [-] (char[20]). The hardware (MAC) address of this interface.
        self.nextgateway_networkinterfacewifi_ipaddressv4 = self.nextgateway_networkinterfacewifi_start_address + 24    # Property ID: 4, [-] (char[20]). The current IP (v4) address of this interface.
        self.nextgateway_networkinterfacewifi_netmaskv4 = self.nextgateway_networkinterfacewifi_start_address + 34      # Property ID: 5, [-] (char[20]). The net mask of this interface.
        self.nextgateway_networkinterfacewifi_broadcastv4 = self.nextgateway_networkinterfacewifi_start_address + 44    # Property ID: 6, [-] (char[20]). The broadcast address of this interface.
        self.nextgateway_networkinterfacewifi_interfacemode = self.nextgateway_networkinterfacewifi_start_address + 54  # Property ID: 7, [-] (enum). The current interface mode selected (WLAN only).
        self.nextgateway_networkinterfacewifi_forcedisable = self.nextgateway_networkinterfacewifi_start_address + 56   # Property ID: 8, [-] (bool). Force the interface to be disabled.
        self.nextgateway_networkinterfacewifi_wishedipaddressv4 = self.nextgateway_networkinterfacewifi_start_address + 57    # Property ID: 9, [-] (char[20]). The wished IP (v4) address of this interface.
        self.nextgateway_networkinterfacewifi_wishednetmaskv4 = self.nextgateway_networkinterfacewifi_start_address + 67    # Property ID: 10, [-] (char[20]). The wished net mask of this interface.
        self.nextgateway_networkinterfacewifi_wishedgatewayv4 = self.nextgateway_networkinterfacewifi_start_address + 77    # Property ID: 11, [-] (char[20]). The wished network gateway IP (v4) address of this interface.
        self.nextgateway_networkinterfacewifi_dnsipaddressv4 = self.nextgateway_networkinterfacewifi_start_address + 87 # Property ID: 12, [-] (char[20]). The DNS server IP (v4) address of this interface.
        self.nextgateway_networkinterfacewifi_enablestaticip = self.nextgateway_networkinterfacewifi_start_address + 97 # Property ID: 13, [-] (bool). Enable the static IP wished by the user.

        # Object NetworkInterfaceExternal Modbus Address
        self.nextgateway_networkinterfaceexternal_start_address = 5700
        self.nextgateway_networkinterfaceexternal_interfacestatus = self.nextgateway_networkinterfaceexternal_start_address + 2    # Property ID: 1, [-] (enum). Current status of the interface.
        self.nextgateway_networkinterfaceexternal_interfacename = self.nextgateway_networkinterfaceexternal_start_address + 4    # Property ID: 2, [-] (char[20]). The internal name of this interface.
        self.nextgateway_networkinterfaceexternal_hardwareaddress = self.nextgateway_networkinterfaceexternal_start_address + 14    # Property ID: 3, [-] (char[20]). The hardware (MAC) address of this interface.
        self.nextgateway_networkinterfaceexternal_ipaddressv4 = self.nextgateway_networkinterfaceexternal_start_address + 24    # Property ID: 4, [-] (char[20]). The current IP (v4) address of this interface.
        self.nextgateway_networkinterfaceexternal_netmaskv4 = self.nextgateway_networkinterfaceexternal_start_address + 34    # Property ID: 5, [-] (char[20]). The net mask of this interface.
        self.nextgateway_networkinterfaceexternal_broadcastv4 = self.nextgateway_networkinterfaceexternal_start_address + 44    # Property ID: 6, [-] (char[20]). The broadcast address of this interface.
        self.nextgateway_networkinterfaceexternal_interfacemode = self.nextgateway_networkinterfaceexternal_start_address + 54    # Property ID: 7, [-] (enum). The current interface mode selected (WLAN only).
        self.nextgateway_networkinterfaceexternal_forcedisable = self.nextgateway_networkinterfaceexternal_start_address + 56    # Property ID: 8, [-] (bool). Force the interface to be disabled.
        self.nextgateway_networkinterfaceexternal_wishedipaddressv4 = self.nextgateway_networkinterfaceexternal_start_address + 57    # Property ID: 9, [-] (char[20]). The wished IP (v4) address of this interface.
        self.nextgateway_networkinterfaceexternal_wishednetmaskv4 = self.nextgateway_networkinterfaceexternal_start_address + 67    # Property ID: 10, [-] (char[20]). The wished net mask of this interface.
        self.nextgateway_networkinterfaceexternal_wishedgatewayv4 = self.nextgateway_networkinterfaceexternal_start_address + 77    # Property ID: 11, [-] (char[20]). The wished network gateway IP (v4) address of this interface.
        self.nextgateway_networkinterfaceexternal_dnsipaddressv4 = self.nextgateway_networkinterfaceexternal_start_address + 87    # Property ID: 12, [-] (char[20]). The DNS server IP (v4) address of this interface.
        self.nextgateway_networkinterfaceexternal_enablestaticip = self.nextgateway_networkinterfaceexternal_start_address + 97    # Property ID: 13, [-] (bool). Enable the static IP wished by the user.

        # Object GatewayUserLevel Modbus Address
        self.nextgateway_gatewayuserlevel_start_address = 6000
        self.nextgateway_gatewayuserlevel_userlevel = self.nextgateway_gatewayuserlevel_start_address + 0               # Property ID: 0, [-] (uint). Current user level.
        self.nextgateway_gatewayuserlevel_userlevelcodeinput = self.nextgateway_gatewayuserlevel_start_address + 2      # Property ID: 1, [-] (char[7]). Please enter here the user level code for changing the user level.

        # Object Webportal Modbus Address
        self.nextgateway_webportal_start_address = 6300
        self.nextgateway_webportal_webportalconnectionstatus = self.nextgateway_webportal_start_address + 0             # Property ID: 0, [-] (enum). The current status of the connection to the Webportal.
        self.nextgateway_webportal_webportaldatalogsynchrostatus = self.nextgateway_webportal_start_address + 2         # Property ID: 1, [-] (enum). The current Webportal datalog synchronization status.
        self.nextgateway_webportal_certificateeffectivedate = self.nextgateway_webportal_start_address + 4              # Property ID: 2, [s] (uint). Absolute timestamp for certificate's effective date as number of seconds since Epoch (01.01.1970).
        self.nextgateway_webportal_certificateexpirydate = self.nextgateway_webportal_start_address + 6                 # Property ID: 3, [s] (uint). Absolute timestamp for certificate's expiry date as number of seconds since Epoch (01.01.1970).
        self.nextgateway_webportal_uploaddebugdata = self.nextgateway_webportal_start_address + 8                       # Property ID: 4, [-] (signal). Upload all debug data to Studer Innotec servers.
        self.nextgateway_webportal_readonly = self.nextgateway_webportal_start_address + 9                              # Property ID: 5, [-] (bool). Used to set the properties access to read-only for Webportal control.
        self.nextgateway_webportal_certificateauthoritykeyidentifier = self.nextgateway_webportal_start_address + 10    # Property ID: 6, [-] (char[100]). The authority key identifier field of the SSL certificate extension. 
        self.nextgateway_webportal_certificateauthoritycommonname = self.nextgateway_webportal_start_address + 60       # Property ID: 7, [-] (char[100]). The certificate authority common name. 
        self.nextgateway_webportal_maxnumberofdaystosynchronize = self.nextgateway_webportal_start_address + 110        # Property ID: 8, [days] (uint). Max. number of days to synchronize the datalog.

        # Object UsbInterface1 Modbus Address
        self.nextgateway_usbinterface1_start_address = 6600
        self.nextgateway_usbinterface1_usbportdevicetype = self.nextgateway_usbinterface1_start_address + 2             # Property ID: 1, [-] (enum). Type of device connected to this USB port.

        # Object UsbInterface2 Modbus Address
        self.nextgateway_usbinterface2_start_address = 6900
        self.nextgateway_usbinterface2_usbportdevicetype = self.nextgateway_usbinterface2_start_address + 2             # Property ID: 1, [-] (enum). Type of device connected to this USB port.

        # Object UsbInterface3 Modbus Address
        self.nextgateway_usbinterface3_start_address = 7200
        self.nextgateway_usbinterface3_usbportdevicetype = self.nextgateway_usbinterface3_start_address + 2             # Property ID: 1, [-] (enum). Type of device connected to this USB port.

        # Object UsbInterface4 Modbus Address
        self.nextgateway_usbinterface4_start_address = 7500
        self.nextgateway_usbinterface4_usbportdevicetype = self.nextgateway_usbinterface4_start_address + 2             # Property ID: 1, [-] (enum). Type of device connected to this USB port.

        # Object HmiSettings Modbus Address
        self.nextgateway_hmisettings_start_address = 7800
        self.nextgateway_hmisettings_language = self.nextgateway_hmisettings_start_address + 0                          # Property ID: 0, [-] (enum). Language used for the user interface.
        self.nextgateway_hmisettings_defaultview = self.nextgateway_hmisettings_start_address + 2                       # Property ID: 1, [-] (enum). Default view that will be displayed at startup.

        # Object SystemView Modbus Address
        self.nextgateway_systemview_start_address = 8100
        self.nextgateway_systemview_installationstatus = self.nextgateway_systemview_start_address + 0                  # Property ID: 0, [-] (enum). Installation status.
        self.nextgateway_systemview_nodestatus = self.nextgateway_systemview_start_address + 2                          # Property ID: 1, [-] (uint). Status of the nodes provided by the installation monitor.
        self.nextgateway_systemview_controllertimeoutenabled = self.nextgateway_systemview_start_address + 4            # Property ID: 2, [-] (bool). When an external controller is used (WriteInRAM operations), this setting activates a timeout mechanism that will automatically reset all externally modified settings to their original (NVM) values.
        self.nextgateway_systemview_controllertimeoutdurationsec = self.nextgateway_systemview_start_address + 5        # Property ID: 3, [s] (uint). When \"Enable timeout for ext. control\" (id 2) is active, this setting defines the timeout period in seconds. After this time has elapsed since the last WriteInRAM operation, all modified settings will automatically reset to their original (NVM) values.
        self.nextgateway_systemview_controllerallpropertiesreset = self.nextgateway_systemview_start_address + 7        # Property ID: 4, [-] (signal). Resets all settings modified through WriteInRAM to their original values from non-volatile memory (NVM). This restores settings that have been changed by an external controller.

        # Object Webcommand Modbus Address
        self.nextgateway_webcommand_start_address = 8400
        self.nextgateway_webcommand_username = self.nextgateway_webcommand_start_address + 0                            # Property ID: 0, [-] (char[25]). Default username for web interface.
        self.nextgateway_webcommand_password = self.nextgateway_webcommand_start_address + 13                           # Property ID: 1, [-] (char[15]). Default password for web interface.
        self.nextgateway_webcommand_webcommandstatus = self.nextgateway_webcommand_start_address + 21                   # Property ID: 2, [-] (enum). Web interface server status.
        self.nextgateway_webcommand_connections = self.nextgateway_webcommand_start_address + 23                        # Property ID: 3, [-] (uint). Number of established connections.
        self.nextgateway_webcommand_accesspointname = self.nextgateway_webcommand_start_address + 25                    # Property ID: 4, [-] (char[25]). The access point name.
        self.nextgateway_webcommand_accesspointpassword = self.nextgateway_webcommand_start_address + 38                # Property ID: 5, [-] (char[25]). The access point password.

        # Object NetworkInterfaceAccessPoint Modbus Address
        self.nextgateway_networkinterfaceaccesspoint_start_address = 8700
        self.nextgateway_networkinterfaceaccesspoint_interfacestatus = self.nextgateway_networkinterfaceaccesspoint_start_address + 2    # Property ID: 1, [-] (enum). Current status of the interface.
        self.nextgateway_networkinterfaceaccesspoint_interfacename = self.nextgateway_networkinterfaceaccesspoint_start_address + 4    # Property ID: 2, [-] (char[20]). The internal name of this interface.
        self.nextgateway_networkinterfaceaccesspoint_hardwareaddress = self.nextgateway_networkinterfaceaccesspoint_start_address + 14    # Property ID: 3, [-] (char[20]). The hardware (MAC) address of this interface.
        self.nextgateway_networkinterfaceaccesspoint_ipaddressv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 24    # Property ID: 4, [-] (char[20]). The current IP (v4) address of this interface.
        self.nextgateway_networkinterfaceaccesspoint_netmaskv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 34    # Property ID: 5, [-] (char[20]). The net mask of this interface.
        self.nextgateway_networkinterfaceaccesspoint_broadcastv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 44    # Property ID: 6, [-] (char[20]). The broadcast address of this interface.
        self.nextgateway_networkinterfaceaccesspoint_interfacemode = self.nextgateway_networkinterfaceaccesspoint_start_address + 54    # Property ID: 7, [-] (enum). The current interface mode selected (WLAN only).
        self.nextgateway_networkinterfaceaccesspoint_forcedisable = self.nextgateway_networkinterfaceaccesspoint_start_address + 56    # Property ID: 8, [-] (bool). Force the interface to be disabled.
        self.nextgateway_networkinterfaceaccesspoint_wishedipaddressv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 57    # Property ID: 9, [-] (char[20]). The wished IP (v4) address of this interface.
        self.nextgateway_networkinterfaceaccesspoint_wishednetmaskv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 67    # Property ID: 10, [-] (char[20]). The wished net mask of this interface.
        self.nextgateway_networkinterfaceaccesspoint_wishedgatewayv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 77    # Property ID: 11, [-] (char[20]). The wished network gateway IP (v4) address of this interface.
        self.nextgateway_networkinterfaceaccesspoint_dnsipaddressv4 = self.nextgateway_networkinterfaceaccesspoint_start_address + 87    # Property ID: 12, [-] (char[20]). The DNS server IP (v4) address of this interface.
        self.nextgateway_networkinterfaceaccesspoint_enablestaticip = self.nextgateway_networkinterfaceaccesspoint_start_address + 97    # Property ID: 13, [-] (bool). Enable the static IP wished by the user.


        # Group Powermeters Modbus Address
        # Object Powermeter Modbus Address
        self.powermeters_powermeter_start_address = 0
        self.powermeters_powermeter_brandmodel = self.powermeters_powermeter_start_address + 0                          # Property ID: 0, [-] (enum). The brand and model of the powermeter.
        self.powermeters_powermeter_baseaddress = self.powermeters_powermeter_start_address + 2                         # Property ID: 1, [-] (uint). Modbus device address used by the powermeter.
        self.powermeters_powermeter_function = self.powermeters_powermeter_start_address + 4                            # Property ID: 2, [-] (enum). The function of the powermeter.
        self.powermeters_powermeter_warnings = self.powermeters_powermeter_start_address + 6                            # Property ID: 3, [-] (bitfield). Current warning(s).
        self.powermeters_powermeter_errors = self.powermeters_powermeter_start_address + 8                              # Property ID: 4, [-] (bitfield). Current error(s).
        self.powermeters_powermeter_deviceid = self.powermeters_powermeter_start_address + 10                           # Property ID: 5, [-] (int). The ID of the device connected to this powermeter.

        # Object PowermeterMeasure Modbus Address
        self.powermeters_powermetermeasure_start_address = 300
        self.powermeters_powermetermeasure_activepowerl1 = self.powermeters_powermetermeasure_start_address + 0         # Property ID: 0, [W] (float). Active power L1 measured.
        self.powermeters_powermetermeasure_activepowerl2 = self.powermeters_powermetermeasure_start_address + 2         # Property ID: 2, [W] (float). Active power L2 measured.
        self.powermeters_powermetermeasure_activepowerl3 = self.powermeters_powermetermeasure_start_address + 4         # Property ID: 4, [W] (float). Active power L3 measured.
        self.powermeters_powermetermeasure_reactivepowerl1 = self.powermeters_powermetermeasure_start_address + 6       # Property ID: 6, [VAR] (float). Reactive power L1 measured.
        self.powermeters_powermetermeasure_reactivepowerl2 = self.powermeters_powermetermeasure_start_address + 8       # Property ID: 8, [VAR] (float). Reactive power L2 measured.
        self.powermeters_powermetermeasure_reactivepowerl3 = self.powermeters_powermetermeasure_start_address + 10      # Property ID: 10, [VAR] (float). Reactive power L3 measured.
        self.powermeters_powermetermeasure_dayconsumedenergyl1 = self.powermeters_powermetermeasure_start_address + 12  # Property ID: 12, [Wh] (float). Consumed energy of the current day on L1.
        self.powermeters_powermetermeasure_dayconsumedenergyl2 = self.powermeters_powermetermeasure_start_address + 14  # Property ID: 13, [Wh] (float). Consumed energy of the current day on L2.
        self.powermeters_powermetermeasure_dayconsumedenergyl3 = self.powermeters_powermetermeasure_start_address + 16  # Property ID: 14, [Wh] (float). Consumed energy of the current day on L3.
        self.powermeters_powermetermeasure_dayproducedenergyl1 = self.powermeters_powermetermeasure_start_address + 18  # Property ID: 15, [Wh] (float). Produced energy of the current day on L1.
        self.powermeters_powermetermeasure_dayproducedenergyl2 = self.powermeters_powermetermeasure_start_address + 20  # Property ID: 16, [Wh] (float). Produced energy of the current day on L2.
        self.powermeters_powermetermeasure_dayproducedenergyl3 = self.powermeters_powermetermeasure_start_address + 22  # Property ID: 17, [Wh] (float). Produced energy of the current day on L3.


