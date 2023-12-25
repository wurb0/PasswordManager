import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        System.out.println("Enter main Password");
        String main_pass = "a";

        Scanner in = new Scanner(System.in);
        String temp = in.next();

        Boolean flag = false;
        if ( temp.equals(main_pass))
        {
            flag = true;
        }
        else{
            flag = false;
        }

        while (flag == true)
        {
            System.out.println("View all passwords, Add a new password, Create a new password or Search for a password (view,add,create,search and q to quit)");
            String option = in.next();
            switch (option)
            {
                case "view": 
                {
                    view_pass();
                    break;
                }
                case "add":
                {
                    System.out.println("Enter new Username:");
                    String username = in.next(); 
                    System.out.println("Enter new password");
                    String newpass = in.next();
                    add_pass(username, newpass);
                    break;
                    
                }
                case "create":
                {
                    System.out.println("How long should the password be?");
                    int length = in.nextInt();
                    create_pass(length);
                    break;
                }

                case "search":
                {
                    System.out.println("Enter a username to view its password");
                    String username = in.next();
                    search(username);
                    break;
        
                }
                case "q":
                {
                    flag = false;
                    break;
                }
                default: System.out.println("Invalid input, Try again.");
            }
        }

        }

}
    
