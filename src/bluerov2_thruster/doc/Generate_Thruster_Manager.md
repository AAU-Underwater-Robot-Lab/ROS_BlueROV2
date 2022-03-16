[Go back](../README.md)

# Generate Thruster Manager
This is a MatLab script, therefore you need MatLab to run it.

The script is used to generate the *thruster_manager.yaml* in *config/<model_name>/*.

The function uses a thruster function (line 7-8 in *thruster_manager_generator.m*).
```matlab class:"lineNo"
%% Thruster Function (input (-1..1) to thrustforce in Newton for one thruster
T(u) = -140.25*u^9+389.9*u^7-404.1*u^5+175.95*u^3+8.935*u;
```
To find the relationship between input and output. These are used to determine a custom thruster function for uuv_thruster_manager, which is the underlaying mechanism used for this thruster manager.

Beside the thruster manager some other relevant parameters to set is the following: (line 10-17 in *thruster_manager_generator.m*).
```matlab class:"lineNo"
%% Parameters for thruster_manager.yaml
pwm = false; %PWM (1100..1900) or Input (-1..1)
% Stepsize for Thruster function (Also used in thruster_manager.yaml)
stepsize = 0.01;
% Paramters
model_name = "bluerov2_heavy" %'bluerov' or 'bluerov2_heavy'
maxThrust = 60; %Maximum thrust force for one thruster. (m)
updateRate = 50; %Update rate for thruster manager. (Hz)
```

**Note that T(u) should be defined as function with inputs within the range -1..1, no matter if pwm is true or false.**

If a *thruster_manager.yaml* already exists for the chosen ROV (model_name), you will be asked whether you want to overwrite it or not. If you overwrite the file, there is no way to recreate the old *thruster_manager.yaml*, therefore it is a good idea to make a backup by either renaming the file or copy it to a different folder, if you have an already working *thruster_manager.yaml*.