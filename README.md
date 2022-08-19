# IAS-simulation
creating an IAS processor simulation which performs addition, multiplication and greater of two numbers.

 1 --> Simple Addition of 10 numbers.
 2 --> Simple Multiplication
 3 --> Greater of two numbers.
 ----------------------------------------------------------------------------------------------------------------------------------
 ----------------------------------------------------------------------------------------------------------------------------------

#ADDITION INPUTS.

enter operation:1
enter number in location 100: 1 
enter number in location 101: 2
enter number in location 102: 3
enter number in location 103: 4
enter number in location 104: 5
enter number in location 105: 6
enter number in location 106: 7
enter number in location 107: 8
enter number in location 108: 9
enter number in location 109: 12

#MULTIPLICATION INPUTS.

enter operation:2
enter number in memory location 500: 12
enter number in memory location 501: 3

#GREATER NUMBER INPUTS.

enter operation:3
enter number in location 100: 98
enter number in location 101: 43

#INPUTS STORED IN THE MEMORY. (ADDITION)

Memory location : 100    
Memory Value : 1 

Memory location : 101
Memory Value : 2

Memory location : 102
Memory Value : 3

Memory location : 103
Memory Value : 4

Memory location : 104
Memory Value : 5

Memory location : 105
Memory Value : 6

Memory location : 106
Memory Value : 7

Memory location : 107
Memory Value : 8

Memory location : 108
Memory Value : 9

Memory location : 109
Memory Value : 12

#INSTRUCTION STORED IN MEMORY, ASSEMBLY LANGUAGE IN BINARY 40 BIT INSTRUCTION..

Memory location : 1
Memory Value : 0000000100000110010000000101000001100101       #LOAD M(100) ADD M(101)

Memory location : 2
Memory Value : 0000010100000110011000000101000001100111       #ADD M(102) ADD M(103)

Memory location : 3
Memory Value : 0000010100000110100000000101000001101001       #ADD M(104) ADD M(105)

Memory location : 4
Memory Value : 0000010100000110101000000101000001101011       #ADD M(106) ADD M(107)

Memory location : 5
Memory Value : 0000010100000110110000000101000001101101       #ADD M(108) ADD M(109)

Memory location : 6
Memory Value : 0000000000000000000000100001000011001000       #STOR M(200)

#OUTPUT STORED IN MEMORY.
Memory location : 200
Memory value : 57

-----------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------

#INPUTS STORED IN THE MEMORY. (MULTIPLICATION)

Memory location : 500    
Memory Value : 12 

Memory location : 501
Memory Value : 3

#INSTRUCTION STORED IN MEMORY, ASSEMBLY LANGUAGE IN BINARY 40 BIT.

Memory location : 3
Memory Value : 0000000100011111010000001011000111110101       #LOAD M(500) MUL M(501)

Memory location : 4
Memory Value : 0000000000000000000000100001000000001010	#STOR M(10)

#OUTPUT STORED IN MEMORY.

Memory location : 10
Memory Value : 36

------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------

#INPUTS STORED IN THE MEMORY.(GREATER OF TWO NUMBERS)

Memory location : 100
Memory Value : 98

Memory location : 101
Memory Value : 43

#INSTRUCTION STORED IN MEMORY,ASSEMBLY LANGUAGE IN 40 BIT.

Memory location : 1
Memory Value : 0000000100000110010000000110000001100101	#LOAD M(100) SUB M(101)

Memory location : 2
Memory Value : 0000000000000000000000010000000000000100	#JUMP+ M(4,20:39)

Memory location : 3
Memory Value : 0000000000000000000000100001000000000101	#LOAD M(100) LOAD M(101)

Memory location : 4
Memory Value : 0000000100000110010000000001000001100101	#STOR M(5)

#OUTPUT STORED IN MEMORY

Memory location : 5
Memory Value : 98

****************************
*    VINEET PRIYEDARSHI    *
*       IMT2021018         *
****************************
