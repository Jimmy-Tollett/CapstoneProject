class ParsedInfo:
    def __init__(self, 
                 dataSource = "", 
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
        self.dataSource = dataSource
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
    
def parse(pushedInfo: str) -> ParsedInfo:
    for char in pushedInfo:
        print(".")

obj = parse("test")

