import java.util.*;
class diffiehellman

{
   public static void main(String args[])
   {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter modulo(n) / Prime No.");
     long n=sc.nextInt();
     System.out.println("Enter primitive root of Prime No: "+n);
     long g=sc.nextInt();
     System.out.println("Choose 1st Secret Key of (Alice1) X_a:");
     long X_a=sc.nextInt();
     System.out.println("Choose 2st Secret Key of (Bob2) X_b:");
     long X_b=sc.nextInt();
     
     long Y_a=(long)Math.pow(g,X_a)%n;
     long Y_b=(long)Math.pow(g,X_b)%n;
     
     long K_A=(long)Math.pow(Y_b,X_a)%n;
         System.out.println("They share a secret key for (Alice1) is: "+K_A);
     long K_B=(long)Math.pow(Y_a,X_b)%n;
         System.out.println("They share a secret key for (Bob2) is: "+K_B);
         
         if(K_A==K_B)
         {
           System.out.println("Alice and Bob can communicate7 with each other!!!");
           System.out.println("As they share a Secret No:"+K_B);
         }
           
           else
           {
             System.out.println("Alice and Bob cannot communicate with each other!!!");
           }
   }
 }  

// OUTPUT :
// javac Diffie_Hellman.java
// java Diffie_Hellman
// Enter modulo(n)
// 11
// Enter primitive root of11
// 2
// Choose 1st secret no (Alice):X_a:
// 6
// Choose 2st secret no (BOB):X_b:
// 8
// They share a secret key for User-A is=3
// They share a secret key for User-B is=3
// Alice and Bob can communicate with each other!!!
// They share a secret no=3

