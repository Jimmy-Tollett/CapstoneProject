import graphene, time

class Aircraft(graphene.ObjectType):
    id = graphene.Int()
    callsign = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()
    altitude = graphene.Float()
    speed = graphene.Float()
    heading = graphene.Float()
    aircraft_type = graphene.String()
    timestamp = graphene.Int()


example_db = [
        Aircraft(
            id=0, 
            callsign="ABC123", 
            latitude=33.0, 
            longitude=-97.0, 
            altitude=15000, 
            speed=200, 
            heading=0, 
            aircraft_type="B737", 
            timestamp=int(time.time())
        ),
        Aircraft(
            id=1, 
            callsign="XYZ789", 
            latitude=32.5, 
            longitude=-97.5, 
            altitude=40000, 
            speed=500, 
            heading=180, 
            aircraft_type="A320", 
            timestamp=int(time.time())
        )
    ]


class Query(graphene.ObjectType):
    all_aircraft = graphene.List(Aircraft)
    aircraft = graphene.Field(Aircraft, callsign=graphene.String(required=True))

    def resolve_all_aircraft(root, info):
        return example_db
    
    def resolve_aircraft(root, info, callsign):
        return next((ac for ac in example_db if ac.callsign == callsign), None)

schema = graphene.Schema(query=Query)