from flask import Flask, jsonify

app = Flask(__name__)


class ParsedInfo:
    def __init__(self, cat = "",
                 systemAreaCode = "", 
                 systemIdentificationCode = "",
                 ATP = "",
                 ARC = "",
                 RC = "",
                 RAB = "",
                 DCR = "",
                 GBS = "",
                 SIM = "",
                 TST = "",
                 SAA = "",
                 CL = "",
                 TargetReportDescriptor = "", 
                 TrackNumber = "", 
                 ServiceID = "", 
                 TimeofApplicabilityForPosition = 0,
                 TimeOfApplicVelocity = "", 
                 AirSpeed = "", 
                 TrueAirSpeed = "", 
                 TargetAddr = "", 
                 MessageReceptionOfPosTime = "", 
                 MessageReceptionOfPosTimeHighPres = "", 
                 MessageReceptionofVel = "", 
                 TimeMessageReceptionVelHighP = "", 
                 GeometricHeight = "", 
                 QualityIndicators = "", 
                 MOPSVers = "", 
                 Mode3ACode = "", 
                 RollAngle = "", 
                 FlightLevel = "", 
                 MagneticHeading = "", 
                 TargetStatus = "", 
                 BarometricVerticalRate = "", 
                 GeometricVerticalRate = "", 
                 AirborneGroundVector = "", 
                 TrackAngleRate = "", 
                 TimeReportTransmission = "", 
                 TargetIdentification = "", 
                 EmitterCategory = "",
                 MetInformation = "", 
                 SelectedAltitude = "", 
                 FinalStateSelectedAltitude = "", 
                 TrajIntent = "",
                 ServManagement = "", 
                 AircraftOpStatus = "", 
                 SurfaceCapabilitiesAndCharacteristics = "", 
                 MessageAmplitude = "", 
                 BDSRegisterData = "", 
                 ACASResAdvReport = "", 
                 ReceiverID = "", 
                 DataAges = "", 
                 ReservedExpansionField = "", 
                 SpecialPurposeField = "",
                 LLC = "",
                 IPC = "",
                 NOGO = "",
                 CPR = "",
                 LDPJ = "",
                 RCF = "",
                 TBC_EP = "",
                 TBC_Val = 0,
                 MBC_EP = "",
                 MBC_Val = 0,
                 messageLength = 0,
                 DELETE_EVERYTHING = "False"):
        self.cat = cat
        self.messageLength = messageLength
        self.systemAreaCode = systemAreaCode
        self.systemIdentificationCode = systemIdentificationCode
        self.TargetReportDescriptor = TargetReportDescriptor
        self.ATP = ATP
        self.ARC = ARC
        self.RC = RC
        self.RAB = RAB
        self.DCR = DCR,
        self.GBS = GBS,
        self.SIM = SIM,
        self.TST = TST,
        self.SAA = SAA,
        self.CL = CL,
        self.TrackNumber = TrackNumber
        self.ServiceID = ServiceID
        self.TimeofApplicabilityForPosition = TimeofApplicabilityForPosition
        self.PosWGS84Latitude = 0
        self.PosWGS84Longitude = 0
        self.PosWGS84HighResLat = 0
        self.PosWGS84HighResLong = 0
        self.TimeOfApplicVelocity = TimeOfApplicVelocity
        self.AirSpeed = AirSpeed
        self.TrueAirSpeed = TrueAirSpeed
        self.TargetAddr = TargetAddr
        self.MessageReceptionOfPosTime = MessageReceptionOfPosTime
        self.MessageReceptionOfPosTimeHighPres = MessageReceptionOfPosTimeHighPres
        self.MessageReceptionofVel = MessageReceptionofVel
        self.TimeMessageReceptionVelHighP = TimeMessageReceptionVelHighP
        self.GeometricHeight = GeometricHeight
        self.QualityIndicators = QualityIndicators
        self.MOPSVers = MOPSVers
        self.Mode3ACode = Mode3ACode
        self.RollAngle = RollAngle
        self.FlightLevel = FlightLevel
        self.MagneticHeading = MagneticHeading
        self.TargetStatus = TargetStatus
        self.BarometricVerticalRate = BarometricVerticalRate
        self.GeometricVerticalRate = GeometricVerticalRate
        self.AirborneGroundVector = AirborneGroundVector
        self.TrackAngleRate = TrackAngleRate
        self.TimeReportTransmission = TimeReportTransmission
        self.TargetIdentification = TargetIdentification
        self.EmitterCategory = EmitterCategory
        self.MetInformation = MetInformation
        self.SelectedAltitude = SelectedAltitude
        self.FinalStateSelectedAltitude = FinalStateSelectedAltitude
        self.TrajIntent = TrajIntent
        self.ServManagement = ServManagement
        self.AircraftOpStatus = AircraftOpStatus
        self.SurfaceCapabilitiesAndCharacteristics = SurfaceCapabilitiesAndCharacteristics
        self.MessageAmplitude = MessageAmplitude
        self.BDSRegisterData = BDSRegisterData
        self.ACASResAdvReport = ACASResAdvReport
        self.ReceiverID = ReceiverID
        self.DataAges = DataAges
        self.ReservedExpansionField = ReservedExpansionField
        self.SpecialPurposeField = SpecialPurposeField
        self.DELETE_EVERYTHING = DELETE_EVERYTHING
        self.LLC = LLC
        self.IPC = IPC
        self.NOGO = NOGO
        self.CPR = CPR
        self.LDPJ = LDPJ
        self.RCF = RCF
        self.TBC_EP = TBC_EP
        self.TBC_Val = TBC_Val
        self.MBC_EP = MBC_EP
        self.MBC_Val = MBC_Val
        self.NUCr = ""
        self.NUCp = ""
        self.NICbaro = ""
        self.SIL = ""
        self.NACp = ""
        self.SILS = ""
        self.SDA = ""
        self.GVA = ""
        self.PIC = ""
        self.VAL_STATE_EP = ""
        self.VAL_STATE_Val = ""
        self.VAL_DIST = 0
        self.VD = ""
        self.VQ = ""
        self.VAL_DIST_QUAL = 0
        self.tempVar = 0
        self.tempVar2 = 0
        self.tempVar3 = 0
        self.VNS = ""
        self.VN = ""
        self.LTT = ""
        self.USE_NEGATIVE_FORM_WGS84 = True
        self.ICF = ""
        self.LNAV = ""
        self.ME = ""
        self.PS = ""
        self.SS = ""

    def to_dict(self):

        testingString = {"Test1", "Test2"}
        return {"Cat": self.cat,
        "Intent Change flag": self.ICF,
        "LNAV Mode": self.LNAV,
        "Military Emergency": self.ME,
        "Priority Status": self.PS,
        "Surveillance Status": self.SS,
        "System area code": self.systemAreaCode,
        "Version Support": self.VNS,
        "Version Number": self.VN,
        "Link Technology Type": self.LTT,
        "System Identification Code": self.systemIdentificationCode,
        "TargetReportDescriptor": self.TargetReportDescriptor,
        "Address Type": self.ATP,
        "Position Integrity Category": self.PIC,
        "Validation Distance Availability": self.VD,
        "Validation Distance Quality": self.VQ,
        "SIL-Supplement": self.SILS,
        "Position Validation Distance": self.VAL_DIST,
        "Position Validation Distance Quality": self.VAL_DIST_QUAL,
        "Position Validation State Element Populated": self.VAL_STATE_EP,
        "VAL_STATE Value": self.VAL_STATE_Val,
        "Horizontal Position System Design Assurance Level": self.SDA,
        "Geometric Altitude Accurace": self.GVA,
        "Navigation Uncertainty Category for Velocity": self.NUCr,
        "Navigation Integrity Category": self.NUCp,
        "Navigation Accuracy Category for Position": self.NACp,
        "Navigation Integrity Category for Barometric Altitude": self.NICbaro,
        "Source Integrity Level": self.SIL,
        "Altitude Reporting Capability": self.ARC,
        "Range Check": self.RC,
        "RAB Report Type": self.RAB,
        "Differential Connection": self.DCR,
        "Ground Bit Setting": self.GBS,
        "Simulated Target": self.SIM,
        "Test Target": self.TST,
        "Selected Altitude Available": self.SAA,
        "Confidence Level": self.CL,
        "TrackNumber": self.TrackNumber,
        "ServiceID": self.ServiceID,
        "TimeOfApplicabilityForPosition": self.TimeofApplicabilityForPosition,
        "PosWGS84Lat": self.PosWGS84Latitude,
        "PosWGS84Long": self.PosWGS84Longitude,
        "PosWGS84HighResLat": self.PosWGS84HighResLat,
        "PosWGS84HighResLong": self.PosWGS84HighResLong,
        "TimeOfApplicVelocity":self.TimeOfApplicVelocity,
        "AirSpeed":self.AirSpeed,
        "TrueAirSpeed": self.TrueAirSpeed,
        "TargetAddr":self.TargetAddr,
        "MessageReceptionOfPosTime":self.MessageReceptionOfPosTime,
        "MessageReceptionOfPosTimeHighPres":self.MessageReceptionOfPosTimeHighPres,
        "MessageReceptionOfVel":self.MessageReceptionofVel,
        "MMessageReceptionOfVelHighP":self.TimeMessageReceptionVelHighP,
        "GeometricHeight":self.GeometricHeight,
        "QualityIndicators":self.QualityIndicators,
        "MOPSVers":self.MOPSVers,
        "Mode3ACode":self.Mode3ACode,
        "RollAngle":self.RollAngle,
        "FlightLevel":self.FlightLevel,
        "MagneticHeading":self.MagneticHeading,
        "TargetStatus":self.TargetStatus,
        "BarometricVerticalRate":self.BarometricVerticalRate,
        "GeometricVerticalRate":self.GeometricVerticalRate,
        "AirborneGroundVector":self.AirborneGroundVector,
        "TrackAngleRate":self.TrackAngleRate,
        "TimeReportTransmission":self.TimeReportTransmission,
        "TargetIdentification":self.TargetIdentification,
        "EmitterCategory":self.EmitterCategory,
        "MetInformation":self.MetInformation,
        "SelectedAltitude":self.SelectedAltitude,
        "FinalStateSelectedAltitude":self.FinalStateSelectedAltitude,
        "TrajIntent":self.TrajIntent,
        "ServManagement":self.ServManagement,
        "AircraftOpStatus":self.AircraftOpStatus,
        "SurfaceCapabilitiesAndCharacteristics":self.SurfaceCapabilitiesAndCharacteristics,
        "MessageAmplitude":self.MessageAmplitude,
        "BDSRegisterData":self.BDSRegisterData,
        "ACASResAdvReport":self.ACASResAdvReport,
        "ReceiverID":self.ReceiverID,
        "DataAges":self.DataAges,
        "ReservedExpansionField":self.ReservedExpansionField,
        "SpecialPurposeField":self.SpecialPurposeField,
        "List Lookup Check": self.LLC,
        "Independent Position Check": self.IPC,
        "No-go Bit Status": self.NOGO,
        "Compact Position Reporting": self.CPR,
        "Local Decoding Position Jump": self.LDPJ,
        "Range Check F": self.RCF,
        "Total Bits Corrected Element Populated": self.TBC_EP,
        "Total Bits Corrected Value": self.TBC_Val,
        "Maximum Bits Corrected Element Populated": self.MBC_EP,
        "Maximum Bits Corrected Value": self.MBC_Val,
        "Message Length": self.messageLength,
        "DELETE_EVERYTHING": self.DELETE_EVERYTHING}



