[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1

**Question 1**

 this program demonstrates the use of the cryptographic services package in python, more specifically the hashlib library[1]

2. you run this program by first providing the prompt with your password, then after you will be prompted to put if you want your password to be secures or not,
   if no is chosen then the program ends, but if yes is chosen you are then prompted to chose if you want the password to be secured automaticaly or manually,
   if automatically is chosen you will be prompted to put if you want your secured password in hex or not, then it returns the new secured password, then the program ends,
   but if manually is chosen then you are first prompted to provide which hashing digest algorithm you wish to use[2], after one has been chosen you are then
   prompted to chose between having your password hexed or not , then you are prompted to provide the program with your desired salt string and 
   your desired key length. these values are then passed through, and the program returns the new secured password.
	
3. this program takes a user inputed password and uses key derivation for secure password hashing, this program specifically uses the pbkd2 hmac()[3] function
   it takes in a hashing agorithm , the password, a slat string and the derived key length, and then the password returns as either hex or not depending on thier preference. 
   In my program the user has the choice between having these values chosen automatically or to input them in manually. if they chose automatically, the function uses the sha256 
   hashing digest algorithm(i chose this one because it is the best one)[3], the the user inputed password, then i input a randomly selected salt(using os.urandom)[4], then i chose 16 as the key length. 
   if the user choses manually i ask them to give me the hash digest algorithm they wish to use(i give them five choices). then when one is chosen i ask they to provide me with their desired salt 
   string and their desired key length. these values are passed into the pbkd2 hmac() function, as (<thier desired hash digest algorithm>, <thier password>, <chosen salt>, <chosen key length>)
   then the password returns as either hex or not depending on the users preference. 
   
4. some sample output would be for example if i give the password "fjhdk" and the user chose the automatically option then my program would either return 
   7502e399ee5a9f5147f1da8ac266d372ec2b8eadf3326da455f120afdbc502ef if the user wanted the password hexed
   or b'u\x02\xe3\x99\xeeZ\x9fQG\xf1\xda\x8a\xc2f\xd3r\xec+\x8e\xad\xf32m\xa4U\xf1 \xaf\xdb\xc5\x02\xef' if they did not.
   another example could be if i give the password "savsfbsdfb" and the user chose the manually option, and within this option they chose
   the sha384 hashing digest algorithm, and then within this option they chose the salt string("dafjkskfk") and the key length(12)
   then my program would either return  6c4f5a6a9d7f27bde3cd74c9387e65f79562e333e37fd167c4a62556faaf99858468946b67ec63310ba32723f3c2d287 
   if they wanted it hexed or  b"lOZj\x9d\x7f'\xbd\xe3\xcdt\xc98~e\xf7\x95b\xe33\xe3\x7f\xd1g\xc4\xa6%V\xfa\xaf\x99\x85\x84h\x94kg\xecc1\x0b\xa3'#\xf3\xc2\xd2\x87"
   if they did not.
	

References:
[1] https://docs.python.org/3/library/hashlib.html
[2] https://www.sciencedirect.com/topics/computer-science/hashing-algorithm#:~:text=The%20Secure%20Hash%20Standard%20specifies,representation%20called%20a%20message%20digest.
[3] https://codesigningstore.com/what-is-the-most-secure-hashing-algorithm#:~:text=To%20the%20time%20of%20writing,government%2C%20to%20protect%20sensitive%20information.
[4] https://docs.python.org/3/library/os.html#os.urandom