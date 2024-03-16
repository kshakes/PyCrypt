# PyCrypt

Since studying information security in Aberystwyth, I've became very interested in encryption and vunerabilities with data.

This is a short program that includes one of the more standard encryptions which is the Caesar Cipher. This program allows you to encrypt and decrypt text with a shift of your choice.

## What is the shift?
The shift is a number that will determine how the message is scrambled. For example, a shift of 1 would result in:
- a = b
- b = c
- etc

## How do you brute force a Caesar Cipher?
It is very simple to break the Caesar Cipher. Simply because there's only 26 ways of encrypting the message. So if you loop through all these, you are eventually going to get a result.
The way I solved this is by looping through 1-26 and reversing the cipher with each variation of the shift. However to find if there is plain english, I would save the result and then check if one of the words are in a list of the top 1,000 most common words. If it is, it will reveal the decrypted message!


 
