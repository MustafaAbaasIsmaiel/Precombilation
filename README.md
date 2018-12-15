# Precombilation
This Project purpose is to help overcoming the structural hazards in a processor by passing the assembly code on a pre-compilation step where the assembly code is modified to overcome these hazards.

# Code Brief Description
In this code if forwarding is supported, as a consequence only LOD, DIV and MUL instructions will cause a problem, if not ADD and SUB instructions will also cause a problem.
Noticing that at the beginning of the code there is a variable called ‘Cycles’ that actually represents how many cycles are needed for DIV and MUL instructions to get the output ready, so anyone can customize this variable dependent on which processor the code is used for.
Also at the beginning, it’s a user choice to require the code with forwarding or without!
For the LOD instruction and by definition the stall is only one cycle in case of forwarding.
It’s probably worth noting that the code can easily be modified to add stall after any required instruction, and it has no register-file capacity limit, which means any numbers of registers can be used.

# HOW TO USE
Can simply be used, by writing your code in the code.txt file included with this report and run the program, then by seeking the output in the output.txt file.
The code will ask for the number of cycles needed in the execution stage for DIV and MUL instructions to finish.
Then the code will ask whether forwarding as assumed or not, if it was not assumed it will ask for number of stages after the execution stage.

# PRE-CAUTIONS
* The (LOAD) instruction is donated by LOD.
* Make sure that in the code.txt file there is no spaces added after the code since it’s obvious that python will consider them as input
* Instructions must be in capital letters, it won’t make any difference if the registers names are small or capital, as long as they are all the same of course!
* Instructions must consist of 3 letters, so anything can work fine as long as it consists of 3 letters.
* If Cycles were chosen to be anything greater than one, then the code must check the upcoming instructions right after the DIV or the MUL, number of instruction checked equals number of stalls required and number of the stalls instruction inserted itself is dependent on which instruction was found to be dependent on the DIV or MUL instruction.
* Reading the memory is assumed to be available at the negative edge!
