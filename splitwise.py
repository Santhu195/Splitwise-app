#Simplify Debts is a feature of an application which can be used to restructure debt within a group. 
# It makes it easier to pay people back by minimizing the total number of payments. 
import json
import operator

with open('input.json','r') as f:
    b = json.load(f)

total = 0
paid_by=[]
person_spent={}
person_spent1={}

#Get the total money spent by each 
for i in range(len(b)):
    c = b[i]
    total_i = c['total_bill_amount']
    people = c['split_between']
    total +=total_i
    
    if c['paid_by'] in paid_by:
        
        if c['paid_by'] in person_spent:
            person_spent[c['paid_by']]+=total_i


    else:
        paid_by.append(c['paid_by'])
        for i in paid_by:
            if i == c['paid_by']:
                person_spent[i]= total_i

    

N = len(people)               
cost_per_head= total//N
#get the new cost spent by subtracting cost_per_head
for i in person_spent:
    person_spent1[i] = person_spent[i]-cost_per_head
#finding Person with max debt and credit
Max_debt = min(person_spent1.items(), key =operator.itemgetter(1))[0]
Max_Cred = max(person_spent1.items(), key =operator.itemgetter(1))[0]
#finding th remaining people
for i in person_spent1:
    indiviual_debts = dict(person_spent1)
    if i not in [Max_Cred,Max_debt]:
        remaining = i
    if i in person_spent1:
        indiviual_debts.pop(i)
        for k,v in indiviual_debts.items():
            indiviual_debts[k]= -v
            if person_spent1[i] == 0:
                indiviual_debts[k]= 0

        
    print(json.dumps(
        {
        i:{
            "total_debt":person_spent1[i],
              "individual_debt": indiviual_debts
        }
        } 
    )) 
#print('{} has to give {}  '.format(Max_debt,Max_Cred))


