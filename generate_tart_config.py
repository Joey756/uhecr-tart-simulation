import math

def generate_corsika_files():
    # 1. Generate SIM000001.list (40x40 grid over 500 meters)
    print("Generating SIM000001.list...")
    # 500 meters = 50,000 cm. Centered at 0, this means -25,000 to 25,000 cm.
    # 40 antennas across 50,000 cm gives a spacing of roughly 1282.05 cm.
    grid_points = 40
    min_coord = -25000.0
    max_coord = 25000.0
    step = (max_coord - min_coord) / (grid_points - 1)
    
    with open("SIM000001.list", "w") as f:
        for i in range(grid_points):
            x = min_coord + i * step
            for j in range(grid_points):
                y = min_coord + j * step
                # Z coordinate is fixed to 140000.0 cm (1,400 m a.s.l)
                f.write(f"AntennaPosition = {x:.1f}\t{y:.1f}\t140000.0\tantenna_{i:02d}_{j:02d}\n")

    # 2. Generate RUN000001.inp
    print("Generating RUN000001.inp...")
    inp_content = """RUNNR   1
EVTNR   1
SEED    1 0 0
SEED    2 0 0
SEED    3 0 0
PRMPAR  14
ERANGE  1.000E+9 1.000E+9
ESLOPE  0.000E+00
THETAP  45.0  45.0
PHIP    0.000E+00 0.000E+00
ECUTS   3.000E-01 3.000E-01 4.010E-04 4.010E-04
ELMFLG  T  T
THIN    1.000E-06 1.000E+02 0.000E+00
THINH   1.000E+00 1.000E+00
NSHOW   1
USER    joel
HOST    schmalzburg
DIRECT  './'
OBSLEV  140000.0
ECTMAP  1.000E+05
STEPFC  1.000E+00
MUMULT  T
MUADDI  T
PAROUT  F  F
MAXPRT  1
MAGNET  19.71 -14.18
LONGI   T    5.  T  T
RADNKG  5.000E+05
DATBAS  F
EXIT
"""
    with open("RUN000001.inp", "w") as f:
        f.write(inp_content)

    # 3. Generate SIM000001.reas
    print("Generating SIM000001.reas...")
    reas_content = """# CoREAS V1.4 by Tim Huege <tim.huege@kit.edu> with contributions by Marianne Ludwig and Clancy James - parameter file

# parameters setting up the spatial observer configuration:
CoreCoordinateNorth = 0                 ; in cm
CoreCoordinateWest = 0                  ; in cm
CoreCoordinateVertical = 140000         ; in cm

# parameters setting up the temporal observer configuration:
TimeResolution = 2e-10                  ; in s
AutomaticTimeBoundaries = 4e-07         ; 0: off, x: automatic boundaries with width x in s
TimeLowerBoundary = -1                  ; in s, only if AutomaticTimeBoundaries set to 0
TimeUpperBoundary = 1                   ; in s, only if AutomaticTimeBoundaries set to 0
ResolutionReductionScale = 0            ; 0: off, x: decrease time resolution linearly every x cm in radius

# parameters setting up the simulation functionality:
GroundLevelRefractiveIndex = 1.000292   ; specify refractive index at 0 m asl

# event information for Offline simulations:
EventNumber = 1
RunNumber = 1
GPSSecs = 0
GPSNanoSecs = 0
CoreEastingOffline = 0                  ; in meters
CoreNorthingOffline = 0                 ; in meters
CoreVerticalOffline = 0                 ; in meters
OfflineCoordinateSystem = Reference
RotationAngleForMagfieldDeclination = 0 ; in degrees
Comment = 

# event information for your convenience and backwards compatibility with other software, these values are not used as input parameters for the simulation:
ShowerZenithAngle = 45.0                ; in degrees
ShowerAzimuthAngle = 0                  ; in degrees, 0: shower propagates to north, 90: to west
PrimaryParticleEnergy = 1e+18           ; in eV
PrimaryParticleType = 14                ; as defined in CORSIKA
DepthOfShowerMaximum = 670.7138436      ; slant depth in g/cm^2
DistanceOfShowerMaximum = 213000        ; geometrical distance of shower maximum from core in cm
MagneticFieldStrength = 0.2428078402    ; in Gauss
MagneticFieldInclinationAngle = -35.7324412 ; in degrees, >0: in northern hemisphere, <0: in southern hemisphere
GeomagneticAngle = 125.7324412          ; in degrees
CorsikaFilePath = ./
CorsikaParameterFile = RUN000001.inp
"""
    with open("SIM000001.reas", "w") as f:
        f.write(reas_content)

    print("All configuration files successfully generated!")

if __name__ == "__main__":
    generate_corsika_files()
