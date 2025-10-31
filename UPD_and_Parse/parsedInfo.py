class ParsedInfo:
    def __init__(self, cat = "",
                 systemAreaCode = "", 
                 systemIdentificationCode = "",
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

def assignTargetReportDescriptor(pushedInfo, assignTo: ParsedInfo):
    # TODO
    assignTo.TargetReportDescriptor = "TODO"
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


def parse(pushedInfo: bytes):
    # TODO: Calculate length of expected byte array
    # Ask about this
    # Start case: 


    thisMessage = ParsedInfo()

    byte_array_length = (pushedInfo.bit_length()) // 8
    byte_array_big_endian = pushedInfo.to_bytes(byte_array_length, 'big')
    currentState = "Start"
    print(byte_array_big_endian)
    stateList = []
    while(len(byte_array_big_endian) > 0):
        infoToPush = byte_array_big_endian.pop()
        print(f"Info: {infoToPush}")
        match currentState:
            case "Start":
                print("CAT Assigned:")
                assignCAT(infoToPush, thisMessage)
                print(thisMessage.cat)

                # Deals with length: not needed to be found since python already has libraries that find this information
                # and we already use this information to build the byte array
                byte_array_big_endian.pop()
                # two octets (bytes)
                byte_array_big_endian.pop()
                # Next information is the fspec
                currentState = "First fspec"
            case "First fspec":
                # if the info to push modulo 2 == 1, then we set current state to Second fspec after adding things into statelist
                # if info to push modulo 2 == 0, then we move to the next state in State List
                # Repeat for fspec up to 7 times
                print("First fspec")
                if(infoToPush / 128 == 1):
                    stateList.append("Data Source Identification")
                    infoToPush -= 128
                if(infoToPush / 64 == 1):
                    stateList.append("Target Report Descripton")
                    infoToPush -= 64
                if(infoToPush / 32 == 1):
                    stateList.append("Track Number")
                    infoToPush -= 32
                if(infoToPush / 16 == 1):
                    stateList.append("Service ID")
                    infoToPush -= 8
                if(infoToPush / 8 == 1):
                    stateList.append("Time of Applicability for Position")
                    infoToPush -= 8
                if(infoToPush / 4 == 1):
                    stateList.append("Position in WGS-84 co-ordinates")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Position in WGS-84 coords high res")


                # After going through the bytes:
                if(infoToPush % 2 == 1):
                    currentState = "Second fspec"
                else:
                    currentState = stateList.pop(0)
            case "Second fspec":


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
                    currentState = stateList.pop(0)
            case "Third fspec":
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
                    currentState = stateList.pop(0)

            case "Fourth fspec":
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
                    currentState = stateList.pop(0)
            
            case "Fifth fspec":
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
                    currentState = stateList.pop(0)
            
            case "Sixth fspec":

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
                    currentState = stateList.pop(0)

            case "Seventh fspec":

                if(infoToPush / 4 == 1):
                    stateList.append("Received Expansion Field")
                    infoToPush -= 4
                if(infoToPush // 2 == 1):
                    stateList.append("Special Purpose Field")

                currentState = stateList.pop(0)

            case "Data Source Identification":
                # 
                assignDataSource(pushedInfo, thisMessage, "first")
                pushedInfo = byte_array_big_endian.pop()
                assignDataSource(pushedInfo, thisMessage, "second")
                currentState = stateList.pop(0)
            
            case "Target Report Descripton":
                hasValues = True
                while(hasValues):


                    if(pushedInfo % 2 == 1):
                        # Extension case - hasValues doesn't update, 
                        print("test")


            





                


parse(0xFF0000FF)