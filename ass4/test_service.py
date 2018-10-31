import service

sr = service.Service()

def absTest():
    assert sr.abs_plus(1) == 2,                    "fail 1"
    assert sr.abs_plus(-1) == 2,                   "fail 2"
    assert sr.abs_plus(0) == 1,                    "fail 3"
    assert sr.abs_plus(2147483647) == 2147483648,  "fail 4"
    assert sr.abs_plus(-2147483647) == 2147483648, "fail 5"
    assert type(sr.abs_plus(1337)) == int,         "fail 6"
    assert sr.abs_plus(69.9) == 70.9,              "fail 7"
    assert sr.abs_plus(-0x1a4) == 421,             "fail 8"
    assert type(sr.abs_plus(666.6)) == float,      "fail 9"
    
def divideTest():
    assert type(sr.divide(1.1)) == float ,         "fail 10"
    assert type(sr.divide(2147483647)) == int,     "fail 11"
    assert sr.divide(-1) > 0,                      "fail 12"
                    

def complicatedTest():
    assert type(sr.complicated_function(99)) == tuple, "fail 13"
    assert len(sr.complicated_function(1123)) == 2, "fail 14"
    assert sr.complicated_function(2147483647)[0] == 0, "fail 15" 
    assert sr.complicated_function(123333)[1] in [0,1], "fail 16"
    assert sr.complicated_function(1233321)[1] in [0,1], "fail 17"
    assert type(sr.complicated_function(99)[0]) == int, "fail 18"
    assert type(sr.complicated_function(99)[1]) == int, "fail 19"  
    
def badRandomTest():
    assert type(sr.bad_random()) == int, "fail 20"
    assert sr.bad_random() > 0, "fail 21"
    assert sr.bad_random() != None, "fail 22" 


def main():
    absTest()
    print("abs_plus test passed")
    divideTest()
    print("divide test passed")
    complicatedTest()
    print("complicated function test passed")
    badRandomTest()
    print("bad random test passed")
    
main()
