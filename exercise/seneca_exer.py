#PROBLEM 1:
#Array partition


class PartitionArray:
    def partition_array(self,l):
        return (len(l)+1)//2
    
    def display_sub_lists(self):
        index=self.partition_array(sl)
        sub_lists=[sl[:index]]+[sl[index:]]
        return sub_lists


p=PartitionArray()
        
l=[5,-1,4,8,6]

#l=[24,5,6,-2,-1,-4,32,2]

sl=sorted(l)

print(p.partition_array(sl))

print(p.display_sub_lists())

print('\n')

print("################################\n")


#PROBLEM 2:
#Max continous seq of same color

from collections import defaultdict

class MaxContinousSequence:

    def cont_seq(self,l):
        res = []
        for l1 in l:
            sub_list=[]
            index=1
            while index<len(l1):
                if l1[index] - l1[index-1]==1:
                    sub_list.append(l1[index-1])
                    n_flag = True
                    next_index = l1[index]
                    index+=1
                    
                else:
                    index+=1
                    
            if(n_flag):
                sub_list.append(next_index)
                n_flag=False
            res.append(sub_list)
        return res

    def max_continous_seq(self,l):

        colors,numbers=[i[-1] for i in l],[[int(i[:-1])] for i in l]

        d=(list(zip(colors,numbers)))
        
        dd=defaultdict(list)
        for a,b in d:
            dd[a].extend(b)
        
        dd=dict(dd)

        sorted_dd={k:sorted(v) for k,v in dd.items()}

        keys=list(sorted_dd.keys())
        vals=list(sorted_dd.values())

        continous_seq=self.cont_seq(vals)

        res_d=dict(zip(keys,continous_seq))


        max_seq_tup=max(res_d.items(),key=lambda x:len(x[1]))
        print(max_seq_tup)

        final_res=[str(i)+max_seq_tup[0] for i in max_seq_tup[1]]
        return final_res


m=MaxContinousSequence()

l=['5C', '2D', '10C', '4S', '6S', '2H', '1S', '8D', '4C', '6C','8H', '5S', '1H','3C']


#l=['5S','6S','7S','1H','2H','3H','4H','7H','8S','9S']

print(m.max_continous_seq(l))

