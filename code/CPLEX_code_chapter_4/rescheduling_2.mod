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
range DeviceNumber = 1..NbDeviceNumber;
int TransportTime[DeviceClass][DeviceNumber][DeviceClass][DeviceNumber] = ...;
int MaxOperationTime[DeviceClass] = ...;
int MinOperationTime[DeviceClass] = ...;

dvar float StartTime[Pouring][Furnace][DeviceClass] in 0..500;
dvar float EndTime[Pouring][Furnace][DeviceClass] in 0..500;
dvar int UseDevice[Pouring][Furnace][DeviceClass][DeviceNumber] in 0..1;

minimize
	1000*sum(i in Pouring) sum(j in Furnace)
	(StartTime[i][j][2]-EndTime[i][j][1]+StartTime[i][j][3]-EndTime[i][j][2])
	+ max(i in Pouring)EndTime[i][6][3];

subject to {

	A_operation_can_only_be_arranged_on_one_device://***********************************************************
	forall(i in Pouring)
		forall(j in Furnace)
			forall(k in DeviceClass)
			  {
			  	  UseDevice[i][j][k][1] + 
			  	  UseDevice[i][j][k][2] + 
			  	  UseDevice[i][j][k][3] == 1;
      		  }
	
	operation_order_in_one_furnace://***************************************************************************
	forall(i in Pouring)
		forall(j in Furnace)
		  forall(k in 1..2)
		  	forall(n1 in DeviceNumber)
		    	forall(n2 in DeviceNumber)
				{
					StartTime[i][j][k+1] - EndTime[i][j][k]
					- TransportTime[k][n1][k+1][n2] 
					+ 500 * (1-UseDevice[i][j][k][n1])
					+ 500 * (1-UseDevice[i][j][k+1][n2]) >= 0;
                    
					StartTime[i][j][k+1] - EndTime[i][j][k] 
					- TransportTime[k][n1][k+1][n2] 
			    	- 500 * (1-UseDevice[i][j][k][n1])
			    	- 500 * (1-UseDevice[i][j][k+1][n2]) <= 0;
					StartTime[i][j][k+1] - EndTime[i][j][k] >= 10;//不知道为什么这一行能明显加快求解过程。
	   			}
   			
   	operation_time_limit://*************************************************************************************
	forall(i in Pouring)
		forall(j in Furnace)
		  forall(k in DeviceClass)
		    {
		    	EndTime[i][j][k] - StartTime[i][j][k] >= MinOperationTime[k];
		    	EndTime[i][j][k] - StartTime[i][j][k] <= MaxOperationTime[k];
       		}

	operation_order_in_one_device://****************************************************************************
	forall(i1 in Pouring)
		forall(j1 in Furnace)
		  forall(i2 in Pouring)
			forall(j2 in Furnace)
			  forall(k in DeviceClass)
			    forall(n in DeviceNumber)	
			  		{
			  			if(i1 != i2 || j1 != j2)
						{	  		
			  			StartTime[i1][j1][k] - EndTime[i2][j2][k] 
			  			+ 1000*(1-UseDevice[i1][j1][k][n])
			  			+ 1000*(1-UseDevice[i2][j2][k][n])
			  			>= 0
			  			||
			  			StartTime[i2][j2][k] - EndTime[i1][j1][k] 
			  			+ 1000*(1-UseDevice[i1][j1][k][n])
			  			+ 1000*(1-UseDevice[i2][j2][k][n]) >= 0;
      					}			  			
			  		}

	Pouring_device_limit://*************************************************************************************
	forall(i in Pouring)
		forall(j in Furnace)
		  	UseDevice[i][j][3][i] == 1;
    contiual_pouring://*****************************************************************************************
	forall(i in Pouring)
		forall(j in 1..5)
		  	StartTime[i][j+1][3] - EndTime[i][j][3] == 0;
 	  
	existed_operation://****************************************************************************************
	{
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
	
	UseDevice[1][1][1][1] == 1;UseDevice[1][2][1][1] == 1;UseDevice[1][3][1][1] == 1;UseDevice[1][4][1][1] == 1;
	UseDevice[2][1][1][2] == 1;UseDevice[2][2][1][2] == 1;UseDevice[2][3][1][2] == 1;
	UseDevice[3][1][1][3] == 1;UseDevice[3][2][1][3] == 1;UseDevice[3][3][1][3] == 1;
	
	UseDevice[1][1][2][1] == 1;UseDevice[1][2][2][1] == 1;UseDevice[1][3][2][1] == 1;
	UseDevice[2][1][2][2] == 1;UseDevice[2][2][2][2] == 1;
	UseDevice[3][1][2][3] == 1;UseDevice[3][1][2][3] == 1;
	}	
	
}