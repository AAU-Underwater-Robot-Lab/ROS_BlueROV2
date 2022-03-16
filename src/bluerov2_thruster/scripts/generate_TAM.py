#!/usr/bin/env python
from os.path import exists
import rospy
import yaml
import numpy as np
from numpy import pi
from numpy import cos as oldcos
from numpy import sin as oldsin

def sin(x):
	if x % pi == 0: 
		#if x is an integer mult of pi, like pi, 2pi, -7pi, etc.
		return 0
	else:
		return oldsin(x)

def cos(x):
	if x % (pi/2) == 0 and x % pi != 0: 
		#if x is an integer mult of pi/2, like pi/2, 3pi/2, -3pi/2, etc.
		#but no an integer mult of pi, like pi, 2pi, -7pi etc.
		return 0
	else:
		return oldcos(x)

def FxC(Ori,Dir):
	return eval(str(Dir))*cos(eval(str(Ori[0])))*cos(eval(str(Ori[1])))*cos(eval(str(Ori[2])))
	

def FyC(Ori,Dir):
	return eval(str(Dir))*-cos(eval(str(Ori[0])))*cos(eval(str(Ori[1])))*sin(eval(str(Ori[2])))

def FzC(Ori,Dir):
	return eval(str(Dir))*-cos(eval(str(Ori[0])))*sin(eval(str(Ori[1])))*cos(eval(str(Ori[2])))

def TphiC(Fy,Fz,Pos):
	return Fz*eval(str(Pos[1]))-Fy*eval(str(Pos[2]))

def TthetaC(Fx,Fz,Pos):
	return Fx*eval(str(Pos[2]))-Fz*eval(str(Pos[0]))

def TpsiC(Fx,Fy,Pos):
	return Fy*eval(str(Pos[0]))-Fx*eval(str(Pos[1]))

