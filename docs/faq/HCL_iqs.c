									"HCL INTERVIEW QUESTIONS" (July/August 2014)


How float a = 2.5; is represented in memory?

char a = 128, printf("%d", a)?

How negative values are stored in memory?

Scope and lifetime of all the storage classes?

In which storage section, static variables are stored?

In file a.c int i declared as global and 
		b.c extern int i is declared?
somewhere in the program i is printed. what is the value of i?

Diff b/w const char *ptr and char const *ptr and char *const ptr?

Program to print fibinocci series using recursion?

program to print "hello world" without using main()?

program to check whether the machine is "Little endian" or "BIG ENDIAN"

Register float a = 2.5, printf("%f", a)



**************************************"STRINGS"**************************************************

char *ptr
strcpy(ptr,	"HCL") does it works, if so how?

implement strstr() strrev()(try without using a temp varaible)?

char a[30] = "I am an Indian"
write a program to count numbers os 'a' in the above string?


************************************"Bit Manupulations"*****************************************************

Program to "toggle" a bit at nth pos.

Given two positions. Asked to print the bit (ON/OFF) at both the positions.
	if (bit is ON)
		make it OFF
	else
		make it ON

Given a number, asked to "rotate" the bits twice and print the number.

Given two positions in a num. "Swap" the bits at two positions.
							!     !
						0 0 0 1 1 1 0 0 becomes
						0 0 1 1 1 0 0 0

Good to know
HOW to 	
		check if bit is o or 1
		set a bit at the given position
		reverse bits

*******************************************"LINKED LISTS"*****************************************************

"Single linked list"
	  Add a node in the middle of the lists
	  Delete a node at the nth positon from the last
	  check if there exists a loop in linked lists
	  Given a pointer to the last node of SLL. how do you point to the head in list provided list is not circular?
	 
"DLL"
	Delete a node in the DLL at the nth pos from the last.

GOOD to know. 

		Reverse a linked list (tech mahindra)
		find and remove the duplicates the single linked lists.


***************************"OPERATING SYSTEM"*******************************************

How to create a tree of processes

creat n number of childs with one parent. i.e one parent and n childs

What is IPC and explain IPC mechanisms.

Arguments to a pipe()

How to know if the message queue is empty or not

what is named and unamed pipe. explain one major difference between both.

Given an array of ten elements: int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
     in process A creat a shared memory segment.
	 			  add the two consecutive elements in the array 
				  write into the shared memory 
				  wait()
	
	in process b read into the shared memory
				 wait()

i.e while process A is using the segment, process B show wait and vice versa.





