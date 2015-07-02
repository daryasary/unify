# final test org
# coded by DARYASARY
#######################
#unify function
def unify(L1,L2):
	dic={}
	lst=[]
	
	if(len(L1)!=len(L2)):
		print("The functions have different number of arguments")
	elif check_arg(L1,L2):
		print("sorry!!\nyou can't unify this functions")
	else: # compare argument of each functions
		for i in range(len(L1)):
			A1=L1[i]
			A2=L2[i]
			if A1[0].islower() and A2[0].islower() :
				lst.append(A1)
				dic[A1]=A2
				for n in L1:#apply change
					if n==i:
						n=A2
			
			elif A1[0].isupper() and  A2[0].islower():
					lst.append(A2)
					dic[A2]=A1
					for n in L2:#apply change
						if n==i:
							n=A1
						
			
			elif A2[0].isupper() and A1[0].islower():
					lst.append(A1)
					dic[A1]=A2
					for n in L1:#apply change
						if n==i:
							n=A2
					
			else:print("sorry\nthis condition in not programmed ;-)")
			
		### print the dic values..........
		for i in lst:
			print("(%s,%s)"%(i,dic[i]) )
		print("\n")
		
############################
#check the rapid argumentes
def check_arg(L1,L2):
			for i in range(len(L1)):
				A1=L1[i]
				A2=L2[i]

				if A1[0].isupper():
					inlistL1=make_list(L1[i])
					for n in L2:
						for m in inlistL1:
							if n==m : return(1)

						
			
				elif A2[0].isupper():
					inlistL2=make_list(L2[i])
					for n in L1:
						for m in inlistL2:
							if n==m : return(1)
				else:
					for j in L2:
						if A1==j:return(1)
					return(0)
		
		
############################
#make_list func
def make_list(func): # change the function to a list for ex: P(x,y,z,F(a,b),e,t) ==> ["x","y","z","F(a,b)","e","t"]
	A=[]
	item=''
	word=''
	i=2
	while(i<len(func)):
		if (func[i].isupper()):
			for j in range(len(func))[i::]:
				word+=func[j]
				if (func[j]==")"):
					#print(word)
					A.append(word)
					i=j+2
					break
		elif(func[i]==','):
			A.append(item)
			item=''
			i+=1
		elif(func[i]==')' and item!=''):
			A.append(item)
			item=''
			i+=1
		else:
			item+=func[i]
			i+=1
	return(A)
	
	

# the main code....
func1=input('Enter your 1st function (for ex: P(x,y,z)):\n')
func2=input('Enter your 2nd function:\n')
L1=make_list(func1)
L2=make_list(func2)
if(func1[0]!=func2[0]): # check the predicate symboles
		print("The initial predicate Symbole in 1st and 2nd function are not indentical")
else:unify(L1,L2)


