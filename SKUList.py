import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

final = []
driver = webdriver.Firefox()
driver.get("http://www.kmstools.com/") #change to portal website

def checkPortal(code):
    elem = driver.find_element_by_id("search_input")
    elem.clear()
    elem.send_keys(code)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    result = driver.find_element_by_class_name("itemTitle").text
    #add if statement for if result not found
    return result

def scanCode():
    test = "aaa"
    while (test != "done"):

        test = input("Scan Barcode ")
        if(test != "done"):
            SKU = checkPortal(test)
            if(SKU != "not found"):
                addToList(SKU)
                print("Added to List ")
            else:
                print("Not found ")
    driver.close()


def addToList(SKU):


    if (len(final) == 0):
        final.append([SKU, 0])

    for i in final:
        test = True
        if i[0] == SKU:
            i[1] += 1
            test = False
            break

    if test:
        second = True
        for i in range(len(final)):
            if final[i][0] < SKU:
                continue
            elif final[i][0] > SKU:
                final.insert(i, [SKU, 1])
                second = False
                break
        if second:
            final.append([SKU, 1])

    print(SKU + " Added to list")


def main():
    scanCode()
    print(final)

main()
