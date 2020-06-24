/*********************************************
 * OPL 12.9.0.0 Model
 * Author: zihao
 * Creation Date: 2020年6月8日 at 下午4:32:34
 *********************************************/
int NbPouring = ...;
int NbFurnace = ...;
int NbDeviceClass = ...;
int NbDeviceNumber = ...;
range Pouring = 1..NbPouring;
range Furnace = 1..NbFurnace;
range DeviceClass = 1..NbDeviceClass;
int TransportTime[Pouring][Furnace][DeviceClass] = ...;
int MaxOperatingTime[DeviceClass] = ...;
int MinOperatingTime[DeviceClass] = ...;

dvar int StartTime[Pouring][Furnace][DeviceClass] in 0..500;
dvar int EndTime[Pouring][Furnace][DeviceClass] in 0..500;

minimize
	sum(i in Pouring) sum(j in Furnace) 
	(StartTime[i][j][2]-EndTime[i][j][1]+StartTime[i][j][3]-EndTime[i][j][2])
	+EndTime[3][6][3];
      
subject to {
	StartTime[1][1][1] == 0; EndTime[1][1][1] == 35;
	StartTime[1][2][1] == 45; EndTime[1][2][1] == 80;
	StartTime[1][3][1] == 90; EndTime[1][3][1] == 125;
	StartTime[1][4][1] == 135;
	
	StartTime[2][1][1] == 11; EndTime[2][1][1] == 46;
	StartTime[2][2][1] == 56; EndTime[2][2][1] == 91;
	StartTime[2][3][1] == 101; EndTime[2][3][1] == 136;
	
	StartTime[3][1][1] == 34; EndTime[3][1][1] == 69;
	StartTime[3][2][1] == 79; EndTime[3][2][1] == 114;
	StartTime[3][3][1] == 144;
	
	StartTime[1][1][2] == 45; EndTime[1][1][2] == 65;
	StartTime[1][2][2] == 90; EndTime[1][2][2] == 110;
	StartTime[1][3][2] == 135;

	StartTime[2][1][2] == 61; EndTime[2][1][2] == 81;
	StartTime[2][2][2] == 106; EndTime[2][2][2] == 126;
	
	StartTime[3][1][2] == 82; EndTime[3][1][2] == 102;
	StartTime[3][2][2] == 127;
	
	StartTime[1][1][3] == 87; EndTime[1][1][3] == 132;
	StartTime[1][2][3] == 132;
	
	StartTime[2][1][3] == 106;
	
	StartTime[3][1][3] == 124;
	
	

	forall(i in Pouring)
		forall(j in Furnace)
			Operating_order_in_one_furnace:
			{
				StartTime[i][j][3] - EndTime[i][j][2] >= TransportTime[i][j][2];
				StartTime[i][j][2] - EndTime[i][j][1] >= TransportTime[i][j][1];
   			}
	forall(i in Pouring)
		forall(j in Furnace)
		  forall(k in DeviceClass)
		    Operating_time_limit:
		    {
		    	EndTime[i][j][k] - StartTime[i][j][k] >= MinOperatingTime[k];
		    	EndTime[i][j][k] - StartTime[i][j][k] <= MaxOperatingTime[k];
       		}
	
	Operating_order_in_one_device:
	
		StartTime[1][2][1] - EndTime[1][1][1] >= 0;StartTime[1][3][1] - EndTime[1][2][1] >= 0;
		StartTime[1][4][1] - EndTime[1][3][1] >= 0;StartTime[1][5][1] - EndTime[1][4][1] >= 0;
		StartTime[1][6][1] - EndTime[1][5][1] >= 0;
		
		StartTime[2][2][1] - EndTime[2][1][1] >= 0;StartTime[2][3][1] - EndTime[2][2][1] >= 0;
		StartTime[2][4][1] - EndTime[2][3][1] >= 0;StartTime[3][4][1] - EndTime[2][4][1] >= 0;
		StartTime[3][5][1] - EndTime[3][4][1] >= 0;StartTime[3][6][1] - EndTime[3][5][1] >= 0;
		
		StartTime[3][2][1] - EndTime[3][1][1] >= 0;StartTime[3][3][1] - EndTime[3][2][1] >= 0;
		StartTime[2][5][1] - EndTime[3][3][1] >= 0;StartTime[2][6][1] - EndTime[2][5][1] >= 0;
		
		
		StartTime[1][2][2] - EndTime[1][1][2] >= 0;StartTime[1][3][2] - EndTime[1][2][2] >= 0;
		StartTime[1][4][2] - EndTime[1][3][2] >= 0;StartTime[2][5][2] - EndTime[1][3][2] >= 0;
		StartTime[2][6][2] - EndTime[2][5][2] >= 0;
		
		StartTime[2][2][2] - EndTime[2][1][2] >= 0;StartTime[2][3][2] - EndTime[2][2][2] >= 0;
		StartTime[2][4][2] - EndTime[2][3][2] >= 0;StartTime[3][4][2] - EndTime[2][4][2] >= 0;
		StartTime[3][5][2] - EndTime[3][4][2] >= 0;StartTime[3][6][2] - EndTime[3][5][2] >= 0;
		
		StartTime[3][2][2] - EndTime[3][1][2] >= 0;StartTime[3][3][2] - EndTime[3][2][2] >= 0;
		StartTime[1][5][2] - EndTime[3][3][2] >= 0;StartTime[1][6][2] - EndTime[1][5][2] >= 0;
		
		
		StartTime[1][2][3] - EndTime[1][1][3] == 0;StartTime[1][3][3] - EndTime[1][2][3] == 0;
		StartTime[1][4][3] - EndTime[1][3][3] == 0;StartTime[1][5][3] - EndTime[1][4][3] == 0;
		StartTime[1][6][3] - EndTime[1][5][3] == 0;
		
		StartTime[2][2][3] - EndTime[2][1][3] == 0;StartTime[2][3][3] - EndTime[2][2][3] == 0;
		StartTime[2][4][3] - EndTime[2][3][3] == 0;StartTime[2][5][3] - EndTime[2][4][3] == 0;
		StartTime[2][6][3] - EndTime[2][5][3] == 0;
		
		StartTime[3][2][3] - EndTime[3][1][3] == 0;StartTime[3][3][3] - EndTime[3][2][3] == 0;
		StartTime[3][4][3] - EndTime[3][3][3] == 0;StartTime[3][5][3] - EndTime[3][4][3] == 0;
		StartTime[3][6][3] - EndTime[3][5][3] == 0;
	
}