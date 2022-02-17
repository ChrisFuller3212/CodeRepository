import java.io.*;
import java.text.DecimalFormat;
import java.util.*;

//By: Christian Fuller

public class PayrollMain {
	
	public static void main (String[] args) throws
			FileNotFoundException, IOException
		{
//			create reference variable of all three employee types
			FullTimeEmployee fullTimeEmployee;
			PartTimeEmployee partTimeEmployee;
			SalesEmployee salesEmployee;
			
//			declare variables to input
			char inputEmployeeType;
			String inputFirstName;
			String inputLastName;
			double inputBaseSalary;
			double inputPayPerHour;
			int inputSalesVolume;
			int inputHoursWorked;
			
//			new instantiated variables for counting up the
//			total of:
//				fulltime hours worked,
//				fulltime base salary,
//				parttime hours worked,
//				parttime payed per hour,
//				salesemp sales volume,
//				and salesemp base salary
//			
//			the use of decimalFormat is imported
//			for average calculation
			
			int fullTimeHoursWorkedTotal = 0;
			double fullTimeBaseSalaryTotal = 0;
			char fullTimeEmployeeCounter = 0;
			int partTimeHoursWorkedTotal = 0;
			double partTimePayedPerHourTotal = 0;
			char partTimeEmployeeCounter = 0;
			int sSalesVolumeTotal = 0;
			double salesBaseSalaryTotal = 0;
			char salesCounter = 0;
			DecimalFormat currencyFormat = new DecimalFormat ("0.00");
			
			
			
//			get two input values
			Scanner scannedInfo = new Scanner(new File("/Users/christianfuller/Desktop/employee.txt"));
			PrintWriter outFile = new PrintWriter(new FileWriter("/Users/christianfuller/Desktop/payroll2.txt"));
			
				
				
				while (scannedInfo.hasNext()) {
					inputEmployeeType = scannedInfo.next().charAt(0);
					
					switch (inputEmployeeType) {
					
						case 'F' :
						case 'f' :
							
//							get necessary values as input
							
							inputFirstName = scannedInfo.next();
							inputLastName = scannedInfo.next();
							inputBaseSalary = scannedInfo.nextDouble();
							inputHoursWorked = scannedInfo.nextInt();
							
							
//							create an object and initialize data members
							
							//USE OF 4 PARAMETER FULLTIMEEMPLOYEE CONSTRUCTOR
							fullTimeEmployee = new FullTimeEmployee(inputFirstName, inputLastName, 
									inputBaseSalary, inputHoursWorked);
							fullTimeEmployee.setFirstName(inputFirstName);
							fullTimeEmployee.setLastName(inputLastName);
							fullTimeEmployee.setBaseSalary(inputBaseSalary);
							fullTimeEmployee.setHoursWorked(inputHoursWorked);
						
							
//							lines 83, 84 have the totals for future averaging
							fullTimeHoursWorkedTotal += inputHoursWorked;
							fullTimeBaseSalaryTotal += inputBaseSalary;
							
//							counting employees scanned for full time
							fullTimeEmployeeCounter++;
							
//							invoke the printPayStub method
							outFile.println(fullTimeEmployee.createPayStub());
							
							break;
							
							
						case 'P' :
						case 'p' :
							
//							get necessary values as input
							
							inputFirstName = scannedInfo.next();
							inputLastName = scannedInfo.next();
							inputPayPerHour = scannedInfo.nextDouble();
							inputHoursWorked = scannedInfo.nextInt();
							
							
//							create an object and initialize data members
							
							//USE OF 4 PARAMETER PARTTIMEEMPLOYEE CONSTRUCTOR
							partTimeEmployee = new PartTimeEmployee(inputFirstName, inputLastName, 
									inputPayPerHour, inputHoursWorked);
							partTimeEmployee.setFirstName(inputFirstName);
							partTimeEmployee.setLastName(inputLastName);
							partTimeEmployee.setPayPerHour(inputPayPerHour);
							partTimeEmployee.setHoursWorked(inputHoursWorked);
							
							
//							lines 118, 119 have the totals for future averaging
							partTimeHoursWorkedTotal += inputHoursWorked;
							partTimePayedPerHourTotal += inputPayPerHour;
							
//							counting employees scanned for part time
							partTimeEmployeeCounter++;
							
//							invoke the printPayStub method
							outFile.print(partTimeEmployee.createPayStub());
							
							
							break;
							
							
						case 'S' :
						case 's' :
							
//							get necessary values as input
							
							inputFirstName = scannedInfo.next();
							inputLastName = scannedInfo.next();
							inputBaseSalary = scannedInfo.nextDouble();
							inputSalesVolume = scannedInfo.nextInt();
							
							
//							create an object and initialize data members
							
							//USE OF 4 PARAMETER SALESEMPLOYEE CONSTRUCTOR
							salesEmployee = new SalesEmployee(inputFirstName, inputLastName, 
									inputBaseSalary, inputSalesVolume);
							salesEmployee.setFirstName(inputFirstName);
							salesEmployee.setLastName(inputLastName);
							salesEmployee.setBaseSalary(inputBaseSalary);
							salesEmployee.setSalesVolume(inputSalesVolume);
							
//							lines 153, 154 have the totals for future averaging
							sSalesVolumeTotal += inputSalesVolume;
							salesBaseSalaryTotal += inputBaseSalary;
							
//							counting employees scanned for sales 
							salesCounter++;
							
//							invoke the printPayStub method
							outFile.print(salesEmployee.createPayStub());
							
							
							break;
						
							
				}
					
			}
			
				
				outFile.close();
				
//				new change to close the scanner
				scannedInfo.close();
				
//				logic for averaging. if the counter
//				for all employees is greater than 0, 
//				the average time for each data type 
//				is displayed
				
					if (fullTimeEmployeeCounter > 0 ) {
						System.out.println("Average full-time employee base salary $ = " + currencyFormat.format(fullTimeBaseSalaryTotal/fullTimeEmployeeCounter) 
						+ ", hours worked = "+ fullTimeHoursWorkedTotal/fullTimeEmployeeCounter);
					}
					if (partTimeEmployeeCounter > 0 ) {
						System.out.println("Average part-time pay per hour $ = " + currencyFormat.format(partTimePayedPerHourTotal/partTimeEmployeeCounter) 
						+ ", hours worked = "+ partTimeHoursWorkedTotal/partTimeEmployeeCounter);
					}
					if (salesCounter > 0 ) {
						System.out.println("Average sales employee base salary $ = " + currencyFormat.format(salesBaseSalaryTotal/salesCounter) 
						+ ", sales volume = "+ sSalesVolumeTotal/salesCounter);
					}
		}
	}


