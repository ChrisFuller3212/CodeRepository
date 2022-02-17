import java.util.Scanner;

// By: Christian Fuller

public class HeartlandCarsOfAmericaPayroll {
	
	public static void main (String[] args)
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
		Scanner scannedInfo = new Scanner(System.in);
		System.out.print("Enter Employee Type : ");
		System.out.flush();
		inputEmployeeType = scannedInfo.next().charAt(0);
		System.out.println();
		
		switch (inputEmployeeType)
		{
		case 'F' :
		case 'f' :
			
			//get necessary values as input
			System.out.print("Enter First Name, Last Name, "+"Base Salary, Hours worked : ");
			System.out.flush();
			inputFirstName = scannedInfo.next();
			inputLastName = scannedInfo.next();
			inputBaseSalary = scannedInfo.nextDouble();
			inputHoursWorked = scannedInfo.nextInt();
			System.out.println();
			
			//create an object and initialize data members
			fullTimeEmployee = new FullTimeEmp();
			fullTimeEmployee.setFirstName(inputFirstName);
			fullTimeEmployee.setLastName(inputLastName);
			fullTimeEmployee.setBaseSalary(inputBaseSalary);
			fullTimeEmployee.setHoursWorked(inputHoursWorked);
			
			//invoke the printPayStub method
			System.out.print(fullTimeEmployee.createPayStub());
			
			break;
			
		case 'P' :
		case 'p' :
			
			//get necessary values as input
			System.out.print("Enter First Name, Last Name, "+"Pay per hour, Hours worked : ");
			System.out.flush();
			inputFirstName = scannedInfo.next();
			inputLastName = scannedInfo.next();
			inputPayPerHour = scannedInfo.nextDouble();
			inputHoursWorked = scannedInfo.nextInt();
			System.out.println();
			
			//create an object and initialize data members
			partTimeEmployee = new PartTimeEmp();
			partTimeEmployee.setFirstName(inputFirstName);
			partTimeEmployee.setLastName(inputLastName);
			partTimeEmployee.setPayPerHour(inputPayPerHour);
			partTimeEmployee.setHoursWorked(inputHoursWorked);
			
			//invoke the printPayStub method
			System.out.print(partTimeEmployee.createPayStub());
			
			break;
			
		case 'S' :
		case 's' :
			//get necessary values as input
			System.out.print("Enter First Name, Last Name, "+"Base Salary, Sales Volume : ");
			System.out.flush();
			inputFirstName = scannedInfo.next();
			inputLastName = scannedInfo.next();
			inputBaseSalary = scannedInfo.nextDouble();
			inputSalesVolume = scannedInfo.nextInt();
			System.out.println();
				
			//create an object and initialize data members
			salesEmployee = new SalesEmp();
			salesEmployee.setFirstName(inputFirstName);
			salesEmployee.setLastName(inputLastName);
			salesEmployee.setBaseSalary(inputBaseSalary);
			salesEmployee.setSalesVolume(inputSalesVolume);
			
			//invoke the printPayStub method
			System.out.print(salesEmployee.createPayStub());
			
			break;
		}
		
	}

}