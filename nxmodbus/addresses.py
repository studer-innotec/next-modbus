#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Addresses:
    """
    This class stores all accessible addresses from the Next devices
    """
    def __init__(self, offset):
        self.version_major = 10
        self.version_minor = 61

        self.deviceAddressDefault = offset + 1
        self.device_address_system = offset + 1;
        self.device_address_battery = offset + 2;
        self.device_address_acsource = offset + 7;
        self.device_address_acflexload = offset + 9;
        self.device_address_next3 = offset + 14;
        self.device_address_next1 = offset + 29;
        self.device_address_nextgateway = offset + 59;
        self.device_address_last_valid_address = offset + self.device_address_nextgateway + 1;

        # Group System Modbus Address
        # Object EarthingScheme Modbus Address
        self.system_earthingscheme_start_address = 1200;
        self.system_earthingscheme_earthingmodeselection = self.system_earthingscheme_start_address + 0;
        self.system_earthingscheme_disablecheck = self.system_earthingscheme_start_address + 2;
        self.system_earthingscheme_isearthingmaster = self.system_earthingscheme_start_address + 3;
        self.system_earthingscheme_relayisclosed = self.system_earthingscheme_start_address + 4;
        self.system_earthingscheme_earthingerrors = self.system_earthingscheme_start_address + 5;
        self.system_earthingscheme_earthingwarnings = self.system_earthingscheme_start_address + 18;

        # Object EnergyPolicy Modbus Address
        self.system_energypolicy_start_address = 1800;
        self.system_energypolicy_acsourcepriority = self.system_energypolicy_start_address + 0;
        self.system_energypolicy_currentlyactiveacsourceindex = self.system_energypolicy_start_address + 2;

        # Object Installation Modbus Address
        self.system_installation_start_address = 2100;
        self.system_installation_guid = self.system_installation_start_address + 3;
        self.system_installation_datetimeinternetupdate = self.system_installation_start_address + 21;
        self.system_installation_country = self.system_installation_start_address + 22;
        self.system_installation_timezone = self.system_installation_start_address + 24;

        # Object AllDevices Modbus Address
        self.system_alldevices_start_address = 2400;
        self.system_alldevices_buzzersenabled = self.system_alldevices_start_address + 3;
        self.system_alldevices_frontpanelbuttonsenabled = self.system_alldevices_start_address + 4;
        self.system_alldevices_nbrofcmdentries = self.system_alldevices_start_address + 5;
        self.system_alldevices_nbrofrelevantdevices = self.system_alldevices_start_address + 7;
        self.system_alldevices_nbrofnext3 = self.system_alldevices_start_address + 9;
        self.system_alldevices_next3status = self.system_alldevices_start_address + 11;
        self.system_alldevices_nbrofnext1 = self.system_alldevices_start_address + 13;
        self.system_alldevices_next1status = self.system_alldevices_start_address + 15;

        # Object TriPhaseInverter Modbus Address
        self.system_triphaseinverter_start_address = 2700;
        self.system_triphaseinverter_turnonallphases = self.system_triphaseinverter_start_address + 3;
        self.system_triphaseinverter_turnoffallphases = self.system_triphaseinverter_start_address + 4;
        self.system_triphaseinverter_onoffstateallphases = self.system_triphaseinverter_start_address + 5;
        self.system_triphaseinverter_turnonl1 = self.system_triphaseinverter_start_address + 6;
        self.system_triphaseinverter_turnoffl1 = self.system_triphaseinverter_start_address + 7;
        self.system_triphaseinverter_onoffstatel1 = self.system_triphaseinverter_start_address + 8;
        self.system_triphaseinverter_turnonl2 = self.system_triphaseinverter_start_address + 9;
        self.system_triphaseinverter_turnoffl2 = self.system_triphaseinverter_start_address + 10;
        self.system_triphaseinverter_onoffstatel2 = self.system_triphaseinverter_start_address + 11;
        self.system_triphaseinverter_turnonl3 = self.system_triphaseinverter_start_address + 12;
        self.system_triphaseinverter_turnoffl3 = self.system_triphaseinverter_start_address + 13;
        self.system_triphaseinverter_onoffstatel3 = self.system_triphaseinverter_start_address + 14;
        self.system_triphaseinverter_threephasesystem = self.system_triphaseinverter_start_address + 17;
        self.system_triphaseinverter_linevoltage = self.system_triphaseinverter_start_address + 19;
        self.system_triphaseinverter_phasevoltagel1 = self.system_triphaseinverter_start_address + 21;
        self.system_triphaseinverter_phasevoltagel2 = self.system_triphaseinverter_start_address + 23;
        self.system_triphaseinverter_phasevoltagel3 = self.system_triphaseinverter_start_address + 25;
        self.system_triphaseinverter_relativeanglel2 = self.system_triphaseinverter_start_address + 27;
        self.system_triphaseinverter_relativeanglel3 = self.system_triphaseinverter_start_address + 29;
        self.system_triphaseinverter_nominalfrequency = self.system_triphaseinverter_start_address + 31;
        self.system_triphaseinverter_rocofmax = self.system_triphaseinverter_start_address + 33;
        self.system_triphaseinverter_alternatefrequency = self.system_triphaseinverter_start_address + 84;
        self.system_triphaseinverter_cmdentryidxforalternatefrequency = self.system_triphaseinverter_start_address + 86;
        self.system_triphaseinverter_allowpowersinkingfromacloadports = self.system_triphaseinverter_start_address + 88;
        self.system_triphaseinverter_standbysensitivity = self.system_triphaseinverter_start_address + 93;
        self.system_triphaseinverter_standbydetectionratio = self.system_triphaseinverter_start_address + 95;
        self.system_triphaseinverter_allowindividualphaseoperation = self.system_triphaseinverter_start_address + 97;
        self.system_triphaseinverter_overloadthresholdstage1 = self.system_triphaseinverter_start_address + 98;
        self.system_triphaseinverter_overloadoperatetimestage1 = self.system_triphaseinverter_start_address + 100;
        self.system_triphaseinverter_overloadthresholdstage2 = self.system_triphaseinverter_start_address + 102;
        self.system_triphaseinverter_overloadoperatetimestage2 = self.system_triphaseinverter_start_address + 104;
        self.system_triphaseinverter_overloadrestartdelay = self.system_triphaseinverter_start_address + 106;
        self.system_triphaseinverter_maxolnbduringobsperiod = self.system_triphaseinverter_start_address + 108;
        self.system_triphaseinverter_overloadobservationperiod = self.system_triphaseinverter_start_address + 110;
        self.system_triphaseinverter_errorrestartdelay = self.system_triphaseinverter_start_address + 112;
        self.system_triphaseinverter_maxerrorsnbduringobsperiod = self.system_triphaseinverter_start_address + 114;
        self.system_triphaseinverter_errorobservationperiod = self.system_triphaseinverter_start_address + 116;
        self.system_triphaseinverter_insmstrength = self.system_triphaseinverter_start_address + 132;
        self.system_triphaseinverter_status = self.system_triphaseinverter_start_address + 134;
        self.system_triphaseinverter_phaseexistance = self.system_triphaseinverter_start_address + 136;

        # Object InverterL1 Modbus Address
        self.system_inverterl1_start_address = 3000;
        self.system_inverterl1_status = self.system_inverterl1_start_address + 0;
        self.system_inverterl1_warnings = self.system_inverterl1_start_address + 2;
        self.system_inverterl1_causeoferror = self.system_inverterl1_start_address + 4;

        # Object InverterL2 Modbus Address
        self.system_inverterl2_start_address = 3300;
        self.system_inverterl2_status = self.system_inverterl2_start_address + 0;
        self.system_inverterl2_warnings = self.system_inverterl2_start_address + 2;
        self.system_inverterl2_causeoferror = self.system_inverterl2_start_address + 4;

        # Object InverterL3 Modbus Address
        self.system_inverterl3_start_address = 3600;
        self.system_inverterl3_status = self.system_inverterl3_start_address + 0;
        self.system_inverterl3_warnings = self.system_inverterl3_start_address + 2;
        self.system_inverterl3_causeoferror = self.system_inverterl3_start_address + 4;

        # Object AcLoadTriPhaseMeasure Modbus Address
        self.system_acloadtriphasemeasure_start_address = 3900;
        self.system_acloadtriphasemeasure_frequency = self.system_acloadtriphasemeasure_start_address + 0;
        self.system_acloadtriphasemeasure_linevoltagel1l2 = self.system_acloadtriphasemeasure_start_address + 2;
        self.system_acloadtriphasemeasure_linevoltagel2l3 = self.system_acloadtriphasemeasure_start_address + 4;
        self.system_acloadtriphasemeasure_linevoltagel3l1 = self.system_acloadtriphasemeasure_start_address + 6;
        self.system_acloadtriphasemeasure_totalactivepower = self.system_acloadtriphasemeasure_start_address + 8;
        self.system_acloadtriphasemeasure_totalapparentpower = self.system_acloadtriphasemeasure_start_address + 10;
        self.system_acloadtriphasemeasure_anglel2relativetol1 = self.system_acloadtriphasemeasure_start_address + 12;
        self.system_acloadtriphasemeasure_anglel3relativetol1 = self.system_acloadtriphasemeasure_start_address + 14;
        self.system_acloadtriphasemeasure_dayconsumedenergy = self.system_acloadtriphasemeasure_start_address + 16;
        self.system_acloadtriphasemeasure_previousdayconsumedenergy = self.system_acloadtriphasemeasure_start_address + 18;
        self.system_acloadtriphasemeasure_resetableconsumedenergy = self.system_acloadtriphasemeasure_start_address + 20;
        self.system_acloadtriphasemeasure_totalconsumedenergy = self.system_acloadtriphasemeasure_start_address + 24;
        self.system_acloadtriphasemeasure_dayproducedenergy = self.system_acloadtriphasemeasure_start_address + 28;
        self.system_acloadtriphasemeasure_previousdayproducedenergy = self.system_acloadtriphasemeasure_start_address + 30;
        self.system_acloadtriphasemeasure_resetableproducedenergy = self.system_acloadtriphasemeasure_start_address + 32;
        self.system_acloadtriphasemeasure_totalproducedenergy = self.system_acloadtriphasemeasure_start_address + 36;
        self.system_acloadtriphasemeasure_dayruntime = self.system_acloadtriphasemeasure_start_address + 40;
        self.system_acloadtriphasemeasure_totalruntime = self.system_acloadtriphasemeasure_start_address + 42;
        self.system_acloadtriphasemeasure_daypeakpower = self.system_acloadtriphasemeasure_start_address + 44;
        self.system_acloadtriphasemeasure_previousdaypeakpower = self.system_acloadtriphasemeasure_start_address + 46;
        self.system_acloadtriphasemeasure_dayminactivepower = self.system_acloadtriphasemeasure_start_address + 48;
        self.system_acloadtriphasemeasure_previousdayminactivepower = self.system_acloadtriphasemeasure_start_address + 50;
        self.system_acloadtriphasemeasure_daymaxactivepower = self.system_acloadtriphasemeasure_start_address + 52;
        self.system_acloadtriphasemeasure_previousdaymaxactivepower = self.system_acloadtriphasemeasure_start_address + 54;

        # Object AcLoadL1Measure Modbus Address
        self.system_acloadl1measure_start_address = 4200;
        self.system_acloadl1measure_phasevoltage = self.system_acloadl1measure_start_address + 0;
        self.system_acloadl1measure_current = self.system_acloadl1measure_start_address + 2;
        self.system_acloadl1measure_activepower = self.system_acloadl1measure_start_address + 4;
        self.system_acloadl1measure_reactivepower = self.system_acloadl1measure_start_address + 6;
        self.system_acloadl1measure_apparentpower = self.system_acloadl1measure_start_address + 8;
        self.system_acloadl1measure_cosphi = self.system_acloadl1measure_start_address + 10;
        self.system_acloadl1measure_daypeakpower = self.system_acloadl1measure_start_address + 12;
        self.system_acloadl1measure_previousdaypeakpower = self.system_acloadl1measure_start_address + 14;
        self.system_acloadl1measure_dayminactivepower = self.system_acloadl1measure_start_address + 16;
        self.system_acloadl1measure_previousdayminactivepower = self.system_acloadl1measure_start_address + 18;
        self.system_acloadl1measure_daymaxactivepower = self.system_acloadl1measure_start_address + 20;
        self.system_acloadl1measure_previousdaymaxactivepower = self.system_acloadl1measure_start_address + 22;
        self.system_acloadl1measure_dayconsumedenergy = self.system_acloadl1measure_start_address + 28;
        self.system_acloadl1measure_previousdayconsumedenergy = self.system_acloadl1measure_start_address + 30;
        self.system_acloadl1measure_resetableconsumedenergy = self.system_acloadl1measure_start_address + 32;
        self.system_acloadl1measure_totalconsumedenergy = self.system_acloadl1measure_start_address + 36;
        self.system_acloadl1measure_dayproducedenergy = self.system_acloadl1measure_start_address + 40;
        self.system_acloadl1measure_previousdayproducedenergy = self.system_acloadl1measure_start_address + 42;
        self.system_acloadl1measure_resetableproducedenergy = self.system_acloadl1measure_start_address + 44;
        self.system_acloadl1measure_totalproducedenergy = self.system_acloadl1measure_start_address + 48;

        # Object AcLoadL2Measure Modbus Address
        self.system_acloadl2measure_start_address = 4500;
        self.system_acloadl2measure_phasevoltage = self.system_acloadl2measure_start_address + 0;
        self.system_acloadl2measure_current = self.system_acloadl2measure_start_address + 2;
        self.system_acloadl2measure_activepower = self.system_acloadl2measure_start_address + 4;
        self.system_acloadl2measure_reactivepower = self.system_acloadl2measure_start_address + 6;
        self.system_acloadl2measure_apparentpower = self.system_acloadl2measure_start_address + 8;
        self.system_acloadl2measure_cosphi = self.system_acloadl2measure_start_address + 10;
        self.system_acloadl2measure_daypeakpower = self.system_acloadl2measure_start_address + 12;
        self.system_acloadl2measure_previousdaypeakpower = self.system_acloadl2measure_start_address + 14;
        self.system_acloadl2measure_dayminactivepower = self.system_acloadl2measure_start_address + 16;
        self.system_acloadl2measure_previousdayminactivepower = self.system_acloadl2measure_start_address + 18;
        self.system_acloadl2measure_daymaxactivepower = self.system_acloadl2measure_start_address + 20;
        self.system_acloadl2measure_previousdaymaxactivepower = self.system_acloadl2measure_start_address + 22;
        self.system_acloadl2measure_dayconsumedenergy = self.system_acloadl2measure_start_address + 28;
        self.system_acloadl2measure_previousdayconsumedenergy = self.system_acloadl2measure_start_address + 30;
        self.system_acloadl2measure_resetableconsumedenergy = self.system_acloadl2measure_start_address + 32;
        self.system_acloadl2measure_totalconsumedenergy = self.system_acloadl2measure_start_address + 36;
        self.system_acloadl2measure_dayproducedenergy = self.system_acloadl2measure_start_address + 40;
        self.system_acloadl2measure_previousdayproducedenergy = self.system_acloadl2measure_start_address + 42;
        self.system_acloadl2measure_resetableproducedenergy = self.system_acloadl2measure_start_address + 44;
        self.system_acloadl2measure_totalproducedenergy = self.system_acloadl2measure_start_address + 48;

        # Object AcLoadL3Measure Modbus Address
        self.system_acloadl3measure_start_address = 4800;
        self.system_acloadl3measure_phasevoltage = self.system_acloadl3measure_start_address + 0;
        self.system_acloadl3measure_current = self.system_acloadl3measure_start_address + 2;
        self.system_acloadl3measure_activepower = self.system_acloadl3measure_start_address + 4;
        self.system_acloadl3measure_reactivepower = self.system_acloadl3measure_start_address + 6;
        self.system_acloadl3measure_apparentpower = self.system_acloadl3measure_start_address + 8;
        self.system_acloadl3measure_cosphi = self.system_acloadl3measure_start_address + 10;
        self.system_acloadl3measure_daypeakpower = self.system_acloadl3measure_start_address + 12;
        self.system_acloadl3measure_previousdaypeakpower = self.system_acloadl3measure_start_address + 14;
        self.system_acloadl3measure_dayminactivepower = self.system_acloadl3measure_start_address + 16;
        self.system_acloadl3measure_previousdayminactivepower = self.system_acloadl3measure_start_address + 18;
        self.system_acloadl3measure_daymaxactivepower = self.system_acloadl3measure_start_address + 20;
        self.system_acloadl3measure_previousdaymaxactivepower = self.system_acloadl3measure_start_address + 22;
        self.system_acloadl3measure_dayconsumedenergy = self.system_acloadl3measure_start_address + 28;
        self.system_acloadl3measure_previousdayconsumedenergy = self.system_acloadl3measure_start_address + 30;
        self.system_acloadl3measure_resetableconsumedenergy = self.system_acloadl3measure_start_address + 32;
        self.system_acloadl3measure_totalconsumedenergy = self.system_acloadl3measure_start_address + 36;
        self.system_acloadl3measure_dayproducedenergy = self.system_acloadl3measure_start_address + 40;
        self.system_acloadl3measure_previousdayproducedenergy = self.system_acloadl3measure_start_address + 42;
        self.system_acloadl3measure_resetableproducedenergy = self.system_acloadl3measure_start_address + 44;
        self.system_acloadl3measure_totalproducedenergy = self.system_acloadl3measure_start_address + 48;

        # Object AcInvertersTriPhaseMeasure Modbus Address
        self.system_acinverterstriphasemeasure_start_address = 5100;
        self.system_acinverterstriphasemeasure_frequency = self.system_acinverterstriphasemeasure_start_address + 0;
        self.system_acinverterstriphasemeasure_linevoltagel1l2 = self.system_acinverterstriphasemeasure_start_address + 2;
        self.system_acinverterstriphasemeasure_linevoltagel2l3 = self.system_acinverterstriphasemeasure_start_address + 4;
        self.system_acinverterstriphasemeasure_linevoltagel3l1 = self.system_acinverterstriphasemeasure_start_address + 6;
        self.system_acinverterstriphasemeasure_totalactivepower = self.system_acinverterstriphasemeasure_start_address + 8;
        self.system_acinverterstriphasemeasure_totalapparentpower = self.system_acinverterstriphasemeasure_start_address + 10;
        self.system_acinverterstriphasemeasure_anglel2relativetol1 = self.system_acinverterstriphasemeasure_start_address + 12;
        self.system_acinverterstriphasemeasure_anglel3relativetol1 = self.system_acinverterstriphasemeasure_start_address + 14;
        self.system_acinverterstriphasemeasure_dayconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 16;
        self.system_acinverterstriphasemeasure_previousdayconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 18;
        self.system_acinverterstriphasemeasure_resetableconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 20;
        self.system_acinverterstriphasemeasure_totalconsumedenergy = self.system_acinverterstriphasemeasure_start_address + 24;
        self.system_acinverterstriphasemeasure_dayproducedenergy = self.system_acinverterstriphasemeasure_start_address + 28;
        self.system_acinverterstriphasemeasure_previousdayproducedenergy = self.system_acinverterstriphasemeasure_start_address + 30;
        self.system_acinverterstriphasemeasure_resetableproducedenergy = self.system_acinverterstriphasemeasure_start_address + 32;
        self.system_acinverterstriphasemeasure_totalproducedenergy = self.system_acinverterstriphasemeasure_start_address + 36;
        self.system_acinverterstriphasemeasure_dayruntime = self.system_acinverterstriphasemeasure_start_address + 40;
        self.system_acinverterstriphasemeasure_totalruntime = self.system_acinverterstriphasemeasure_start_address + 42;
        self.system_acinverterstriphasemeasure_daypeakpower = self.system_acinverterstriphasemeasure_start_address + 44;
        self.system_acinverterstriphasemeasure_previousdaypeakpower = self.system_acinverterstriphasemeasure_start_address + 46;
        self.system_acinverterstriphasemeasure_dayminactivepower = self.system_acinverterstriphasemeasure_start_address + 48;
        self.system_acinverterstriphasemeasure_previousdayminactivepower = self.system_acinverterstriphasemeasure_start_address + 50;
        self.system_acinverterstriphasemeasure_daymaxactivepower = self.system_acinverterstriphasemeasure_start_address + 52;
        self.system_acinverterstriphasemeasure_previousdaymaxactivepower = self.system_acinverterstriphasemeasure_start_address + 54;

        # Object AcInvertersL1Measure Modbus Address
        self.system_acinvertersl1measure_start_address = 5400;
        self.system_acinvertersl1measure_phasevoltage = self.system_acinvertersl1measure_start_address + 0;
        self.system_acinvertersl1measure_current = self.system_acinvertersl1measure_start_address + 2;
        self.system_acinvertersl1measure_activepower = self.system_acinvertersl1measure_start_address + 4;
        self.system_acinvertersl1measure_reactivepower = self.system_acinvertersl1measure_start_address + 6;
        self.system_acinvertersl1measure_apparentpower = self.system_acinvertersl1measure_start_address + 8;
        self.system_acinvertersl1measure_cosphi = self.system_acinvertersl1measure_start_address + 10;
        self.system_acinvertersl1measure_daypeakpower = self.system_acinvertersl1measure_start_address + 12;
        self.system_acinvertersl1measure_previousdaypeakpower = self.system_acinvertersl1measure_start_address + 14;
        self.system_acinvertersl1measure_dayminactivepower = self.system_acinvertersl1measure_start_address + 16;
        self.system_acinvertersl1measure_previousdayminactivepower = self.system_acinvertersl1measure_start_address + 18;
        self.system_acinvertersl1measure_daymaxactivepower = self.system_acinvertersl1measure_start_address + 20;
        self.system_acinvertersl1measure_previousdaymaxactivepower = self.system_acinvertersl1measure_start_address + 22;
        self.system_acinvertersl1measure_dayconsumedenergy = self.system_acinvertersl1measure_start_address + 28;
        self.system_acinvertersl1measure_previousdayconsumedenergy = self.system_acinvertersl1measure_start_address + 30;
        self.system_acinvertersl1measure_resetableconsumedenergy = self.system_acinvertersl1measure_start_address + 32;
        self.system_acinvertersl1measure_totalconsumedenergy = self.system_acinvertersl1measure_start_address + 36;
        self.system_acinvertersl1measure_dayproducedenergy = self.system_acinvertersl1measure_start_address + 40;
        self.system_acinvertersl1measure_previousdayproducedenergy = self.system_acinvertersl1measure_start_address + 42;
        self.system_acinvertersl1measure_resetableproducedenergy = self.system_acinvertersl1measure_start_address + 44;
        self.system_acinvertersl1measure_totalproducedenergy = self.system_acinvertersl1measure_start_address + 48;

        # Object AcInvertersL2Measure Modbus Address
        self.system_acinvertersl2measure_start_address = 5700;
        self.system_acinvertersl2measure_phasevoltage = self.system_acinvertersl2measure_start_address + 0;
        self.system_acinvertersl2measure_current = self.system_acinvertersl2measure_start_address + 2;
        self.system_acinvertersl2measure_activepower = self.system_acinvertersl2measure_start_address + 4;
        self.system_acinvertersl2measure_reactivepower = self.system_acinvertersl2measure_start_address + 6;
        self.system_acinvertersl2measure_apparentpower = self.system_acinvertersl2measure_start_address + 8;
        self.system_acinvertersl2measure_cosphi = self.system_acinvertersl2measure_start_address + 10;
        self.system_acinvertersl2measure_daypeakpower = self.system_acinvertersl2measure_start_address + 12;
        self.system_acinvertersl2measure_previousdaypeakpower = self.system_acinvertersl2measure_start_address + 14;
        self.system_acinvertersl2measure_dayminactivepower = self.system_acinvertersl2measure_start_address + 16;
        self.system_acinvertersl2measure_previousdayminactivepower = self.system_acinvertersl2measure_start_address + 18;
        self.system_acinvertersl2measure_daymaxactivepower = self.system_acinvertersl2measure_start_address + 20;
        self.system_acinvertersl2measure_previousdaymaxactivepower = self.system_acinvertersl2measure_start_address + 22;
        self.system_acinvertersl2measure_dayconsumedenergy = self.system_acinvertersl2measure_start_address + 28;
        self.system_acinvertersl2measure_previousdayconsumedenergy = self.system_acinvertersl2measure_start_address + 30;
        self.system_acinvertersl2measure_resetableconsumedenergy = self.system_acinvertersl2measure_start_address + 32;
        self.system_acinvertersl2measure_totalconsumedenergy = self.system_acinvertersl2measure_start_address + 36;
        self.system_acinvertersl2measure_dayproducedenergy = self.system_acinvertersl2measure_start_address + 40;
        self.system_acinvertersl2measure_previousdayproducedenergy = self.system_acinvertersl2measure_start_address + 42;
        self.system_acinvertersl2measure_resetableproducedenergy = self.system_acinvertersl2measure_start_address + 44;
        self.system_acinvertersl2measure_totalproducedenergy = self.system_acinvertersl2measure_start_address + 48;

        # Object AcInvertersL3Measure Modbus Address
        self.system_acinvertersl3measure_start_address = 6000;
        self.system_acinvertersl3measure_phasevoltage = self.system_acinvertersl3measure_start_address + 0;
        self.system_acinvertersl3measure_current = self.system_acinvertersl3measure_start_address + 2;
        self.system_acinvertersl3measure_activepower = self.system_acinvertersl3measure_start_address + 4;
        self.system_acinvertersl3measure_reactivepower = self.system_acinvertersl3measure_start_address + 6;
        self.system_acinvertersl3measure_apparentpower = self.system_acinvertersl3measure_start_address + 8;
        self.system_acinvertersl3measure_cosphi = self.system_acinvertersl3measure_start_address + 10;
        self.system_acinvertersl3measure_daypeakpower = self.system_acinvertersl3measure_start_address + 12;
        self.system_acinvertersl3measure_previousdaypeakpower = self.system_acinvertersl3measure_start_address + 14;
        self.system_acinvertersl3measure_dayminactivepower = self.system_acinvertersl3measure_start_address + 16;
        self.system_acinvertersl3measure_previousdayminactivepower = self.system_acinvertersl3measure_start_address + 18;
        self.system_acinvertersl3measure_daymaxactivepower = self.system_acinvertersl3measure_start_address + 20;
        self.system_acinvertersl3measure_previousdaymaxactivepower = self.system_acinvertersl3measure_start_address + 22;
        self.system_acinvertersl3measure_dayconsumedenergy = self.system_acinvertersl3measure_start_address + 28;
        self.system_acinvertersl3measure_previousdayconsumedenergy = self.system_acinvertersl3measure_start_address + 30;
        self.system_acinvertersl3measure_resetableconsumedenergy = self.system_acinvertersl3measure_start_address + 32;
        self.system_acinvertersl3measure_totalconsumedenergy = self.system_acinvertersl3measure_start_address + 36;
        self.system_acinvertersl3measure_dayproducedenergy = self.system_acinvertersl3measure_start_address + 40;
        self.system_acinvertersl3measure_previousdayproducedenergy = self.system_acinvertersl3measure_start_address + 42;
        self.system_acinvertersl3measure_resetableproducedenergy = self.system_acinvertersl3measure_start_address + 44;
        self.system_acinvertersl3measure_totalproducedenergy = self.system_acinvertersl3measure_start_address + 48;

        # Object AllFlexLoadsTriPhaseAcMeasure Modbus Address
        self.system_allflexloadstriphaseacmeasure_start_address = 6300;
        self.system_allflexloadstriphaseacmeasure_frequency = self.system_allflexloadstriphaseacmeasure_start_address + 0;
        self.system_allflexloadstriphaseacmeasure_linevoltagel1l2 = self.system_allflexloadstriphaseacmeasure_start_address + 2;
        self.system_allflexloadstriphaseacmeasure_linevoltagel2l3 = self.system_allflexloadstriphaseacmeasure_start_address + 4;
        self.system_allflexloadstriphaseacmeasure_linevoltagel3l1 = self.system_allflexloadstriphaseacmeasure_start_address + 6;
        self.system_allflexloadstriphaseacmeasure_totalactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 8;
        self.system_allflexloadstriphaseacmeasure_totalapparentpower = self.system_allflexloadstriphaseacmeasure_start_address + 10;
        self.system_allflexloadstriphaseacmeasure_anglel2relativetol1 = self.system_allflexloadstriphaseacmeasure_start_address + 12;
        self.system_allflexloadstriphaseacmeasure_anglel3relativetol1 = self.system_allflexloadstriphaseacmeasure_start_address + 14;
        self.system_allflexloadstriphaseacmeasure_dayconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 16;
        self.system_allflexloadstriphaseacmeasure_previousdayconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 18;
        self.system_allflexloadstriphaseacmeasure_resetableconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 20;
        self.system_allflexloadstriphaseacmeasure_totalconsumedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 24;
        self.system_allflexloadstriphaseacmeasure_dayproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 28;
        self.system_allflexloadstriphaseacmeasure_previousdayproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 30;
        self.system_allflexloadstriphaseacmeasure_resetableproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 32;
        self.system_allflexloadstriphaseacmeasure_totalproducedenergy = self.system_allflexloadstriphaseacmeasure_start_address + 36;
        self.system_allflexloadstriphaseacmeasure_dayruntime = self.system_allflexloadstriphaseacmeasure_start_address + 40;
        self.system_allflexloadstriphaseacmeasure_totalruntime = self.system_allflexloadstriphaseacmeasure_start_address + 42;
        self.system_allflexloadstriphaseacmeasure_daypeakpower = self.system_allflexloadstriphaseacmeasure_start_address + 44;
        self.system_allflexloadstriphaseacmeasure_previousdaypeakpower = self.system_allflexloadstriphaseacmeasure_start_address + 46;
        self.system_allflexloadstriphaseacmeasure_dayminactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 48;
        self.system_allflexloadstriphaseacmeasure_previousdayminactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 50;
        self.system_allflexloadstriphaseacmeasure_daymaxactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 52;
        self.system_allflexloadstriphaseacmeasure_previousdaymaxactivepower = self.system_allflexloadstriphaseacmeasure_start_address + 54;

        # Object AllFlexLoadsL1AcMeasure Modbus Address
        self.system_allflexloadsl1acmeasure_start_address = 6600;
        self.system_allflexloadsl1acmeasure_phasevoltage = self.system_allflexloadsl1acmeasure_start_address + 0;
        self.system_allflexloadsl1acmeasure_current = self.system_allflexloadsl1acmeasure_start_address + 2;
        self.system_allflexloadsl1acmeasure_activepower = self.system_allflexloadsl1acmeasure_start_address + 4;
        self.system_allflexloadsl1acmeasure_reactivepower = self.system_allflexloadsl1acmeasure_start_address + 6;
        self.system_allflexloadsl1acmeasure_apparentpower = self.system_allflexloadsl1acmeasure_start_address + 8;
        self.system_allflexloadsl1acmeasure_cosphi = self.system_allflexloadsl1acmeasure_start_address + 10;
        self.system_allflexloadsl1acmeasure_daypeakpower = self.system_allflexloadsl1acmeasure_start_address + 12;
        self.system_allflexloadsl1acmeasure_previousdaypeakpower = self.system_allflexloadsl1acmeasure_start_address + 14;
        self.system_allflexloadsl1acmeasure_dayminactivepower = self.system_allflexloadsl1acmeasure_start_address + 16;
        self.system_allflexloadsl1acmeasure_previousdayminactivepower = self.system_allflexloadsl1acmeasure_start_address + 18;
        self.system_allflexloadsl1acmeasure_daymaxactivepower = self.system_allflexloadsl1acmeasure_start_address + 20;
        self.system_allflexloadsl1acmeasure_previousdaymaxactivepower = self.system_allflexloadsl1acmeasure_start_address + 22;
        self.system_allflexloadsl1acmeasure_dayconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 28;
        self.system_allflexloadsl1acmeasure_previousdayconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 30;
        self.system_allflexloadsl1acmeasure_resetableconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 32;
        self.system_allflexloadsl1acmeasure_totalconsumedenergy = self.system_allflexloadsl1acmeasure_start_address + 36;
        self.system_allflexloadsl1acmeasure_dayproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 40;
        self.system_allflexloadsl1acmeasure_previousdayproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 42;
        self.system_allflexloadsl1acmeasure_resetableproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 44;
        self.system_allflexloadsl1acmeasure_totalproducedenergy = self.system_allflexloadsl1acmeasure_start_address + 48;

        # Object AllFlexLoadsL2AcMeasure Modbus Address
        self.system_allflexloadsl2acmeasure_start_address = 6900;
        self.system_allflexloadsl2acmeasure_phasevoltage = self.system_allflexloadsl2acmeasure_start_address + 0;
        self.system_allflexloadsl2acmeasure_current = self.system_allflexloadsl2acmeasure_start_address + 2;
        self.system_allflexloadsl2acmeasure_activepower = self.system_allflexloadsl2acmeasure_start_address + 4;
        self.system_allflexloadsl2acmeasure_reactivepower = self.system_allflexloadsl2acmeasure_start_address + 6;
        self.system_allflexloadsl2acmeasure_apparentpower = self.system_allflexloadsl2acmeasure_start_address + 8;
        self.system_allflexloadsl2acmeasure_cosphi = self.system_allflexloadsl2acmeasure_start_address + 10;
        self.system_allflexloadsl2acmeasure_daypeakpower = self.system_allflexloadsl2acmeasure_start_address + 12;
        self.system_allflexloadsl2acmeasure_previousdaypeakpower = self.system_allflexloadsl2acmeasure_start_address + 14;
        self.system_allflexloadsl2acmeasure_dayminactivepower = self.system_allflexloadsl2acmeasure_start_address + 16;
        self.system_allflexloadsl2acmeasure_previousdayminactivepower = self.system_allflexloadsl2acmeasure_start_address + 18;
        self.system_allflexloadsl2acmeasure_daymaxactivepower = self.system_allflexloadsl2acmeasure_start_address + 20;
        self.system_allflexloadsl2acmeasure_previousdaymaxactivepower = self.system_allflexloadsl2acmeasure_start_address + 22;
        self.system_allflexloadsl2acmeasure_dayconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 28;
        self.system_allflexloadsl2acmeasure_previousdayconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 30;
        self.system_allflexloadsl2acmeasure_resetableconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 32;
        self.system_allflexloadsl2acmeasure_totalconsumedenergy = self.system_allflexloadsl2acmeasure_start_address + 36;
        self.system_allflexloadsl2acmeasure_dayproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 40;
        self.system_allflexloadsl2acmeasure_previousdayproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 42;
        self.system_allflexloadsl2acmeasure_resetableproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 44;
        self.system_allflexloadsl2acmeasure_totalproducedenergy = self.system_allflexloadsl2acmeasure_start_address + 48;

        # Object AllFlexLoadsL3AcMeasure Modbus Address
        self.system_allflexloadsl3acmeasure_start_address = 7200;
        self.system_allflexloadsl3acmeasure_phasevoltage = self.system_allflexloadsl3acmeasure_start_address + 0;
        self.system_allflexloadsl3acmeasure_current = self.system_allflexloadsl3acmeasure_start_address + 2;
        self.system_allflexloadsl3acmeasure_activepower = self.system_allflexloadsl3acmeasure_start_address + 4;
        self.system_allflexloadsl3acmeasure_reactivepower = self.system_allflexloadsl3acmeasure_start_address + 6;
        self.system_allflexloadsl3acmeasure_apparentpower = self.system_allflexloadsl3acmeasure_start_address + 8;
        self.system_allflexloadsl3acmeasure_cosphi = self.system_allflexloadsl3acmeasure_start_address + 10;
        self.system_allflexloadsl3acmeasure_daypeakpower = self.system_allflexloadsl3acmeasure_start_address + 12;
        self.system_allflexloadsl3acmeasure_previousdaypeakpower = self.system_allflexloadsl3acmeasure_start_address + 14;
        self.system_allflexloadsl3acmeasure_dayminactivepower = self.system_allflexloadsl3acmeasure_start_address + 16;
        self.system_allflexloadsl3acmeasure_previousdayminactivepower = self.system_allflexloadsl3acmeasure_start_address + 18;
        self.system_allflexloadsl3acmeasure_daymaxactivepower = self.system_allflexloadsl3acmeasure_start_address + 20;
        self.system_allflexloadsl3acmeasure_previousdaymaxactivepower = self.system_allflexloadsl3acmeasure_start_address + 22;
        self.system_allflexloadsl3acmeasure_dayconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 28;
        self.system_allflexloadsl3acmeasure_previousdayconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 30;
        self.system_allflexloadsl3acmeasure_resetableconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 32;
        self.system_allflexloadsl3acmeasure_totalconsumedenergy = self.system_allflexloadsl3acmeasure_start_address + 36;
        self.system_allflexloadsl3acmeasure_dayproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 40;
        self.system_allflexloadsl3acmeasure_previousdayproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 42;
        self.system_allflexloadsl3acmeasure_resetableproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 44;
        self.system_allflexloadsl3acmeasure_totalproducedenergy = self.system_allflexloadsl3acmeasure_start_address + 48;

        # Object SolarCommonAll Modbus Address
        self.system_solarcommonall_start_address = 7500;
        self.system_solarcommonall_turnon = self.system_solarcommonall_start_address + 0;
        self.system_solarcommonall_turnoff = self.system_solarcommonall_start_address + 1;
        self.system_solarcommonall_onoffstate = self.system_solarcommonall_start_address + 2;
        self.system_solarcommonall_enabledepolarization = self.system_solarcommonall_start_address + 3;
        self.system_solarcommonall_disabledepolarization = self.system_solarcommonall_start_address + 4;
        self.system_solarcommonall_power = self.system_solarcommonall_start_address + 5;
        self.system_solarcommonall_previousdayenergy = self.system_solarcommonall_start_address + 7;
        self.system_solarcommonall_powerlimit = self.system_solarcommonall_start_address + 9;
        self.system_solarcommonall_dayenergy = self.system_solarcommonall_start_address + 11;
        self.system_solarcommonall_resetableenergy = self.system_solarcommonall_start_address + 15;
        self.system_solarcommonall_totalenergy = self.system_solarcommonall_start_address + 19;

        # Object SolarGroupAll Modbus Address
        self.system_solargroupall_start_address = 7800;
        self.system_solargroupall_nbr = self.system_solargroupall_start_address + 0;
        self.system_solargroupall_status = self.system_solargroupall_start_address + 2;

        # Object SystemTotal Modbus Address
        self.system_systemtotal_start_address = 8100;
        self.system_systemtotal_clearerrors = self.system_systemtotal_start_address + 0;
        self.system_systemtotal_turnon = self.system_systemtotal_start_address + 1;
        self.system_systemtotal_turnoff = self.system_systemtotal_start_address + 2;
        self.system_systemtotal_onoffstate = self.system_systemtotal_start_address + 3;
        self.system_systemtotal_acsourcepower = self.system_systemtotal_start_address + 4;
        self.system_systemtotal_consummerspower = self.system_systemtotal_start_address + 6;
        self.system_systemtotal_consummerapparentpower = self.system_systemtotal_start_address + 8;
        self.system_systemtotal_warnings = self.system_systemtotal_start_address + 10;
        self.system_systemtotal_errorsrestarting = self.system_systemtotal_start_address + 12;
        self.system_systemtotal_acsourcedayconsumedenergy = self.system_systemtotal_start_address + 14;
        self.system_systemtotal_acsourcedayproducedenergy = self.system_systemtotal_start_address + 16;
        self.system_systemtotal_errorshalted = self.system_systemtotal_start_address + 18;
        self.system_systemtotal_errorsrestartingorhalted = self.system_systemtotal_start_address + 20;
        self.system_systemtotal_cmdentryidxforemergencystop = self.system_systemtotal_start_address + 22;
        self.system_systemtotal_acsourcenbr = self.system_systemtotal_start_address + 24;
        self.system_systemtotal_consummersdayconsumedenergy = self.system_systemtotal_start_address + 26;
        self.system_systemtotal_acflexloadnbr = self.system_systemtotal_start_address + 28;
        self.system_systemtotal_status = self.system_systemtotal_start_address + 30;

        # Object BatteryCommonAll Modbus Address
        self.system_batterycommonall_start_address = 8400;
        self.system_batterycommonall_chargingpower = self.system_batterycommonall_start_address + 0;
        self.system_batterycommonall_daychargingenergy = self.system_batterycommonall_start_address + 2;
        self.system_batterycommonall_previousdaychargingenergy = self.system_batterycommonall_start_address + 4;
        self.system_batterycommonall_resetablechargingenergy = self.system_batterycommonall_start_address + 6;
        self.system_batterycommonall_totalchargingenergy = self.system_batterycommonall_start_address + 10;
        self.system_batterycommonall_daydischargingenergy = self.system_batterycommonall_start_address + 14;
        self.system_batterycommonall_previousdaydischargingenergy = self.system_batterycommonall_start_address + 16;
        self.system_batterycommonall_resetabledischargingenergy = self.system_batterycommonall_start_address + 18;
        self.system_batterycommonall_totaldischargingenergy = self.system_batterycommonall_start_address + 22;
        self.system_batterycommonall_socinpercent = self.system_batterycommonall_start_address + 26;

        # Object BatteryGroupAll Modbus Address
        self.system_batterygroupall_start_address = 8700;
        self.system_batterygroupall_nbr = self.system_batterygroupall_start_address + 0;
        self.system_batterygroupall_status = self.system_batterygroupall_start_address + 2;


        # Group Battery Modbus Address
        # Object BatteryCommon Modbus Address
        self.battery_batterycommon_start_address = 0;
        self.battery_batterycommon_chargingpower = self.battery_batterycommon_start_address + 0;
        self.battery_batterycommon_daychargingenergy = self.battery_batterycommon_start_address + 2;
        self.battery_batterycommon_previousdaychargingenergy = self.battery_batterycommon_start_address + 4;
        self.battery_batterycommon_resetablechargingenergy = self.battery_batterycommon_start_address + 6;
        self.battery_batterycommon_totalchargingenergy = self.battery_batterycommon_start_address + 10;
        self.battery_batterycommon_daydischargingenergy = self.battery_batterycommon_start_address + 14;
        self.battery_batterycommon_previousdaydischargingenergy = self.battery_batterycommon_start_address + 16;
        self.battery_batterycommon_resetabledischargingenergy = self.battery_batterycommon_start_address + 18;
        self.battery_batterycommon_totaldischargingenergy = self.battery_batterycommon_start_address + 22;
        self.battery_batterycommon_socinpercent = self.battery_batterycommon_start_address + 26;

        # Object Battery Modbus Address
        self.battery_battery_start_address = 300;
        self.battery_battery_status = self.battery_battery_start_address + 0;
        self.battery_battery_errors = self.battery_battery_start_address + 2;
        self.battery_battery_warnings = self.battery_battery_start_address + 4;
        self.battery_battery_targetchargingcurrentlowlimit = self.battery_battery_start_address + 6;
        self.battery_battery_targetchargingcurrenthighlimit = self.battery_battery_start_address + 8;
        self.battery_battery_chargingcurrentlowlimit = self.battery_battery_start_address + 10;
        self.battery_battery_chargingcurrenthighlimit = self.battery_battery_start_address + 12;
        self.battery_battery_targetvoltagemax = self.battery_battery_start_address + 14;
        self.battery_battery_targetvoltagemin = self.battery_battery_start_address + 16;
        self.battery_battery_voltage = self.battery_battery_start_address + 18;
        self.battery_battery_chargingcurrent = self.battery_battery_start_address + 20;
        self.battery_battery_nbrcycles = self.battery_battery_start_address + 22;
        self.battery_battery_sohinpercent = self.battery_battery_start_address + 26;
        self.battery_battery_temperatureavailable = self.battery_battery_start_address + 28;
        self.battery_battery_temperature = self.battery_battery_start_address + 29;
        self.battery_battery_userdefinedlimitwithcommunicatingbatteryenabled = self.battery_battery_start_address + 31;
        self.battery_battery_maxdischargingcurrentlimit = self.battery_battery_start_address + 32;
        self.battery_battery_maxchargingcurrentlimit = self.battery_battery_start_address + 34;
        self.battery_battery_currentlimitsmargingfactor = self.battery_battery_start_address + 36;
        self.battery_battery_managementofenergy = self.battery_battery_start_address + 38;
        self.battery_battery_socslopeforlimits = self.battery_battery_start_address + 40;
        self.battery_battery_socforendofchargeinpercent = self.battery_battery_start_address + 42;
        self.battery_battery_socforgridfeedinginpercent = self.battery_battery_start_address + 44;
        self.battery_battery_socforbackupinpercent = self.battery_battery_start_address + 46;
        self.battery_battery_adaptivesocforbackup = self.battery_battery_start_address + 48;
        self.battery_battery_adaptivesocforbackupslopeinpercentperday = self.battery_battery_start_address + 49;
        self.battery_battery_timebeforeresetingadaptivesocforbackup = self.battery_battery_start_address + 51;
        self.battery_battery_socinpercenttoresetadaptivesocforbackup = self.battery_battery_start_address + 53;
        self.battery_battery_socinpercenttoincreaseadaptivesocforbackup = self.battery_battery_start_address + 55;
        self.battery_battery_adaptivesocforbackupinpercent = self.battery_battery_start_address + 57;
        self.battery_battery_voltageforgridfeeding = self.battery_battery_start_address + 59;
        self.battery_battery_voltageforbackup = self.battery_battery_start_address + 61;
        self.battery_battery_nominaltemperature = self.battery_battery_start_address + 63;
        self.battery_battery_temperaturecoefficient = self.battery_battery_start_address + 65;
        self.battery_battery_forcedmode = self.battery_battery_start_address + 67;
        self.battery_battery_forcedtargetvoltagemax = self.battery_battery_start_address + 68;
        self.battery_battery_forcedtargetvoltagemin = self.battery_battery_start_address + 70;
        self.battery_battery_forcedtargetchargingcurrent = self.battery_battery_start_address + 72;
        self.battery_battery_limitslevel = self.battery_battery_start_address + 74;
        self.battery_battery_setpointslevel = self.battery_battery_start_address + 76;
        self.battery_battery_cominterface = self.battery_battery_start_address + 83;
        self.battery_battery_nominalvoltage = self.battery_battery_start_address + 85;
        self.battery_battery_nominalcapacity = self.battery_battery_start_address + 89;
        self.battery_battery_canprotocol = self.battery_battery_start_address + 91;
        self.battery_battery_rs485protocol = self.battery_battery_start_address + 93;
        self.battery_battery_manufacturername = self.battery_battery_start_address + 95;
        self.battery_battery_baudrate = self.battery_battery_start_address + 97;
        self.battery_battery_technology = self.battery_battery_start_address + 100;
        self.battery_battery_adaptivesocforbackupundervoltageincrement = self.battery_battery_start_address + 111;
        self.battery_battery_allowperiodicalfullcharge = self.battery_battery_start_address + 113;
        self.battery_battery_waitingtimebetweenperiodicalfullcharge = self.battery_battery_start_address + 114;
        self.battery_battery_timefullychargedbeforeresetingperiodicalfullcharge = self.battery_battery_start_address + 116;
        self.battery_battery_socforendofdischargeinpercent = self.battery_battery_start_address + 118;
        self.battery_battery_cmdentryidxtoprohibitcharging = self.battery_battery_start_address + 120;
        self.battery_battery_ignorebmsrecommendedcurrents = self.battery_battery_start_address + 122;
        self.battery_battery_bmsmaxchargingcurrent = self.battery_battery_start_address + 123;
        self.battery_battery_bmsmaxdischargingcurrent = self.battery_battery_start_address + 125;
        self.battery_battery_bmsrecommendedchargingcurrent = self.battery_battery_start_address + 127;
        self.battery_battery_bmsrecommendeddischargingcurrent = self.battery_battery_start_address + 129;
        self.battery_battery_communicationlosstimeout = self.battery_battery_start_address + 131;
        self.battery_battery_chargingrecoverymode = self.battery_battery_start_address + 133;
        self.battery_battery_stopchargingrecoverymode = self.battery_battery_start_address + 135;

        # Object BatteryCycle Modbus Address
        self.battery_batterycycle_start_address = 600;
        self.battery_batterycycle_requestfloating = self.battery_batterycycle_start_address + 0;
        self.battery_batterycycle_requestreducedfloating = self.battery_batterycycle_start_address + 1;
        self.battery_batterycycle_requestabsorption = self.battery_batterycycle_start_address + 2;
        self.battery_batterycycle_requestequalization = self.battery_batterycycle_start_address + 3;
        self.battery_batterycycle_floatingvoltage = self.battery_batterycycle_start_address + 4;
        self.battery_batterycycle_reducedfloatingenabled = self.battery_batterycycle_start_address + 6;
        self.battery_batterycycle_reducedfloatingvoltage = self.battery_batterycycle_start_address + 7;
        self.battery_batterycycle_timeatfloatingvoltagebeforeenteringreducedfloating = self.battery_batterycycle_start_address + 9;
        self.battery_batterycycle_periodicalabsorptionenabled = self.battery_batterycycle_start_address + 11;
        self.battery_batterycycle_periodicalabsorptionvoltage = self.battery_batterycycle_start_address + 12;
        self.battery_batterycycle_periodicalabsorptionmaxduration = self.battery_batterycycle_start_address + 14;
        self.battery_batterycycle_timeinreducedfloatingbeforeaskingperiodicalabsorption = self.battery_batterycycle_start_address + 16;
        self.battery_batterycycle_absorption = self.battery_batterycycle_start_address + 18;
        self.battery_batterycycle_absorptionconditions = self.battery_batterycycle_start_address + 19;
        self.battery_batterycycle_absorptionvoltage = self.battery_batterycycle_start_address + 21;
        self.battery_batterycycle_amphourdischargedforaskingabsorption = self.battery_batterycycle_start_address + 23;
        self.battery_batterycycle_voltageforaskingabsorption = self.battery_batterycycle_start_address + 25;
        self.battery_batterycycle_voltagedurationbeforeaskingabsorption = self.battery_batterycycle_start_address + 27;
        self.battery_batterycycle_absorptionmaxduration = self.battery_batterycycle_start_address + 29;
        self.battery_batterycycle_absorptionterminatedbycurrent = self.battery_batterycycle_start_address + 31;
        self.battery_batterycycle_currenttoterminateabsorption = self.battery_batterycycle_start_address + 32;
        self.battery_batterycycle_minimumwaitingtimebetweenabsorptions = self.battery_batterycycle_start_address + 34;
        self.battery_batterycycle_equalization = self.battery_batterycycle_start_address + 36;
        self.battery_batterycycle_equalizationconditions = self.battery_batterycycle_start_address + 37;
        self.battery_batterycycle_equalizationvoltage = self.battery_batterycycle_start_address + 39;
        self.battery_batterycycle_elapsedtimeforaskinganequalization = self.battery_batterycycle_start_address + 41;
        self.battery_batterycycle_amphourdischargedforaskingequalization = self.battery_batterycycle_start_address + 43;
        self.battery_batterycycle_equalizationduration = self.battery_batterycycle_start_address + 45;
        self.battery_batterycycle_equalizationafterabsorption = self.battery_batterycycle_start_address + 47;
        self.battery_batterycycle_equalizationmaxcurrentifequalizationafterabsorption = self.battery_batterycycle_start_address + 48;
        self.battery_batterycycle_phase = self.battery_batterycycle_start_address + 50;
        self.battery_batterycycle_timespentinactualphase = self.battery_batterycycle_start_address + 52;
        self.battery_batterycycle_transition = self.battery_batterycycle_start_address + 54;
        self.battery_batterycycle_transitionreasons = self.battery_batterycycle_start_address + 56;
        self.battery_batterycycle_remainingtimebeforenextabsorptionallowed = self.battery_batterycycle_start_address + 58;
        self.battery_batterycycle_remainingamphourdischargedbeforeabsorptionistriggered = self.battery_batterycycle_start_address + 60;
        self.battery_batterycycle_remainingtimebeforeabsorptionistriggeredbylowsoc = self.battery_batterycycle_start_address + 62;
        self.battery_batterycycle_remainingtimebeforeabsorptionistriggeredbyvoltage = self.battery_batterycycle_start_address + 64;
        self.battery_batterycycle_remainingtimebeforeequalizationistriggeredbytimeperiod = self.battery_batterycycle_start_address + 66;
        self.battery_batterycycle_remainingamphourdischargedbeforeequalizationistriggered = self.battery_batterycycle_start_address + 68;
        self.battery_batterycycle_remainingtimebeforeequalizationistriggeredbylowsoc = self.battery_batterycycle_start_address + 70;

        # Object BatteryProtection Modbus Address
        self.battery_batteryprotection_start_address = 900;
        self.battery_batteryprotection_undervoltageatrest = self.battery_batteryprotection_start_address + 0;
        self.battery_batteryprotection_undervoltageatcnomoverfive = self.battery_batteryprotection_start_address + 2;
        self.battery_batteryprotection_durationinundervoltagebeforeerror = self.battery_batteryprotection_start_address + 4;
        self.battery_batteryprotection_timeperiodforresetingundervoltagecnt = self.battery_batteryprotection_start_address + 6;
        self.battery_batteryprotection_undervoltagecntvalueforprohibitautorestart = self.battery_batteryprotection_start_address + 8;
        self.battery_batteryprotection_timeperiodforresetingcriticalundervoltagecnt = self.battery_batteryprotection_start_address + 10;
        self.battery_batteryprotection_criticalundervoltagecntvalueforprohibitautorestart = self.battery_batteryprotection_start_address + 12;
        self.battery_batteryprotection_restartvoltageafterundervoltageoccured = self.battery_batteryprotection_start_address + 14;
        self.battery_batteryprotection_bloenabled = self.battery_batteryprotection_start_address + 16;
        self.battery_batteryprotection_blovoltageincrement = self.battery_batteryprotection_start_address + 17;
        self.battery_batteryprotection_blomaxvoltage = self.battery_batteryprotection_start_address + 19;
        self.battery_batteryprotection_bloresetvoltage = self.battery_batteryprotection_start_address + 21;
        self.battery_batteryprotection_overvoltage = self.battery_batteryprotection_start_address + 23;
        self.battery_batteryprotection_hightempforwarning = self.battery_batteryprotection_start_address + 25;
        self.battery_batteryprotection_hightempforerror = self.battery_batteryprotection_start_address + 27;
        self.battery_batteryprotection_lowtempforwarning = self.battery_batteryprotection_start_address + 29;
        self.battery_batteryprotection_lowtempforerror = self.battery_batteryprotection_start_address + 31;
        self.battery_batteryprotection_overcurrent = self.battery_batteryprotection_start_address + 33;
        self.battery_batteryprotection_undervoltageatrestwithblo = self.battery_batteryprotection_start_address + 35;
        self.battery_batteryprotection_undervoltageatcnomoverfivewithblo = self.battery_batteryprotection_start_address + 37;
        self.battery_batteryprotection_undervoltagecnt = self.battery_batteryprotection_start_address + 39;
        self.battery_batteryprotection_criticalundervoltagecnt = self.battery_batteryprotection_start_address + 41;

        # Object SocEstimator Modbus Address
        self.battery_socestimator_start_address = 1200;
        self.battery_socestimator_peukertfactor = self.battery_socestimator_start_address + 26;
        self.battery_socestimator_selfdischargecoefficient = self.battery_socestimator_start_address + 28;
        self.battery_socestimator_endofchargesynchronization = self.battery_socestimator_start_address + 30;
        self.battery_socestimator_endofchargevoltagelevel = self.battery_socestimator_start_address + 31;
        self.battery_socestimator_endofchargecurrentlevel = self.battery_socestimator_start_address + 33;
        self.battery_socestimator_minimumtimebeforeendofcharge = self.battery_socestimator_start_address + 35;
        self.battery_socestimator_resetsocvalue = self.battery_socestimator_start_address + 37;
        self.battery_socestimator_desiredsocvalueinpercent = self.battery_socestimator_start_address + 38;
        self.battery_socestimator_configuredassimplecounter = self.battery_socestimator_start_address + 40;


        # Group AcSource Modbus Address
        # Object TriPhaseMeasure Modbus Address
        self.acsource_triphasemeasure_start_address = 0;
        self.acsource_triphasemeasure_frequency = self.acsource_triphasemeasure_start_address + 0;
        self.acsource_triphasemeasure_linevoltagel1l2 = self.acsource_triphasemeasure_start_address + 2;
        self.acsource_triphasemeasure_linevoltagel2l3 = self.acsource_triphasemeasure_start_address + 4;
        self.acsource_triphasemeasure_linevoltagel3l1 = self.acsource_triphasemeasure_start_address + 6;
        self.acsource_triphasemeasure_totalactivepower = self.acsource_triphasemeasure_start_address + 8;
        self.acsource_triphasemeasure_totalapparentpower = self.acsource_triphasemeasure_start_address + 10;
        self.acsource_triphasemeasure_anglel2relativetol1 = self.acsource_triphasemeasure_start_address + 12;
        self.acsource_triphasemeasure_anglel3relativetol1 = self.acsource_triphasemeasure_start_address + 14;
        self.acsource_triphasemeasure_dayconsumedenergy = self.acsource_triphasemeasure_start_address + 16;
        self.acsource_triphasemeasure_previousdayconsumedenergy = self.acsource_triphasemeasure_start_address + 18;
        self.acsource_triphasemeasure_resetableconsumedenergy = self.acsource_triphasemeasure_start_address + 20;
        self.acsource_triphasemeasure_totalconsumedenergy = self.acsource_triphasemeasure_start_address + 24;
        self.acsource_triphasemeasure_dayproducedenergy = self.acsource_triphasemeasure_start_address + 28;
        self.acsource_triphasemeasure_previousdayproducedenergy = self.acsource_triphasemeasure_start_address + 30;
        self.acsource_triphasemeasure_resetableproducedenergy = self.acsource_triphasemeasure_start_address + 32;
        self.acsource_triphasemeasure_totalproducedenergy = self.acsource_triphasemeasure_start_address + 36;
        self.acsource_triphasemeasure_dayruntime = self.acsource_triphasemeasure_start_address + 40;
        self.acsource_triphasemeasure_totalruntime = self.acsource_triphasemeasure_start_address + 42;
        self.acsource_triphasemeasure_daypeakpower = self.acsource_triphasemeasure_start_address + 44;
        self.acsource_triphasemeasure_previousdaypeakpower = self.acsource_triphasemeasure_start_address + 46;
        self.acsource_triphasemeasure_dayminactivepower = self.acsource_triphasemeasure_start_address + 48;
        self.acsource_triphasemeasure_previousdayminactivepower = self.acsource_triphasemeasure_start_address + 50;
        self.acsource_triphasemeasure_daymaxactivepower = self.acsource_triphasemeasure_start_address + 52;
        self.acsource_triphasemeasure_previousdaymaxactivepower = self.acsource_triphasemeasure_start_address + 54;

        # Object L1Measure Modbus Address
        self.acsource_l1measure_start_address = 300;
        self.acsource_l1measure_phasevoltage = self.acsource_l1measure_start_address + 0;
        self.acsource_l1measure_current = self.acsource_l1measure_start_address + 2;
        self.acsource_l1measure_activepower = self.acsource_l1measure_start_address + 4;
        self.acsource_l1measure_reactivepower = self.acsource_l1measure_start_address + 6;
        self.acsource_l1measure_apparentpower = self.acsource_l1measure_start_address + 8;
        self.acsource_l1measure_cosphi = self.acsource_l1measure_start_address + 10;
        self.acsource_l1measure_daypeakpower = self.acsource_l1measure_start_address + 12;
        self.acsource_l1measure_previousdaypeakpower = self.acsource_l1measure_start_address + 14;
        self.acsource_l1measure_dayminactivepower = self.acsource_l1measure_start_address + 16;
        self.acsource_l1measure_previousdayminactivepower = self.acsource_l1measure_start_address + 18;
        self.acsource_l1measure_daymaxactivepower = self.acsource_l1measure_start_address + 20;
        self.acsource_l1measure_previousdaymaxactivepower = self.acsource_l1measure_start_address + 22;
        self.acsource_l1measure_dayconsumedenergy = self.acsource_l1measure_start_address + 28;
        self.acsource_l1measure_previousdayconsumedenergy = self.acsource_l1measure_start_address + 30;
        self.acsource_l1measure_resetableconsumedenergy = self.acsource_l1measure_start_address + 32;
        self.acsource_l1measure_totalconsumedenergy = self.acsource_l1measure_start_address + 36;
        self.acsource_l1measure_dayproducedenergy = self.acsource_l1measure_start_address + 40;
        self.acsource_l1measure_previousdayproducedenergy = self.acsource_l1measure_start_address + 42;
        self.acsource_l1measure_resetableproducedenergy = self.acsource_l1measure_start_address + 44;
        self.acsource_l1measure_totalproducedenergy = self.acsource_l1measure_start_address + 48;

        # Object L2Measure Modbus Address
        self.acsource_l2measure_start_address = 600;
        self.acsource_l2measure_phasevoltage = self.acsource_l2measure_start_address + 0;
        self.acsource_l2measure_current = self.acsource_l2measure_start_address + 2;
        self.acsource_l2measure_activepower = self.acsource_l2measure_start_address + 4;
        self.acsource_l2measure_reactivepower = self.acsource_l2measure_start_address + 6;
        self.acsource_l2measure_apparentpower = self.acsource_l2measure_start_address + 8;
        self.acsource_l2measure_cosphi = self.acsource_l2measure_start_address + 10;
        self.acsource_l2measure_daypeakpower = self.acsource_l2measure_start_address + 12;
        self.acsource_l2measure_previousdaypeakpower = self.acsource_l2measure_start_address + 14;
        self.acsource_l2measure_dayminactivepower = self.acsource_l2measure_start_address + 16;
        self.acsource_l2measure_previousdayminactivepower = self.acsource_l2measure_start_address + 18;
        self.acsource_l2measure_daymaxactivepower = self.acsource_l2measure_start_address + 20;
        self.acsource_l2measure_previousdaymaxactivepower = self.acsource_l2measure_start_address + 22;
        self.acsource_l2measure_dayconsumedenergy = self.acsource_l2measure_start_address + 28;
        self.acsource_l2measure_previousdayconsumedenergy = self.acsource_l2measure_start_address + 30;
        self.acsource_l2measure_resetableconsumedenergy = self.acsource_l2measure_start_address + 32;
        self.acsource_l2measure_totalconsumedenergy = self.acsource_l2measure_start_address + 36;
        self.acsource_l2measure_dayproducedenergy = self.acsource_l2measure_start_address + 40;
        self.acsource_l2measure_previousdayproducedenergy = self.acsource_l2measure_start_address + 42;
        self.acsource_l2measure_resetableproducedenergy = self.acsource_l2measure_start_address + 44;
        self.acsource_l2measure_totalproducedenergy = self.acsource_l2measure_start_address + 48;

        # Object L3Measure Modbus Address
        self.acsource_l3measure_start_address = 900;
        self.acsource_l3measure_phasevoltage = self.acsource_l3measure_start_address + 0;
        self.acsource_l3measure_current = self.acsource_l3measure_start_address + 2;
        self.acsource_l3measure_activepower = self.acsource_l3measure_start_address + 4;
        self.acsource_l3measure_reactivepower = self.acsource_l3measure_start_address + 6;
        self.acsource_l3measure_apparentpower = self.acsource_l3measure_start_address + 8;
        self.acsource_l3measure_cosphi = self.acsource_l3measure_start_address + 10;
        self.acsource_l3measure_daypeakpower = self.acsource_l3measure_start_address + 12;
        self.acsource_l3measure_previousdaypeakpower = self.acsource_l3measure_start_address + 14;
        self.acsource_l3measure_dayminactivepower = self.acsource_l3measure_start_address + 16;
        self.acsource_l3measure_previousdayminactivepower = self.acsource_l3measure_start_address + 18;
        self.acsource_l3measure_daymaxactivepower = self.acsource_l3measure_start_address + 20;
        self.acsource_l3measure_previousdaymaxactivepower = self.acsource_l3measure_start_address + 22;
        self.acsource_l3measure_dayconsumedenergy = self.acsource_l3measure_start_address + 28;
        self.acsource_l3measure_previousdayconsumedenergy = self.acsource_l3measure_start_address + 30;
        self.acsource_l3measure_resetableconsumedenergy = self.acsource_l3measure_start_address + 32;
        self.acsource_l3measure_totalconsumedenergy = self.acsource_l3measure_start_address + 36;
        self.acsource_l3measure_dayproducedenergy = self.acsource_l3measure_start_address + 40;
        self.acsource_l3measure_previousdayproducedenergy = self.acsource_l3measure_start_address + 42;
        self.acsource_l3measure_resetableproducedenergy = self.acsource_l3measure_start_address + 44;
        self.acsource_l3measure_totalproducedenergy = self.acsource_l3measure_start_address + 48;

        # Object Source Modbus Address
        self.acsource_source_start_address = 1200;
        self.acsource_source_type = self.acsource_source_start_address + 3;
        self.acsource_source_gridcode = self.acsource_source_start_address + 5;
        self.acsource_source_connectionallowed = self.acsource_source_start_address + 7;
        self.acsource_source_gridfeedingallowed = self.acsource_source_start_address + 8;
        self.acsource_source_ratedcurrent = self.acsource_source_start_address + 9;
        self.acsource_source_relativeangletolerance = self.acsource_source_start_address + 11;
        self.acsource_source_allowindividualphaseconnection = self.acsource_source_start_address + 13;
        self.acsource_source_mindisconnetedtimebeforenewconnection = self.acsource_source_start_address + 14;
        self.acsource_source_activateinertialsmoothing = self.acsource_source_start_address + 16;
        self.acsource_source_compensateloaddccurrent = self.acsource_source_start_address + 17;
        self.acsource_source_enablefastenvelopedetection = self.acsource_source_start_address + 20;
        self.acsource_source_envelopetolerance = self.acsource_source_start_address + 21;
        self.acsource_source_antiislandingdetectionlevel = self.acsource_source_start_address + 24;
        self.acsource_source_antiislandingfrequency = self.acsource_source_start_address + 26;
        self.acsource_source_antiislandingperturbationamplitude = self.acsource_source_start_address + 28;
        self.acsource_source_antiislandingminimalamplitude = self.acsource_source_start_address + 30;
        self.acsource_source_overvoltagecurveu1 = self.acsource_source_start_address + 35;
        self.acsource_source_overvoltagecurvet1 = self.acsource_source_start_address + 37;
        self.acsource_source_overvoltagecurveu2 = self.acsource_source_start_address + 39;
        self.acsource_source_overvoltagecurvet2 = self.acsource_source_start_address + 41;
        self.acsource_source_overvoltagecurveu3 = self.acsource_source_start_address + 43;
        self.acsource_source_overvoltagecurvet3 = self.acsource_source_start_address + 45;
        self.acsource_source_maxvoltagefaultonset = self.acsource_source_start_address + 47;
        self.acsource_source_maxpermanentvoltage = self.acsource_source_start_address + 49;
        self.acsource_source_minpermanentvoltage = self.acsource_source_start_address + 51;
        self.acsource_source_minvoltagefaultonset = self.acsource_source_start_address + 53;
        self.acsource_source_undervoltagecurvet2 = self.acsource_source_start_address + 55;
        self.acsource_source_undervoltagecurveu1 = self.acsource_source_start_address + 57;
        self.acsource_source_undervoltagecurvet1 = self.acsource_source_start_address + 59;
        self.acsource_source_zerocurrentmodeenabled = self.acsource_source_start_address + 61;
        self.acsource_source_zerocurrentmodeovervoltagethreshold = self.acsource_source_start_address + 62;
        self.acsource_source_zerocurrentmodeundervoltagethreshold = self.acsource_source_start_address + 64;
        self.acsource_source_thresholdfrequencyforoverfrequency = self.acsource_source_start_address + 66;
        self.acsource_source_statismforoverfrequency = self.acsource_source_start_address + 68;
        self.acsource_source_intensionaldelayforoverfrequency = self.acsource_source_start_address + 70;
        self.acsource_source_disablingthresholdfrequencyforoverfrequency = self.acsource_source_start_address + 72;
        self.acsource_source_disablingdelayforoverfrequency = self.acsource_source_start_address + 74;
        self.acsource_source_prefforoverfrequency = self.acsource_source_start_address + 76;
        self.acsource_source_thresholdfrequencyforunderfrequency = self.acsource_source_start_address + 78;
        self.acsource_source_statismforunderfrequency = self.acsource_source_start_address + 80;
        self.acsource_source_intensionaldelayforunderfrequency = self.acsource_source_start_address + 82;
        self.acsource_source_prefforunderfrequency = self.acsource_source_start_address + 84;
        self.acsource_source_overexcitedcosphicapacity = self.acsource_source_start_address + 86;
        self.acsource_source_underexcitedcosphicapacity = self.acsource_source_start_address + 88;
        self.acsource_source_reactivepowermethod = self.acsource_source_start_address + 90;
        self.acsource_source_reactivepowersetpoint = self.acsource_source_start_address + 92;
        self.acsource_source_cosphisetpoint = self.acsource_source_start_address + 94;
        self.acsource_source_reactivepowerdirection = self.acsource_source_start_address + 96;
        self.acsource_source_reactivepowercurveq1 = self.acsource_source_start_address + 98;
        self.acsource_source_reactivepowercurveq2 = self.acsource_source_start_address + 100;
        self.acsource_source_reactivepowercurveq3 = self.acsource_source_start_address + 102;
        self.acsource_source_reactivepowercurveq4 = self.acsource_source_start_address + 104;
        self.acsource_source_reactivepowercurveu1 = self.acsource_source_start_address + 106;
        self.acsource_source_reactivepowercurveu2 = self.acsource_source_start_address + 108;
        self.acsource_source_reactivepowercurveu3 = self.acsource_source_start_address + 110;
        self.acsource_source_reactivepowercurveu4 = self.acsource_source_start_address + 112;
        self.acsource_source_reactivepowercontroltimebehaviour = self.acsource_source_start_address + 114;
        self.acsource_source_reactivepowercontrolcosphimin = self.acsource_source_start_address + 116;
        self.acsource_source_reactivepowercontrollockinactivepower = self.acsource_source_start_address + 118;
        self.acsource_source_reactivepowercontrollockoutactivepower = self.acsource_source_start_address + 120;
        self.acsource_source_reactivepowercurvecosphioverexcited1 = self.acsource_source_start_address + 122;
        self.acsource_source_reactivepowercurvecosphioverexcited2 = self.acsource_source_start_address + 124;
        self.acsource_source_reactivepowercurvecosphiunderexcited3 = self.acsource_source_start_address + 126;
        self.acsource_source_reactivepowercurvecosphiunderexcited4 = self.acsource_source_start_address + 128;
        self.acsource_source_reactivepowercurvep1 = self.acsource_source_start_address + 130;
        self.acsource_source_reactivepowercurvep2 = self.acsource_source_start_address + 132;
        self.acsource_source_reactivepowercurvep3 = self.acsource_source_start_address + 134;
        self.acsource_source_reactivepowercurvep4 = self.acsource_source_start_address + 136;
        self.acsource_source_overvoltagethresholdstage2 = self.acsource_source_start_address + 138;
        self.acsource_source_overvoltageoperatetimestage2 = self.acsource_source_start_address + 140;
        self.acsource_source_overvoltagethresholdstage1 = self.acsource_source_start_address + 142;
        self.acsource_source_overvoltageoperatetimestage1 = self.acsource_source_start_address + 144;
        self.acsource_source_overvoltagethreshold10minmean = self.acsource_source_start_address + 146;
        self.acsource_source_undervoltagethresholdstage1 = self.acsource_source_start_address + 148;
        self.acsource_source_undervoltageoperatetimestage1 = self.acsource_source_start_address + 150;
        self.acsource_source_undervoltagethresholdstage2 = self.acsource_source_start_address + 152;
        self.acsource_source_undervoltageoperatetimestage2 = self.acsource_source_start_address + 154;
        self.acsource_source_overfrequencythresholdstage1 = self.acsource_source_start_address + 158;
        self.acsource_source_overfrequencyoperatetimestage1 = self.acsource_source_start_address + 160;
        self.acsource_source_overfrequencythresholdstage2 = self.acsource_source_start_address + 162;
        self.acsource_source_overfrequencyoperatetimestage2 = self.acsource_source_start_address + 164;
        self.acsource_source_underfrequencythresholdstage2 = self.acsource_source_start_address + 166;
        self.acsource_source_underfrequencyoperatetimestage2 = self.acsource_source_start_address + 168;
        self.acsource_source_underfrequencythresholdstage1 = self.acsource_source_start_address + 170;
        self.acsource_source_underfrequencyoperatetimestage1 = self.acsource_source_start_address + 172;
        self.acsource_source_cmdentryidxtoswitchtonarrowfrequencyband = self.acsource_source_start_address + 176;
        self.acsource_source_overfrequencythresholdnarrowband = self.acsource_source_start_address + 178;
        self.acsource_source_overfrequencyoperatetimenarrowband = self.acsource_source_start_address + 180;
        self.acsource_source_underfrequencythresholdnarrowband = self.acsource_source_start_address + 182;
        self.acsource_source_underfrequencyoperatetimenarrowband = self.acsource_source_start_address + 184;
        self.acsource_source_uppervoltageforautoreconnection = self.acsource_source_start_address + 186;
        self.acsource_source_lowervoltageforautoreconnection = self.acsource_source_start_address + 188;
        self.acsource_source_upperfrequencyforautoreconnection = self.acsource_source_start_address + 190;
        self.acsource_source_lowerfrequencyforautoreconnection = self.acsource_source_start_address + 192;
        self.acsource_source_observationtimeforautoreconnection = self.acsource_source_start_address + 194;
        self.acsource_source_activepowerincreasegradientforautoreconnection = self.acsource_source_start_address + 196;
        self.acsource_source_uppervoltageforstartgeneration = self.acsource_source_start_address + 198;
        self.acsource_source_lowervoltageforstartgeneration = self.acsource_source_start_address + 200;
        self.acsource_source_upperfrequencyforstartgeneration = self.acsource_source_start_address + 202;
        self.acsource_source_lowerfrequencyforstartgeneration = self.acsource_source_start_address + 204;
        self.acsource_source_observationtimeforstartgeneration = self.acsource_source_start_address + 206;
        self.acsource_source_activepowerincreasegradientforstartgeneration = self.acsource_source_start_address + 208;
        self.acsource_source_cmdentryidxtoallowtransfertripping = self.acsource_source_start_address + 210;
        self.acsource_source_cmdentryidxforceasingactivepower = self.acsource_source_start_address + 212;
        self.acsource_source_cmdentryidxforreductionofactivepoweronsetpoint = self.acsource_source_start_address + 214;
        self.acsource_source_reductionofactivepowersetpoint = self.acsource_source_start_address + 216;
        self.acsource_source_reductionofactivepowersetpointslope = self.acsource_source_start_address + 218;
        self.acsource_source_voltagetostartproducedactivepowerreduction = self.acsource_source_start_address + 220;
        self.acsource_source_voltageforreducedproducedactivepower = self.acsource_source_start_address + 222;
        self.acsource_source_activepowercurvetimeconstant = self.acsource_source_start_address + 224;
        self.acsource_source_activepowercurvepref = self.acsource_source_start_address + 226;
        self.acsource_source_usetriphasetargetactivepower = self.acsource_source_start_address + 229;
        self.acsource_source_targetactivepowerperphase = self.acsource_source_start_address + 230;
        self.acsource_source_setpointslevel = self.acsource_source_start_address + 232;
        self.acsource_source_phaseexistance = self.acsource_source_start_address + 240;
        self.acsource_source_antiislanding = self.acsource_source_start_address + 242;
        self.acsource_source_antiislandingrocofthreshold = self.acsource_source_start_address + 244;
        self.acsource_source_antiislandingrocofoperatetime = self.acsource_source_start_address + 246;
        self.acsource_source_reducedproducedactivepower = self.acsource_source_start_address + 248;
        self.acsource_source_reducedconsummedactivepower = self.acsource_source_start_address + 250;
        self.acsource_source_voltageforreducedconsummedactivepower = self.acsource_source_start_address + 252;
        self.acsource_source_voltagetostartconsummedactivepowerreduction = self.acsource_source_start_address + 254;
        self.acsource_source_transitionfrequencyforoverfrequency = self.acsource_source_start_address + 256;
        self.acsource_source_pminfrequencyforoverfrequency = self.acsource_source_start_address + 258;
        self.acsource_source_stopchfrequencyforunderfrequency = self.acsource_source_start_address + 260;
        self.acsource_source_pmaxfrequencyforunderfrequency = self.acsource_source_start_address + 262;
        self.acsource_source_hystfrequencyforoverunderfrequency = self.acsource_source_start_address + 264;
        self.acsource_source_compensateharmonics = self.acsource_source_start_address + 266;
        self.acsource_source_cmdentryidxforreducofactivepowerat10 = self.acsource_source_start_address + 267;
        self.acsource_source_cmdentryidxforreducofactivepowerat20 = self.acsource_source_start_address + 269;
        self.acsource_source_cmdentryidxforreducofactivepowerat30 = self.acsource_source_start_address + 271;
        self.acsource_source_cmdentryidxforreducofactivepowerat40 = self.acsource_source_start_address + 273;
        self.acsource_source_cmdentryidxforreducofactivepowerat50 = self.acsource_source_start_address + 275;
        self.acsource_source_cmdentryidxforreducofactivepowerat60 = self.acsource_source_start_address + 277;
        self.acsource_source_cmdentryidxforreducofactivepowerat70 = self.acsource_source_start_address + 279;
        self.acsource_source_cmdentryidxforreducofactivepowerat80 = self.acsource_source_start_address + 281;
        self.acsource_source_cmdentryidxforreducofactivepowerat90 = self.acsource_source_start_address + 283;
        self.acsource_source_phasebalancing = self.acsource_source_start_address + 285;

        # Object L1Source Modbus Address
        self.acsource_l1source_start_address = 1800;
        self.acsource_l1source_status = self.acsource_l1source_start_address + 0;
        self.acsource_l1source_unconnectedreasons = self.acsource_l1source_start_address + 2;
        self.acsource_l1source_warnings = self.acsource_l1source_start_address + 4;
        self.acsource_l1source_errors = self.acsource_l1source_start_address + 6;
        self.acsource_l1source_causeofdisconnection = self.acsource_l1source_start_address + 8;
        self.acsource_l1source_voltage10minmean = self.acsource_l1source_start_address + 12;
        self.acsource_l1source_connectionallowed = self.acsource_l1source_start_address + 14;
        self.acsource_l1source_gridfeedingallowed = self.acsource_l1source_start_address + 15;
        self.acsource_l1source_maxsourcedactivepower = self.acsource_l1source_start_address + 16;
        self.acsource_l1source_maxsinkedactivepower = self.acsource_l1source_start_address + 18;
        self.acsource_l1source_maxsourcedreactivepower = self.acsource_l1source_start_address + 20;
        self.acsource_l1source_maxsinkedreactivepower = self.acsource_l1source_start_address + 22;
        self.acsource_l1source_targetsourcedactivepower = self.acsource_l1source_start_address + 24;
        self.acsource_l1source_limitslevel = self.acsource_l1source_start_address + 28;
        self.acsource_l1source_setpointslevel = self.acsource_l1source_start_address + 30;

        # Object L2Source Modbus Address
        self.acsource_l2source_start_address = 2100;
        self.acsource_l2source_status = self.acsource_l2source_start_address + 0;
        self.acsource_l2source_unconnectedreasons = self.acsource_l2source_start_address + 2;
        self.acsource_l2source_warnings = self.acsource_l2source_start_address + 4;
        self.acsource_l2source_errors = self.acsource_l2source_start_address + 6;
        self.acsource_l2source_causeofdisconnection = self.acsource_l2source_start_address + 8;
        self.acsource_l2source_voltage10minmean = self.acsource_l2source_start_address + 12;
        self.acsource_l2source_connectionallowed = self.acsource_l2source_start_address + 14;
        self.acsource_l2source_gridfeedingallowed = self.acsource_l2source_start_address + 15;
        self.acsource_l2source_maxsourcedactivepower = self.acsource_l2source_start_address + 16;
        self.acsource_l2source_maxsinkedactivepower = self.acsource_l2source_start_address + 18;
        self.acsource_l2source_maxsourcedreactivepower = self.acsource_l2source_start_address + 20;
        self.acsource_l2source_maxsinkedreactivepower = self.acsource_l2source_start_address + 22;
        self.acsource_l2source_targetsourcedactivepower = self.acsource_l2source_start_address + 24;
        self.acsource_l2source_limitslevel = self.acsource_l2source_start_address + 28;
        self.acsource_l2source_setpointslevel = self.acsource_l2source_start_address + 30;

        # Object L3Source Modbus Address
        self.acsource_l3source_start_address = 2400;
        self.acsource_l3source_status = self.acsource_l3source_start_address + 0;
        self.acsource_l3source_unconnectedreasons = self.acsource_l3source_start_address + 2;
        self.acsource_l3source_warnings = self.acsource_l3source_start_address + 4;
        self.acsource_l3source_errors = self.acsource_l3source_start_address + 6;
        self.acsource_l3source_causeofdisconnection = self.acsource_l3source_start_address + 8;
        self.acsource_l3source_voltage10minmean = self.acsource_l3source_start_address + 12;
        self.acsource_l3source_connectionallowed = self.acsource_l3source_start_address + 14;
        self.acsource_l3source_gridfeedingallowed = self.acsource_l3source_start_address + 15;
        self.acsource_l3source_maxsourcedactivepower = self.acsource_l3source_start_address + 16;
        self.acsource_l3source_maxsinkedactivepower = self.acsource_l3source_start_address + 18;
        self.acsource_l3source_maxsourcedreactivepower = self.acsource_l3source_start_address + 20;
        self.acsource_l3source_maxsinkedreactivepower = self.acsource_l3source_start_address + 22;
        self.acsource_l3source_targetsourcedactivepower = self.acsource_l3source_start_address + 24;
        self.acsource_l3source_limitslevel = self.acsource_l3source_start_address + 28;
        self.acsource_l3source_setpointslevel = self.acsource_l3source_start_address + 30;


        # Group AcFlexLoad Modbus Address
        # Object TriPhaseMeasure Modbus Address
        self.acflexload_triphasemeasure_start_address = 0;
        self.acflexload_triphasemeasure_frequency = self.acflexload_triphasemeasure_start_address + 0;
        self.acflexload_triphasemeasure_linevoltagel1l2 = self.acflexload_triphasemeasure_start_address + 2;
        self.acflexload_triphasemeasure_linevoltagel2l3 = self.acflexload_triphasemeasure_start_address + 4;
        self.acflexload_triphasemeasure_linevoltagel3l1 = self.acflexload_triphasemeasure_start_address + 6;
        self.acflexload_triphasemeasure_totalactivepower = self.acflexload_triphasemeasure_start_address + 8;
        self.acflexload_triphasemeasure_totalapparentpower = self.acflexload_triphasemeasure_start_address + 10;
        self.acflexload_triphasemeasure_anglel2relativetol1 = self.acflexload_triphasemeasure_start_address + 12;
        self.acflexload_triphasemeasure_anglel3relativetol1 = self.acflexload_triphasemeasure_start_address + 14;
        self.acflexload_triphasemeasure_dayconsumedenergy = self.acflexload_triphasemeasure_start_address + 16;
        self.acflexload_triphasemeasure_previousdayconsumedenergy = self.acflexload_triphasemeasure_start_address + 18;
        self.acflexload_triphasemeasure_resetableconsumedenergy = self.acflexload_triphasemeasure_start_address + 20;
        self.acflexload_triphasemeasure_totalconsumedenergy = self.acflexload_triphasemeasure_start_address + 24;
        self.acflexload_triphasemeasure_dayproducedenergy = self.acflexload_triphasemeasure_start_address + 28;
        self.acflexload_triphasemeasure_previousdayproducedenergy = self.acflexload_triphasemeasure_start_address + 30;
        self.acflexload_triphasemeasure_resetableproducedenergy = self.acflexload_triphasemeasure_start_address + 32;
        self.acflexload_triphasemeasure_totalproducedenergy = self.acflexload_triphasemeasure_start_address + 36;
        self.acflexload_triphasemeasure_dayruntime = self.acflexload_triphasemeasure_start_address + 40;
        self.acflexload_triphasemeasure_totalruntime = self.acflexload_triphasemeasure_start_address + 42;
        self.acflexload_triphasemeasure_daypeakpower = self.acflexload_triphasemeasure_start_address + 44;
        self.acflexload_triphasemeasure_previousdaypeakpower = self.acflexload_triphasemeasure_start_address + 46;
        self.acflexload_triphasemeasure_dayminactivepower = self.acflexload_triphasemeasure_start_address + 48;
        self.acflexload_triphasemeasure_previousdayminactivepower = self.acflexload_triphasemeasure_start_address + 50;
        self.acflexload_triphasemeasure_daymaxactivepower = self.acflexload_triphasemeasure_start_address + 52;
        self.acflexload_triphasemeasure_previousdaymaxactivepower = self.acflexload_triphasemeasure_start_address + 54;

        # Object L1Measure Modbus Address
        self.acflexload_l1measure_start_address = 300;
        self.acflexload_l1measure_phasevoltage = self.acflexload_l1measure_start_address + 0;
        self.acflexload_l1measure_current = self.acflexload_l1measure_start_address + 2;
        self.acflexload_l1measure_activepower = self.acflexload_l1measure_start_address + 4;
        self.acflexload_l1measure_reactivepower = self.acflexload_l1measure_start_address + 6;
        self.acflexload_l1measure_apparentpower = self.acflexload_l1measure_start_address + 8;
        self.acflexload_l1measure_cosphi = self.acflexload_l1measure_start_address + 10;
        self.acflexload_l1measure_daypeakpower = self.acflexload_l1measure_start_address + 12;
        self.acflexload_l1measure_previousdaypeakpower = self.acflexload_l1measure_start_address + 14;
        self.acflexload_l1measure_dayminactivepower = self.acflexload_l1measure_start_address + 16;
        self.acflexload_l1measure_previousdayminactivepower = self.acflexload_l1measure_start_address + 18;
        self.acflexload_l1measure_daymaxactivepower = self.acflexload_l1measure_start_address + 20;
        self.acflexload_l1measure_previousdaymaxactivepower = self.acflexload_l1measure_start_address + 22;
        self.acflexload_l1measure_dayconsumedenergy = self.acflexload_l1measure_start_address + 28;
        self.acflexload_l1measure_previousdayconsumedenergy = self.acflexload_l1measure_start_address + 30;
        self.acflexload_l1measure_resetableconsumedenergy = self.acflexload_l1measure_start_address + 32;
        self.acflexload_l1measure_totalconsumedenergy = self.acflexload_l1measure_start_address + 36;
        self.acflexload_l1measure_dayproducedenergy = self.acflexload_l1measure_start_address + 40;
        self.acflexload_l1measure_previousdayproducedenergy = self.acflexload_l1measure_start_address + 42;
        self.acflexload_l1measure_resetableproducedenergy = self.acflexload_l1measure_start_address + 44;
        self.acflexload_l1measure_totalproducedenergy = self.acflexload_l1measure_start_address + 48;

        # Object L2Measure Modbus Address
        self.acflexload_l2measure_start_address = 600;
        self.acflexload_l2measure_phasevoltage = self.acflexload_l2measure_start_address + 0;
        self.acflexload_l2measure_current = self.acflexload_l2measure_start_address + 2;
        self.acflexload_l2measure_activepower = self.acflexload_l2measure_start_address + 4;
        self.acflexload_l2measure_reactivepower = self.acflexload_l2measure_start_address + 6;
        self.acflexload_l2measure_apparentpower = self.acflexload_l2measure_start_address + 8;
        self.acflexload_l2measure_cosphi = self.acflexload_l2measure_start_address + 10;
        self.acflexload_l2measure_daypeakpower = self.acflexload_l2measure_start_address + 12;
        self.acflexload_l2measure_previousdaypeakpower = self.acflexload_l2measure_start_address + 14;
        self.acflexload_l2measure_dayminactivepower = self.acflexload_l2measure_start_address + 16;
        self.acflexload_l2measure_previousdayminactivepower = self.acflexload_l2measure_start_address + 18;
        self.acflexload_l2measure_daymaxactivepower = self.acflexload_l2measure_start_address + 20;
        self.acflexload_l2measure_previousdaymaxactivepower = self.acflexload_l2measure_start_address + 22;
        self.acflexload_l2measure_dayconsumedenergy = self.acflexload_l2measure_start_address + 28;
        self.acflexload_l2measure_previousdayconsumedenergy = self.acflexload_l2measure_start_address + 30;
        self.acflexload_l2measure_resetableconsumedenergy = self.acflexload_l2measure_start_address + 32;
        self.acflexload_l2measure_totalconsumedenergy = self.acflexload_l2measure_start_address + 36;
        self.acflexload_l2measure_dayproducedenergy = self.acflexload_l2measure_start_address + 40;
        self.acflexload_l2measure_previousdayproducedenergy = self.acflexload_l2measure_start_address + 42;
        self.acflexload_l2measure_resetableproducedenergy = self.acflexload_l2measure_start_address + 44;
        self.acflexload_l2measure_totalproducedenergy = self.acflexload_l2measure_start_address + 48;

        # Object L3Measure Modbus Address
        self.acflexload_l3measure_start_address = 900;
        self.acflexload_l3measure_phasevoltage = self.acflexload_l3measure_start_address + 0;
        self.acflexload_l3measure_current = self.acflexload_l3measure_start_address + 2;
        self.acflexload_l3measure_activepower = self.acflexload_l3measure_start_address + 4;
        self.acflexload_l3measure_reactivepower = self.acflexload_l3measure_start_address + 6;
        self.acflexload_l3measure_apparentpower = self.acflexload_l3measure_start_address + 8;
        self.acflexload_l3measure_cosphi = self.acflexload_l3measure_start_address + 10;
        self.acflexload_l3measure_daypeakpower = self.acflexload_l3measure_start_address + 12;
        self.acflexload_l3measure_previousdaypeakpower = self.acflexload_l3measure_start_address + 14;
        self.acflexload_l3measure_dayminactivepower = self.acflexload_l3measure_start_address + 16;
        self.acflexload_l3measure_previousdayminactivepower = self.acflexload_l3measure_start_address + 18;
        self.acflexload_l3measure_daymaxactivepower = self.acflexload_l3measure_start_address + 20;
        self.acflexload_l3measure_previousdaymaxactivepower = self.acflexload_l3measure_start_address + 22;
        self.acflexload_l3measure_dayconsumedenergy = self.acflexload_l3measure_start_address + 28;
        self.acflexload_l3measure_previousdayconsumedenergy = self.acflexload_l3measure_start_address + 30;
        self.acflexload_l3measure_resetableconsumedenergy = self.acflexload_l3measure_start_address + 32;
        self.acflexload_l3measure_totalconsumedenergy = self.acflexload_l3measure_start_address + 36;
        self.acflexload_l3measure_dayproducedenergy = self.acflexload_l3measure_start_address + 40;
        self.acflexload_l3measure_previousdayproducedenergy = self.acflexload_l3measure_start_address + 42;
        self.acflexload_l3measure_resetableproducedenergy = self.acflexload_l3measure_start_address + 44;
        self.acflexload_l3measure_totalproducedenergy = self.acflexload_l3measure_start_address + 48;

        # Object L1FlexLoadContrRelay Modbus Address
        self.acflexload_l1flexloadcontrrelay_start_address = 1200;
        self.acflexload_l1flexloadcontrrelay_isconnected = self.acflexload_l1flexloadcontrrelay_start_address + 0;
        self.acflexload_l1flexloadcontrrelay_currentrelayposition = self.acflexload_l1flexloadcontrrelay_start_address + 1;
        self.acflexload_l1flexloadcontrrelay_errors = self.acflexload_l1flexloadcontrrelay_start_address + 3;
        self.acflexload_l1flexloadcontrrelay_operatingmodeselect = self.acflexload_l1flexloadcontrrelay_start_address + 7;
        self.acflexload_l1flexloadcontrrelay_automodeselect = self.acflexload_l1flexloadcontrrelay_start_address + 9;
        self.acflexload_l1flexloadcontrrelay_safestateselect = self.acflexload_l1flexloadcontrrelay_start_address + 11;
        self.acflexload_l1flexloadcontrrelay_presetbatvoltactvth = self.acflexload_l1flexloadcontrrelay_start_address + 13;
        self.acflexload_l1flexloadcontrrelay_presetbatvoltdeactvth = self.acflexload_l1flexloadcontrrelay_start_address + 15;
        self.acflexload_l1flexloadcontrrelay_presetbatsocactth = self.acflexload_l1flexloadcontrrelay_start_address + 17;
        self.acflexload_l1flexloadcontrrelay_presetbatsocdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 19;
        self.acflexload_l1flexloadcontrrelay_presetbattempactth = self.acflexload_l1flexloadcontrrelay_start_address + 21;
        self.acflexload_l1flexloadcontrrelay_presetbattempdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 23;
        self.acflexload_l1flexloadcontrrelay_presetbatstateselect = self.acflexload_l1flexloadcontrrelay_start_address + 25;
        self.acflexload_l1flexloadcontrrelay_presetpacselect = self.acflexload_l1flexloadcontrrelay_start_address + 27;
        self.acflexload_l1flexloadcontrrelay_presetpacpowactth = self.acflexload_l1flexloadcontrrelay_start_address + 29;
        self.acflexload_l1flexloadcontrrelay_presetpacpowdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 31;
        self.acflexload_l1flexloadcontrrelay_presetsolarexcessongridpowactth = self.acflexload_l1flexloadcontrrelay_start_address + 33;
        self.acflexload_l1flexloadcontrrelay_presetsolarexcessongridpowdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 35;
        self.acflexload_l1flexloadcontrrelay_presetsolarexcessoffgridpowactth = self.acflexload_l1flexloadcontrrelay_start_address + 37;
        self.acflexload_l1flexloadcontrrelay_presetsolarexcessoffgridpowdeactth = self.acflexload_l1flexloadcontrrelay_start_address + 39;
        self.acflexload_l1flexloadcontrrelay_presetcmdentryidx = self.acflexload_l1flexloadcontrrelay_start_address + 41;
        self.acflexload_l1flexloadcontrrelay_preseterrorwarningselect = self.acflexload_l1flexloadcontrrelay_start_address + 43;
        self.acflexload_l1flexloadcontrrelay_presetonsourceselect = self.acflexload_l1flexloadcontrrelay_start_address + 45;

        # Object L2FlexLoadContrRelay Modbus Address
        self.acflexload_l2flexloadcontrrelay_start_address = 1500;
        self.acflexload_l2flexloadcontrrelay_isconnected = self.acflexload_l2flexloadcontrrelay_start_address + 0;
        self.acflexload_l2flexloadcontrrelay_currentrelayposition = self.acflexload_l2flexloadcontrrelay_start_address + 1;
        self.acflexload_l2flexloadcontrrelay_errors = self.acflexload_l2flexloadcontrrelay_start_address + 3;
        self.acflexload_l2flexloadcontrrelay_operatingmodeselect = self.acflexload_l2flexloadcontrrelay_start_address + 7;
        self.acflexload_l2flexloadcontrrelay_automodeselect = self.acflexload_l2flexloadcontrrelay_start_address + 9;
        self.acflexload_l2flexloadcontrrelay_safestateselect = self.acflexload_l2flexloadcontrrelay_start_address + 11;
        self.acflexload_l2flexloadcontrrelay_presetbatvoltactvth = self.acflexload_l2flexloadcontrrelay_start_address + 13;
        self.acflexload_l2flexloadcontrrelay_presetbatvoltdeactvth = self.acflexload_l2flexloadcontrrelay_start_address + 15;
        self.acflexload_l2flexloadcontrrelay_presetbatsocactth = self.acflexload_l2flexloadcontrrelay_start_address + 17;
        self.acflexload_l2flexloadcontrrelay_presetbatsocdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 19;
        self.acflexload_l2flexloadcontrrelay_presetbattempactth = self.acflexload_l2flexloadcontrrelay_start_address + 21;
        self.acflexload_l2flexloadcontrrelay_presetbattempdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 23;
        self.acflexload_l2flexloadcontrrelay_presetbatstateselect = self.acflexload_l2flexloadcontrrelay_start_address + 25;
        self.acflexload_l2flexloadcontrrelay_presetpacselect = self.acflexload_l2flexloadcontrrelay_start_address + 27;
        self.acflexload_l2flexloadcontrrelay_presetpacpowactth = self.acflexload_l2flexloadcontrrelay_start_address + 29;
        self.acflexload_l2flexloadcontrrelay_presetpacpowdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 31;
        self.acflexload_l2flexloadcontrrelay_presetsolarexcessongridpowactth = self.acflexload_l2flexloadcontrrelay_start_address + 33;
        self.acflexload_l2flexloadcontrrelay_presetsolarexcessongridpowdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 35;
        self.acflexload_l2flexloadcontrrelay_presetsolarexcessoffgridpowactth = self.acflexload_l2flexloadcontrrelay_start_address + 37;
        self.acflexload_l2flexloadcontrrelay_presetsolarexcessoffgridpowdeactth = self.acflexload_l2flexloadcontrrelay_start_address + 39;
        self.acflexload_l2flexloadcontrrelay_presetcmdentryidx = self.acflexload_l2flexloadcontrrelay_start_address + 41;
        self.acflexload_l2flexloadcontrrelay_preseterrorwarningselect = self.acflexload_l2flexloadcontrrelay_start_address + 43;
        self.acflexload_l2flexloadcontrrelay_presetonsourceselect = self.acflexload_l2flexloadcontrrelay_start_address + 45;

        # Object L3FlexLoadContrRelay Modbus Address
        self.acflexload_l3flexloadcontrrelay_start_address = 1800;
        self.acflexload_l3flexloadcontrrelay_isconnected = self.acflexload_l3flexloadcontrrelay_start_address + 0;
        self.acflexload_l3flexloadcontrrelay_currentrelayposition = self.acflexload_l3flexloadcontrrelay_start_address + 1;
        self.acflexload_l3flexloadcontrrelay_errors = self.acflexload_l3flexloadcontrrelay_start_address + 3;
        self.acflexload_l3flexloadcontrrelay_operatingmodeselect = self.acflexload_l3flexloadcontrrelay_start_address + 7;
        self.acflexload_l3flexloadcontrrelay_automodeselect = self.acflexload_l3flexloadcontrrelay_start_address + 9;
        self.acflexload_l3flexloadcontrrelay_safestateselect = self.acflexload_l3flexloadcontrrelay_start_address + 11;
        self.acflexload_l3flexloadcontrrelay_presetbatvoltactvth = self.acflexload_l3flexloadcontrrelay_start_address + 13;
        self.acflexload_l3flexloadcontrrelay_presetbatvoltdeactvth = self.acflexload_l3flexloadcontrrelay_start_address + 15;
        self.acflexload_l3flexloadcontrrelay_presetbatsocactth = self.acflexload_l3flexloadcontrrelay_start_address + 17;
        self.acflexload_l3flexloadcontrrelay_presetbatsocdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 19;
        self.acflexload_l3flexloadcontrrelay_presetbattempactth = self.acflexload_l3flexloadcontrrelay_start_address + 21;
        self.acflexload_l3flexloadcontrrelay_presetbattempdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 23;
        self.acflexload_l3flexloadcontrrelay_presetbatstateselect = self.acflexload_l3flexloadcontrrelay_start_address + 25;
        self.acflexload_l3flexloadcontrrelay_presetpacselect = self.acflexload_l3flexloadcontrrelay_start_address + 27;
        self.acflexload_l3flexloadcontrrelay_presetpacpowactth = self.acflexload_l3flexloadcontrrelay_start_address + 29;
        self.acflexload_l3flexloadcontrrelay_presetpacpowdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 31;
        self.acflexload_l3flexloadcontrrelay_presetsolarexcessongridpowactth = self.acflexload_l3flexloadcontrrelay_start_address + 33;
        self.acflexload_l3flexloadcontrrelay_presetsolarexcessongridpowdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 35;
        self.acflexload_l3flexloadcontrrelay_presetsolarexcessoffgridpowactth = self.acflexload_l3flexloadcontrrelay_start_address + 37;
        self.acflexload_l3flexloadcontrrelay_presetsolarexcessoffgridpowdeactth = self.acflexload_l3flexloadcontrrelay_start_address + 39;
        self.acflexload_l3flexloadcontrrelay_presetcmdentryidx = self.acflexload_l3flexloadcontrrelay_start_address + 41;
        self.acflexload_l3flexloadcontrrelay_preseterrorwarningselect = self.acflexload_l3flexloadcontrrelay_start_address + 43;
        self.acflexload_l3flexloadcontrrelay_presetonsourceselect = self.acflexload_l3flexloadcontrrelay_start_address + 45;

        # Object L1FlexLoadTimeCtrl Modbus Address
        self.acflexload_l1flexloadtimectrl_start_address = 2100;
        self.acflexload_l1flexloadtimectrl_timecontrolledmodeselect = self.acflexload_l1flexloadtimectrl_start_address + 0;
        self.acflexload_l1flexloadtimectrl_actmindelay = self.acflexload_l1flexloadtimectrl_start_address + 2;
        self.acflexload_l1flexloadtimectrl_deactmindelay = self.acflexload_l1flexloadtimectrl_start_address + 4;
        self.acflexload_l1flexloadtimectrl_actmintime = self.acflexload_l1flexloadtimectrl_start_address + 6;
        self.acflexload_l1flexloadtimectrl_deactmintime = self.acflexload_l1flexloadtimectrl_start_address + 8;
        self.acflexload_l1flexloadtimectrl_actmaxtime = self.acflexload_l1flexloadtimectrl_start_address + 10;
        self.acflexload_l1flexloadtimectrl_acthourallow1 = self.acflexload_l1flexloadtimectrl_start_address + 12;
        self.acflexload_l1flexloadtimectrl_acthourallow2 = self.acflexload_l1flexloadtimectrl_start_address + 14;
        self.acflexload_l1flexloadtimectrl_actweekdaysallow = self.acflexload_l1flexloadtimectrl_start_address + 16;
        self.acflexload_l1flexloadtimectrl_startingdate = self.acflexload_l1flexloadtimectrl_start_address + 18;
        self.acflexload_l1flexloadtimectrl_startingtimesec = self.acflexload_l1flexloadtimectrl_start_address + 20;
        self.acflexload_l1flexloadtimectrl_endingtimesec = self.acflexload_l1flexloadtimectrl_start_address + 22;
        self.acflexload_l1flexloadtimectrl_selectedweekday = self.acflexload_l1flexloadtimectrl_start_address + 24;
        self.acflexload_l1flexloadtimectrl_recurrenceweeks = self.acflexload_l1flexloadtimectrl_start_address + 26;
        self.acflexload_l1flexloadtimectrl_rangeofrecurrenceselect = self.acflexload_l1flexloadtimectrl_start_address + 28;
        self.acflexload_l1flexloadtimectrl_endingdate = self.acflexload_l1flexloadtimectrl_start_address + 30;
        self.acflexload_l1flexloadtimectrl_nbrofoccurrences = self.acflexload_l1flexloadtimectrl_start_address + 32;
        self.acflexload_l1flexloadtimectrl_resettimecontrolled = self.acflexload_l1flexloadtimectrl_start_address + 34;

        # Object L2FlexLoadTimeCtrl Modbus Address
        self.acflexload_l2flexloadtimectrl_start_address = 2400;
        self.acflexload_l2flexloadtimectrl_timecontrolledmodeselect = self.acflexload_l2flexloadtimectrl_start_address + 0;
        self.acflexload_l2flexloadtimectrl_actmindelay = self.acflexload_l2flexloadtimectrl_start_address + 2;
        self.acflexload_l2flexloadtimectrl_deactmindelay = self.acflexload_l2flexloadtimectrl_start_address + 4;
        self.acflexload_l2flexloadtimectrl_actmintime = self.acflexload_l2flexloadtimectrl_start_address + 6;
        self.acflexload_l2flexloadtimectrl_deactmintime = self.acflexload_l2flexloadtimectrl_start_address + 8;
        self.acflexload_l2flexloadtimectrl_actmaxtime = self.acflexload_l2flexloadtimectrl_start_address + 10;
        self.acflexload_l2flexloadtimectrl_acthourallow1 = self.acflexload_l2flexloadtimectrl_start_address + 12;
        self.acflexload_l2flexloadtimectrl_acthourallow2 = self.acflexload_l2flexloadtimectrl_start_address + 14;
        self.acflexload_l2flexloadtimectrl_actweekdaysallow = self.acflexload_l2flexloadtimectrl_start_address + 16;
        self.acflexload_l2flexloadtimectrl_startingdate = self.acflexload_l2flexloadtimectrl_start_address + 18;
        self.acflexload_l2flexloadtimectrl_startingtimesec = self.acflexload_l2flexloadtimectrl_start_address + 20;
        self.acflexload_l2flexloadtimectrl_endingtimesec = self.acflexload_l2flexloadtimectrl_start_address + 22;
        self.acflexload_l2flexloadtimectrl_selectedweekday = self.acflexload_l2flexloadtimectrl_start_address + 24;
        self.acflexload_l2flexloadtimectrl_recurrenceweeks = self.acflexload_l2flexloadtimectrl_start_address + 26;
        self.acflexload_l2flexloadtimectrl_rangeofrecurrenceselect = self.acflexload_l2flexloadtimectrl_start_address + 28;
        self.acflexload_l2flexloadtimectrl_endingdate = self.acflexload_l2flexloadtimectrl_start_address + 30;
        self.acflexload_l2flexloadtimectrl_nbrofoccurrences = self.acflexload_l2flexloadtimectrl_start_address + 32;
        self.acflexload_l2flexloadtimectrl_resettimecontrolled = self.acflexload_l2flexloadtimectrl_start_address + 34;

        # Object L3FlexLoadTimeCtrl Modbus Address
        self.acflexload_l3flexloadtimectrl_start_address = 2700;
        self.acflexload_l3flexloadtimectrl_timecontrolledmodeselect = self.acflexload_l3flexloadtimectrl_start_address + 0;
        self.acflexload_l3flexloadtimectrl_actmindelay = self.acflexload_l3flexloadtimectrl_start_address + 2;
        self.acflexload_l3flexloadtimectrl_deactmindelay = self.acflexload_l3flexloadtimectrl_start_address + 4;
        self.acflexload_l3flexloadtimectrl_actmintime = self.acflexload_l3flexloadtimectrl_start_address + 6;
        self.acflexload_l3flexloadtimectrl_deactmintime = self.acflexload_l3flexloadtimectrl_start_address + 8;
        self.acflexload_l3flexloadtimectrl_actmaxtime = self.acflexload_l3flexloadtimectrl_start_address + 10;
        self.acflexload_l3flexloadtimectrl_acthourallow1 = self.acflexload_l3flexloadtimectrl_start_address + 12;
        self.acflexload_l3flexloadtimectrl_acthourallow2 = self.acflexload_l3flexloadtimectrl_start_address + 14;
        self.acflexload_l3flexloadtimectrl_actweekdaysallow = self.acflexload_l3flexloadtimectrl_start_address + 16;
        self.acflexload_l3flexloadtimectrl_startingdate = self.acflexload_l3flexloadtimectrl_start_address + 18;
        self.acflexload_l3flexloadtimectrl_startingtimesec = self.acflexload_l3flexloadtimectrl_start_address + 20;
        self.acflexload_l3flexloadtimectrl_endingtimesec = self.acflexload_l3flexloadtimectrl_start_address + 22;
        self.acflexload_l3flexloadtimectrl_selectedweekday = self.acflexload_l3flexloadtimectrl_start_address + 24;
        self.acflexload_l3flexloadtimectrl_recurrenceweeks = self.acflexload_l3flexloadtimectrl_start_address + 26;
        self.acflexload_l3flexloadtimectrl_rangeofrecurrenceselect = self.acflexload_l3flexloadtimectrl_start_address + 28;
        self.acflexload_l3flexloadtimectrl_endingdate = self.acflexload_l3flexloadtimectrl_start_address + 30;
        self.acflexload_l3flexloadtimectrl_nbrofoccurrences = self.acflexload_l3flexloadtimectrl_start_address + 32;
        self.acflexload_l3flexloadtimectrl_resettimecontrolled = self.acflexload_l3flexloadtimectrl_start_address + 34;

        # Object FlexLoad Modbus Address
        self.acflexload_flexload_start_address = 3000;
        self.acflexload_flexload_phaseexistance = self.acflexload_flexload_start_address + 0;
        self.acflexload_flexload_allowindividualphaseoperation = self.acflexload_flexload_start_address + 2;


        # Group Next3 Modbus Address
        # Object IdCardConverter Modbus Address
        self.next3_idcardconverter_start_address = 0;
        self.next3_idcardconverter_serialnumber = self.next3_idcardconverter_start_address + 4;
        self.next3_idcardconverter_softwarepackageversion = self.next3_idcardconverter_start_address + 14;
        self.next3_idcardconverter_softwarerevisionsha1 = self.next3_idcardconverter_start_address + 18;
        self.next3_idcardconverter_objectmodelversion = self.next3_idcardconverter_start_address + 30;

        # Object IdCardTransfer Modbus Address
        self.next3_idcardtransfer_start_address = 300;
        self.next3_idcardtransfer_serialnumber = self.next3_idcardtransfer_start_address + 4;
        self.next3_idcardtransfer_softwarepackageversion = self.next3_idcardtransfer_start_address + 14;
        self.next3_idcardtransfer_softwarerevisionsha1 = self.next3_idcardtransfer_start_address + 18;
        self.next3_idcardtransfer_objectmodelversion = self.next3_idcardtransfer_start_address + 30;

        # Object BaseAppConverter Modbus Address
        self.next3_baseappconverter_start_address = 600;
        self.next3_baseappconverter_warnings = self.next3_baseappconverter_start_address + 5;

        # Object BaseAppTransfer Modbus Address
        self.next3_baseapptransfer_start_address = 900;
        self.next3_baseapptransfer_warnings = self.next3_baseapptransfer_start_address + 5;

        # Object CanNodeConverter Modbus Address
        self.next3_cannodeconverter_start_address = 1800;
        self.next3_cannodeconverter_status = self.next3_cannodeconverter_start_address + 2;
        self.next3_cannodeconverter_txerrorcounter = self.next3_cannodeconverter_start_address + 4;
        self.next3_cannodeconverter_rxerrorcounter = self.next3_cannodeconverter_start_address + 6;
        self.next3_cannodeconverter_busterminationset = self.next3_cannodeconverter_start_address + 8;

        # Object CanNodeTransfer Modbus Address
        self.next3_cannodetransfer_start_address = 2100;
        self.next3_cannodetransfer_status = self.next3_cannodetransfer_start_address + 2;
        self.next3_cannodetransfer_txerrorcounter = self.next3_cannodetransfer_start_address + 4;
        self.next3_cannodetransfer_rxerrorcounter = self.next3_cannodetransfer_start_address + 6;
        self.next3_cannodetransfer_busterminationset = self.next3_cannodetransfer_start_address + 8;

        # Object Device Modbus Address
        self.next3_device_start_address = 4200;
        self.next3_device_blinkingstate = self.next3_device_start_address + 0;
        self.next3_device_totalfunctioningtimesec = self.next3_device_start_address + 5;

        # Object Next3Converter Modbus Address
        self.next3_next3converter_start_address = 5100;
        self.next3_next3converter_status = self.next3_next3converter_start_address + 0;
        self.next3_next3converter_errors = self.next3_next3converter_start_address + 2;
        self.next3_next3converter_fan1speed = self.next3_next3converter_start_address + 4;
        self.next3_next3converter_fan2speed = self.next3_next3converter_start_address + 6;
        self.next3_next3converter_fan3speed = self.next3_next3converter_start_address + 8;
        self.next3_next3converter_fan4speed = self.next3_next3converter_start_address + 10;
        self.next3_next3converter_fan5speed = self.next3_next3converter_start_address + 12;
        self.next3_next3converter_externalpowersupplycurrent = self.next3_next3converter_start_address + 14;
        self.next3_next3converter_powersupplyvoltage = self.next3_next3converter_start_address + 16;
        self.next3_next3converter_warningnoisedadcchannels = self.next3_next3converter_start_address + 56;
        self.next3_next3converter_errornoisedadcchannels = self.next3_next3converter_start_address + 58;
        self.next3_next3converter_selectedadcchannel = self.next3_next3converter_start_address + 60;
        self.next3_next3converter_selectedadcchannelnoise = self.next3_next3converter_start_address + 62;

        # Object SolarCommonDevice Modbus Address
        self.next3_solarcommondevice_start_address = 5700;
        self.next3_solarcommondevice_turnon = self.next3_solarcommondevice_start_address + 0;
        self.next3_solarcommondevice_turnoff = self.next3_solarcommondevice_start_address + 1;
        self.next3_solarcommondevice_onoffstate = self.next3_solarcommondevice_start_address + 2;
        self.next3_solarcommondevice_enabledepolarization = self.next3_solarcommondevice_start_address + 3;
        self.next3_solarcommondevice_disabledepolarization = self.next3_solarcommondevice_start_address + 4;
        self.next3_solarcommondevice_power = self.next3_solarcommondevice_start_address + 5;
        self.next3_solarcommondevice_previousdayenergy = self.next3_solarcommondevice_start_address + 7;
        self.next3_solarcommondevice_powerlimit = self.next3_solarcommondevice_start_address + 9;
        self.next3_solarcommondevice_dayenergy = self.next3_solarcommondevice_start_address + 11;
        self.next3_solarcommondevice_resetableenergy = self.next3_solarcommondevice_start_address + 15;
        self.next3_solarcommondevice_totalenergy = self.next3_solarcommondevice_start_address + 19;

        # Object SolarCommon1 Modbus Address
        self.next3_solarcommon1_start_address = 6000;
        self.next3_solarcommon1_turnon = self.next3_solarcommon1_start_address + 0;
        self.next3_solarcommon1_turnoff = self.next3_solarcommon1_start_address + 1;
        self.next3_solarcommon1_onoffstate = self.next3_solarcommon1_start_address + 2;
        self.next3_solarcommon1_enabledepolarization = self.next3_solarcommon1_start_address + 3;
        self.next3_solarcommon1_disabledepolarization = self.next3_solarcommon1_start_address + 4;
        self.next3_solarcommon1_power = self.next3_solarcommon1_start_address + 5;
        self.next3_solarcommon1_previousdayenergy = self.next3_solarcommon1_start_address + 7;
        self.next3_solarcommon1_powerlimit = self.next3_solarcommon1_start_address + 9;
        self.next3_solarcommon1_dayenergy = self.next3_solarcommon1_start_address + 11;
        self.next3_solarcommon1_resetableenergy = self.next3_solarcommon1_start_address + 15;
        self.next3_solarcommon1_totalenergy = self.next3_solarcommon1_start_address + 19;

        # Object SolarCommon2 Modbus Address
        self.next3_solarcommon2_start_address = 6300;
        self.next3_solarcommon2_turnon = self.next3_solarcommon2_start_address + 0;
        self.next3_solarcommon2_turnoff = self.next3_solarcommon2_start_address + 1;
        self.next3_solarcommon2_onoffstate = self.next3_solarcommon2_start_address + 2;
        self.next3_solarcommon2_enabledepolarization = self.next3_solarcommon2_start_address + 3;
        self.next3_solarcommon2_disabledepolarization = self.next3_solarcommon2_start_address + 4;
        self.next3_solarcommon2_power = self.next3_solarcommon2_start_address + 5;
        self.next3_solarcommon2_previousdayenergy = self.next3_solarcommon2_start_address + 7;
        self.next3_solarcommon2_powerlimit = self.next3_solarcommon2_start_address + 9;
        self.next3_solarcommon2_dayenergy = self.next3_solarcommon2_start_address + 11;
        self.next3_solarcommon2_resetableenergy = self.next3_solarcommon2_start_address + 15;
        self.next3_solarcommon2_totalenergy = self.next3_solarcommon2_start_address + 19;

        # Object SolarGroupDevice Modbus Address
        self.next3_solargroupdevice_start_address = 6600;
        self.next3_solargroupdevice_nbr = self.next3_solargroupdevice_start_address + 0;
        self.next3_solargroupdevice_status = self.next3_solargroupdevice_start_address + 2;

        # Object Solar1 Modbus Address
        self.next3_solar1_start_address = 6900;
        self.next3_solar1_voltage = self.next3_solar1_start_address + 0;
        self.next3_solar1_current = self.next3_solar1_start_address + 2;
        self.next3_solar1_daysunshine = self.next3_solar1_start_address + 4;
        self.next3_solar1_previousdaysunshine = self.next3_solar1_start_address + 6;
        self.next3_solar1_status = self.next3_solar1_start_address + 8;
        self.next3_solar1_causeoferror = self.next3_solar1_start_address + 10;
        self.next3_solar1_errors = self.next3_solar1_start_address + 12;
        self.next3_solar1_warnings = self.next3_solar1_start_address + 14;
        self.next3_solar1_depolarizationstate = self.next3_solar1_start_address + 16;
        self.next3_solar1_limitationstate = self.next3_solar1_start_address + 18;

        # Object Solar2 Modbus Address
        self.next3_solar2_start_address = 7200;
        self.next3_solar2_voltage = self.next3_solar2_start_address + 0;
        self.next3_solar2_current = self.next3_solar2_start_address + 2;
        self.next3_solar2_daysunshine = self.next3_solar2_start_address + 4;
        self.next3_solar2_previousdaysunshine = self.next3_solar2_start_address + 6;
        self.next3_solar2_status = self.next3_solar2_start_address + 8;
        self.next3_solar2_causeoferror = self.next3_solar2_start_address + 10;
        self.next3_solar2_errors = self.next3_solar2_start_address + 12;
        self.next3_solar2_warnings = self.next3_solar2_start_address + 14;
        self.next3_solar2_depolarizationstate = self.next3_solar2_start_address + 16;
        self.next3_solar2_limitationstate = self.next3_solar2_start_address + 18;

        # Object AlgoMppt1 Modbus Address
        self.next3_algomppt1_start_address = 7500;
        self.next3_algomppt1_algoselected = self.next3_algomppt1_start_address + 0;
        self.next3_algomppt1_fvvoltagesetpoint = self.next3_algomppt1_start_address + 2;
        self.next3_algomppt1_lsfcheckforglobalmpp = self.next3_algomppt1_start_address + 4;
        self.next3_algomppt1_lsftimeperiodforglobalmppcheck = self.next3_algomppt1_start_address + 5;
        self.next3_algomppt1_focvrvoltageratio = self.next3_algomppt1_start_address + 7;
        self.next3_algomppt1_focvrtimeperiodforvoccheck = self.next3_algomppt1_start_address + 9;

        # Object AlgoMppt2 Modbus Address
        self.next3_algomppt2_start_address = 7800;
        self.next3_algomppt2_algoselected = self.next3_algomppt2_start_address + 0;
        self.next3_algomppt2_fvvoltagesetpoint = self.next3_algomppt2_start_address + 2;
        self.next3_algomppt2_lsfcheckforglobalmpp = self.next3_algomppt2_start_address + 4;
        self.next3_algomppt2_lsftimeperiodforglobalmppcheck = self.next3_algomppt2_start_address + 5;
        self.next3_algomppt2_focvrvoltageratio = self.next3_algomppt2_start_address + 7;
        self.next3_algomppt2_focvrtimeperiodforvoccheck = self.next3_algomppt2_start_address + 9;

        # Object RelayAux1 Modbus Address
        self.next3_relayaux1_start_address = 8100;
        self.next3_relayaux1_isconnected = self.next3_relayaux1_start_address + 0;
        self.next3_relayaux1_currentrelayposition = self.next3_relayaux1_start_address + 1;
        self.next3_relayaux1_errors = self.next3_relayaux1_start_address + 3;
        self.next3_relayaux1_operatingmodeselect = self.next3_relayaux1_start_address + 7;
        self.next3_relayaux1_automodeselect = self.next3_relayaux1_start_address + 9;
        self.next3_relayaux1_safestateselect = self.next3_relayaux1_start_address + 11;
        self.next3_relayaux1_presetbatvoltactvth = self.next3_relayaux1_start_address + 13;
        self.next3_relayaux1_presetbatvoltdeactvth = self.next3_relayaux1_start_address + 15;
        self.next3_relayaux1_presetbatsocactth = self.next3_relayaux1_start_address + 17;
        self.next3_relayaux1_presetbatsocdeactth = self.next3_relayaux1_start_address + 19;
        self.next3_relayaux1_presetbattempactth = self.next3_relayaux1_start_address + 21;
        self.next3_relayaux1_presetbattempdeactth = self.next3_relayaux1_start_address + 23;
        self.next3_relayaux1_presetbatstateselect = self.next3_relayaux1_start_address + 25;
        self.next3_relayaux1_presetpacselect = self.next3_relayaux1_start_address + 27;
        self.next3_relayaux1_presetpacpowactth = self.next3_relayaux1_start_address + 29;
        self.next3_relayaux1_presetpacpowdeactth = self.next3_relayaux1_start_address + 31;
        self.next3_relayaux1_presetsolarexcessongridpowactth = self.next3_relayaux1_start_address + 33;
        self.next3_relayaux1_presetsolarexcessongridpowdeactth = self.next3_relayaux1_start_address + 35;
        self.next3_relayaux1_presetsolarexcessoffgridpowactth = self.next3_relayaux1_start_address + 37;
        self.next3_relayaux1_presetsolarexcessoffgridpowdeactth = self.next3_relayaux1_start_address + 39;
        self.next3_relayaux1_presetcmdentryidx = self.next3_relayaux1_start_address + 41;
        self.next3_relayaux1_preseterrorwarningselect = self.next3_relayaux1_start_address + 43;
        self.next3_relayaux1_presetonsourceselect = self.next3_relayaux1_start_address + 45;

        # Object RelayAux2 Modbus Address
        self.next3_relayaux2_start_address = 8400;
        self.next3_relayaux2_isconnected = self.next3_relayaux2_start_address + 0;
        self.next3_relayaux2_currentrelayposition = self.next3_relayaux2_start_address + 1;
        self.next3_relayaux2_errors = self.next3_relayaux2_start_address + 3;
        self.next3_relayaux2_operatingmodeselect = self.next3_relayaux2_start_address + 7;
        self.next3_relayaux2_automodeselect = self.next3_relayaux2_start_address + 9;
        self.next3_relayaux2_safestateselect = self.next3_relayaux2_start_address + 11;
        self.next3_relayaux2_presetbatvoltactvth = self.next3_relayaux2_start_address + 13;
        self.next3_relayaux2_presetbatvoltdeactvth = self.next3_relayaux2_start_address + 15;
        self.next3_relayaux2_presetbatsocactth = self.next3_relayaux2_start_address + 17;
        self.next3_relayaux2_presetbatsocdeactth = self.next3_relayaux2_start_address + 19;
        self.next3_relayaux2_presetbattempactth = self.next3_relayaux2_start_address + 21;
        self.next3_relayaux2_presetbattempdeactth = self.next3_relayaux2_start_address + 23;
        self.next3_relayaux2_presetbatstateselect = self.next3_relayaux2_start_address + 25;
        self.next3_relayaux2_presetpacselect = self.next3_relayaux2_start_address + 27;
        self.next3_relayaux2_presetpacpowactth = self.next3_relayaux2_start_address + 29;
        self.next3_relayaux2_presetpacpowdeactth = self.next3_relayaux2_start_address + 31;
        self.next3_relayaux2_presetsolarexcessongridpowactth = self.next3_relayaux2_start_address + 33;
        self.next3_relayaux2_presetsolarexcessongridpowdeactth = self.next3_relayaux2_start_address + 35;
        self.next3_relayaux2_presetsolarexcessoffgridpowactth = self.next3_relayaux2_start_address + 37;
        self.next3_relayaux2_presetsolarexcessoffgridpowdeactth = self.next3_relayaux2_start_address + 39;
        self.next3_relayaux2_presetcmdentryidx = self.next3_relayaux2_start_address + 41;
        self.next3_relayaux2_preseterrorwarningselect = self.next3_relayaux2_start_address + 43;
        self.next3_relayaux2_presetonsourceselect = self.next3_relayaux2_start_address + 45;

        # Object RelayAux1TimeCtrl Modbus Address
        self.next3_relayaux1timectrl_start_address = 8700;
        self.next3_relayaux1timectrl_timecontrolledmodeselect = self.next3_relayaux1timectrl_start_address + 0;
        self.next3_relayaux1timectrl_actmindelay = self.next3_relayaux1timectrl_start_address + 2;
        self.next3_relayaux1timectrl_deactmindelay = self.next3_relayaux1timectrl_start_address + 4;
        self.next3_relayaux1timectrl_actmintime = self.next3_relayaux1timectrl_start_address + 6;
        self.next3_relayaux1timectrl_deactmintime = self.next3_relayaux1timectrl_start_address + 8;
        self.next3_relayaux1timectrl_actmaxtime = self.next3_relayaux1timectrl_start_address + 10;
        self.next3_relayaux1timectrl_acthourallow1 = self.next3_relayaux1timectrl_start_address + 12;
        self.next3_relayaux1timectrl_acthourallow2 = self.next3_relayaux1timectrl_start_address + 14;
        self.next3_relayaux1timectrl_actweekdaysallow = self.next3_relayaux1timectrl_start_address + 16;
        self.next3_relayaux1timectrl_startingdate = self.next3_relayaux1timectrl_start_address + 18;
        self.next3_relayaux1timectrl_startingtimesec = self.next3_relayaux1timectrl_start_address + 20;
        self.next3_relayaux1timectrl_endingtimesec = self.next3_relayaux1timectrl_start_address + 22;
        self.next3_relayaux1timectrl_selectedweekday = self.next3_relayaux1timectrl_start_address + 24;
        self.next3_relayaux1timectrl_recurrenceweeks = self.next3_relayaux1timectrl_start_address + 26;
        self.next3_relayaux1timectrl_rangeofrecurrenceselect = self.next3_relayaux1timectrl_start_address + 28;
        self.next3_relayaux1timectrl_endingdate = self.next3_relayaux1timectrl_start_address + 30;
        self.next3_relayaux1timectrl_nbrofoccurrences = self.next3_relayaux1timectrl_start_address + 32;
        self.next3_relayaux1timectrl_resettimecontrolled = self.next3_relayaux1timectrl_start_address + 34;

        # Object RelayAux2TimeCtrl Modbus Address
        self.next3_relayaux2timectrl_start_address = 9000;
        self.next3_relayaux2timectrl_timecontrolledmodeselect = self.next3_relayaux2timectrl_start_address + 0;
        self.next3_relayaux2timectrl_actmindelay = self.next3_relayaux2timectrl_start_address + 2;
        self.next3_relayaux2timectrl_deactmindelay = self.next3_relayaux2timectrl_start_address + 4;
        self.next3_relayaux2timectrl_actmintime = self.next3_relayaux2timectrl_start_address + 6;
        self.next3_relayaux2timectrl_deactmintime = self.next3_relayaux2timectrl_start_address + 8;
        self.next3_relayaux2timectrl_actmaxtime = self.next3_relayaux2timectrl_start_address + 10;
        self.next3_relayaux2timectrl_acthourallow1 = self.next3_relayaux2timectrl_start_address + 12;
        self.next3_relayaux2timectrl_acthourallow2 = self.next3_relayaux2timectrl_start_address + 14;
        self.next3_relayaux2timectrl_actweekdaysallow = self.next3_relayaux2timectrl_start_address + 16;
        self.next3_relayaux2timectrl_startingdate = self.next3_relayaux2timectrl_start_address + 18;
        self.next3_relayaux2timectrl_startingtimesec = self.next3_relayaux2timectrl_start_address + 20;
        self.next3_relayaux2timectrl_endingtimesec = self.next3_relayaux2timectrl_start_address + 22;
        self.next3_relayaux2timectrl_selectedweekday = self.next3_relayaux2timectrl_start_address + 24;
        self.next3_relayaux2timectrl_recurrenceweeks = self.next3_relayaux2timectrl_start_address + 26;
        self.next3_relayaux2timectrl_rangeofrecurrenceselect = self.next3_relayaux2timectrl_start_address + 28;
        self.next3_relayaux2timectrl_endingdate = self.next3_relayaux2timectrl_start_address + 30;
        self.next3_relayaux2timectrl_nbrofoccurrences = self.next3_relayaux2timectrl_start_address + 32;
        self.next3_relayaux2timectrl_resettimecontrolled = self.next3_relayaux2timectrl_start_address + 34;

        # Object CmdEntry1 Modbus Address
        self.next3_cmdentry1_start_address = 9300;
        self.next3_cmdentry1_currentstate = self.next3_cmdentry1_start_address + 2;
        self.next3_cmdentry1_cmdinsysidx = self.next3_cmdentry1_start_address + 3;
        self.next3_cmdentry1_configuration = self.next3_cmdentry1_start_address + 5;

        # Object CmdEntry2 Modbus Address
        self.next3_cmdentry2_start_address = 9600;
        self.next3_cmdentry2_currentstate = self.next3_cmdentry2_start_address + 2;
        self.next3_cmdentry2_cmdinsysidx = self.next3_cmdentry2_start_address + 3;
        self.next3_cmdentry2_configuration = self.next3_cmdentry2_start_address + 5;

        # Object BatteryContributor Modbus Address
        self.next3_batterycontributor_start_address = 9900;
        self.next3_batterycontributor_chargingcurrent = self.next3_batterycontributor_start_address + 0;
        self.next3_batterycontributor_temperaturesensorstate = self.next3_batterycontributor_start_address + 2;
        self.next3_batterycontributor_temperature = self.next3_batterycontributor_start_address + 4;
        self.next3_batterycontributor_voltage = self.next3_batterycontributor_start_address + 10;

        # Object Rs485iCommunicationBus Modbus Address
        self.next3_rs485icommunicationbus_start_address = 10200;
        self.next3_rs485icommunicationbus_isterminationset = self.next3_rs485icommunicationbus_start_address + 2;
        self.next3_rs485icommunicationbus_baudrate = self.next3_rs485icommunicationbus_start_address + 3;
        self.next3_rs485icommunicationbus_parity = self.next3_rs485icommunicationbus_start_address + 5;
        self.next3_rs485icommunicationbus_stopbits = self.next3_rs485icommunicationbus_start_address + 7;
        self.next3_rs485icommunicationbus_databits = self.next3_rs485icommunicationbus_start_address + 9;

        # Object CaniCommunicationBus Modbus Address
        self.next3_canicommunicationbus_start_address = 10500;
        self.next3_canicommunicationbus_isterminationset = self.next3_canicommunicationbus_start_address + 2;
        self.next3_canicommunicationbus_baudrate = self.next3_canicommunicationbus_start_address + 3;
        self.next3_canicommunicationbus_parity = self.next3_canicommunicationbus_start_address + 5;
        self.next3_canicommunicationbus_stopbits = self.next3_canicommunicationbus_start_address + 7;
        self.next3_canicommunicationbus_databits = self.next3_canicommunicationbus_start_address + 9;


        # Group Next1 Modbus Address
        # Object IdCard Modbus Address
        self.next1_idcard_start_address = 0;
        self.next1_idcard_serialnumber = self.next1_idcard_start_address + 4;
        self.next1_idcard_softwarepackageversion = self.next1_idcard_start_address + 14;
        self.next1_idcard_softwarerevisionsha1 = self.next1_idcard_start_address + 18;
        self.next1_idcard_objectmodelversion = self.next1_idcard_start_address + 30;

        # Object BaseApp Modbus Address
        self.next1_baseapp_start_address = 300;
        self.next1_baseapp_warnings = self.next1_baseapp_start_address + 5;

        # Object CanNode Modbus Address
        self.next1_cannode_start_address = 900;
        self.next1_cannode_status = self.next1_cannode_start_address + 2;
        self.next1_cannode_txerrorcounter = self.next1_cannode_start_address + 4;
        self.next1_cannode_rxerrorcounter = self.next1_cannode_start_address + 6;
        self.next1_cannode_busterminationset = self.next1_cannode_start_address + 8;

        # Object Device Modbus Address
        self.next1_device_start_address = 1800;
        self.next1_device_blinkingstate = self.next1_device_start_address + 0;
        self.next1_device_totalfunctioningtimesec = self.next1_device_start_address + 5;

        # Object Next1 Modbus Address
        self.next1_next1_start_address = 2700;
        self.next1_next1_status = self.next1_next1_start_address + 0;
        self.next1_next1_errors = self.next1_next1_start_address + 2;
        self.next1_next1_fan1speed = self.next1_next1_start_address + 32;
        self.next1_next1_fan2speed = self.next1_next1_start_address + 34;
        self.next1_next1_fan3speed = self.next1_next1_start_address + 36;
        self.next1_next1_externalpowersupplycurrent = self.next1_next1_start_address + 42;

        # Object RelayAux1 Modbus Address
        self.next1_relayaux1_start_address = 3000;
        self.next1_relayaux1_isconnected = self.next1_relayaux1_start_address + 0;
        self.next1_relayaux1_currentrelayposition = self.next1_relayaux1_start_address + 1;
        self.next1_relayaux1_errors = self.next1_relayaux1_start_address + 3;
        self.next1_relayaux1_operatingmodeselect = self.next1_relayaux1_start_address + 7;
        self.next1_relayaux1_automodeselect = self.next1_relayaux1_start_address + 9;
        self.next1_relayaux1_safestateselect = self.next1_relayaux1_start_address + 11;
        self.next1_relayaux1_presetbatvoltactvth = self.next1_relayaux1_start_address + 13;
        self.next1_relayaux1_presetbatvoltdeactvth = self.next1_relayaux1_start_address + 15;
        self.next1_relayaux1_presetbatsocactth = self.next1_relayaux1_start_address + 17;
        self.next1_relayaux1_presetbatsocdeactth = self.next1_relayaux1_start_address + 19;
        self.next1_relayaux1_presetbattempactth = self.next1_relayaux1_start_address + 21;
        self.next1_relayaux1_presetbattempdeactth = self.next1_relayaux1_start_address + 23;
        self.next1_relayaux1_presetbatstateselect = self.next1_relayaux1_start_address + 25;
        self.next1_relayaux1_presetpacselect = self.next1_relayaux1_start_address + 27;
        self.next1_relayaux1_presetpacpowactth = self.next1_relayaux1_start_address + 29;
        self.next1_relayaux1_presetpacpowdeactth = self.next1_relayaux1_start_address + 31;
        self.next1_relayaux1_presetsolarexcessongridpowactth = self.next1_relayaux1_start_address + 33;
        self.next1_relayaux1_presetsolarexcessongridpowdeactth = self.next1_relayaux1_start_address + 35;
        self.next1_relayaux1_presetsolarexcessoffgridpowactth = self.next1_relayaux1_start_address + 37;
        self.next1_relayaux1_presetsolarexcessoffgridpowdeactth = self.next1_relayaux1_start_address + 39;
        self.next1_relayaux1_presetcmdentryidx = self.next1_relayaux1_start_address + 41;
        self.next1_relayaux1_preseterrorwarningselect = self.next1_relayaux1_start_address + 43;
        self.next1_relayaux1_presetonsourceselect = self.next1_relayaux1_start_address + 45;

        # Object RelayAux2 Modbus Address
        self.next1_relayaux2_start_address = 3300;
        self.next1_relayaux2_isconnected = self.next1_relayaux2_start_address + 0;
        self.next1_relayaux2_currentrelayposition = self.next1_relayaux2_start_address + 1;
        self.next1_relayaux2_errors = self.next1_relayaux2_start_address + 3;
        self.next1_relayaux2_operatingmodeselect = self.next1_relayaux2_start_address + 7;
        self.next1_relayaux2_automodeselect = self.next1_relayaux2_start_address + 9;
        self.next1_relayaux2_safestateselect = self.next1_relayaux2_start_address + 11;
        self.next1_relayaux2_presetbatvoltactvth = self.next1_relayaux2_start_address + 13;
        self.next1_relayaux2_presetbatvoltdeactvth = self.next1_relayaux2_start_address + 15;
        self.next1_relayaux2_presetbatsocactth = self.next1_relayaux2_start_address + 17;
        self.next1_relayaux2_presetbatsocdeactth = self.next1_relayaux2_start_address + 19;
        self.next1_relayaux2_presetbattempactth = self.next1_relayaux2_start_address + 21;
        self.next1_relayaux2_presetbattempdeactth = self.next1_relayaux2_start_address + 23;
        self.next1_relayaux2_presetbatstateselect = self.next1_relayaux2_start_address + 25;
        self.next1_relayaux2_presetpacselect = self.next1_relayaux2_start_address + 27;
        self.next1_relayaux2_presetpacpowactth = self.next1_relayaux2_start_address + 29;
        self.next1_relayaux2_presetpacpowdeactth = self.next1_relayaux2_start_address + 31;
        self.next1_relayaux2_presetsolarexcessongridpowactth = self.next1_relayaux2_start_address + 33;
        self.next1_relayaux2_presetsolarexcessongridpowdeactth = self.next1_relayaux2_start_address + 35;
        self.next1_relayaux2_presetsolarexcessoffgridpowactth = self.next1_relayaux2_start_address + 37;
        self.next1_relayaux2_presetsolarexcessoffgridpowdeactth = self.next1_relayaux2_start_address + 39;
        self.next1_relayaux2_presetcmdentryidx = self.next1_relayaux2_start_address + 41;
        self.next1_relayaux2_preseterrorwarningselect = self.next1_relayaux2_start_address + 43;
        self.next1_relayaux2_presetonsourceselect = self.next1_relayaux2_start_address + 45;

        # Object RelayAux1TimeCtrl Modbus Address
        self.next1_relayaux1timectrl_start_address = 3600;
        self.next1_relayaux1timectrl_timecontrolledmodeselect = self.next1_relayaux1timectrl_start_address + 0;
        self.next1_relayaux1timectrl_actmindelay = self.next1_relayaux1timectrl_start_address + 2;
        self.next1_relayaux1timectrl_deactmindelay = self.next1_relayaux1timectrl_start_address + 4;
        self.next1_relayaux1timectrl_actmintime = self.next1_relayaux1timectrl_start_address + 6;
        self.next1_relayaux1timectrl_deactmintime = self.next1_relayaux1timectrl_start_address + 8;
        self.next1_relayaux1timectrl_actmaxtime = self.next1_relayaux1timectrl_start_address + 10;
        self.next1_relayaux1timectrl_acthourallow1 = self.next1_relayaux1timectrl_start_address + 12;
        self.next1_relayaux1timectrl_acthourallow2 = self.next1_relayaux1timectrl_start_address + 14;
        self.next1_relayaux1timectrl_actweekdaysallow = self.next1_relayaux1timectrl_start_address + 16;
        self.next1_relayaux1timectrl_startingdate = self.next1_relayaux1timectrl_start_address + 18;
        self.next1_relayaux1timectrl_startingtimesec = self.next1_relayaux1timectrl_start_address + 20;
        self.next1_relayaux1timectrl_endingtimesec = self.next1_relayaux1timectrl_start_address + 22;
        self.next1_relayaux1timectrl_selectedweekday = self.next1_relayaux1timectrl_start_address + 24;
        self.next1_relayaux1timectrl_recurrenceweeks = self.next1_relayaux1timectrl_start_address + 26;
        self.next1_relayaux1timectrl_rangeofrecurrenceselect = self.next1_relayaux1timectrl_start_address + 28;
        self.next1_relayaux1timectrl_endingdate = self.next1_relayaux1timectrl_start_address + 30;
        self.next1_relayaux1timectrl_nbrofoccurrences = self.next1_relayaux1timectrl_start_address + 32;
        self.next1_relayaux1timectrl_resettimecontrolled = self.next1_relayaux1timectrl_start_address + 34;

        # Object RelayAux2TimeCtrl Modbus Address
        self.next1_relayaux2timectrl_start_address = 3900;
        self.next1_relayaux2timectrl_timecontrolledmodeselect = self.next1_relayaux2timectrl_start_address + 0;
        self.next1_relayaux2timectrl_actmindelay = self.next1_relayaux2timectrl_start_address + 2;
        self.next1_relayaux2timectrl_deactmindelay = self.next1_relayaux2timectrl_start_address + 4;
        self.next1_relayaux2timectrl_actmintime = self.next1_relayaux2timectrl_start_address + 6;
        self.next1_relayaux2timectrl_deactmintime = self.next1_relayaux2timectrl_start_address + 8;
        self.next1_relayaux2timectrl_actmaxtime = self.next1_relayaux2timectrl_start_address + 10;
        self.next1_relayaux2timectrl_acthourallow1 = self.next1_relayaux2timectrl_start_address + 12;
        self.next1_relayaux2timectrl_acthourallow2 = self.next1_relayaux2timectrl_start_address + 14;
        self.next1_relayaux2timectrl_actweekdaysallow = self.next1_relayaux2timectrl_start_address + 16;
        self.next1_relayaux2timectrl_startingdate = self.next1_relayaux2timectrl_start_address + 18;
        self.next1_relayaux2timectrl_startingtimesec = self.next1_relayaux2timectrl_start_address + 20;
        self.next1_relayaux2timectrl_endingtimesec = self.next1_relayaux2timectrl_start_address + 22;
        self.next1_relayaux2timectrl_selectedweekday = self.next1_relayaux2timectrl_start_address + 24;
        self.next1_relayaux2timectrl_recurrenceweeks = self.next1_relayaux2timectrl_start_address + 26;
        self.next1_relayaux2timectrl_rangeofrecurrenceselect = self.next1_relayaux2timectrl_start_address + 28;
        self.next1_relayaux2timectrl_endingdate = self.next1_relayaux2timectrl_start_address + 30;
        self.next1_relayaux2timectrl_nbrofoccurrences = self.next1_relayaux2timectrl_start_address + 32;
        self.next1_relayaux2timectrl_resettimecontrolled = self.next1_relayaux2timectrl_start_address + 34;

        # Object CmdEntry1 Modbus Address
        self.next1_cmdentry1_start_address = 4200;
        self.next1_cmdentry1_currentstate = self.next1_cmdentry1_start_address + 2;
        self.next1_cmdentry1_cmdinsysidx = self.next1_cmdentry1_start_address + 3;
        self.next1_cmdentry1_configuration = self.next1_cmdentry1_start_address + 5;

        # Object CmdEntry2 Modbus Address
        self.next1_cmdentry2_start_address = 4500;
        self.next1_cmdentry2_currentstate = self.next1_cmdentry2_start_address + 2;
        self.next1_cmdentry2_cmdinsysidx = self.next1_cmdentry2_start_address + 3;
        self.next1_cmdentry2_configuration = self.next1_cmdentry2_start_address + 5;

        # Object BatteryContributor Modbus Address
        self.next1_batterycontributor_start_address = 4800;
        self.next1_batterycontributor_chargingcurrent = self.next1_batterycontributor_start_address + 0;
        self.next1_batterycontributor_temperaturesensorstate = self.next1_batterycontributor_start_address + 2;
        self.next1_batterycontributor_temperature = self.next1_batterycontributor_start_address + 4;
        self.next1_batterycontributor_voltage = self.next1_batterycontributor_start_address + 10;

        # Object Rs485iCommunicationBus Modbus Address
        self.next1_rs485icommunicationbus_start_address = 5100;
        self.next1_rs485icommunicationbus_isterminationset = self.next1_rs485icommunicationbus_start_address + 2;
        self.next1_rs485icommunicationbus_baudrate = self.next1_rs485icommunicationbus_start_address + 3;
        self.next1_rs485icommunicationbus_parity = self.next1_rs485icommunicationbus_start_address + 5;
        self.next1_rs485icommunicationbus_stopbits = self.next1_rs485icommunicationbus_start_address + 7;
        self.next1_rs485icommunicationbus_databits = self.next1_rs485icommunicationbus_start_address + 9;

        # Object CaniCommunicationBus Modbus Address
        self.next1_canicommunicationbus_start_address = 5400;
        self.next1_canicommunicationbus_isterminationset = self.next1_canicommunicationbus_start_address + 2;
        self.next1_canicommunicationbus_baudrate = self.next1_canicommunicationbus_start_address + 3;
        self.next1_canicommunicationbus_parity = self.next1_canicommunicationbus_start_address + 5;
        self.next1_canicommunicationbus_stopbits = self.next1_canicommunicationbus_start_address + 7;
        self.next1_canicommunicationbus_databits = self.next1_canicommunicationbus_start_address + 9;


        # Group NextGateway Modbus Address
        # Object IdCard Modbus Address
        self.nextgateway_idcard_start_address = 0;
        self.nextgateway_idcard_serialnumber = self.nextgateway_idcard_start_address + 4;
        self.nextgateway_idcard_softwarepackageversion = self.nextgateway_idcard_start_address + 14;
        self.nextgateway_idcard_softwarerevisionsha1 = self.nextgateway_idcard_start_address + 18;
        self.nextgateway_idcard_objectmodelversion = self.nextgateway_idcard_start_address + 30;

        # Object BaseApplication Modbus Address
        self.nextgateway_baseapplication_start_address = 300;
        self.nextgateway_baseapplication_warnings = self.nextgateway_baseapplication_start_address + 5;

        # Object CanNode Modbus Address
        self.nextgateway_cannode_start_address = 600;
        self.nextgateway_cannode_status = self.nextgateway_cannode_start_address + 2;
        self.nextgateway_cannode_txerrorcounter = self.nextgateway_cannode_start_address + 4;
        self.nextgateway_cannode_rxerrorcounter = self.nextgateway_cannode_start_address + 6;
        self.nextgateway_cannode_busterminationset = self.nextgateway_cannode_start_address + 8;

        # Object Device Modbus Address
        self.nextgateway_device_start_address = 900;
        self.nextgateway_device_blinkingstate = self.nextgateway_device_start_address + 0;
        self.nextgateway_device_totalfunctioningtimesec = self.nextgateway_device_start_address + 5;

        # Object GatewayModule Modbus Address
        self.nextgateway_gatewaymodule_start_address = 1200;
        self.nextgateway_gatewaymodule_errors = self.nextgateway_gatewaymodule_start_address + 0;
        self.nextgateway_gatewaymodule_warnings = self.nextgateway_gatewaymodule_start_address + 2;
        self.nextgateway_gatewaymodule_emmctotalsizekib = self.nextgateway_gatewaymodule_start_address + 6;
        self.nextgateway_gatewaymodule_usbmountedpartitionsnumber = self.nextgateway_gatewaymodule_start_address + 10;
        self.nextgateway_gatewaymodule_cputemperature = self.nextgateway_gatewaymodule_start_address + 16;

        # Object HmiDisplay Modbus Address
        self.nextgateway_hmidisplay_start_address = 1500;
        self.nextgateway_hmidisplay_brightness = self.nextgateway_hmidisplay_start_address + 0;
        self.nextgateway_hmidisplay_sleepdelaysec = self.nextgateway_hmidisplay_start_address + 2;
        self.nextgateway_hmidisplay_unlockcode = self.nextgateway_hmidisplay_start_address + 4;
        self.nextgateway_hmidisplay_unlockmechanism = self.nextgateway_hmidisplay_start_address + 8;
        self.nextgateway_hmidisplay_totaldisplayontimesec = self.nextgateway_hmidisplay_start_address + 14;

        # Object Rs485iCommunicationBus Modbus Address
        self.nextgateway_rs485icommunicationbus_start_address = 1800;
        self.nextgateway_rs485icommunicationbus_isterminationset = self.nextgateway_rs485icommunicationbus_start_address + 2;
        self.nextgateway_rs485icommunicationbus_baudrate = self.nextgateway_rs485icommunicationbus_start_address + 3;
        self.nextgateway_rs485icommunicationbus_parity = self.nextgateway_rs485icommunicationbus_start_address + 5;
        self.nextgateway_rs485icommunicationbus_stopbits = self.nextgateway_rs485icommunicationbus_start_address + 7;
        self.nextgateway_rs485icommunicationbus_databits = self.nextgateway_rs485icommunicationbus_start_address + 9;

        # Object CaniCommunicationBus Modbus Address
        self.nextgateway_canicommunicationbus_start_address = 2100;
        self.nextgateway_canicommunicationbus_isterminationset = self.nextgateway_canicommunicationbus_start_address + 2;
        self.nextgateway_canicommunicationbus_baudrate = self.nextgateway_canicommunicationbus_start_address + 3;
        self.nextgateway_canicommunicationbus_parity = self.nextgateway_canicommunicationbus_start_address + 5;
        self.nextgateway_canicommunicationbus_stopbits = self.nextgateway_canicommunicationbus_start_address + 7;
        self.nextgateway_canicommunicationbus_databits = self.nextgateway_canicommunicationbus_start_address + 9;

        # Object MemoryPartitionEmmcRootfs Modbus Address
        self.nextgateway_memorypartitionemmcrootfs_start_address = 2400;
        self.nextgateway_memorypartitionemmcrootfs_media = self.nextgateway_memorypartitionemmcrootfs_start_address + 0;
        self.nextgateway_memorypartitionemmcrootfs_filesystem = self.nextgateway_memorypartitionemmcrootfs_start_address + 2;
        self.nextgateway_memorypartitionemmcrootfs_totalsizekib = self.nextgateway_memorypartitionemmcrootfs_start_address + 4;
        self.nextgateway_memorypartitionemmcrootfs_usedsizekib = self.nextgateway_memorypartitionemmcrootfs_start_address + 6;

        # Object MemoryPartitionEmmcConfig Modbus Address
        self.nextgateway_memorypartitionemmcconfig_start_address = 2700;
        self.nextgateway_memorypartitionemmcconfig_media = self.nextgateway_memorypartitionemmcconfig_start_address + 0;
        self.nextgateway_memorypartitionemmcconfig_filesystem = self.nextgateway_memorypartitionemmcconfig_start_address + 2;
        self.nextgateway_memorypartitionemmcconfig_totalsizekib = self.nextgateway_memorypartitionemmcconfig_start_address + 4;
        self.nextgateway_memorypartitionemmcconfig_usedsizekib = self.nextgateway_memorypartitionemmcconfig_start_address + 6;

        # Object MemoryPartitionEmmcData Modbus Address
        self.nextgateway_memorypartitionemmcdata_start_address = 3000;
        self.nextgateway_memorypartitionemmcdata_media = self.nextgateway_memorypartitionemmcdata_start_address + 0;
        self.nextgateway_memorypartitionemmcdata_filesystem = self.nextgateway_memorypartitionemmcdata_start_address + 2;
        self.nextgateway_memorypartitionemmcdata_totalsizekib = self.nextgateway_memorypartitionemmcdata_start_address + 4;
        self.nextgateway_memorypartitionemmcdata_usedsizekib = self.nextgateway_memorypartitionemmcdata_start_address + 6;

        # Object MemoryPartitionUsb1 Modbus Address
        self.nextgateway_memorypartitionusb1_start_address = 3300;
        self.nextgateway_memorypartitionusb1_media = self.nextgateway_memorypartitionusb1_start_address + 0;
        self.nextgateway_memorypartitionusb1_filesystem = self.nextgateway_memorypartitionusb1_start_address + 2;
        self.nextgateway_memorypartitionusb1_totalsizekib = self.nextgateway_memorypartitionusb1_start_address + 4;
        self.nextgateway_memorypartitionusb1_usedsizekib = self.nextgateway_memorypartitionusb1_start_address + 6;

        # Object MemoryPartitionUsb2 Modbus Address
        self.nextgateway_memorypartitionusb2_start_address = 3600;
        self.nextgateway_memorypartitionusb2_media = self.nextgateway_memorypartitionusb2_start_address + 0;
        self.nextgateway_memorypartitionusb2_filesystem = self.nextgateway_memorypartitionusb2_start_address + 2;
        self.nextgateway_memorypartitionusb2_totalsizekib = self.nextgateway_memorypartitionusb2_start_address + 4;
        self.nextgateway_memorypartitionusb2_usedsizekib = self.nextgateway_memorypartitionusb2_start_address + 6;

        # Object MemoryPartitionUsb3 Modbus Address
        self.nextgateway_memorypartitionusb3_start_address = 3900;
        self.nextgateway_memorypartitionusb3_media = self.nextgateway_memorypartitionusb3_start_address + 0;
        self.nextgateway_memorypartitionusb3_filesystem = self.nextgateway_memorypartitionusb3_start_address + 2;
        self.nextgateway_memorypartitionusb3_totalsizekib = self.nextgateway_memorypartitionusb3_start_address + 4;
        self.nextgateway_memorypartitionusb3_usedsizekib = self.nextgateway_memorypartitionusb3_start_address + 6;

        # Object Modbus Modbus Address
        self.nextgateway_modbus_start_address = 4200;
        self.nextgateway_modbus_baseaddress = self.nextgateway_modbus_start_address + 0;
        self.nextgateway_modbus_modbustcpport = self.nextgateway_modbus_start_address + 2;
        self.nextgateway_modbus_modbustcpserverstatus = self.nextgateway_modbus_start_address + 14;
        self.nextgateway_modbus_modbusrtuserverstatus = self.nextgateway_modbus_start_address + 16;
        self.nextgateway_modbus_mode = self.nextgateway_modbus_start_address + 18;
        self.nextgateway_modbus_writepersistent = self.nextgateway_modbus_start_address + 20;

        # Object ModbusUserLevel Modbus Address
        self.nextgateway_modbususerlevel_start_address = 4500;
        self.nextgateway_modbususerlevel_userlevel = self.nextgateway_modbususerlevel_start_address + 0;
        self.nextgateway_modbususerlevel_userlevelcodeinput = self.nextgateway_modbususerlevel_start_address + 2;

        # Object NetworkInterfaceEthernet Modbus Address
        self.nextgateway_networkinterfaceethernet_start_address = 5100;
        self.nextgateway_networkinterfaceethernet_interfacestatus = self.nextgateway_networkinterfaceethernet_start_address + 2;
        self.nextgateway_networkinterfaceethernet_interfacename = self.nextgateway_networkinterfaceethernet_start_address + 4;
        self.nextgateway_networkinterfaceethernet_hardwareaddress = self.nextgateway_networkinterfaceethernet_start_address + 14;
        self.nextgateway_networkinterfaceethernet_ipaddressv4 = self.nextgateway_networkinterfaceethernet_start_address + 24;
        self.nextgateway_networkinterfaceethernet_netmaskv4 = self.nextgateway_networkinterfaceethernet_start_address + 34;
        self.nextgateway_networkinterfaceethernet_broadcastv4 = self.nextgateway_networkinterfaceethernet_start_address + 44;
        self.nextgateway_networkinterfaceethernet_interfacemode = self.nextgateway_networkinterfaceethernet_start_address + 54;

        # Object NetworkInterfaceWifi Modbus Address
        self.nextgateway_networkinterfacewifi_start_address = 5400;
        self.nextgateway_networkinterfacewifi_interfacestatus = self.nextgateway_networkinterfacewifi_start_address + 2;
        self.nextgateway_networkinterfacewifi_interfacename = self.nextgateway_networkinterfacewifi_start_address + 4;
        self.nextgateway_networkinterfacewifi_hardwareaddress = self.nextgateway_networkinterfacewifi_start_address + 14;
        self.nextgateway_networkinterfacewifi_ipaddressv4 = self.nextgateway_networkinterfacewifi_start_address + 24;
        self.nextgateway_networkinterfacewifi_netmaskv4 = self.nextgateway_networkinterfacewifi_start_address + 34;
        self.nextgateway_networkinterfacewifi_broadcastv4 = self.nextgateway_networkinterfacewifi_start_address + 44;
        self.nextgateway_networkinterfacewifi_interfacemode = self.nextgateway_networkinterfacewifi_start_address + 54;

        # Object NetworkInterfaceExternal Modbus Address
        self.nextgateway_networkinterfaceexternal_start_address = 5700;
        self.nextgateway_networkinterfaceexternal_interfacestatus = self.nextgateway_networkinterfaceexternal_start_address + 2;
        self.nextgateway_networkinterfaceexternal_interfacename = self.nextgateway_networkinterfaceexternal_start_address + 4;
        self.nextgateway_networkinterfaceexternal_hardwareaddress = self.nextgateway_networkinterfaceexternal_start_address + 14;
        self.nextgateway_networkinterfaceexternal_ipaddressv4 = self.nextgateway_networkinterfaceexternal_start_address + 24;
        self.nextgateway_networkinterfaceexternal_netmaskv4 = self.nextgateway_networkinterfaceexternal_start_address + 34;
        self.nextgateway_networkinterfaceexternal_broadcastv4 = self.nextgateway_networkinterfaceexternal_start_address + 44;
        self.nextgateway_networkinterfaceexternal_interfacemode = self.nextgateway_networkinterfaceexternal_start_address + 54;

        # Object GatewayUserLevel Modbus Address
        self.nextgateway_gatewayuserlevel_start_address = 6000;
        self.nextgateway_gatewayuserlevel_userlevel = self.nextgateway_gatewayuserlevel_start_address + 0;
        self.nextgateway_gatewayuserlevel_userlevelcodeinput = self.nextgateway_gatewayuserlevel_start_address + 2;

        # Object Webportal Modbus Address
        self.nextgateway_webportal_start_address = 6300;
        self.nextgateway_webportal_webportalconnectionstatus = self.nextgateway_webportal_start_address + 0;
        self.nextgateway_webportal_webportaldatalogsynchrostatus = self.nextgateway_webportal_start_address + 2;
        self.nextgateway_webportal_certificateeffectivedate = self.nextgateway_webportal_start_address + 4;
        self.nextgateway_webportal_certificateexpirydate = self.nextgateway_webportal_start_address + 6;
        self.nextgateway_webportal_uploaddebugdata = self.nextgateway_webportal_start_address + 8;
        self.nextgateway_webportal_readonly = self.nextgateway_webportal_start_address + 9;

        # Object UsbInterface1 Modbus Address
        self.nextgateway_usbinterface1_start_address = 6600;
        self.nextgateway_usbinterface1_usbportdevicetype = self.nextgateway_usbinterface1_start_address + 2;

        # Object UsbInterface2 Modbus Address
        self.nextgateway_usbinterface2_start_address = 6900;
        self.nextgateway_usbinterface2_usbportdevicetype = self.nextgateway_usbinterface2_start_address + 2;

        # Object UsbInterface3 Modbus Address
        self.nextgateway_usbinterface3_start_address = 7200;
        self.nextgateway_usbinterface3_usbportdevicetype = self.nextgateway_usbinterface3_start_address + 2;

        # Object UsbInterface4 Modbus Address
        self.nextgateway_usbinterface4_start_address = 7500;
        self.nextgateway_usbinterface4_usbportdevicetype = self.nextgateway_usbinterface4_start_address + 2;

        # Object HmiSettings Modbus Address
        self.nextgateway_hmisettings_start_address = 7800;
        self.nextgateway_hmisettings_language = self.nextgateway_hmisettings_start_address + 0;
        self.nextgateway_hmisettings_defaultview = self.nextgateway_hmisettings_start_address + 2;

        # Object SystemView Modbus Address
        self.nextgateway_systemview_start_address = 8100;
        self.nextgateway_systemview_installationstatus = self.nextgateway_systemview_start_address + 0;
        self.nextgateway_systemview_nodestatus = self.nextgateway_systemview_start_address + 2;

        # Object Webcommand Modbus Address
        self.nextgateway_webcommand_start_address = 8400;
        self.nextgateway_webcommand_webcommandstatus = self.nextgateway_webcommand_start_address + 21;
        self.nextgateway_webcommand_connections = self.nextgateway_webcommand_start_address + 23;


