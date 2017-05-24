#
# PySNMP MIB module T11-FC-FABRIC-LOCK-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/T11-FC-FABRIC-LOCK-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:29:58 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( OctetString, ObjectIdentifier, Integer, ) = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
( fcmInstanceIndex, fcmSwitchIndex, ) = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex", "fcmSwitchIndex")
( InetAddressType, InetAddress, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
( NotificationGroup, ObjectGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
( MibIdentifier, Unsigned32, ModuleIdentity, Counter64, Bits, Gauge32, IpAddress, mib_2, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ObjectIdentity, Integer32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "Gauge32", "IpAddress", "mib-2", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ObjectIdentity", "Integer32")
( RowStatus, DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
( T11NsGs4RejectReasonCode, ) = mibBuilder.importSymbols("T11-FC-NAME-SERVER-MIB", "T11NsGs4RejectReasonCode")
( T11FabricIndex, ) = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FabricLockMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 159)).setRevisions(("2007-06-27 00:00",))
if mibBuilder.loadTexts: t11FabricLockMIB.setLastUpdated('200706270000Z')
if mibBuilder.loadTexts: t11FabricLockMIB.setOrganization("For the initial versions, T11.\n                   For later versions, the IETF's IMSS Working Group.")
if mibBuilder.loadTexts: t11FabricLockMIB.setContactInfo('      Claudio DeSanti\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  EMail: cds@cisco.com\n\n                  Keith McCloghrie\n\n\n\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  EMail: kzm@cisco.com')
if mibBuilder.loadTexts: t11FabricLockMIB.setDescription("The MIB module for the management of locks on a Fibre\n           Channel Fabric.  A Fibre Channel Fabric lock is used to\n           ensure serialized access to some types of management data\n           related to a Fabric, e.g., the Fabric's Zoning Database.\n\n           Some (managing) applications generate Fabric locks by\n           initiating server sessions.  Server sessions are\n           defined generically in FC-GS-5 to represent a collection of\n           one or more requests to the session's server, e.g., to the\n           Zone Server.  Such a session is started by a Server Session\n           Begin (SSB) request, and terminated by a Server Session End\n           (SSE) request.  The switch receiving the SSB is called the\n           'managing' switch.  Some applications require the\n           'managing' switch to lock the Fabric for the particular\n           application, e.g., for Enhanced Zoning, before it can\n           respond successfully to the SSB.  On receipt of the\n           subsequent SSE, the lock is released.  For this usage, the\n           managing switch sends an Acquire Change Authorization (ACA)\n           request to other switches to lock the Fabric.\n\n           For some other applications, a managing switch locks the\n           Fabric using an Enhanced Acquire Change Authorization (EACA)\n           request, which identifies the application on whose behalf\n           the Fabric is being locked with an Application_ID.\n\n           Fabric locks can also be requested more directly, e.g.,\n           through the use of this MIB.  In these situations, the term\n           'managing' switch is used to indicate the switch that\n           receives such a request and executes it by issuing either\n           ACA or EACA requests to other switches in the Fabric.\n\n           This MIB module defines information about the 'managing'\n           switch for currently-active Fabric locks.\n\n           Copyright (C) The IETF Trust (2007).  This version\n           of this MIB module is part of RFC 4936;  see the RFC\n           itself for full legal notices.")
t11FLockMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 159, 1))
t11FLockMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 159, 2))
t11FLockMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 159, 0))
t11FLockConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 159, 1, 1))
t11FLockTable = MibTable((1, 3, 6, 1, 2, 1, 159, 1, 1, 1), )
if mibBuilder.loadTexts: t11FLockTable.setDescription("A table containing information about the 'managing'\n           switch of each current Fabric lock, e.g., for the\n           types of Servers defined in FC-GS-5.\n\n           Each entry in this table represents either:\n\n           1) a current Fabric lock,\n           2) an in-progress attempt, requested via SNMP, to set up\n              a lock, or\n           3) a failed attempt, requested via SNMP, to set up a lock.\n\n           If an entry is created via t11FLockRowStatus, but the\n           attempt to obtain the lock fails, then the entry continues\n           to exist until it is deleted via t11FLockRowStatus, or\n           it is overwritten by the lock being established via\n           a means other than SNMP.  However, rows created via\n           t11FLockRowStatus are not retained over restarts.")
t11FLockEntry = MibTableRow((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-LOCK-MIB", "t11FLockFabricIndex"), (0, "T11-FC-FABRIC-LOCK-MIB", "t11FLockApplicationID"))
if mibBuilder.loadTexts: t11FLockEntry.setDescription("Each entry contains information specific to a current\n           Fabric lock set up by a particular 'managing' switch on a\n           particular Fabric.  The 'managing switch' is identified by\n           values of fcmInstanceIndex and fcmSwitchIndex.\n\n           Server sessions for several different types of servers\n           are defined in FC-GS-5.  The behavior of a server with\n\n\n\n           respect to commands received within a server session is\n           specified for each type of server.  For some types,\n           parameter changes can only be made within the context of a\n           session, and the setting up of a session requires that the\n           Fabric be locked.  A Fabric is locked by one switch, called\n           the 'managing' switch, sending Acquire Change Authorization\n           (ACA) requests to all other switches in the Fabric.\n\n           For other applications, a Fabric lock is established by the\n           'managing' switch sending Enhanced Acquire Change\n           Authorization (EACA) requests to other switches in the\n           Fabric.  Each EACA request includes an Application_ID\n           value to identify the application requesting the lock.\n\n           For the benefit of this MIB module, a distinct value of\n           Application_ID has also been assigned/reserved (see\n           ANSI INCITS T11/06-679v0, titled 'FC-SW-5 Letter to\n           T11.5') as a means of distinguishing locks established via\n           Acquire Change Authorization (ACA) requests.  This\n           additional assignment allows an Application_ID to be used to\n           uniquely identify any active lock amongst all those\n           established by either an EACA or an ACA.\n\n           Whenever a Fabric is locked, by the sending of either an ACA\n           or an EACA, a row gets created in the representation of this\n           table for the 'managing' switch.\n\n           In order to process SNMP SetRequests that make parameter\n           changes for the relevant types of servers (e.g., to the\n           Zoning Database), the SNMP agent must get serialized access\n           to the Fabric (for the relevant type of management data),\n           i.e., the Fabric must be locked by creating an entry in\n           this table via an SNMP SetRequest.  Creating an entry in\n           this table via an SNMP SetRequest causes an ACA or an EACA\n           to be sent to all other switches in the Fabric.  The value\n           of t11FLockApplicationID for such an entry determines\n           whether an ACA or an EACA is sent.\n\n           If an entry in this table is created by an SNMP SetRequest,\n           the value of the t11FLockInitiatorType object in that entry\n           will normally be 'snmp'.  A row for which the value of\n           t11FLockInitiatorType is not 'snmp' cannot be modified\n           via SNMP.  In particular, it cannot be deleted via\n           t11FLockRowStatus.  Note that it's possible for a row to be\n           created by an SNMP SetRequest, but for the setup of the lock\n           to fail, and immediately thereafter be replaced by a lock\n           successfully set up by some other means; in such a case, the\n           value of t11FLockInitiatorType would change as and when the\n\n\n\n           lock was set up by the other means, and so the row could\n           not thereafter be deleted via t11FLockRowStatus.\n\n           FC-GS-5 mentions various error situations in which a\n           Fabric lock is released so as to avoid a deadlock.  In\n           such situations, the agent removes the corresponding row\n           in this table as and when the lock is released.  This can\n           happen for all values of t11FLockInitiatorType.")
t11FLockFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11FLockFabricIndex.setDescription('A unique index value that uniquely identifies a\n           particular Fabric.\n\n           In a Fabric conformant to FC-SW-4, multiple Virtual Fabrics\n           can operate within one (or more) physical infrastructures,\n           and this index value is used to uniquely identify a\n\n\n\n           particular (physical or virtual) Fabric within a physical\n           infrastructure.\n\n           In a Fabric conformant to versions earlier than FC-SW-4,\n           only a single Fabric could operate within a physical\n           infrastructure, and thus, the value of this Fabric Index\n           was defined to always be 1.')
t11FLockApplicationID = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1,1)).setFixedLength(1))
if mibBuilder.loadTexts: t11FLockApplicationID.setDescription("The Application_ID value that identifies the type of\n           application for which the Fabric is locked.\n\n           A lock established via Acquire Change Authorization (ACA)\n           does not, strictly speaking, have an Application_ID value.\n           However, the value 'FF'h (255 decimal) has been reserved\n           by T11 to be used as the value of this MIB object as and\n           when a lock is established by an ACA.  This value was\n           initially documented in a letter from the FC-SW-5 Editor\n           to T11.5, which was approved by the T11 and T11.5 plenary\n           meetings on October 5, 2006.")
t11FLockInitiatorType = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4,))).clone(namedValues=NamedValues(("other", 1), ("ssb", 2), ("cli", 3), ("snmp", 4),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockInitiatorType.setDescription('This object specifies what type of initiator generated\n           the request that caused this lock to be established:\n\n               other     - none of the following.\n\n\n\n               ssb       - this lock was established due to the\n                           receipt of an SSB, e.g., from a GS-5\n                           client.\n               cli       - this lock was established in order\n                           to process a Command Line Interface\n                           (CLI) command.\n               snmp      - this lock was established as a result\n                           of an SNMP SetRequest.\n           ')
t11FLockInitiator = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockInitiator.setDescription("This object specifies the initiator whose request\n           caused this lock to be established.\n\n           If the value of the corresponding instance\n           of t11FLockInitiatorType is 'ssb', this\n           object will contain the FC_ID of the client\n           that issued the Server Session Begin (SSB)\n           that required the lock to be established.\n\n           If the value of the corresponding instance\n           of t11FLockInitiatorType object is 'cli', this\n           object will contain the user name of the CLI\n           (Command Line Interface) user on whose behalf\n           the lock was established.\n\n           If the value of the corresponding instance of\n           t11FLockInitiatorType is 'snmp', this object\n           will contain the SNMP securityName used by the\n           SNMPv3 message containing the SetRequest that\n           created this row.  (If the row was created via\n           SNMPv1 or SNMPv2c, then the appropriate value of\n           the snmpCommunitySecurityName is used.)")
t11FLockInitiatorIpAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockInitiatorIpAddrType.setDescription("This object specifies the type of IP address contained\n           in the corresponding instance of t11FLockInitiatorIpAddr.\n           If the IP address of the location of the initiator is\n           unknown or not applicable, this object has the value:\n           'unknown'.")
t11FLockInitiatorIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockInitiatorIpAddr.setDescription("This object specifies the IP address of the location\n           of the initiator that established this lock via a\n           request of the type given by the corresponding instance\n           of t11FLockInitiatorType.  In cases where the\n           corresponding instance of t11FLockInitiatorIpAddrType has\n           the value: 'unknown', the value of this object is the\n           zero-length string.")
t11FLockStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4,))).clone(namedValues=NamedValues(("active", 1), ("settingUp", 2), ("rejectFailure", 3), ("otherFailure", 4),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockStatus.setDescription("This object gives the current status of the lock:\n\n              'active'        -- the lock is currently established.\n              'settingUp'     -- the 'managing' switch is currently\n                                 attempting to set up the lock, e.g.,\n                                 it is waiting to receive Accepts\n                                 for ACAs from every switch in the\n                                 Fabric.\n\n\n\n              'rejectFailure' -- the 'managing' switch's attempt to\n                                 set up the lock was rejected with\n                                 the reason codes given by:\n                                    t11FLockRejectReasonCode,\n                                    t11FLockRejectReasonCodeExp and\n                                    t11FLockRejectReasonVendorCode.\n              'otherFailure'  -- the 'managing' switch's attempt\n                                 to set up the lock failed (but no\n                                 reason codes are available).\n\n           For values of t11FLockInitiatorType other than 'snmp',\n           a row is only required to be instantiated in this table\n           when the value of this object is 'active'.\n\n           If the value of the corresponding instance of\n           t11FLockInitiatorType is 'snmp', the initial value of this\n           object when the row is first created is 'settingUp'.  As\n           and when the setup succeeds, the value transitions to\n           'active'.  If the setup fails, the value transitions to\n           either 'rejectFailure' or 'otherFailure'.  Note that such a\n           failure value is overwritten on the next attempt to obtain\n           the lock, which could be immediately after the failure,\n           e.g., by a GS-5 client.\n\n           When the value of this object is 'rejectFailure', the\n           rejection's reason codes are given by the corresponding\n           values of t11FLockRejectReasonCode,\n           t11FLockRejectReasonCodeExp and\n           t11FLockRejectReasonVendorCode.")
t11FLockRejectReasonCode = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 8), T11NsGs4RejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockRejectReasonCode.setDescription("When the value of the corresponding instance of\n           t11FLockStatus is 'rejectFailure', this object contains\n           the rejection's reason code.")
t11FLockRejectReasonCodeExp = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockRejectReasonCodeExp.setDescription("When the value of the corresponding instance of\n           t11FLockStatus is 'rejectFailure', this object contains\n           the rejection's reason code explanation.")
t11FLockRejectReasonVendorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FLockRejectReasonVendorCode.setDescription("When the value of the corresponding instance of\n           t11FLockStatus is 'rejectFailure', this object contains\n           the rejection's vendor-specific code.")
t11FLockRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FLockRowStatus.setDescription("The status of this conceptual row.\n\n           A row in this table can be modified or deleted via\n           this object only when the row's value of\n           t11FLockInitiatorType is 'snmp'.")
t11FLockMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 159, 2, 1))
t11FLockMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 159, 2, 2))
t11FLockMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 159, 2, 1, 1)).setObjects(*(("T11-FC-FABRIC-LOCK-MIB", "t11FLockActiveGroup"),))
if mibBuilder.loadTexts: t11FLockMIBCompliance.setDescription('The compliance statement for entities that support\n           Fabric locks in support of GS-5 Server applications.')
t11FLockActiveGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 159, 2, 2, 1)).setObjects(*(("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiatorType"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiator"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiatorIpAddrType"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiatorIpAddr"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockStatus"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRejectReasonCode"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRejectReasonCodeExp"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRejectReasonVendorCode"), ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRowStatus"),))
if mibBuilder.loadTexts: t11FLockActiveGroup.setDescription('A collection of objects containing information\n           about current Fabric locks.')
mibBuilder.exportSymbols("T11-FC-FABRIC-LOCK-MIB", t11FLockInitiatorIpAddrType=t11FLockInitiatorIpAddrType, t11FLockStatus=t11FLockStatus, t11FLockMIBNotifications=t11FLockMIBNotifications, t11FLockEntry=t11FLockEntry, t11FLockConfiguration=t11FLockConfiguration, t11FLockInitiatorType=t11FLockInitiatorType, t11FLockMIBCompliances=t11FLockMIBCompliances, t11FLockApplicationID=t11FLockApplicationID, t11FLockMIBConformance=t11FLockMIBConformance, t11FLockMIBCompliance=t11FLockMIBCompliance, t11FLockActiveGroup=t11FLockActiveGroup, t11FLockInitiatorIpAddr=t11FLockInitiatorIpAddr, t11FLockTable=t11FLockTable, t11FLockRejectReasonCode=t11FLockRejectReasonCode, t11FLockRejectReasonVendorCode=t11FLockRejectReasonVendorCode, t11FLockInitiator=t11FLockInitiator, PYSNMP_MODULE_ID=t11FabricLockMIB, t11FLockRowStatus=t11FLockRowStatus, t11FLockMIBGroups=t11FLockMIBGroups, t11FLockRejectReasonCodeExp=t11FLockRejectReasonCodeExp, t11FLockMIBObjects=t11FLockMIBObjects, t11FabricLockMIB=t11FabricLockMIB, t11FLockFabricIndex=t11FLockFabricIndex)