# #for loop
#
# lis=[1,2,3,4]
# for i in lis:
#     print(i)
#
# dic_list={'R1':'ram','R2':2,'R3':3}
#
# for i,j in dic_list.items():
#     print(i)
#
# val=[(1,2),(3,4),('hai','bye')]
#
# for i in val:
#     print(i[0])
#     print(i[1])
#
# i=0
# for letter in 'letter':
#
#     print('At index {} then letter {} is present'.format(i,letter))
#     i+=1
#
#
#
# items=[]
# for i in range(0,11):
#     items.append(i)
# print(items)
#
# val=[i for i in items]
# print(val)
#

# #Code here
# st = 'Print only the words that start with s in this sentence'
# a=st.split(' ')
# print(a)


st = 'Print every word in this sentence that has an even number of letters'

#Code in this cell
word=st.split(' ')
for i in word:
    a=len(i)
    if(a%2==0):
        print('Words : ',i,'length :',len(i),' : even')
