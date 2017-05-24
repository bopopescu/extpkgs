#
# PySNMP MIB module VDSL-LINE-EXT-SCM-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/VDSL-LINE-EXT-SCM-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:32:51 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( ObjectIdentifier, OctetString, Integer, ) = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ObjectGroup, ModuleCompliance, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
( IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Gauge32, Bits, transmission, Unsigned32, MibIdentifier, ObjectIdentity, Counter64, Integer32, ModuleIdentity, TimeTicks, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Gauge32", "Bits", "transmission", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter64", "Integer32", "ModuleIdentity", "TimeTicks", "Counter32")
( TruthValue, TextualConvention, RowStatus, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
( vdslLineConfProfileName, ) = mibBuilder.importSymbols("VDSL-LINE-MIB", "vdslLineConfProfileName")
vdslExtSCMMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 228)).setRevisions(("2005-04-28 00:00",))
if mibBuilder.loadTexts: vdslExtSCMMIB.setLastUpdated('200504280000Z')
if mibBuilder.loadTexts: vdslExtSCMMIB.setOrganization('ADSLMIB Working Group')
if mibBuilder.loadTexts: vdslExtSCMMIB.setContactInfo('WG-email:  adslmib@ietf.org\n         Info:      https://www1.ietf.org/mailman/listinfo/adslmib\n\n         Chair:     Mike Sneed\n                    Sand Channel Systems\n         Postal:    P.O. Box 37324\n                    Raleigh NC 27627-732\n         Email:     sneedmike@hotmail.com\n         Phone:     +1 206 600 7022\n\n         Co-Chair/Co-editor:\n                    Bob Ray\n                    PESA Switching Systems, Inc.\n         Postal:    330-A Wynn Drive\n                    Huntsville, AL 35805\n                    USA\n         Email:     rray@pesa.com\n         Phone:     +1 256 726 9200 ext.  142\n\n\n\n         Co-editor: Menachem Dodge\n                    ECI Telecom Ltd.\n         Postal:    30 Hasivim St.\n                    Petach Tikva 49517,\n                    Israel\n         Email:     mbdodge@ieee.org\n         Phone:     +972 3 926 8421\n        ')
if mibBuilder.loadTexts: vdslExtSCMMIB.setDescription('The VDSL-LINE-MIB found in RFC 3728 defines objects for the\n   management of a pair of VDSL transceivers at each end of the VDSL\n   line.  The VDSL-LINE-MIB configures and monitors the line code\n   independent parameters (TC layer) of the VDSL line.  This MIB\n   module is an optional extension of the VDSL-LINE-MIB and defines\n   objects for configuration and monitoring of the line code specific\n   (LCS) elements (PMD layer) for VDSL lines using SCM coding.  The\n   objects in this extension MIB MUST NOT be used for VDSL lines\n   using Multiple Carrier Modulation (MCM) line coding.  If an object\n   in this extension MIB is referenced by a line which does not use\n   SCM, it has no effect on the operation of that line.\n\n   Naming Conventions:\n\n      Vtuc -- VDSL transceiver at near (Central) end of line\n      Vtur -- VDSL transceiver at Remote end of line\n      Vtu  -- One of either Vtuc or Vtur\n      Curr -- Current\n      Atn  -- Attenuation\n      LCS  -- Line Code Specific\n      Max  -- Maximum\n      Mgn  -- Margin\n      PSD  -- Power Spectral Density\n      Rx   -- Receive\n      Snr  -- Signal to Noise Ratio\n      Tx   -- Transmit\n\n   Copyright (C) The Internet Society (2005).  This version\n   of this MIB module is part of RFC 4069: see the RFC\n   itself for full legal notices.')
vdslLineExtSCMMib = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1))
vdslLineExtSCMMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 1))
class VdslSCMBandId(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,))
    namedValues = NamedValues(("optionalBand", 1), ("firstDownstreamBand", 2), ("firstUpstreamBand", 3), ("secondDownstreamBand", 4), ("secondUpstreamBand", 5), ("thirdDownstreamBand", 6), ("thirdUpstreamBand", 7),)

