from tkinter import *

root=TK()

root.title("fibonacci")
root.geomitry("400*400")

label_series = Label(root, text="fibonacci series: ")
label_flower = Label(root)
label_spisal = label(root)

def fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    
    while(counter <= num):
        label_series["text"] += str(num) + " "
        counter = counter+1
        first_no= second_no
        second_no = sum
        sum = first_no + second_no
        label_flower['text']="flower is fully bloomed"
        label_spiral['text']="spiral in right direction are" +
        str(first_no)+"and spiral in left direction are"+ str(second_no)+
        "\n. total spiral are" =  str(sum)
    
    btn = Button(root, text="Show fibonacci series", command=fibonacci)
    btn.pack()
    label_series.pack()
    label_spisal.pack()
    label_flower.pack()
    
    root.main()