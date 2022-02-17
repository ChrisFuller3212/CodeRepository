import java.io.*;
import java.util.*;
import java.util.Scanner;
//import package.PsalmsInputValidator;

// By: Christian Fuller

public class BookOfPsalms {
	
	public static void main (String[] args) throws
		FileNotFoundException, IOException 
	{
//		Starting variables
		int psalmsChapter = 0;
		int psalmsVerse = 0;
		boolean isNumber = false;
		boolean foundVerse = false;
		
//		Using try, catch to catch exceptions if error occurs
		try {
//		      Calling file, scanner and scanner.in for input
		      File biblePsalms = new File("/Users/christianfuller/Desktop/bible-psalms.txt");
		      Scanner myReader = new Scanner(biblePsalms);
		      Scanner in = new Scanner(System.in);
		      do {
					System.out.print("Enter a Book of Psalms Chapter: ");
					if (in.hasNextInt()) {
						psalmsChapter = in.nextInt();
						if (psalmsChapter >= 1) {
							isNumber = true;
						} else {
							System.err.println("\nError, not a Chapter, try again please. ");					
							isNumber = false;					
						}
					} else {
						System.err.println("\nError, not a Chapter, try again. ");
						isNumber = false;
						in.next();
					}
				} while (!(isNumber));
		      
//		      I used two do-whiles to execute the different inputs. Not required but I was a little lazy
		      
		      do {
					System.out.print("Enter a Book of Psalms Verse: ");
					if (in.hasNextInt()) {
						psalmsVerse = in.nextInt();
						if (psalmsVerse >= 1) {
							isNumber = true;
						} else {
							System.err.println("Error, not a Verse, try again please. ");					
							isNumber = false;					
						}
					} else {
						System.err.println("Error, not a Verse, try again. ");
						isNumber = false;
						in.next();
					}
				} while (!(isNumber));
		      
//		      Here, I used the string builders to create strings to convert the int inputs into
//		      (I hated this part because it made me miss python so much)
		      
		      StringBuilder sb1 = new StringBuilder();
		      sb1.append("");
		      sb1.append(psalmsChapter);
		      String psalmsChapterStr = sb1.toString();
		      
		      StringBuilder sb2 = new StringBuilder();
		      sb2.append("");
		      sb2.append(psalmsVerse);
		      String psalmsVerseStr = sb2.toString();
		      
//		      Extremely cheesy with the addition of psalms variable but I had having issues with
//		      My variables matching so why not be safe and add another constant
		      
		      String psalms = "Psalms ";
		      
		      String cVConcat = psalms + psalmsChapterStr + ':' + psalmsVerseStr;	  
		      
		      
//		      This is the meat. It took some time for syntax correction but here it is.
		      
//		      I use a while loop to simulate the for loop when I solved this in python.
//		      As you suggested, I split the data or scanner list by the tab and also I
//		      Only make one split list opposed to my double split list in python
//		      From there its pretty simple. If the string input matches with the string in 
//		      bible-psalms.txt, it prints the verse (verse variable)
		      while (myReader.hasNextLine()) {	
			     String data[] = myReader.nextLine().split("\t");
			      String refAndVerse = Arrays.toString(data);
			      String Reference = data[0];
		    	  if (cVConcat.equals(Reference)) {
		    		  foundVerse = true;
		    		  String Verse = data[1];
		    		  System.out.println("Your Psalms verse is: " + "\n" + Verse);
		    		  break;
		    		  
		    	  } if (!(cVConcat.equals(Reference))) {
		    		  foundVerse = false;
		    	  } else {
				      System.out.println("Verse not found");
		    	  }
		    	  
		      } 
//		      closing of the scanner and input scanner 
		      myReader.close();
		      in.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }

	}
	

}