vdslLineSCMConfProfileBandTable = MibTable((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1), )
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandTable.setDescription('This table contains transmit band descriptor configuration\n        information for a VDSL line.  Each entry in this table\n        reflects the configuration for one of possibly many bands\n        of a single carrier modulation (SCM) VDSL line.  For each\n        profile which is associated with a VDSL line using SCM\n        line coding, five entries in this table will exist, one for\n        each of the five bands.  Bands which are not in use will be\n        marked as unused.  These entries are defined by a manager\n        and can be used to configure the VDSL line.  If an entry in\n\n\n\n\n\n        this table is referenced by a line which does not use SCM,\n        it has no effect on the operation of that line.')
vdslLineSCMConfProfileBandEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1), ).setIndexNames((0, "VDSL-LINE-MIB", "vdslLineConfProfileName"), (0, "VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandId"))
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandEntry.setDescription("Each entry consists of a list of parameters that\n        represents the configuration of a single carrier\n        modulation VDSL modem transmit band.\n\n        A default profile with an index of 'DEFVAL', will\n        always exist and its parameters will be set to vendor\n        specific values, unless otherwise specified in this\n        document.\n\n        All read-create objects defined in this MIB module SHOULD be\n        stored persistently.")
vdslLineSCMConfProfileBandId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 1), VdslSCMBandId())
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandId.setDescription('The BandId for this entry, which specifies which band\n        is being referred to.')
vdslLineSCMConfProfileBandInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandInUse.setDescription('Indicates whether this band is in use.\n        If set to True this band is in use.')
vdslLineSCMConfProfileBandCenterFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 3), Unsigned32()).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandCenterFrequency.setDescription('Specifies the center frequency in Hz')
vdslLineSCMConfProfileBandSymbolRate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 4), Unsigned32()).setUnits('baud').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandSymbolRate.setDescription('The requested symbol rate in baud.')
vdslLineSCMConfProfileBandConstellationSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,16))).setUnits('log2').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandConstellationSize.setDescription('Specifies the constellation size.')
vdslLineSCMConfProfileBandTransmitPSDLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 6), Unsigned32()).setUnits('-0.25 dBm/Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandTransmitPSDLevel.setDescription('The requested transmit power spectral density for the VDSL\n        modem.  The Actual value in -0.25 dBm/Hz.')
vdslLineSCMConfProfileBandRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandRowStatus.setDescription("This object is used to create a new row or modify or\n        delete an existing row in this table.\n\n        A profile activated by setting this object to `active'.\n        When `active' is set, the system will validate the profile.\n\n        None of the columns in this row may be modified while the\n        row is in the `active' state.\n\n        Before a profile can be deleted or taken out of\n        service, (by setting this object to `destroy' or\n        `notInService') it must be first unreferenced\n        from all associated lines.")
vdslLineSCMPhysBandTable = MibTable((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2), )
if mibBuilder.loadTexts: vdslLineSCMPhysBandTable.setDescription('This table provides one row for each SCM Vtu band.  This\n        table is read only as it reflects the current physical\n        parameters of each band.  For each ifIndex which is\n        associated with a VDSL line using SCM line coding, five\n        entries in this table will exist, one for each of the\n        five bands.  Bands which are not in use will be marked\n        as unused.')
vdslLineSCMPhysBandEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandId"))
if mibBuilder.loadTexts: vdslLineSCMPhysBandEntry.setDescription('An entry in the vdslLineSCMPhysBandTable.')
vdslLineSCMPhysBandId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 1), VdslSCMBandId())
if mibBuilder.loadTexts: vdslLineSCMPhysBandId.setDescription('The BandId for this entry, which specifies which band\n         is being referred to.')
vdslLineSCMPhysBandInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandInUse.setDescription('Indicates whether this band is in use.\n        If set to True this band is in use.')
vdslLineSCMPhysBandCurrCenterFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 3), Unsigned32()).setUnits('Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrCenterFrequency.setDescription('The current center frequency in Hz for this band.')
vdslLineSCMPhysBandCurrSymbolRate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 4), Unsigned32()).setUnits('baud').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrSymbolRate.setDescription('The current value of the symbol rate in baud for this\n        band.')
vdslLineSCMPhysBandCurrConstellationSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,16))).setUnits('log2').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrConstellationSize.setDescription('The current constellation size on this band.')
vdslLineSCMPhysBandCurrPSDLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 6), Unsigned32()).setUnits('- 0.25 dBm/Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrPSDLevel.setDescription('The transmit power spectral density for the\n        VDSL modem.')
vdslLineSCMPhysBandCurrSnrMgn = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 7), Integer32()).setUnits('0.25 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrSnrMgn.setDescription('Noise margin as seen by this Vtu and band with respect\n        to its received signal in 0.25 dB.')
vdslLineSCMPhysBandCurrAtn = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,255))).setUnits('0.25 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrAtn.setDescription('Measured difference in the total power transmitted by\n        the peer Vtu on this band and the total power received\n        by this Vtu on this band in 0.25 dB.')
vdslLineExtSCMConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 2))
vdslLineExtSCMGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 1))
vdslLineExtSCMCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 2))
vdslLineExtSCMMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 2, 1)).setObjects(*(("VDSL-LINE-EXT-SCM-MIB", "vdslLineExtSCMGroup"),))
if mibBuilder.loadTexts: vdslLineExtSCMMibCompliance.setDescription('The compliance statement for SNMP entities which\n        manage VDSL interfaces.')
vdslLineExtSCMGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 1, 1)).setObjects(*(("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandInUse"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandTransmitPSDLevel"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandSymbolRate"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandConstellationSize"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandCenterFrequency"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandRowStatus"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandInUse"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrPSDLevel"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrSymbolRate"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrConstellationSize"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrCenterFrequency"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrSnrMgn"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrAtn"),))
if mibBuilder.loadTexts: vdslLineExtSCMGroup.setDescription('A collection of objects providing configuration\n        information for a VDSL line based upon single carrier\n        modulation modem.')
mibBuilder.exportSymbols("VDSL-LINE-EXT-SCM-MIB", vdslLineSCMPhysBandCurrCenterFrequency=vdslLineSCMPhysBandCurrCenterFrequency, vdslLineSCMPhysBandCurrSnrMgn=vdslLineSCMPhysBandCurrSnrMgn, vdslLineExtSCMCompliances=vdslLineExtSCMCompliances, vdslLineExtSCMGroup=vdslLineExtSCMGroup, vdslLineSCMConfProfileBandInUse=vdslLineSCMConfProfileBandInUse, vdslLineSCMConfProfileBandTable=vdslLineSCMConfProfileBandTable, vdslLineSCMPhysBandEntry=vdslLineSCMPhysBandEntry, vdslLineSCMPhysBandCurrAtn=vdslLineSCMPhysBandCurrAtn, vdslLineSCMPhysBandId=vdslLineSCMPhysBandId, vdslLineSCMPhysBandInUse=vdslLineSCMPhysBandInUse, vdslLineExtSCMMibObjects=vdslLineExtSCMMibObjects, VdslSCMBandId=VdslSCMBandId, vdslLineExtSCMConformance=vdslLineExtSCMConformance, vdslLineSCMConfProfileBandConstellationSize=vdslLineSCMConfProfileBandConstellationSize, vdslLineSCMConfProfileBandId=vdslLineSCMConfProfileBandId, vdslLineExtSCMMibCompliance=vdslLineExtSCMMibCompliance, vdslLineSCMPhysBandCurrConstellationSize=vdslLineSCMPhysBandCurrConstellationSize, vdslExtSCMMIB=vdslExtSCMMIB, vdslLineSCMPhysBandCurrSymbolRate=vdslLineSCMPhysBandCurrSymbolRate, vdslLineSCMConfProfileBandCenterFrequency=vdslLineSCMConfProfileBandCenterFrequency, vdslLineSCMConfProfileBandTransmitPSDLevel=vdslLineSCMConfProfileBandTransmitPSDLevel, PYSNMP_MODULE_ID=vdslExtSCMMIB, vdslLineExtSCMGroups=vdslLineExtSCMGroups, vdslLineExtSCMMib=vdslLineExtSCMMib, vdslLineSCMConfProfileBandEntry=vdslLineSCMConfProfileBandEntry, vdslLineSCMPhysBandCurrPSDLevel=vdslLineSCMPhysBandCurrPSDLevel, vdslLineSCMPhysBandTable=vdslLineSCMPhysBandTable, vdslLineSCMConfProfileBandRowStatus=vdslLineSCMConfProfileBandRowStatus, vdslLineSCMConfProfileBandSymbolRate=vdslLineSCMConfProfileBandSymbolRate)