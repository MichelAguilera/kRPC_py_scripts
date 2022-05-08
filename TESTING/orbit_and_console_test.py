#Global imports
import krpc
import time

#Connecting to the server
conn = krpc.connect(name='Hello World')

#Vessel
vessel = conn.space_center.active_vessel

#Mathematical Variables
kerbin_radius = 600000


#Software interface
print("================================================================================\n================================= System start =================================\n================================================================================")
procedure = input("Select procedure: [ LAUNCH 'l' ] [ ABORT 'a' ] : ")



if procedure == "l":
    #LAUNCH
    stages = []


    #PRINTS - LAUNCH
    print("Launch sequence commencing")
    cdnums = ["Three","Two","One"]
    for i in range(0, len(cdnums)):
        print(cdnums[i])
        time.sleep(1)
    print(f"{vessel.name}: launch")

    #PRINTS - STATUS

    #STAGE - LAUNCH
    vessel.control.throttle = 1
    vessel.control.activate_next_stage()
    vessel.control.sas = True

    #PROGRAM - TERMINAL VELOCITY LIMITER
    print("$----[X]----$ Instruments $----[X]----$")
    while vessel.control.throttle > 0:
        print(f" Throttle : {vessel.control.throttle:.2f} | Atmosphere : {vessel.flight().atmosphere_density:.2f} | Speed : {vessel.flight().true_air_speed:.2f} | Pressure : {vessel.flight().dynamic_pressure:.2f} | Height : {vessel.flight().mean_altitude:.2f}", end="\r")
        

elif procedure == "a":
    #ABORT
    print("Launch sequence aborted")