def assignCAT(pushedInfo, assignTo: ParsedInfo):
    strToAdd = "CAT"
    strToAdd += str(pushedInfo)
    assignTo.cat = strToAdd
    return
def assignDataSource(pushedInfo, assignTo: ParsedInfo, firstOrSecond):
    match firstOrSecond:
        case "first":
            # NOTE: System Area Code refers to the ASTERIX list referred to here: http://www.eurocontrol.int/asterix
            # Assuming this will always be within the United States/Canada area. If not, then new implementations of this parser should fix this.
            if(pushedInfo <= 195 or pushedInfo >= 218):
                assignTo.systemAreaCode = "Reserved for United States"
            elif(pushedInfo <= 217):
                match pushedInfo:
                    case 0xD0:
                        assignTo.systemAreaCode = "Atlantic Provinces"
                    case 0xD1:
                        assignTo.systemAreaCode = "Quebec"
                    case 0xD2:
                        assignTo.systemAreaCode = "Ontario"
                    case 0xD3:
                        assignTo.systemAreaCode = "Spare"
                    case 0xD4:
                        assignTo.systemAreaCode = "Testing/Training Fcilities"
                    case 0xD5:
                        assignTo.systemAreaCode = "Central Provinces East"
                    case 0xD6:
                        assignTo.systemAreaCode = "Central Provinces West"
                    case 0xD7:
                        assignTo.systemAreaCode = "British Columbia Province"
                    case 0xD8:
                        assignTo.systemAreaCode = "Nunavut"
                    case 0xD9:
                        assignTo.systemAreaCode = "Northern Territory incl. Yukon"
                    case _:
                        #If none of the above:
                        assignTo.systemAreaCode = "Reserved for Canada"
        case "second":
            assignTo.systemIdentificationCode = pushedInfo

