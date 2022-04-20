import emmlang

while True:
    ftxt = input("$ ")
    fn = "<stdin>"
    result, error = emmlang.run(fn, ftxt)
    if error:
        print(error.as_string())
    else:
        print(result)