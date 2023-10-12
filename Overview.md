# ✨Exploration Activity 1✨

# Question 1 
 
  For my exploration activity I chose the cryptographic services library in python, more specifically I made
  use of the hashlib module, and in this library I mostly made use of the key derivation module.[1]

# Question 2

  ## What is the purpose of this package❓
  
  It's purpose is to provide programmers with various algorithms of cryptographic nature. It contains multiple 
  modules, the one i focused on was the hashlib module[2]. This module allows programmers to make use of many different
  secure hash and message digest algorithms. These include the FIPS secure hash algorithms(sha1, sha256....), these 
  algos generate digests of messages, the digests are then used to detect if the messgaes have been changed since the 
  digests were generated[3]. (I made use of these in my program). It also includes the MD5 algorithm, this algo takes an 
  input of any length and returns a 128-bit 'fingerprint'[4]. It also has multiple hash objects, these are constant attirbutes 
  of the hash objects returned by constructors, some examples of these would be hash.digest_size(size of hash in bytes) and 
  hash.update(update hash object with byte-like objects). This module also includes the shake128 and shake256 algorithms, which 
  provide variable length digests with length in bit upto 128 or 256 bits of security. Another cool thing it provides is file
  hashing , where you can use file digest function on a inputed file. One specific part of this module that i used was the key derivation
  algorithm, this allows you to do secure password hashing, the function i used to hash the password was the pbkdf2-hmac(), this function
  provides PKCS#5 password based key derivation function 2 and uses hmac as a pseudorandom function. You can also use BLAKE2, which comes in 
  BLAKE2b(1-32 bit digest) and BLAKE2s(1-64 bit digest), these are cryptographic hash functions, and these functions can also be used as 
  callable objects, like example hashlib.blake2b(), they return the corresponding hash objects. There are two other modules in this library 
  that I did not utilize but I will describe their purpose. The first one is the hmac module [5], this module is used for keyed-hashing for 
  message authentication, it implements the HMAC algorithm, it also has a few built in functions, like hmac.new(), which returns a new hmac
  object, or even hmac.hexdigest(), it returns a string twice the length containing only hexadecimal digits, its used for exchange the value
  safety in email. The last module in this library is called secrets[6], it generates cryptographically secure random numbers for managing secrets, 
  like passwords, account authentication, and security tokens. It has a multitude of pre-build functions, amongst them we have, for example, 
  class secrets.SystemRandom(), which is a class that generates random numbers using the highest quality sources the operating system provides[7].
  You can also generate tokens using this module, by using one of the many token functions, like the secrets.token-bytes(), which returns a random 
  byte string containing nbytes number of bytes. 
  
  ## How do you use this package ⁉️
  
  This library has many different uses within the cybersecurity field. You can use it to secure passwords against hackers, as the hashing algorithms 
  are very difficult to crack, even highly efficient password cracking software has great difficulty cracking them[8]. You usually use this library if
  you are trying to secure data, this is done with the hash algorithms, but be carful as they aren't all strong or safe, so it is important to keep up
  to date with all things regarding this module[9]. If you want secure password hashing, like what i did in my program, you would use key derivation
  functions, like the ones I utilized in my program. If you want to verify both the data integrity and the authenticity of a given message , you should
  use the hmac module, because it uses a secret cryptographic key[10]. If you want secure random numbers, like to use for password hashing or secret
  storage , you would use the secrets module. Additionally you would also use secrets if you wanted to generate secure tokens, to get like hard to guess
  URLs or password resets[11].
  
# Question 3
  
  The functionalities of this library are hashing and data security.
  
  ##some sample code and output:
  
  for hashlib:
  
  
  for key derivation:
  
  for BLAKE2:
  
  
  
# Question 4

  ## When was it created❓
  
  It has a release history dating back to july 3, 2009[12].
  
# Question 5
  
  ## Why did I chose this library❓
  
  I chose this library because the cybersecurity and cryptography side of python has always interested me. 
  I wanted to explore these kinds of topics more in depth because I want to enter the field of cybersecurity 
  after graduation, so I thought that expanding my knowledge on the subject would prove helpful.

# Question 6
  
  ## How did learning the library influence my learning of the language❓
  
  It taught me alot about how flexible python is and it showed me a glimpse of how versatile
  the language is, knowing this has allowed me to get a better understanding of how this language operates
  as compared to java, which is starting to help me become better at programming in python. Doing this library also exposed me 
  to alot of the other built in functions that can be used in python. Because i learnt about this package I have further 
  developed proficiency in writing code in python, and I have even started developing a coding style for the language.
  It also helped me to learn how to better navigate python documentation.

#Question 7
  
  ## When would i recommend this library to someone❓
  
  I would recommend it to someone if they desired to secure somesort of data or message, especially if
  it involves some sort of very important information, like for a government organization, against any
  type of hacker, this library has the potential to produce data that is very hard to crack. 
  
  ## Would I continue to use the library❓
  
  I personally would not, unless I have a job that requires me to secure data, because
  I like the way that hash algorithms secure data. I don't think that it has much practical
  use in everyday coding projects, it is for a specific thing in a specific field, and I have
  never before this activity, used cryptography. 
  
  
References:
[1] https://docs.python.org/3/library/hashlib.html
[2] https://docs.python.org/3/library/hashlib.html
[3] https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
[4] https://datatracker.ietf.org/doc/html/rfc1321.html
[5] https://docs.python.org/3/library/hmac.html
[6] https://docs.python.org/3/library/secrets.html
[7] https://docs.python.org/3/library/random.html#random.SystemRandom
[8] https://medium.com/@Jay_thriple/basic-cryptography-with-python-d98e8182d383
[9] https://rixx.de/blog/december-10-python-cryptographic-service-modules/
[10] https://rixx.de/blog/december-10-python-cryptographic-service-modules/
[11] https://rixx.de/blog/december-10-python-cryptographic-service-modules/
[12] https://pypi.org/project/hashlib/#history

