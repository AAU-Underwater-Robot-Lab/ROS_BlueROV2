[Go back](../README.md)

# Generate Thruster Allocation Matrix (TAM)

Is used to generate the Generate Thruster Allocation Matrix (TAM) which is used by the thruster manager.

To run the generate_TAM launch file run the following command

for BlueROV2:
`roslaunch bluerov2_thruster generate_TAM.launch`

or 

`roslaunch bluerov2_thruster generate_TAM.launch model_name:=bluerov2`

for BlueROV2 Heavy Configuration:

`roslaunch bluerov2_thruster generate_TAM.launch model_name:=bluerov2_heavy`

## <b>*thruster_placement.yaml*</b>

The thruster_placement.yaml file is used to generate the TAM and is located in *config/<model_name>/*.

It is required to able to run `roslaunch bluerov2_thruster generate_TAM.launch`.

Example of the *thruster_placement.yaml*:
```yaml
ThrusterPlacement:
#      l_xi    l_yi    l_zi
 t0: [ 0.156,  0.111,  0.085]
 t1: [ 0.156, -0.111,  0.085]
 t2: [-0.156,  0.111,  0.085]
 t3: [-0.156, -0.111,  0.085]
 t4: [ 0.120,  0.218,  0.000]
 t5: [ 0.120, -0.218,  0.000]
 t6: [-0.120,  0.218,  0.000]
 t7: [-0.120, -0.218,  0.000]

ThrusterOrientaiton:
#      phi   theta   psi
 t0: [ 0.0,  0.0,    pi/4]
 t1: [ 0,0,  0.0,   -pi/4]
 t2: [ 0,0,  0.0,    3*pi/4]
 t3: [ 0,0,  0.0,   -3*pi/4]
 t4: [ 0.0,  pi/2,   0.0]
 t5: [ 0.0, -pi/2,   0.0]
 t6: [ 0.0, -pi/2,   0.0]
 t7: [ 0.0,  pi/2,   0.0]

ThrusterDirection:
# 1 for CW -1 for CCW
 t0: 1
 t1: 1
 t2: 1
 t3: 1
 t4: 1
 t5: -1
 t6: -1
 t7: 1
```

t* is the thruster, with entry *.
The ThrusterPlacement is the position of the thruster in relation to Center of Mass (COM).

The ThrusterOrientation describes how the thruster is orientated, the initial orientation is paralel to the x-axis (Surge). Meaning no thrust force will be prodcued in sway and heavy if orientation is defined as `t*: [0.0, 0.0, 0.0]`.

If you make changes to the thruster_placement.yaml file, you must rerun `roslaunch bluerov2_thruster generate_TAM.launch` to create a new TAM.