def assignTargetReportDescriptor(pushedInfo, assignTo: ParsedInfo, counter: int):
    match counter:
        case 0:
            # primary extension
            # bits 8-6: ATP
            ATP = 0
            ARC = 0
            RC = "default"
            RAB = "Report from Target Transponder"
            if(pushedInfo // 128 == 1):
                ATP += 4
                pushedInfo -= 128
            if(pushedInfo // 64 == 1):
                ATP += 2
                pushedInfo -= 64
            if(pushedInfo // 32 == 1):
                ATP += 1
                pushedInfo -= 32
            if(pushedInfo // 16 == 1):
                ARC += 2
                pushedInfo -= 16
            if(pushedInfo // 8 == 1):
                ARC += 1
                pushedInfo -= 8
            if(pushedInfo // 4 == 1):
                RC = "Range Check passed, CPR Validation pending"
                pushedInfo -= 4
            if(pushedInfo // 2 == 1):
                RAB = "Report from Field Monitor"
            
            assignTo.RC = RC
            assignTo.RAB = RAB
            match ARC:
                case 0:
                    ARC = "25 ft"
                case 1:
                    ARC = "100 ft"
                case 2:
                    ARC = "Unknown"
                case 3:
                    ARC = "Invalid"
            assignTo.ARC = ARC
            match ATP:
                case 0:
                    ATP = "24-Bit ICAO Address"
                case 1:
                    ATP = "Duplicate Address"
                case 2:
                    ATP = "Surface Vehicle Address"
                case 3:
                    ATP = "Anonymous Address"
                    # what's up (secret) fed boy
                case _:
                    # TODO: Should ATP become updated, add other cases in here
                    ATP = "Reserved for Future Use"


            assignTo.ATP = ATP

            
            print("Primary")
        case 1:
            DCR = "No differential correction"
            GBS = "Ground Bit not set"
            SIM = "Actual target report"
            TST = "Default"
            SAA = "Equipment capable to provide Selected Altitude"
            CL = 0
            if(pushedInfo // 128 == 1):
                DCR = "Differential Correction"
                pushedInfo -= 128
            if(pushedInfo // 64 == 1):
                GBS = "Ground Bit set"
                pushedInfo -= 64
            if(pushedInfo // 32 == 1):
                SIM = "Simulated target report"
                pushedInfo -= 32
            if(pushedInfo // 16 == 1):
                TST = "Test Target"
                pushedInfo -= 16
            if(pushedInfo // 8 == 1):
                SAA = "Equipment not capable to provide Selected Altitude"
                pushedInfo -= 8
            if(pushedInfo // 4 == 1):
                CL += 2
                pushedInfo -= 4
            if(pushedInfo // 2 == 1):
                CL += 1
            assignTo.SAA = SAA
            assignTo.TST = TST
            assignTo.SIM = SIM
            assignTo.GBS = GBS
            assignTo.DCR = DCR
            match CL:
                case 0:
                    assignTo.CL = "Report valid"
                case 1:
                    assignTo.CL = "Report suspect"
                case 2:
                    assignTo.CL = "No Information"
                case 3:
                    assignTo.CL = "Reserved for future use"
            print("Extension 1")
        case 2:
            print("Extension 2")
            LLC = "Black-List/White-List clear"
            IPC = "Independent validation not performed/cleared"
            NOGO = "NOGO bit not set"
            CPR = "CPR validation correct"
            LDPJ = "LDPJ not detected"
            RCF = "default"
            if(pushedInfo // 128 == 1):
                # Never happens - spare bit, always set to 0
                # Just in case, going to subtract 128 if this is the case
                # TODO: Fix this if something changes
                print("ERROR: UNEXPECTED BIT SET TO 1")
                print("ENDING PARSE")
                assignTo.DELETE_EVERYTHING = True
                return -1
            if(pushedInfo//64 == 1):
                LLC = "Target Suspect - check Black-List/White-List"
                pushedInfo -= 64
            if(pushedInfo//32 == 1):
                IPC = "Independent validation performed: Discrepancy detected"
                pushedInfo -= 32
            if(pushedInfo//16 == 1):
                # TODO: Ask Kay about this - I023 not found in Asterix file
                NOGO = "NOGO bit set in item I023/100"
                pushedInfo -= 16
            if(pushedInfo//8 == 1):
                CPR = "CPR Validation failed"
            if(pushedInfo // 4 == 1):
                # TODO: Ask Kay about Position Jumps
                LDPJ = "LDPJ detected - likely error in "
            if(pushedInfo // 2 == 1):
                RCF = "Range Check failed"

            assignTo.LLC = LLC
            assignTo.IPC = IPC
            assignTo.NOGO = NOGO
            assignTo.CPR = CPR
            assignTo.LDPJ = LDPJ
            assignTo.RCF = RCF

                

            
        case 3:
            print("Extension 3")
            pushedInfo = pushedInfo >> 1
            if(pushedInfo // 64 == 1):
                assignTo.TBC_EP = "Element Populated"
                pushedInfo -= 64
                assignTo.TBC_Val = pushedInfo
            else:
                assignTo.TBC_EP = "Element not populated"

        case 4:
            print("Extension 4")
            pushedInfo = pushedInfo >> 1
            if(pushedInfo // 64 == 1):
                assignTo.MBC_EP = "Element Populated"
                pushedInfo -= 64
                assignTo.MBC_Val = pushedInfo
            else:
                assignTo.MBC_EP = "Element not populated"


        


    return 1



def assignTrackNumber(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TrackNumber = "TODO"
    return

def assignServiceID(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.ServiceID = "TODO"
    return

def assignTimeOfApplicabilityForPosition(pushedInfo: int, assignTo: ParsedInfo, i):

    match i:
        case 0:
            pushedInfo = pushedInfo * (2 ** 8)
            assignTo.TimeofApplicabilityForPosition = float(pushedInfo)
            print("Time check 1", type(assignTo.TimeofApplicabilityForPosition))
        case 1:
            print("type check", type(assignTo.TimeofApplicabilityForPosition))
            currentTime = float(assignTo.TimeofApplicabilityForPosition)
            currentTime += float(pushedInfo)
            assignTo.TimeofApplicabilityForPosition = currentTime
            print("Time check 2", assignTo.TimeofApplicabilityForPosition)
        case 2:
            pushedInfo = pushedInfo / 128
            assignTo.TimeofApplicabilityForPosition += pushedInfo
            print("Time check 3", assignTo.TimeofApplicabilityForPosition)
    return

def assignPosWGS84(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            print("Lattitude most significant int: ", pushedInfo)
            assignTo.tempVar = pushedInfo
        case 1:
            print("Lattitude int 2: ", pushedInfo)
            assignTo.tempVar2 = pushedInfo
        case 2:
            
            print("Lattitude int 3: ", pushedInfo)

            # TODO I GOT NO CLUE HOW THIS STUFF SHOULD BE WORKING AHHHHHHHH
            middle8 = assignTo.tempVar2
            assignTo.tempVar2 = 0

            front8 = assignTo.tempVar
            assignTo.tempVar = 0





            # Idea: Instead of doing subtraction, convert from signed to unsigned using byte translation

            assignTo.PosWGS84Latitude = pushedInfo
            if(not assignTo.USE_NEGATIVE_FORM_WGS84):
                assignTo.PosWGS84Latitude = -1 * assignTo.PosWGS84Latitude
            assignTo.tempVar = 0
        case 3:
            print("Longitude most significant int: ", pushedInfo)
            assignTo.tempVar = pushedInfo
        case 4:
            print("Longitude int 2: ", pushedInfo)
            assignTo.tempVar2 = pushedInfo
        case 5:
            print("Longitude int 3: ", pushedInfo)

            # TODO I GOT NO CLUE HOW THIS STUFF SHOULD BE WORKING AHHHHHHHH
            middle8 = assignTo.tempVar2
            assignTo.tempVar2 = 0

            front8 = assignTo.tempVar
            assignTo.tempVar = 0





            # Idea: Instead of doing subtraction, convert from signed to unsigned using byte translation

            assignTo.PosWGS84Latitude = pushedInfo
            if(not assignTo.USE_NEGATIVE_FORM_WGS84):
                assignTo.PosWGS84Latitude = -1 * assignTo.PosWGS84Latitude
            assignTo.tempVar = 0


    return

def assignPosWGS84HighRes(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            print("Lattitude most significant int: ", pushedInfo)
            assignTo.tempVar = pushedInfo
        case 1:
            print("Lattitude int 2: ", pushedInfo)
            assignTo.tempVar2 = pushedInfo
        case 2:
            
            print("Lattitude int 3: ", pushedInfo)
            assignTo.tempVar3 = pushedInfo

            
        case 3:
            # TODO I GOT NO CLUE HOW THIS STUFF SHOULD BE WORKING AHHHHHHHH

            print("Lattitude int 4: ", pushedInfo)

            frontback8 = assignTo.tempVar3
            assignTo.tempVar3 = 0 



            frontmiddle8 = assignTo.tempVar2
            assignTo.tempVar2 = 0

            front8 = assignTo.tempVar
            assignTo.tempVar = 0





            # Idea: Instead of doing subtraction, convert from signed to unsigned using byte translation

            assignTo.PosWGS84Latitude = pushedInfo
            if(not assignTo.USE_NEGATIVE_FORM_WGS84):
                assignTo.PosWGS84Latitude = -1 * assignTo.PosWGS84Latitude
            assignTo.tempVar = 0
        case 4:
            print("Longitude int 1: ", pushedInfo)
            assignTo.tempVar = pushedInfo
        case 5:
            print("Longitude int 2: ", pushedInfo)

            assignTo.tempVar2 = pushedInfo
        case 6:
            print("Longitude int 3: ", pushedInfo)
            assignTo.tempVar3 = pushedInfo
        
        case 7:
            print("Longitude int 4: ", pushedInfo)

            # TODO I GOT NO CLUE HOW THIS STUFF SHOULD BE WORKING AHHHHHHHH

            frontback8 = assignTo.tempVar3
            assignTo.tempVar3 = 0 



            frontmiddle8 = assignTo.tempVar2
            assignTo.tempVar2 = 0

            front8 = assignTo.tempVar
            assignTo.tempVar = 0





            # Idea: Instead of doing subtraction, convert from signed to unsigned using byte translation

            assignTo.PosWGS84Latitude = pushedInfo
            if(not assignTo.USE_NEGATIVE_FORM_WGS84):
                assignTo.PosWGS84Latitude = -1 * assignTo.PosWGS84Latitude
            assignTo.tempVar = 0


    return


def assignTimeOfApplicVelocity(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TimeOfApplicVelocity = "TODO"
    return

def assignAirSpeed(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.AirSpeed = "TODO"
    return

def assignTrueAirSpeed(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TrueAirSpeed = "TODO"
    return

def assignTargetAddr(pushedInfo, assignTo: ParsedInfo, i):

    match i:
        case 0:
            pushedInfo = pushedInfo * 256 * 256
            assignTo.TargetAddr = pushedInfo
        case 1:
            pushedInfo = pushedInfo * 256
            assignTo.TargetAddr += pushedInfo
        case 2:
            assignTo.TargetAddr += pushedInfo


    return

def assignMessageReceptionOfPosTime(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            assignTo.MessageReceptionOfPosTime = pushedInfo * (2 ** 10)
        case 1:
            assignTo.MessageReceptionOfPosTime += pushedInfo * 2
        case 2:
            assignTo.MessageReceptionOfPosTime += pushedInfo * (2 ** -7)
    return

def assignMessageReceptionOfPosTimeHighPres(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MessageReceptionOfPosTimeHighPres = "TODO"
    return

def assignMessageReceptionofVel(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            assignTo.MessageReceptionofVel = pushedInfo * (2 ** 10)
        case 1:
            assignTo.MessageReceptionofVel += pushedInfo * 2
        case 2:
            assignTo.MessageReceptionofVel += pushedInfo * (2 ** -7)
    return
    return

def assignTimeMessageReceptionVelHighP(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TimeMessageReceptionVelHighP = "TODO"
    return

def assignGeometricHeight(pushedInfo, assignTo: ParsedInfo, counter):
    match counter:
        case 0:
            assignTo.GeometricHeight = pushedInfo * 256
        case 1: 
            assignTo.GeometricHeight += pushedInfo
    return

def assignQualityIndicators(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            # First primary subfield


            # There is a faster way to calc NUCr that takes up less lines
            # This is the readable form - bit-by-bit

            #if(pushedInfo // 128 == 1):
            #    assignTo.NUCr += 4
            #    pushedInfo -= 128
            #if(pushedInfo // 64 == 1):
            #    assignTo.NUCr += 2
            #    pushedInfo -= 64
            #if(pushedInfo // 32 == 1):
            #    assignTo.NUCr += 1

            # Here is the faster way to do so:
            assignTo.NUCr = pushedInfo // 32
            pushedInfo -= assignTo.NUCr * 32

            assignTo.NUCp = pushedInfo // 2
            pushedInfo -= assignTo.NUCp * 2
        case 1:
            assignTo.NICbaro = pushedInfo // 128
            pushedInfo -= assignTo.NICbaro * 128

            assignTo.SIL = pushedInfo // 32
            pushedInfo -= assignTo.SIL * 32

            assignTo.NACp = pushedInfo // 2
            pushedInfo -= assignTo.NACp * 2
        case 2:
            if(pushedInfo // 32 == 1):
                assignTo.SILS = "Measured per flight-hour"
                pushedInfo -= 32
            else:
                assignTo.SILS = "Measured per sample"
            
            assignTo.SDA = pushedInfo // 8
            pushedInfo -= assignTo.SDA * 8

            assignTo.GVA = pushedInfo // 2
            pushedInfo -= assignTo.GVA * 2
        case 3:
            # Don't understand what the PIC stuff is asking, storing values, 
            # not super important for the project, can be done later TODO
            assignTo.PIC = pushedInfo // 16
            pushedInfo -= assignTo.PIC * 16

            assignTo.SRC = pushedInfo // 8
        case 4:
            assignTo.VAL_STATE_EP = pushedInfo // 32
            pushedInfo -= assignTo.VAL_STATE_EP * 32

            if(pushedInfo // 8 == 0):
                assignTo.VAL_STATE_Val = "Validation not performed"
            elif (pushedInfo // 8 == 1):
                assignTo.VAL_STATE_Val = "Validation performed without pass/fail"
                pushedInfo -= 8
            elif (pushedInfo // 8 == 2):
                assignTo.VAL_STATE_Val = "Validation pass"
                pushedInfo -= 16
            elif (pushedInfo // 8 == 3): 
                assignTo.VAL_STATE_Val = "Validation fail"
                pushedInfo -= 24
            
            assignTo.VD = pushedInfo // 4
            pushedInfo -= assignTo.VD * 4

            assignTo.VQ = pushedInfo // 2
            pushedInfo -= assignTo.VQ * 2
        case 5:
            # multiply by 128 and set num to this
            pushedInfo = pushedInfo // 2
            pushedInfo = pushedInfo * 128
            assignTo.VAL_DIST = pushedInfo
        case 6:
            assignTo.VAL_DIST += (pushedInfo // 2)
        case 7:
            pushedInfo = pushedInfo // 2
            pushedInfo = pushedInfo * 128
            assignTo.VAL_DIST_QUAL = pushedInfo
        case 8:
            assignTo.VAL_DIST_QUAL += (pushedInfo // 2)



        
            


            



    return

def assignMOPSVers(pushedInfo, assignTo: ParsedInfo):
    if(pushedInfo // 64 == 1):
        assignTo.VNS = "MOPS version not supported"
        pushedInfo -= 64
    else:
        assignTo.VNS = "MOPS version supported"


    if(pushedInfo // 8 == 0):
        assignTo.VN = "ED102/DO-260"
    elif(pushedInfo // 8 == 1):
        assignTo.VN = "DO-260A"
        pushedInfo -= 8
    elif(pushedInfo // 8 == 2):
        assignTo.VN = "ED102A/DO-260B"
        pushedInfo -= 16
    elif(pushedInfo // 8 == 3):
        assignTo.VN = "ED-102B/DO-260C"
        pushedInfo -= 24


    if(pushedInfo == 0):
        assignTo.LTT = "Other"
    elif(pushedInfo == 1):
        assignTo.LTT = "UAT"
    elif(pushedInfo == 2):
        assignTo.LTT = "1090 ES"
    elif(pushedInfo == 3):
        assignTo.LTT = "VDL 4"
    else:
        assignTo.LTT = "Not Assigned"
    return

def assignMode3ACode(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            assignTo.tempVar = pushedInfo * 256
        case 1:
            pushedInfo += assignTo.tempVar
            pushedInfo = oct(pushedInfo)
            
            assignTo.Mode3ACode = pushedInfo

    return

def assignRollAngle(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.RollAngle = "TODO"
    return

def assignFlightLevel(pushedInfo, assignTo: ParsedInfo, i):
    match i:
        case 0:
            print("Case 0")
            # Figure out 2's compliment then come back to this
        case 1:
            print("Case 1")
            # See above
    return

def assignMagneticHeading(pushedInfo, assignTo: ParsedInfo, counter):

    match counter:
        case 0:
            assignTo.MagneticHeading = pushedInfo * 256
        case 1:
            assignTo.MagneticHeading += pushedInfo
            assignTo.MagneticHeading = assignTo.MagneticHeading * 360 / (2**16)
    return

def assignTargetStatus(pushedInfo, assignTo: ParsedInfo):
    if(pushedInfo // 128 == 1):
        assignTo.ICF = "Intent change flag raised"
        pushedInfo -= 128
    else:
        assignTo.ICF = "No intent change active"

    if(pushedInfo // 64 == 1):
        assignTo.LNAV = "LNAV mode not engaged"
        pushedInfo -= 64
    else:
        assignTo.LNAV = "LNAV mode engaged"
    
    if(pushedInfo // 32 == 1):
        assignTo.ME = "Military emergency"
        pushedInfo -= 32
    else:
        assignTo.ME = "No military emergency"

    if(pushedInfo // 4 == 0):
        assignTo.PS = "No emergency/not reported"
    elif(pushedInfo // 4 == 1):
        assignTo.PS = "General emergency"
        pushedInfo -= 4
    elif(pushedInfo // 4 == 2):
        assignTo.PS = "Lifeguard/medical emergency"
        pushedInfo -= 8
    elif(pushedInfo // 4 == 3):
        assignTo.PS = "Minimum fuel"
        pushedInfo -= 12
    elif(pushedInfo // 4 == 4):
        assignTo.PS = "No communications"
        pushedInfo -= 16
    elif(pushedInfo // 4 == 5):
        assignTo.PS = "Unlawful interference"
        pushedInfo -= 20
    elif(pushedInfo // 4 == 6):
        assignTo.PS = "Aircraft in distress - automatic activation"
        pushedInfo -= 24
    elif(pushedInfo // 4 == 7):
        assignTo.PS = "Aircraft in distress - manual activation"
        pushedInfo -= 28
    

    if(pushedInfo == 0):
        assignTo.SS = "No condition reported"
    elif(pushedInfo == 1):
        assignTo.SS = "Permanent alert (emergency condition)"
    elif(pushedInfo == 2):
        assignTo.SS = "Temporary alert"
    elif(pushedInfo == 3):
        assignTo.SS = "SPI set"
    
    

    return

def assignBarometricVerticalRate(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.BarometricVerticalRate = "TODO"
    return

def assignGeometricVerticalRate(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.GeometricVerticalRate = "TODO"
    return

def assignAirborneGroundVector(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.GeometricVerticalRate = "TODO"
    return

def assignTrackAngleRate(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TrackAngleRate = "TODO"
    return

def assignTimeReportTransmission(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TrackAngleRate = "TODO"
    return

def assignTargetIdentification(pushedInfo, assignTo: ParsedInfo, i):
    character = 0
    match i % 3:
        case 0:
            assignTo.tempVar = 0
            if(pushedInfo // 128 == 1):
                character += 32
                pushedInfo -= 128
            if(pushedInfo // 64 == 1):
                character += 16
                pushedInfo -= 64
            if(pushedInfo // 32 == 1):
                character += 8
                pushedInfo -= 32
            if(pushedInfo // 16 == 1):
                character += 4
                pushedInfo -= 16
            if(pushedInfo // 8 == 1):
                character += 2
                pushedInfo -= 8
            if(pushedInfo // 4 == 1):
                character += 1
                pushedInfo -= 4
            if(pushedInfo // 2 == 1):
                assignTo.tempVar += 32
            if(pushedInfo % 2 == 1):
                assignTo.tempVar += 16
            assignTo.TargetIdentification += chr(character)
            print("Assigning character: ", chr(character))
        case 1:
            character = assignTo.tempVar
            assignTo.tempVar = 0
            if(pushedInfo // 128 == 1):
                character += 8
                pushedInfo -= 128
            if(pushedInfo // 64 == 1):
                character += 4
                pushedInfo -= 64
            if(pushedInfo // 32 == 1):
                character += 2
                pushedInfo -= 32
            if(pushedInfo // 16 == 1):
                character += 1
                pushedInfo -= 16
            if(pushedInfo // 8 == 1):
                assignTo.tempVar += 32
                pushedInfo -= 8
            if(pushedInfo // 4 == 1):
                assignTo.tempVar += 16
                pushedInfo -= 4
            if(pushedInfo // 2 == 1):
                assignTo.tempVar += 8
            if(pushedInfo % 2 == 1):
                assignTo.tempVar += 4
            assignTo.TargetIdentification += chr(character)
            print("Assigning character: ", chr(character))
        case 2:
            character = assignTo.tempVar
            assignTo.tempVar = 0
            if(pushedInfo // 128 == 1):
                character += 2
                pushedInfo -= 128
            if(pushedInfo // 64 == 1):
                character += 1
                pushedInfo -= 64
            if(pushedInfo // 32 == 1):
                assignTo.tempVar += 32
                pushedInfo -= 32
            if(pushedInfo // 16 == 1):
                assignTo.tempVar += 16
                pushedInfo -= 16
            if(pushedInfo // 8 == 1):
                assignTo.tempVar += 8
                pushedInfo -= 8
            if(pushedInfo // 4 == 1):
                assignTo.tempVar += 4
                pushedInfo -= 4
            if(pushedInfo // 2 == 1):
                assignTo.tempVar += 2
            if(pushedInfo % 2 == 1):
                assignTo.tempVar += 1
            assignTo.TargetIdentification += chr(character)
            assignTo.TargetIdentification += chr(assignTo.tempVar)
            print("Assigning character: ", chr(character))
            assignTo.tempVar = 0

        


    return

def assignEmitterCategory(pushedInfo, assignTo: ParsedInfo):
    
    ECAT = ""
    match pushedInfo:
        case 0:
            ECAT = "no ADS-B ECAT info"
        case 1:
            # ECAT = "Light Aircraft (x <= 15500 lbs)"
            ECAT = "Light Aircraft"
        case 2:
            # ECAT = "Small Aircraft (15500 lbs < x < 750000 lbs)"
            ECAT = "Small Aircraft"
        case 3:
            # ECAT = "Medium Aircraft (75000 lbs < x < 300000 lbs)"
            ECAT = "Medium Aircraft"
        case 4:
            ECAT = "High Vortex Large"
        case 5:
            # ECAT = "Heavy Aircraft (300000 <= x)"
            ECAT = "Heavy Aircraft"
        case 6:
            # ECAT = "Highly Manoeuvrable and High Speed (5g acceleration capability, >400 knots cruise)"
            ECAT = "Highly Manoeuvrable and High Speed"
        case 7:
            ECAT = "Reserved"
        case 8:
            ECAT = "Reserved"
        case 9:
            ECAT = "Reserved"
        case 10:
            ECAT = "Rotocraft"
        case 11:
            ECAT = "Glider/Sailplane"
        case 12:
            ECAT = "Lighter-than-air"
        case 13:
            ECAT = "Unmanned aerial vehicle"
        case 14:
            ECAT = "Space/Transatmospheric vehicle"
        case 15:
            ECAT = "Ultralight/Handglider/Paraglider"
        case 16:
            ECAT = "Parachutist/Skydiver"
        case 17:
            ECAT = "Reserved"
        case 18:
            ECAT = "Reserved"
        case 19:
            ECAT = "Reserved"
        case 20:
            ECAT = "Surface emergency vehicle"
        case 21:
            ECAT = "Surface service vehicle"
        case 22:
            ECAT = "Fixed ground or tethered obstruction"
        case 23:
            ECAT = "cluster obstacle"
        case 24:
            ECAT = "line obstacle"
        case _:
            ECAT = "Unassigned"

    
    assignTo.EmitterCategory = ECAT
    return

def assignMetInformation(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MetInformation = "TODO"
    return

def assignSelectedAltitude(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.SelectedAltitude = "TODO"
    return

def assignFinalStateSelectedAltitude(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.FinalStateSelectedAltitude = "TODO"
    return

def assignTrajIntent(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TrajIntent = "TODO"
    return

def assignServManagement(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.ServManagement = "TODO"
    return

def assignAircraftOpStatus(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.AircraftOpStatus = "TODO"
    return

def assignSurfaceCapabilitiesAndCharacteristics(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.SurfaceCapabilitiesAndCharacteristics = "TODO"
    return

def assignMessageAmplitude(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MessageAmplitude = "TODO"
    return

def assignBDSRegisterData(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.BDSRegisterData = "TODO"
    return

def assignACASResAdvReport(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.ACASResAdvReport = "TODO"
    return

def assignReceiverID(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.ReceiverID = "TODO"
    return

def assignDataAges(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.DataAges = "TODO"
    return

def assignReservedExpansionField(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.ReservedExpansionField = "TODO"
    return

def assignSpecialPurposeField(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.SpecialPurposeField = "TODO"
    return

def getNewInfo(pushedInfoList):
    #TODO - popping new info and returning it, but also error checking beforehand. 
    # Needs while loop to make sure of str len 2, along with a try/except of translating from string to hex representation of an int

    while(len(pushedInfoList) > 0):
        newInfo = pushedInfoList.pop()
        print("Testing: ", newInfo)
        while(len(str(newInfo)) != 2):
            newInfo = pushedInfoList.pop()
            print("Testing: ", newInfo)
        try:
            newInfo = int(newInfo, 16)
            print("Found info: ", newInfo)
            return newInfo
        except:
            print("new info not able to be swapped")

    return -1


def parse(pushedInfo: str):

    pushedInfo = pushedInfo.split(" ")
    # Pop method goes from back to front, so for ease of complexity's sake we're reversing the list
    pushedInfo.reverse()


    thisMessage = ParsedInfo()

    print(pushedInfo)
    currentState = "Start"
    stateList = []
    while(len(pushedInfo) > 0):
        print("============================")
        infoToPush = getNewInfo(pushedInfo)
        print(f"Info: {infoToPush}")
        match currentState:
            case "Start":
                print("CAT Assigned:")
                assignCAT(infoToPush, thisMessage)
                print(thisMessage.cat)

                # Deals with length: not needed to be found since python already has libraries that find this information
                # and we already use this information to build the byte array
                length = getNewInfo(pushedInfo) * 256
                # two octets (bytes)
                length += getNewInfo(pushedInfo)
                thisMessage.length = length
                # Next information is the fspec
                currentState = "First fspec"
            case "First fspec":
                # if the info to push modulo 2 == 1, then we set current state to Second fspec after adding things into statelist
                # if info to push modulo 2 == 0, then we move to the next state in State List
                # Repeat for fspec up to 7 times
                print("First fspec")
                if(infoToPush // 128 == 1):
                    stateList.append("Data Source Identification")
                    infoToPush -= 128
                if(infoToPush // 64 == 1):
                    stateList.append("Target Report Descripton")
                    infoToPush -= 64
                if(infoToPush // 32 == 1):
                    stateList.append("Track Number")
                    infoToPush -= 32
                if(infoToPush // 16 == 1):
                    stateList.append("Service ID")
                    infoToPush -= 16
                if(infoToPush // 8 == 1):
                    stateList.append("Time of Applicability for Position")
                    infoToPush -= 8
                if(infoToPush // 4 == 1):
                    stateList.append("Position in WGS-84 co-ordinates")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Position in WGS-84 coords high res")


                # After going through the bytes:
                if(infoToPush % 2 == 1):
                    currentState = "Second fspec"
                else:
                    
                    stateList.reverse()
                    currentState = stateList.pop()
            case "Second fspec":
                print("Second fspec")

                if(infoToPush // 128 == 1):
                    stateList.append("Time of Applicability for Velocity")
                    infoToPush -= 128
                if(infoToPush // 64 == 1):
                    stateList.append("Air Speed")
                    infoToPush -= 64
                if(infoToPush // 32 == 1):
                    stateList.append("True Air Speed")
                    infoToPush -= 32
                if(infoToPush // 16 == 1):
                    stateList.append("Target Address")
                    infoToPush -= 16
                if(infoToPush // 8 == 1):
                    stateList.append("Time of Message Reception for Position")
                    infoToPush -= 8
                if(infoToPush // 4 == 1):
                    stateList.append("Time of Message Reception for Position High Precision")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Time of Message Reception of Velocity")
                if(infoToPush % 2 == 1):
                    currentState = "Third fspec"
                else:
                    
                    stateList.reverse()
                    currentState = stateList.pop()

            case "Third fspec":
                print("Third fspec")
                if(infoToPush // 128 == 1):
                    stateList.append("Time of Message Reception of Velocity High Precision")
                    infoToPush -= 128
                if(infoToPush // 64 == 1):
                    stateList.append("Geometric Height")
                    infoToPush -= 64
                if(infoToPush // 32 == 1):
                    stateList.append("Quality Indicators")
                    infoToPush -= 32
                if(infoToPush // 16 == 1):
                    stateList.append("MOPS version")
                    infoToPush -= 16
                if(infoToPush // 8 == 1):
                    stateList.append("Mode 3A Code")
                    infoToPush -= 8
                if(infoToPush // 4 == 1):
                    stateList.append("Roll Angle")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Flight Level")
                if(infoToPush % 2 == 1):
                    currentState = "Fourth fspec"
                else:
                    
                    stateList.reverse()
                    currentState = stateList.pop()

            case "Fourth fspec":
                print("Fourth fspec")
                if(infoToPush // 128 == 1):
                    stateList.append("Magnetic Heading")
                    infoToPush -= 128
                if(infoToPush // 64 == 1):
                    stateList.append("Target Status")
                    infoToPush -= 64
                if(infoToPush // 32 == 1):
                    stateList.append("Barometric Vertical Rate")
                    infoToPush -= 32
                if(infoToPush // 16 == 1):
                    stateList.append("Geometric Vertical Rate")
                    infoToPush -= 16
                if(infoToPush // 8 == 1):
                    stateList.append("Airborne Ground Vector")
                    infoToPush -= 8
                if(infoToPush // 4 == 1):
                    stateList.append("Track Angle Rate")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Time of Report Transmission")
                if(infoToPush % 2 == 1):
                    currentState = "Fifth fspec"
                else:
                    
                    stateList.reverse()
                    currentState = stateList.pop()
            
            case "Fifth fspec":
                print("Fifth fspec")
                if(infoToPush // 128 == 1):
                    stateList.append("Target Identification")
                    infoToPush -= 128
                if(infoToPush // 64 == 1):
                    stateList.append("Emitter Category")
                    infoToPush -= 64
                if(infoToPush // 32 == 1):
                    stateList.append("Met Information")
                    infoToPush -= 32
                if(infoToPush // 16 == 1):
                    stateList.append("Selected Altitude")
                    infoToPush -= 16
                if(infoToPush // 8 == 1):
                    stateList.append("Final State Selected Altitude")
                    infoToPush -= 8
                if(infoToPush // 4 == 1):
                    stateList.append("Trajectory Intent")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Service Management")
                if(infoToPush % 2 == 1):
                    currentState = "Sixth fspec"
                else:
                    
                    stateList.reverse()
                    currentState = stateList.pop()
                print("----------")
            
            case "Sixth fspec":
                print("Sixth fspec")
                if(infoToPush // 128 == 1):
                    stateList.append("Aircraft Operational Status")
                    infoToPush -= 128
                if(infoToPush // 64 == 1):
                    stateList.append("Surface Capabilities and Characteristics")
                    infoToPush -= 64
                if(infoToPush // 32 == 1):
                    stateList.append("Message Amplitude")
                    infoToPush -= 32
                if(infoToPush // 16 == 1):
                    stateList.append("BDS Register Data")
                    infoToPush -= 16
                if(infoToPush // 8 == 1):
                    stateList.append("ACAS Resolution Advisory Report")
                    infoToPush -= 8
                if(infoToPush // 4 == 1):
                    stateList.append("Receiver ID")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Data Ages")
                if(infoToPush % 2 == 1):
                    currentState = "Seventh fspec"
                else:
                    stateList.reverse()
                    currentState = stateList.pop()
                print("------------")

            case "Seventh fspec":
                print("Seventh fspec")
                if(infoToPush // 8 == 1):
                    thisMessage.DELETE_EVERYTHING = True
                    currentState = "ERROR"
                if(infoToPush // 4 == 1):
                    stateList.append("Received Expansion Field")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Special Purpose Field")
                if(infoToPush % 2 == 1):
                    thisMessage.DELETE_EVERYTHING = True
                    currentState = "ERROR"
                    return thisMessage

                print("FSPEC finished, stateList: ", str(stateList))
                stateList.reverse()
                currentState = stateList.pop()
                

            case "MOPS Version":
                assignMOPSVers(infoToPush, thisMessage)
                infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()

            case "Flight Level":
                for i in range(0, 2):
                    assignFlightLevel(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()
            
            case "Data Source Identification":
                # 
                assignDataSource(infoToPush, thisMessage, "first")
                infoToPush = pushedInfo.pop()
                while(len(str(infoToPush)) != 2):
                    # Use the string length in order to determine whether this is actually something we need or not
                    infoToPush = pushedInfo.pop()
                infoToPush = int(infoToPush, 16)
                
                assignDataSource(infoToPush, thisMessage, "second")
                currentState = stateList.pop()
            # Data needed to display:
            # TODO IMPORTANTINFO
            # Altitude (Geometric Height X, )
            # Speed (Air Speed, True Air Speed, )
            # Heading (Magnetic Heading X, )
            # GPS Location (Position in WGS-84 Coordinates, Position in WGS-84 Coordinates)
            # Time I021/072 I021/077
            # Aircraft ID
            # Tail number (Target Identification)
            # Vehicle Type/ground vehicle? (Emitter Category X)
            # 
            # 


            case "Target Status":
                assignTargetStatus(infoToPush, thisMessage)
                infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()

            case "Quality Indicators":
                keepRunning = True
                i = 0
                while(keepRunning):
                    if(infoToPush % 2 == 0):
                        keepRunning = False # We've found the last extension - no need to keep going
                    assignQualityIndicators(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                    i += 1 # Next field extension if needed
                currentState = stateList.pop()


            
            case "Time of Applicability for Position":
                for i in range(0, 2):
                    assignTimeOfApplicabilityForPosition(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()
            case "Target Report Descripton":
                hasValues = True
                counter = 0
                while(hasValues):


                    if(infoToPush % 2 == 1):
                        # Extension case - hasValues doesn't update, 
                        assignTargetReportDescriptor(infoToPush, thisMessage, counter)
                        counter += 1
                        infoToPush = pushedInfo.pop()
                        while(len(str(infoToPush)) != 2):
                            # Use the string length in order to determine whether this is actually something we need or not
                            infoToPush = pushedInfo.pop()
                        infoToPush = int(infoToPush, 16)
                        print("New Info: ", infoToPush)
                        if(counter == 5):
                            print("ERROR DETECTED: TOO MANY EXTENSIONS")
                            thisMessage.DELETE_EVERYTHING = True
                            return thisMessage

                    else:
                        currentState = stateList.pop()
                        assignTargetReportDescriptor(infoToPush, thisMessage, counter)
                        print("New Info: ", infoToPush)
                        hasValues = False
            case "Position in WGS-84 co-ordinates":
                for i in range(0, 6):
                    #do this
                    assignPosWGS84(infoToPush, thisMessage, i)
                    #newInfo
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()
            
            case "Position in WGS-84 coords high res":
                for i in range(0, 8):
                    assignPosWGS84HighRes(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()

            case "Target Address":
                for i in range(0, 3):
                    assignTargetAddr(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()

            case "Time of Message Reception for Position":
                for i in range(0, 3):
                    assignMessageReceptionOfPosTime(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()

            case "Time of Message Reception of Velocity":
                for i in range(0, 3):
                    assignMessageReceptionofVel(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                currentState = stateList.pop()
                

            case "Geometric Height":
                counter = 0
                assignGeometricHeight(infoToPush, thisMessage, counter)
                infoToPush = getNewInfo(pushedInfo)
                counter += 1
                assignGeometricHeight(infoToPush, thisMessage, counter)
                currentState = stateList.pop()

            case "Magnetic Heading":
                counter = 0
                assignMagneticHeading(infoToPush, thisMessage, counter)
                infoToPush = getNewInfo(pushedInfo)
                counter += 1
                assignMagneticHeading(infoToPush, thisMessage, counter)
                currentState = stateList.pop()

            case "Emitter Category":
                assignEmitterCategory(infoToPush, thisMessage)
                currentState = stateList.pop()
            case "Target Identification":
                for i in range(0, 6):
                    assignTargetIdentification(infoToPush, thisMessage, i)
                    infoToPush = getNewInfo(pushedInfo)
                    
                currentState = stateList.pop()
            
                
            case "end":     
                break
            case _:
                if(len(stateList)>0):
                    currentState = stateList.pop()
                else:
                    currentState = "end"
            
    return thisMessage



def sendToDatabase(toPush: ParsedInfo):
    return jsonify(toPush.to_dict())






@app.route("/api/aircraft/update")
def get_data():
    parsingInfo = "Sample Data 0000   15 00 44 cf 1b 7b 5b c1 81 00 df 0c 00 01 00 7a e0 0010    62 19 92 6f ba d5 ea 0c c9 37 46 dd 6a f5 38 a7   0020   90 7c 7a e0 63 7a e0 63 17 d4 31 f7 14 12 05 8e   0030   05 9f 40 00 00 08 6d 82 d8 7a e0 63 31 82 b5 e3    0040   78 20 02 02                                       x "
    parsed = parse(parsingInfo)
    return jsonify(parsed.to_dict())
                




if __name__ == "__main__":
    app.run(debug=True)
    
