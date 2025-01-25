print(3 * 5)  # multiplication
print(7 // 3)  # floor division
print(5 % 3)  # modulus
print(divmod(7, 3))  # division and modulus
print(3 ** 2);print(pow(3,2))  # exponentiation
print(pow(3,2,mod=4))  # exponentiation with modulus
print(pow(3,-1,mod=4))  # negative exponentiation with modulus
print(3 < 5);print(3 == 5);print(3 != 5)  # comparison

a=3; b=4; c=a*b; print(c)  # multiple statements in one line

print(2*'brac'+'ket')  # string concatenation
print('don\'t'," or ","don't")  # escape character

print("line1\nline2")  # new line
print(r"line1\nline2")  # raw string

print("string1\
string2")  # string concatenation
print("""string1
string2
string3""")  # multi-line string

char="world";print(len(char));a=char[0];b=char[-1];print(a);print(b)  # string indexing
c=char[:2];d=char[-2:];print(c);print(d)  # string slicing with positive 2 excludied

list=[1,2,0,4,5];print(list);print(list[0]);print(list[-1])  # list, mutable
list[2]=3;print(list);list.append(6);print(list);list.pop();print(list)  # list modification
list[-2:]=[];print(list);print(len(list))  # length of list
list1=[1,'f'];list2=[3,4];list=[list1,list2];print(list);print(list[1][1])  # list nesting

tuple=(1,2,3);print(tuple);print(tuple[0]);print(tuple[-1])  # tuple, immutable
a=complex('3+4j');b=complex(3,4);c=complex('-Infinity+NaNj');print(a,b,c);print(abs(a));print(a.real);print(a.imag)  # complex number
