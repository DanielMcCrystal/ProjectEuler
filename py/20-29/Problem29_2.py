


def num_terms(max_a, max_b):
    max = (max_a-1)*(max_b-1)
    perfects = []
    for a in range(2, max_a+1):
        for b in range(2, max_b+1):
            power = a**b
            if power > max_a:
                break
            else:
                for b2 in range(2, max_b+1):
                    if b*b2 > max_b:
                        break
                    else:
                        max-=1
                        #print(str(a) + "^(" + str(b2) + ") = " + str(a**b2))
                perfects.append(power)



    print(max+1)

num_terms(100, 100)