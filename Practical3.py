'''Write a program that prints the integers from to 100, but for multiples of 3 print 'FIZZ' instead of number and for multiples of five print 'BUZZ. For numbers which are multiples of both 3 and 5 print FIZZBUZZ'''

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz: "+str(num))
    elif num % 3 == 0:
        print("Fizz:" + str(num))
    elif num % 5 == 0:
        print("Buzz:"+ str(num))
    else:
        print(num)
 
 
'''
Output:
1
2      
Fizz:3 
4      
Buzz:5 
Fizz:6 
7      
8      
Fizz:9 
Buzz:10
11
Fizz:12
13
14
FizzBuzz: 15
16
17
Fizz:18
19
Buzz:20
Fizz:21
22
23
Fizz:24
Buzz:25
26
Fizz:27
28
29
FizzBuzz: 30
31
32
Fizz:33
34
Buzz:35
Fizz:36
37
38
Fizz:39
Buzz:40
41
Fizz:42
43
44
FizzBuzz: 45
46
47
Fizz:48
49
Buzz:50
Fizz:51
52
53
Fizz:54
Buzz:55
56
Fizz:57
58
59
FizzBuzz: 60
61
62
Fizz:63
64
Buzz:65
Fizz:66
67
68
Fizz:69
Buzz:70
71
Fizz:72
73
74
FizzBuzz: 75
76
77
Fizz:78
79
Buzz:80
Fizz:81
82
83
Fizz:84
Buzz:85
86
Fizz:87
88
89
FizzBuzz: 90
91
92
Fizz:93
94
Buzz:95
Fizz:96
97
98
Fizz:99
Buzz:100''' 