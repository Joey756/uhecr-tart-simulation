# UHECR Air Shower Radio Detection — CORSIKA/CoREAS Simulation

## Project Goal
Investigate whether TART (at 1.575 GHz) can detect radio emission from 
ultra-high energy cosmic ray air showers. This is a footprint demonstrator,
not a detection-rate estimate.

## Current Simulation Parameters
- Primary particle: Proton, 1 EeV (10^18 eV)
- Zenith angle: 45°
- Hadronic model: SIBYLL + FLUKA (thin mode)
- Thinning: Wmax=100
- Antenna grid: 40×40
- Key open question: whether Wmax=100 produces noise-dominated output above 1 GHz

## Key Files
- `RUN000001.inp` — main CORSIKA steering file
- `generate_tart_config.py` — generates TART antenna configuration
- `coreas_to_hdf5.py` — converts CoREAS output to HDF5 for analysis
- `SIM000001.reas` — CoREAS-specific configuration
- `tart_run_01.log` — output log from last run

## Stack
- CORSIKA 7.8050 with CoREAS
- Python (analysis scripts)
- Machine: schmalzburg (single-core, Tim Molteno's lab, Otago)


