

def giri(br):
    st = "aaaabbbccccdddddddeeeeeeAaajjjjjaaaa"
    # print("length is ", len(st))
    count = 1
    track = 0
    # print("here ",br)
    for i in range(br, len(st) - 1):
        # print (i)
        if (st[i] == st[i + 1]):
            count = count + 1
        else:
            track = i + 1
            print(st[i], count)
            giri(track);
            break;
            #

    br = track


giri(0)