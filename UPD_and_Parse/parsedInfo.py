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
                 TimeofApplicabilityForPosition = "", 
                 PosWGS84 = "", PosWGS84HighRes = "", 
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
                 SpecialPurposeField = ""):
        self.cat = cat
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
        self.PosWGS84 = PosWGS84
        self.PosWGS84HighRes = PosWGS84HighRes
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

    def to_dict(self):

        testingString = {"Test1", "Test2"}
        return {"cat": self.cat,
        "System area code": self.systemAreaCode,
        "System Identification Code": self.systemIdentificationCode,
        "TargetReportDescriptor": self.TargetReportDescriptor,
        "Address Type": self.ATP,
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
        "PosWGS84": self.PosWGS84,
        "PosWGS84HighRes":self.PosWGS84HighRes,
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
        "SpecialPurposeField":self.SpecialPurposeField}



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
            # TODO
            print("Extension 2")
        case 3:
            # TODO
            print("Extension 3")
        case 4:
            # TODO
            print("Extension 4")
        


    return



def assignTrackNumber(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TrackNumber = "TODO"
    return

def assignServiceID(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.ServiceID = "TODO"
    return

def assignTimeOfApplicabilityForPosition(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TimeofApplicabilityForPosition = "TODO"
    return

def assignPosWGS84(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.PosWGS84 = "TODO"
    return

def assignPosWGS84HighRes(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.posWGS84HighRes = "TODO"
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

def assignTargetAddr(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TargetAddr = "TODO"
    return

def assignMessageReceptionOfPosTime(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MessageReceptionOfPosTime = "TODO"
    return

def assignMessageReceptionOfPosTimeHighPres(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MessageReceptionOfPosTimeHighPres = "TODO"
    return

def assignMessageReceptionofVel(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MessageReceptionofVel = "TODO"
    return

def assignTimeMessageReceptionVelHighP(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TimeMessageReceptionVelHighP = "TODO"
    return

def assignGeometricHeight(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.GeometricHeight = "TODO"
    return

def assignQualityIndicators(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.GeometricHeight = "TODO"
    return

def assignMOPSVers(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MOPSVers = "TODO"
    return

def assignMode3ACode(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.Mode3ACode = "TODO"
    return

def assignRollAngle(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.RollAngle = "TODO"
    return

def assignFlightLevel(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.FlightLevel = "TODO"
    return

def assignMagneticHeading(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.MagneticHeading = "TODO"
    return

def assignTargetStatus(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TargetStatus = "TODO"
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

def assignTargetIdentification(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TargetIdentification = "TODO"
    return

def assignEmitterCategory(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.EmitterCategory = "TODO"
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
    return 0


def parse(pushedInfo: str):
    # TODO: Calculate length of expected byte array
    # Ask about this
    # Start case: 

    pushedInfo = pushedInfo.split(" ")
    # Pop method goes from back to front, so for ease of complexity's sake we're reversing the list
    pushedInfo.reverse()


    thisMessage = ParsedInfo()

    print(pushedInfo)
    currentState = "Start"
    stateList = []
    while(len(pushedInfo) > 0):
        infoToPush = pushedInfo.pop()
        while(len(str(infoToPush)) != 2):
            # Use the string length in order to determine whether this is actually something we need or not
            print("Rejected string: ", infoToPush)
            infoToPush = pushedInfo.pop()

        print('Current infoToPush: ', infoToPush)
        infoToPush = int(infoToPush, 16)
        print(f"Info: {infoToPush}")
        match currentState:
            case "Start":
                print("CAT Assigned:")
                assignCAT(infoToPush, thisMessage)
                print(thisMessage.cat)

                # Deals with length: not needed to be found since python already has libraries that find this information
                # and we already use this information to build the byte array
                pushedInfo.pop()
                # two octets (bytes)
                pushedInfo.pop()
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
                    infoToPush -= 8
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

                if(infoToPush / 128 == 1):
                    stateList.append("Time of Applicability for Velocity")
                    infoToPush -= 128
                if(infoToPush / 64 == 1):
                    stateList.append("Air Speed")
                    infoToPush -= 64
                if(infoToPush / 32 == 1):
                    stateList.append("True Air Speed")
                    infoToPush -= 32
                if(infoToPush / 16 == 1):
                    stateList.append("Target Address")
                    infoToPush -= 8
                if(infoToPush / 8 == 1):
                    stateList.append("Time of Message Reception for Position")
                    infoToPush -= 8
                if(infoToPush / 4 == 1):
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
                if(infoToPush / 128 == 1):
                    stateList.append("Time of Message Reception of Velocity High Precision")
                    infoToPush -= 128
                if(infoToPush / 64 == 1):
                    stateList.append("Geometric Height")
                    infoToPush -= 64
                if(infoToPush / 32 == 1):
                    stateList.append("Quality Indicators")
                    infoToPush -= 32
                if(infoToPush / 16 == 1):
                    stateList.append("MOPS version")
                    infoToPush -= 8
                if(infoToPush / 8 == 1):
                    stateList.append("Mode 3A Code")
                    infoToPush -= 8
                if(infoToPush / 4 == 1):
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
                if(infoToPush / 128 == 1):
                    stateList.append("Magnetic Heading")
                    infoToPush -= 128
                if(infoToPush / 64 == 1):
                    stateList.append("Target Status")
                    infoToPush -= 64
                if(infoToPush / 32 == 1):
                    stateList.append("Barometric Vertical Rate")
                    infoToPush -= 32
                if(infoToPush / 16 == 1):
                    stateList.append("Geometric Vertical Rate")
                    infoToPush -= 8
                if(infoToPush / 8 == 1):
                    stateList.append("Airborne Ground Vector")
                    infoToPush -= 8
                if(infoToPush / 4 == 1):
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
                if(infoToPush / 128 == 1):
                    stateList.append("Target Identification")
                    infoToPush -= 128
                if(infoToPush / 64 == 1):
                    stateList.append("Emitter Category")
                    infoToPush -= 64
                if(infoToPush / 32 == 1):
                    stateList.append("Met Information")
                    infoToPush -= 32
                if(infoToPush / 16 == 1):
                    stateList.append("Selected Altitude")
                    infoToPush -= 8
                if(infoToPush / 8 == 1):
                    stateList.append("Final State Selected Altitude")
                    infoToPush -= 8
                if(infoToPush / 4 == 1):
                    stateList.append("Trajectory Intent")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Service Management")
                if(infoToPush % 2 == 1):
                    currentState = "Sixth fspec"
                else:
                    
                    stateList.reverse()
                    currentState = stateList.pop()
            
            case "Sixth fspec":
                print("Sixth fspec")
                if(infoToPush / 128 == 1):
                    stateList.append("Aircraft Operational Status")
                    infoToPush -= 128
                if(infoToPush / 64 == 1):
                    stateList.append("Surface Capabilities and Characteristics")
                    infoToPush -= 64
                if(infoToPush / 32 == 1):
                    stateList.append("Message Amplitude")
                    infoToPush -= 32
                if(infoToPush / 16 == 1):
                    stateList.append("BDS Register Data")
                    infoToPush -= 8
                if(infoToPush / 8 == 1):
                    stateList.append("ACAS Resolution Advisory Report")
                    infoToPush -= 8
                if(infoToPush / 4 == 1):
                    stateList.append("Receiver ID")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Data Ages")
                if(infoToPush % 2 == 1):
                    currentState = "Seventh fspec"
                else:
                    stateList.reverse()
                    currentState = stateList.pop()


            case "Seventh fspec":
                print("Seventh fspec")
                if(infoToPush / 4 == 1):
                    stateList.append("Received Expansion Field")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Special Purpose Field")

                stateList.reverse()
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
                    else:
                        currentState = stateList.pop()
                        assignTargetReportDescriptor(infoToPush, thisMessage, counter)
                        print("New Info: ", infoToPush)
                        hasValues = False
            

            case _:
                print("File completed parsing")
                break

    return thisMessage



def sendToDatabase(toPush: ParsedInfo):
    return jsonify(toPush.to_dict())






@app.route("/api/aircraft/update")
def get_data():
    parsingInfo = "Sample Data 0000   15 00 44 cf 1b 7b 5b c1 81 df 0c 00 01 00 7a e0 0010    62 19 92 6f ba d5 ea 0c c9 37 46 dd 6a f5 38 a7   0020   90 7c 7a e0 63 7a e0 63 17 d4 31 f7 14 12 05 8e   0030   05 9f 40 00 00 08 6d 82 d8 7a e0 63 31 82 b5 e3    0040   78 20 02 02                                       x "
    parsed = parse(parsingInfo)
    return jsonify(parsed.to_dict())
                




if __name__ == "__main__":
    app.run(debug=True)
    