if __name__=="__main__":
	rospy.init_node('generate_tam',anonymous=True)
	fileName = rospy.get_param("~thrusterplacement_file","None")
	tam_file = rospy.get_param("~tam_file","None")
	model_name = rospy.get_param("~model_name","bluerov2")
	print("Model Name: " + model_name)
	if(fileName != "None"):
		with open(fileName, "r") as yaml_file:
			doc = yaml.load(yaml_file,Loader=yaml.SafeLoader)
			t0Pos = doc["ThrusterPlacement"]["t0"]
			t1Pos = doc["ThrusterPlacement"]["t1"]
			t2Pos = doc["ThrusterPlacement"]["t2"]
			t3Pos = doc["ThrusterPlacement"]["t3"]
			t4Pos = doc["ThrusterPlacement"]["t4"]
			t5Pos = doc["ThrusterPlacement"]["t5"]
			if(model_name == "bluerov2_heavy"):
				t6Pos = doc["ThrusterPlacement"]["t6"]
				t7Pos = doc["ThrusterPlacement"]["t7"]
			t0Ori = doc["ThrusterOrientaiton"]["t0"]
			t1Ori = doc["ThrusterOrientaiton"]["t1"]
			t2Ori = doc["ThrusterOrientaiton"]["t2"]
			t3Ori = doc["ThrusterOrientaiton"]["t3"]
			t4Ori = doc["ThrusterOrientaiton"]["t4"]
			t5Ori = doc["ThrusterOrientaiton"]["t5"]
			if(model_name == "bluerov2_heavy"):
				t6Ori = doc["ThrusterOrientaiton"]["t6"]
				t7Ori = doc["ThrusterOrientaiton"]["t7"]
			t0Dir = doc["ThrusterDirection"]["t0"]
			t1Dir = doc["ThrusterDirection"]["t1"]
			t2Dir = doc["ThrusterDirection"]["t2"]
			t3Dir = doc["ThrusterDirection"]["t3"]
			t4Dir = doc["ThrusterDirection"]["t4"]
			t5Dir = doc["ThrusterDirection"]["t5"]
			if(model_name == "bluerov2_heavy"):
				t6Dir = doc["ThrusterDirection"]["t6"]
				t7Dir = doc["ThrusterDirection"]["t7"]

			Fx = [FxC(t0Ori,t0Dir),FxC(t1Ori,t1Dir),FxC(t2Ori,t2Dir),FxC(t3Ori,t3Dir),FxC(t4Ori,t4Dir),FxC(t5Ori,t5Dir)]
			Fy = [FyC(t0Ori,t0Dir),FyC(t1Ori,t1Dir),FyC(t2Ori,t2Dir),FyC(t3Ori,t3Dir),FyC(t4Ori,t4Dir),FyC(t5Ori,t5Dir)]
			Fz = [FzC(t0Ori,t0Dir),FzC(t1Ori,t1Dir),FzC(t2Ori,t2Dir),FzC(t3Ori,t3Dir),FzC(t4Ori,t4Dir),FzC(t5Ori,t5Dir)]
			Tphi = [TphiC(Fy[0],Fz[0],t0Pos),TphiC(Fy[1],Fz[1],t1Pos),TphiC(Fy[2],Fz[2],t2Pos),TphiC(Fy[3],Fz[3],t3Pos),TphiC(Fy[4],Fz[4],t4Pos),TphiC(Fy[5],Fz[5],t5Pos)]
			Ttheta = [TthetaC(Fx[0],Fz[0],t0Pos),TthetaC(Fx[1],Fz[1],t1Pos),TthetaC(Fx[2],Fz[2],t2Pos),TthetaC(Fx[3],Fz[3],t3Pos),TthetaC(Fx[4],Fz[4],t4Pos),TthetaC(Fx[5],Fz[5],t5Pos)]
			Tpsi = [TpsiC(Fx[0],Fy[0],t0Pos),TpsiC(Fx[1],Fy[1],t1Pos),TpsiC(Fx[2],Fy[2],t2Pos),TpsiC(Fx[3],Fy[3],t3Pos),TpsiC(Fx[4],Fy[4],t4Pos),TpsiC(Fx[5],Fy[5],t5Pos)]
			if(model_name == "bluerov2_heavy"):
				Fx = [FxC(t0Ori,t0Dir),FxC(t1Ori,t1Dir),FxC(t2Ori,t2Dir),FxC(t3Ori,t3Dir),FxC(t4Ori,t4Dir),FxC(t5Ori,t5Dir),FxC(t6Ori,t6Dir),FxC(t7Ori,t7Dir)]
				Fy = [FyC(t0Ori,t0Dir),FyC(t1Ori,t1Dir),FyC(t2Ori,t2Dir),FyC(t3Ori,t3Dir),FyC(t4Ori,t4Dir),FyC(t5Ori,t5Dir),FyC(t6Ori,t6Dir),FyC(t7Ori,t7Dir)]
				Fz = [FzC(t0Ori,t0Dir),FzC(t1Ori,t1Dir),FzC(t2Ori,t2Dir),FzC(t3Ori,t3Dir),FzC(t4Ori,t4Dir),FzC(t5Ori,t5Dir),FzC(t6Ori,t6Dir),FzC(t7Ori,t7Dir)]
				Tphi = [TphiC(Fy[0],Fz[0],t0Pos),TphiC(Fy[1],Fz[1],t1Pos),TphiC(Fy[2],Fz[2],t2Pos),TphiC(Fy[3],Fz[3],t3Pos),TphiC(Fy[4],Fz[4],t4Pos),TphiC(Fy[5],Fz[5],t5Pos),TphiC(Fy[6],Fz[6],t6Pos),TphiC(Fy[7],Fz[7],t7Pos)]
				Ttheta = [TthetaC(Fx[0],Fz[0],t0Pos),TthetaC(Fx[1],Fz[1],t1Pos),TthetaC(Fx[2],Fz[2],t2Pos),TthetaC(Fx[3],Fz[3],t3Pos),TthetaC(Fx[4],Fz[4],t4Pos),TthetaC(Fx[5],Fz[5],t5Pos),TthetaC(Fx[6],Fz[6],t6Pos),TthetaC(Fx[7],Fz[7],t7Pos)]
				Tpsi = [TpsiC(Fx[0],Fy[0],t0Pos),TpsiC(Fx[1],Fy[1],t1Pos),TpsiC(Fx[2],Fy[2],t2Pos),TpsiC(Fx[3],Fy[3],t3Pos),TpsiC(Fx[4],Fy[4],t4Pos),TpsiC(Fx[5],Fy[5],t5Pos),TpsiC(Fx[6],Fy[6],t6Pos),TpsiC(Fx[7],Fy[7],t7Pos)]

			print(Fx)
			print(Fy)
			print(Fz)
			print(Tphi)
			print(Ttheta)
			print(Tpsi)

			dict_file = {'tam' : [np.array(Fx).tolist(),np.array(Fy).tolist(),np.array(Fz).tolist(),np.array(Tphi).tolist(),np.array(Ttheta).tolist(),np.array(Tpsi).tolist()]}

			overwrite = False
			if(exists(tam_file)):
				ans = raw_input("TAM.yaml already exists. Do you want to overwrite the TAM file? [yN]: ")
				if(str(ans) == 'y' or str(ans) == 'Y'):
					overwrite = True
			if(exists(tam_file) == False or overwrite == True):
				print("Writing TAM.yaml")
				with open(tam_file, 'w') as new_tam_file:
					documents = yaml.dump(dict_file,new_tam_file,default_flow_style=True)
				
			print("Done")
			rospy.spin()
