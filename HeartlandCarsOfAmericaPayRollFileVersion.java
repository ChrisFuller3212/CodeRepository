import java.io.*;
import java.util.*;

// By: Christian Fuller

public class HeartlandCarsOfAmericaPayRollFileVersion {
	
	public static void main (String[] args) throws
			FileNotFoundException, IOException
		{
			//create reference variable of all three employee types
			FullTimeEmp fullTimeEmployee;
			PartTimeEmp partTimeEmployee;
			SalesEmp salesEmployee;
			
			//declare variables to input
			char inputEmployeeType;
			String inputFirstName;
			String inputLastName;
			double inputBaseSalary;
			double inputPayPerHour;
			int inputSalesVolume;
			int inputHoursWorked;
			
			
			//get two input values
			Scanner scannedInfo = new Scanner(new File("/Users/christianfuller/Desktop/employee.txt"));
			PrintWriter outFile = new PrintWriter(new FileWriter("/Users/christianfuller/Desktop/payroll.txt"));
			
				
				
				while (scannedInfo.hasNext()) {
					inputEmployeeType = scannedInfo.next().charAt(0);
					
					switch (inputEmployeeType) {
					
						case 'F' :
						case 'f' :
							
							//get necessary values as input
							
							inputFirstName = scannedInfo.next();
							inputLastName = scannedInfo.next();
							inputBaseSalary = scannedInfo.nextDouble();
							inputHoursWorked = scannedInfo.nextInt();
							
							
							//create an object and initialize data members
							fullTimeEmployee = new FullTimeEmp();
							fullTimeEmployee.setFirstName(inputFirstName);
							fullTimeEmployee.setLastName(inputLastName);
							fullTimeEmployee.setBaseSalary(inputBaseSalary);
							fullTimeEmployee.setHoursWorked(inputHoursWorked);
							
							//invoke the printPayStub method
							outFile.println(fullTimeEmployee.createPayStub());
							
							break;
							
							
						case 'P' :
						case 'p' :
							
							//get necessary values as input
							
							inputFirstName = scannedInfo.next();
							inputLastName = scannedInfo.next();
							inputPayPerHour = scannedInfo.nextDouble();
							inputHoursWorked = scannedInfo.nextInt();
							
							
							//create an object and initialize data members
							partTimeEmployee = new PartTimeEmp();
							partTimeEmployee.setFirstName(inputFirstName);
							partTimeEmployee.setLastName(inputLastName);
							partTimeEmployee.setPayPerHour(inputPayPerHour);
							partTimeEmployee.setHoursWorked(inputHoursWorked);
							
							//invoke the printPayStub method
							outFile.print(partTimeEmployee.createPayStub());
							
							
							break;
							
							
						case 'S' :
						case 's' :
							
							//get necessary values as input
							
							inputFirstName = scannedInfo.next();
							inputLastName = scannedInfo.next();
							inputBaseSalary = scannedInfo.nextDouble();
							inputSalesVolume = scannedInfo.nextInt();
							
							
							//create an object and initialize data members
							salesEmployee = new SalesEmp();
							salesEmployee.setFirstName(inputFirstName);
							salesEmployee.setLastName(inputLastName);
							salesEmployee.setBaseSalary(inputBaseSalary);
							salesEmployee.setSalesVolume(inputSalesVolume);
							
							//invoke the printPayStub method
							outFile.print(salesEmployee.createPayStub());
							
							
							break;
						
							
				}
					
			}
			
				
				outFile.close();
		}
	}


